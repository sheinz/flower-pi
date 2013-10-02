import pyjsonrpc
import threading
from Hardware import Hardware

hw = {}

def rpc_light(turn):
    print("Lamp is turning {}".format(turn))
    if turn == 'on':
        hw['hardware'].turn_lamp_low()
    elif turn == 'off':
        hw['hardware'].turn_lamp_off()
    else:
        return "Unknown state"
    return "Success"


class RequestHandler(pyjsonrpc.HttpRequestHandler):

    # Register public JSON-RPC methods
    methods = {
        "light": rpc_light
    }


class RPCServer(object):
    
    def __init__(self, hardware):
        hw['hardware'] = hardware
        # Threading HTTP-Server
        self.http_server = pyjsonrpc.ThreadingHttpServer(
            server_address = ('0.0.0.0', 8000),
            RequestHandlerClass = RequestHandler
        )
    
    def _run(self):
        print("Starting RPC HTTP server...")
        self.http_server.serve_forever()
    
    def start(self):
        self.thread = threading.Thread(target=self._run)
        self.thread.daemon = True
        print("Starting thread...")
        self.thread.start()


    
    