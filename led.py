# GPIOを制御するライブラリ
import wiringpi
# タイマーのライブラリ
import time

# LEDを繋いだGPIOの端子番号
led_pin = 23 # 16番端子

# GPIO初期化
wiringpi.wiringPiSetupGpio()
# GPIOを出力モード（1）に設定
wiringpi.pinMode( led_pin, 1 )

# whileの処理は字下げをするとループの範囲になる（らしい）
while True:
    # GPIOを3.3VにしてLEDを点灯
	wiringpi.digitalWrite( led_pin, 1 )
	# 1秒待ち
	time.sleep(1)
	# GPIOを30VにしてLEDを消灯
	wiringpi.digitalWrite( led_pin, 0 )
	# 1秒待ち
	time.sleep(1)