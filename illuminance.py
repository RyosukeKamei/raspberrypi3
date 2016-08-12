# GPIOを制御するライブラリ
import wiringpi
# タイマーのライブラリ
import time
# 引数取得
import sys

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
        print ("明るい")
    else:
        print ("暗い")
    
    # 1秒ずつ検出
    time.sleep(1)