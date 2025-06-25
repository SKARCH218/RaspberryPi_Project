from pin import pin
from time import sleep

class RGBlamp:
    def __init__(self, R, G, B):
        self.R_pin = R
        self.G_pin = G
        self.B_pin = B

    def R(self, x=True):
        pin.Write(self.R_pin, int(x))

    def G(self, x=True):
        pin.Write(self.G_pin, int(x))

    def B(self, x=True):
        pin.Write(self.B_pin, int(x))

lamp = None

def setup():
    global lamp
    pin.Setup()
    lamp = RGBlamp(27, 22, 17)

def loop():
    lamp.R(True)
    sleep(1)
    lamp.R(False)
    lamp.G(True)
    sleep(1)
    lamp.G(False)
    lamp.B(True)
    sleep(1)
    lamp.B(False)

def main():
    try:
        setup()
        while True:
            loop()
    finally:
        pin.Clean()

if __name__ == "__main__":
    main()
