# GPIOを制御するライブラリ
import wiringpi
# タイマーのライブラリ
import time
# 引数取得
import sys

# GPIO端子の設定
motor1_pin = 23
motor2_pin = 24

# 引数
param = sys.argv

# 第1引数
# go : 回転
# back : 逆回転
# break : ブレーキ
order = param[1]

# 第2引数 秒数
second = int(param[2])

# GPIO出力モードを1に設定する
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode( motor1_pin, 1 )
wiringpi.pinMode( motor2_pin, 1 )

if order == "go":
    if second == 0:
        print("回転 止めるときはbreak 0コマンド！")
    else:
        print(str(second)+"秒回転")
    wiringpi.digitalWrite( motor1_pin, 1 )
    wiringpi.digitalWrite( motor2_pin, 0 )
    time.sleep(second)
elif order == "back":
    if second == 0:
        print("逆回転 止めるときはbreak 0コマンド！")
    else:
        print(str(second)+"秒逆回転")    
    wiringpi.digitalWrite( motor1_pin, 0 )
    wiringpi.digitalWrite( motor2_pin, 1 )
    time.sleep(second)

# 第2引数が0の場合は、ブレーキをしない
# 第1引数がbreakの場合は、ブレーキ
if order == "break" or second != 0:
    print("ブレーキ！")
    wiringpi.digitalWrite( motor1_pin, 1 )
    wiringpi.digitalWrite( motor2_pin, 1 )