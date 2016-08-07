# GPIOを制御するライブラリ
import wiringpi
# タイマーのライブラリ
import time
# 引数取得
import sys

# サーボモータに接続したGPIO端子番号を指定
servo_pin  =  18
# サーボモータを動かす角度を指定する
# set_degree = 90 デフォルト
# 引数指定
param = sys.argv
set_degree = int(param[1])
print(set_degree)

wiringpi.wiringPiSetupGpio()
# ハードウェアPWMで出力する
wiringpi.pinMode( servo_pin, 2 )
# サーボモータに合わせたPWM波形の設定
wiringpi.pwmSetMode(0)
wiringpi.pwmSetRange(1024)
wiringpi.pwmSetClock(375)

# 指定した角度が動作範囲内の場合のみサーボモータを制御
if ( set_degree <= 90 and set_degree >= -90 ):
	# 角度から送り出すPWMのパルス幅を算出する
	move_deg = int( 81 + 41 / 90 * set_degree )
	# サーボモータにPWMを送り、サーボモータを動かす
	wiringpi.pwmWrite( servo_pin, move_deg )