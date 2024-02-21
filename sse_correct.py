import requests
import certifi
from sseclient import SSEClient

session = requests.Session()
self_cert = certifi.where()
self_cert = self_cert.replace("cacert.pem", "Self.pem")
session.verify = self_cert
sse_url = 'https://10.21.1.211/KPCT_2nd_CMS_API/signalr/connect?transport=serverSentEvents&connectionData=%5B%7B%22name%22%3A+%22norisHub%22%7D%5D&ConnectionToken=AQAAANCMnd8BFdERjHoAwE%2FCl%2BsBAAAAhhmmaWXu6ku7IfZ4f23y3wAAAAACAAAAAAAQZgAAAAEAACAAAABurxCvv0Dfn44CQcFeuReogSYexrjcCi3w0hKmsNRd%2FwAAAAAOgAAAAAIAACAAAABbkr7ZpOhlT7GdoWasfD1CV8B%2BJk3fh6PZr8mAH9fY5zAAAABFlKK1PHdILnpZN%2Fx8yx4G680piUMY8s6kn7mvL%2Fl4VEtxdDa22ApFgpDCdLB9q1ZAAAAAKe0iIHtx%2B1Z5TzMGs%2B6IcYPnJvgl4EGbYbVoV0Nih1fxLaPUovjPokVciZawhxvcCO5I3CHxC8SV01Lov9PtmQ%3D%3D&ConnectionId=2ccccb3d-025b-44b8-a193-536a59c6cb4f'
sse_url - 'https://10.21.1.211/KPCT_2nd_CMS_API/signalr/connect?transport=serverSentEvents&connectionData=%5B%7B%22name%22%3A+%22norisHub%22%7D%5D&ConnectionToken=AQAAANCMnd8BFdERjHoAwE%2FCl%2BsBAAAAhhmmaWXu6ku7IfZ4f23y3wAAAAACAAAAAAAQZgAAAAEAACAAAABurxCvv0Dfn44CQcFeuReogSYexrjcCi3w0hKmsNRd%2FwAAAAAOgAAAAAIAACAAAABbkr7ZpOhlT7GdoWasfD1CV8B%2BJk3fh6PZr8mAH9fY5zAAAABFlKK1PHdILnpZN%2Fx8yx4G680piUMY8s6kn7mvL%2Fl4VEtxdDa22ApFgpDCdLB9q1ZAAAAAKe0iIHtx%2B1Z5TzMGs%2B6IcYPnJvgl4EGbYbVoV0Nih1fxLaPUovjPokVciZawhxvcCO5I3CHxC8SV01Lov9PtmQ%3D%3D&ConnectionId=2ccccb3d-025b-44b8-a193-536a59c6cb4f'
messages = SSEClient(url=sse_url,
                     session=session)

for message in messages:
    print(message)