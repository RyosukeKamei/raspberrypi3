# GPIOを制御するライブラリ
import wiringpi
# タイマーのライブラリ
import time

# ボタンスイッチを繋いだGPIOの端子番号
button_pin = 17 # 11番端子
# GPIO端子の設定
motor1_pin = 23 # 16番端子
motor2_pin = 24 # 18番端子

# GPIO初期化
wiringpi.wiringPiSetupGpio()

# ボタンスイッチを入力モード（0）に設定
wiringpi.pinMode( button_pin  , 0 )

# モータードライバーは出力モード（1）に設定
wiringpi.pinMode( motor1_pin, 1 )
wiringpi.pinMode( motor2_pin, 1 )


# 端子に何も接続されていない場合の状態を設定
# 3.3Vの場合には「2」（プルアップ）
# （0Vの場合は「1」と設定する（プルダウン））
wiringpi.pullUpDnControl( button_pin  , 2 )

# whileの処理は字下げをするとループの範囲になる
while True:
    # GPIO端子の状態を読み込む
    # ボタンを押すと直進
    # GPIOの状態が0V(0)であるか比較
    if( wiringpi.digitalRead(button_pin) == 1 ):
        # ボタンを離している時は「3.3V(1)」
        # （1の場合に停止というのもわかりにくい）
        print ("停止")
        # モーターを停止
        wiringpi.digitalWrite( motor1_pin, 1 )
        wiringpi.digitalWrite( motor2_pin, 0 )
    else:
        # ボタンを押している時は「0V(0)」
        print ("直進")
        # モーターを回転
        wiringpi.digitalWrite( motor1_pin, 1 )
        wiringpi.digitalWrite( motor2_pin, 1 )
    time.sleep(0.5)