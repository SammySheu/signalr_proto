import requests
import certifi
import json
import websocket
from sseclient import SSEClient
from urllib.parse import quote_plus, urlparse, urlunparse

session = requests.Session()
self_cert = certifi.where()
self_cert = self_cert.replace("cacert.pem", "Self.pem")
session.verify = self_cert
server_url = 'https://10.21.1.211/KPCT_2nd_CMS_API/signalr'
hub_name = 'norisHub'

class DCCSignalr():
    def __init__(self, url: str, proxy_hub: list[str], cert_loc: str | None = None) -> None:
        self.transport: str = ""
        self.signalr_url = url
        self.session_http = requests.Session()
        self.session_sse = requests.Session()
        self.proxy_hub = proxy_hub
        self.session_http.verify = cert_loc if cert_loc else False
        self.session_sse.verify = cert_loc if cert_loc else False
        self.http = self.session_http
        self.websocket: websocket.WebSocket | None = None
        self.sse: SSEClient | None = None

        self.__set_connection_data(self.proxy_hub)
    
    def __set_connection_data(self, hubs: list[str]):
        self._connection_data: str = json.dumps([{'name': hub_name} for hub_name in hubs])

    @staticmethod
    def __get_base_url(url: str, action: str, **kwargs):
        args = kwargs.copy()
        query = '&'.join(['{key}={value}'.format(key=key, value=quote_plus(args[key])) for key in args])

        return '{url}/{action}?{query}'.format(url=url,
                                               action=action,
                                               query=query)
    @staticmethod
    def __get_sse_url_from(url):
        parsed: tuple = urlparse(url)

        return urlunparse(parsed)
    
    @staticmethod
    def __get_ws_url_from(url):
        parsed: tuple = urlparse(url)
        scheme = 'wss' if parsed.scheme == 'https' else 'ws'
        parsed[0] = scheme
        return urlunparse(parsed)

    def http_negotiate(self):
        negotiate_url = self.__get_base_url(
            url=self.signalr_url,
            action="negotiate",
            connectionData=self._connection_data
            )
        negotiate_data = self.session_http.get(negotiate_url)
        return negotiate_data.json()

    def websocket_handshake(self):
        pass

    def sse_connect(self, **args):
        sse_base_url = self.__get_base_url(
            url=self.signalr_url,
            action="connect",
            transport="serverSentEvents",
            connectionData=self._connection_data,
            **args,
            )
        sse_url = self.__get_sse_url_from(sse_base_url)
        self.sse = SSEClient(url=sse_url, session=self.session_sse)
        return self.sse 

signar_client = DCCSignalr(server_url, [hub_name], self_cert)
data = '{"Url":"/signalr/hubs","ConnectionToken":"AQAAANCMnd8BFdERjHoAwE/Cl+sBAAAAhhmmaWXu6ku7IfZ4f23y3wAAAAACAAAAAAAQZgAAAAEAACAAAABurxCvv0Dfn44CQcFeuReogSYexrjcCi3w0hKmsNRd/wAAAAAOgAAAAAIAACAAAABbkr7ZpOhlT7GdoWasfD1CV8B+Jk3fh6PZr8mAH9fY5zAAAABFlKK1PHdILnpZN/x8yx4G680piUMY8s6kn7mvL/l4VEtxdDa22ApFgpDCdLB9q1ZAAAAAKe0iIHtx+1Z5TzMGs+6IcYPnJvgl4EGbYbVoV0Nih1fxLaPUovjPokVciZawhxvcCO5I3CHxC8SV01Lov9PtmQ==","ConnectionId":"2ccccb3d-025b-44b8-a193-536a59c6cb4f","KeepAliveTimeout":20.0,"DisconnectTimeout":30.0,"ConnectionTimeout":110.0,"TryWebSockets":true,"ProtocolVersion":"1.2","TransportConnectTimeout":5.0,"LongPollDelay":0.0}'
data = json.loads(data)
messages = signar_client.sse_connect(
    ConnectionToken=data["ConnectionToken"],
    ConnectionId=data["ConnectionId"])

for message in messages:
    print(message)