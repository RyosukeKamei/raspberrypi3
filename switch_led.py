# GPIOを制御するライブラリ
import wiringpi
# タイマーのライブラリ
import time
# 引数取得
import sys

# GPIO定義
led1_pin = 23
led2_pin = 24
switch_pin = 17


# 明るさの閾値を引数指定
param = sys.argv
set_interval = int(param[1])

# GPIO初期化
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode( led1_pin, 1 )
wiringpi.pinMode( led2_pin, 1 )
wiringpi.pinMode( switch_pin, 0 )

# どっちのLEDがついているか
led = 0

# この回路は永続的なので、止めるまで繰り返す
while True:
    # LEDを消灯
    wiringpi.digitalWrite( led1_pin, 0 )
    wiringpi.digitalWrite( led2_pin, 0 )
    
    # スライドスイッチを検出
    while ( wiringpi.digitalRead(switch_pin) == 1 ):
        # スイッチオン
        print("スイッチオン")
        
        if ( led == 0 ):
            # LED1を光らせる
            wiringpi.digitalWrite( led1_pin, 1 )
            wiringpi.digitalWrite( led2_pin, 0 )
            led = 1
            print("LED1")
        else:
            # LED2を光らせる
            wiringpi.digitalWrite( led1_pin, 0 )
            wiringpi.digitalWrite( led2_pin, 1 )
            led = 0
            print("LED2")
        # 引数で指定した秒数待機
        print(set_interval, "秒待機")
        time.sleep(set_interval)