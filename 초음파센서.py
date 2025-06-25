from pin import pin
from time import sleep
from os import system

TRIG_PIN = 18
ECHO_PIN = 23
sec = 0

def setup():
    pin.Setup()

def loop():
    global sec
    distance = pin.GetDistance(TRIG_PIN, ECHO_PIN)
    if distance == -1:
        print("초과 거리 또는 신호 없음")
    else:
        print(f"거리: {distance:.2f} cm")
    sec += 1
    print(f"측정 횟수: {sec}")
    sleep(1)
    system("clear")

def main():
    setup()
    try:
        while True:
            loop()
    except KeyboardInterrupt:
        print("\n프로그램 종료")
    finally:
        pin.Clean()

if __name__ == "__main__":
    main()
