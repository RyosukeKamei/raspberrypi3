# GPIOを制御するライブラリ
import wiringpi
# タイマーのライブラリ
import time
# 引数取得
import sys

# GPIO定義 LED
led1_pin = 23

# GPIO初期化
wiringpi.wiringPiSetupGpio()
wiringpi.pinMode( led1_pin, 1 )

# MCP3002（A/Dコンバータ）を接続したチャンネルを指定
SPI_CH = 0

# 読み込み対象のMCP3002（A/Dコンバータ）のアナログ入力チェンネルを指定
READ_CH = 0

# 明るさの閾値を引数指定
param = sys.argv
set_illuminance = int(param[1])

# SPI初期化
wiringpi.wiringPiSPISetup( SPI_CH, 1000000 )

while True:
    # LEDを消灯
    wiringpi.digitalWrite( led1_pin, 0 )

    # MCP3002（A/Dコンバータ）に送るデータを作成
    buffer = 0x6800 | ( 0x1800 * READ_CH )
    buffer = buffer.to_bytes( 2, byteorder='big' )
    
    # SPIを使ってCH0の値を取得
    wiringpi.wiringPiSPIDataRW( SPI_CH, buffer )
    
    # 値が2バイトに分かれて送られるので、1つの値にまとめる
    illuminance_value = ( buffer[0] * 256 + buffer[1] ) & 0x3ff
    
    # 明るさの閾値と照度を出力
    print ("明るさのしきい値 : " + str(set_illuminance) )
    print ("照度 : " + str(illuminance_value) )
    
    # 明るさの基準値を超えたら「明るい」下回ったら「暗い」と表示
    if ( illuminance_value > set_illuminance ):
        print ("明るいのでLEDを消灯")
        wiringpi.digitalWrite( led1_pin, 0 )
    else:
        print ("暗いのでLEDを点灯")
        wiringpi.digitalWrite( led1_pin, 1 )
    
    # 1秒ずつ検出
    time.sleep(1)