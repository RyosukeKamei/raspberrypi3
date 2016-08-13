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

# スイッチの初期状態
switch_status = wiringpi.digitalRead(button_pin)

# whileの処理は字下げをするとループの範囲になる
while True:
    # スイッチの状態を検知
    print("スイッチの初期値", switch_status)
    print("取得したスイッチの状態", wiringpi.digitalRead(button_pin))
    
    # スイッチが変化したらモータを動かす
    if( wiringpi.digitalRead(button_pin) != switch_status ):
        print ("3秒だけモータを動かす")
        # モーターを回転
        wiringpi.digitalWrite( motor1_pin, 1 )
        wiringpi.digitalWrite( motor2_pin, 1 )
        time.sleep(3)
        wiringpi.digitalWrite( motor1_pin, 1 )
        wiringpi.digitalWrite( motor2_pin, 0 )
        switch_status = wiringpi.digitalRead(button_pin)
        
    # 0.5秒ごとにイベントキャッチ
    time.sleep(0.5)