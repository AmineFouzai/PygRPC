import os 
import service_pb2 as ResponseHandler
import service_pb2_grpc as PubSubHandler
import grpc
import time
def run():
    res="hello world"
    with grpc.insecure_channel("localhost:8000") as channel:
            stub=PubSubHandler.RequestServiceStub(channel)
            while True:
                try:
                    start=time.time()
                    response=stub.RequestHandler(ResponseHandler.Response(res=res))
                    print(response.res)
                except KeyboardInterrupt as e:
                    print(e)
                    channel.subscribe(close)
                    exit()
def close(channel):
    channel.close()

if __name__ == '__main__':
    run()
    
