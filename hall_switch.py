# GPIOを制御するライブラリ
import wiringpi
# タイマーのライブラリ
import time

# GPIO端子の設定
hall_switch_pin = 17

# GPIO出力モードを1に設定する
wiringpi.wiringPiSetupGpio()
# GPIOを入力モード(0)にする
wiringpi.pinMode(hall_switch_pin, 0)
# 入力はプルアップに設定
wiringpi.pullUpDnControl(hall_switch_pin, 2)

while True:
    # GPIO端子の状態を読み込み
    # S極 : 0
    # N極 : 1
    if( wiringpi.digitalRead(hall_switch_pin) == 1 ):
        # 入力が0の時がS極
        print ("South Pole")
    else:
        print ("North Pole")
    # 1秒ごとに検出# 出力が1の時がN極
    time.sleep(1)