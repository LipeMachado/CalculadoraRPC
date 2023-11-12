import zerorpc

class Calculadora:
    def sum(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiplication(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return a / b

server = zerorpc.Server(Calculadora())
server.bind("tcp://0.0.0.0:4242")
print("Server Running port 4242")
server.run()