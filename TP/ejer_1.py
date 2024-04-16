import subprocess

class Ping:
    def execute(self, ip_address):
        if ip_address.startswith("192."):
            for _ in range(10):
                result = subprocess.run(['ping', '-c', '1', ip_address], stdout=subprocess.PIPE)
                print(result.stdout.decode())
        else:
            print("La dirección IP no comienza con '192.' y no se puede ejecutar el ping.")

    def executefree(self, ip_address):
        for _ in range(10):
            result = subprocess.run(['ping', '-c', '1', ip_address], stdout=subprocess.PIPE)
            print(result.stdout.decode())

class PingProxy:
    def __init__(self):
        self.ping = Ping()

    def execute(self, ip_address):
        if ip_address == "192.168.0.254":
            self.ping.executefree("www.google.com")
        else:
            self.ping.execute(ip_address)

# Ejemplo de uso
ping_proxy = PingProxy()
ping_proxy.execute("192.168.0.1")
ping_proxy.execute("192.168.0.254")
ping_proxy.execute("8.8.8.8")
