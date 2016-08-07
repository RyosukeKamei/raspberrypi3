# GPIOを制御するライブラリ
import wiringpi
# タイマーのライブラリ
import time
# 引数受け取り
import sys

# ブザーをつないだGPIO端子
buzzer_pin = 23

# 初期設定
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode( buzzer_pin, 1 )

# 引数
param = sys.argv

# 第1引数
# on  : 音が鳴る
# off : 音が止まる
order = param[1]

# 第2引数 音がなる秒数
second = int(param[2])

if order == "on":
    # 第1引数がonの時、音を鳴らす
    wiringpi.digitalWrite( buzzer_pin, 1 ) # 1 : 音を鳴らす
    print ("ブザーオン")
else:
    # 第1引数がoffの時、音を止める
    wiringpi.digitalWrite( buzzer_pin, 0 ) # 0 : 音を鳴らす
    print ("ブザーオフ")

if order == "on" and second > 0:
    # 秒数表示
    print (str(second)+"秒")

    # 秒数が1以上の場合、音を指定秒数だけ鳴らす
    time.sleep( second )
    wiringpi.digitalWrite( buzzer_pin, 0 ) # 音を止める
    print ("ブザーオフ")