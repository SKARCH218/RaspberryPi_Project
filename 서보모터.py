from pin import pin
from time import sleep
import os

SERVO_PIN = 24  # 서보모터 제어 핀

def main():
    # pigpio 데몬 실행 (없으면 자동 시작)
    os.system("sudo pigpiod")
    sleep(1)  # 데몬 기동 대기

    try:
        print("[시작] Setup() 호출")
        pin.Setup()

        print("[서보] 0도")
        pin.ServoWrite(SERVO_PIN, 0)
        sleep(1)

        print("[서보] 90도")
        pin.ServoWrite(SERVO_PIN, 90)
        sleep(1)

        print("[서보] 180도")
        pin.ServoWrite(SERVO_PIN, 180)
        sleep(1)

        print("[서보] 90도")
        pin.ServoWrite(SERVO_PIN, 90)
        sleep(1)

        print("[서보] 멈춤")
        pin.ServoStop(SERVO_PIN)

    except KeyboardInterrupt:
        print("\n[종료] 사용자가 종료함")

    finally:
        # pigpio 데몬 종료
        os.system("sudo killall pigpiod")
        print("[정리] pigpio 데몬 종료")

if __name__ == "__main__":
    main()
