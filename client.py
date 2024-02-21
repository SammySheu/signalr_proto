from signalr import Connection
from signalr.hubs import Hub
import certifi
import requests
import logging
# import threading
import time
# from dotenv import load_dotenv
# load_dotenv()
# import ssl

def signalr_threading():
    # The URL of the SignalR server.
    server_url = 'https://10.21.1.211:443/KPCT_2nd_CMS_API/signalr/hubs'
    hub_name = 'norisHub'

    # session.status
    session = requests.Session()
    self_cert = certifi.where()
    self_cert = self_cert.replace("cacert.pem", "Self.pem")
    session.verify = self_cert
    # ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    # ssl_context.load_verify_locations(self_cert)
    # session.cert = self_cert

    # Create a connection object.
    connection = Connection(url=server_url, session=session)

    hub: Hub = connection.register_hub(hub_name)
    # hub.server.invoke('send', 'Python is here')

    

    # Define a handler for the system notification.
    def notifyValues():
        values = "HHH"
        print('Values notification received:', values)
        with open(file="write.txt", mode="a") as file_writer:
            file_writer.write("values")

        # logging.error("Helloworld")

    # create error handler
    def print_error(error):
        print('error: ', error)

    
    connection.received += notifyValues
    connection.error += print_error
    # hub.server.invoke("NotifyValues")
    hub.client.on('notifySubscriptionStatus.', notifyValues)
    with open(file="write.txt", mode="a") as file_writer:
        file_writer.write("Start signalr listening")
    # Start the connection.
    connection.start()

    print("\n\n\n\n\n", connection.id)
    # connection.listener_thread.start()
    # connection.wait(30000)
signalr_threading()
# time.sleep(300)
# a = threading.Thread(target=signalr_threading, name="signalr")
# a.start()
# a.join()
# Keep the script running.
while True:
    pass