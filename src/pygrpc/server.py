from concurrent import futures
import grpc
import service_pb2 as ResponseHandler
import service_pb2_grpc as PubSubHandler
import time
import threading

class Listener(PubSubHandler.RequestServiceServicer):
    
    def RequestHandler(self,request,context):
        print(request.req)
        return ResponseHandler.Response(res=request.req)

def serve():
    server=grpc.server(futures.ThreadPoolExecutor(max_workers=1))
    PubSubHandler.add_RequestServiceServicer_to_server(Listener(),server)
    server.add_insecure_port("[::]8000")
    server.start()
    try:
        print("[$] => server is runing on port 8000")
        print("[$] => server on :threds %i" % (threading.activeCount()))
            
    except KeyboardInterrupt :
        print(e)
        server.stop(0)

if __name__ == "__main__":
    while True:
        serve()