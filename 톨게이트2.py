from pin import pin
from time import sleep
import os

# RGB 램프 클래스
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

    def all_off(self):
        self.R(False)
        self.G(False)
        self.B(False)

# 핀 설정
TRIG_PIN = 18   # 초음파 센서 Trig 핀
ECHO_PIN = 23   # 초음파 센서 Echo 핀
SERVO_PIN = 24  # 서보모터 핀

RGB_R_PIN = 27  # RGB 빨강
RGB_G_PIN = 22  # RGB 초록
RGB_B_PIN = 17  # RGB 파랑

OPEN_ANGLE = 90         # 문 열림 각도
CLOSE_ANGLE = 0         # 문 닫힘 각도
DISTANCE_THRESHOLD = 80 # cm 임계 거리
DOOR_OPEN_TIME = 5      # 문 열림 유지 시간(초)

def main():
    os.system("sudo pigpiod")
    sleep(1)

    try:
        pin.Setup()
        lamp = RGBlamp(RGB_R_PIN, RGB_G_PIN, RGB_B_PIN)
        lamp.all_off()

        print("[준비] 문 닫힘 상태로 시작")
        pin.ServoWrite(SERVO_PIN, CLOSE_ANGLE)
        lamp.R(True)  # 빨강 램프 ON (문 닫힘)

        while True:
            distance = pin.GetDistance(TRIG_PIN, ECHO_PIN)

            if distance == -1:
                print("거리 측정 실패")
                lamp.all_off()
                lamp.B(True)  # 파랑 램프 ON (오류)
            else:
                print(f"측정 거리: {distance:.2f} cm")

                if distance < DISTANCE_THRESHOLD:
                    print("[동작] 문 열기")
                    pin.ServoWrite(SERVO_PIN, OPEN_ANGLE)
                    lamp.all_off()
                    lamp.G(True)  # 초록 램프 ON (문 열림)
                    #sleep(DOOR_OPEN_TIME)
                    # print("[동작] 문 닫기")
                    # pin.ServoWrite(SERVO_PIN, CLOSE_ANGLE)
                    # lamp.all_off()
                    # lamp.R(True)  # 빨강 램프 ON (문 닫힘)
                else:
                    lamp.all_off()
                    lamp.R(True)  # 빨강 램프 ON (문 닫힘)
                    pin.ServoWrite(SERVO_PIN, CLOSE_ANGLE)

            sleep(1)

    except KeyboardInterrupt:
        print("\n[종료] 사용자 종료")

    finally:
        pin.ServoStop(SERVO_PIN)
        lamp.all_off()
        os.system("sudo killall pigpiod")
        pin.Clean(all=True)
        print("[정리] pigpio 데몬 종료 & 핀 정리")

if __name__ == "__main__":
    main()
