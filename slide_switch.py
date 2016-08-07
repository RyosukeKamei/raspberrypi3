# GPIOを制御するライブラリ
import wiringpi
# タイマーのライブラリ
import time

# GPIO端子の設定
switch_pin = 17

# GPIO出力モードを1に設定する
wiringpi.wiringPiSetupGpio()
# GPIOを入力モード(0)にする
wiringpi.pinMode( switch_pin, 0 )

while True:
    # GPIO端子の状態を読み込み
    # 0V : 0
    # 3.3V : 1
    if( wiringpi.digitalRead(switch_pin) == 1 ):
        print ("Switch ON")
    else:
        print ("Switch OFF")
    # 1秒ごとに検出
    time.sleep(1)