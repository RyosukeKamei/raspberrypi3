# GPIOを制御するライブラリ
import wiringpi
# タイマーのライブラリ
import time
# 引数取得
import sys

# 74HC5411（7セグメントドライバー）に接続しているGPIO端子番号を指定
d0_pin = 18
d1_pin = 23
d2_pin = 24
d3_pin = 25

# 各端子を出力モードにする
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode( d0_pin, 1 )
wiringpi.pinMode( d1_pin, 1 )
wiringpi.pinMode( d2_pin, 1 )
wiringpi.pinMode( d3_pin, 1 )

# 初期化 すべて0にする
wiringpi.digitalWrite( d0_pin, 0 )
wiringpi.digitalWrite( d1_pin, 0 )
wiringpi.digitalWrite( d2_pin, 0 )
wiringpi.digitalWrite( d3_pin, 0 )

# 引数取得
param = sys.argv
set_number = int(param[1])

if( set_number >= 0 and set_number < 10):
    # 1ビット目のANDをとる
    wiringpi.digitalWrite( d0_pin, set_number & 0x01 )

    # 2ビット目のANDをとる
    wiringpi.digitalWrite( d1_pin, set_number & 0x02 )

    # 3ビット目のANDをとる
    wiringpi.digitalWrite( d2_pin, set_number & 0x04 )

    # 4ビット目のANDをとる
    wiringpi.digitalWrite( d3_pin, set_number & 0x08 )
else:
    print("エラー : 引数は0から9までです。")