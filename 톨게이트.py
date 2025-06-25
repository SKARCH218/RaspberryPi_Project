from pin import pin
from time import sleep
import os

TRIG_PIN = 18   # 초음파 센서 Trig 핀
ECHO_PIN = 23   # 초음파 센서 Echo 핀
SERVO_PIN = 24  # 서보모터 핀

OPEN_ANGLE = 90   # 문 열릴 때 서보 각도
CLOSE_ANGLE = 0   # 문 닫힐 때 서보 각도
DISTANCE_THRESHOLD = 80  # cm 이하 거리에서 문 열림
DOOR_OPEN_TIME = 5       # 문이 열려있는 시간 (초)

def main():
    # pigpio 데몬 실행
    os.system("sudo pigpiod")
    sleep(1)

    try:
        print("[시작] Setup() 호출")
        pin.Setup()

        print("[준비] 문 닫힘 상태로 시작")
        pin.ServoWrite(SERVO_PIN, CLOSE_ANGLE)

        while True:
            distance = pin.GetDistance(TRIG_PIN, ECHO_PIN)
            if distance == -1:
                print("거리 측정 실패")
            else:
                print(f"측정 거리: {distance:.2f} cm")

                if distance < DISTANCE_THRESHOLD:
                    print("[동작] 문 열기")
                    pin.ServoWrite(SERVO_PIN, OPEN_ANGLE)
                    sleep(DOOR_OPEN_TIME)
                    print("[동작] 문 닫기")
                    pin.ServoWrite(SERVO_PIN, CLOSE_ANGLE)

            sleep(1)  # 1초 간격 반복

    except KeyboardInterrupt:
        print("\n[종료] 사용자 종료")

    finally:
        pin.ServoStop(SERVO_PIN)
        os.system("sudo killall pigpiod")
        pin.Clean()
        print("[정리] pigpio 데몬 종료 & 핀 정리")

if __name__ == "__main__":
    main()
