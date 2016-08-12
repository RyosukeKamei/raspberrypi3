# GPIOを制御するライブラリ
import wiringpi
# タイマーのライブラリ
import time
# 引数取得 使わない
# import sys

# MCP3002（A/Dコンバータ）を接続したチャンネルを指定
SPI_CH = 0

# 読み込み対象のMCP3002（A/Dコンバータ）のアナログ入力チェンネルを指定
READ_CH = 0

# SPI初期化
wiringpi.wiringPiSPISetup( SPI_CH, 1000000 )

while True:
    # MCP3002（A/Dコンバータ）に送るデータを作成
    buffer = 0x6800 | ( 0x1800 * READ_CH )
    buffer = buffer.to_bytes( 2, byteorder='big' )
    
    # SPIを使ってCH0の値を取得
    wiringpi.wiringPiSPIDataRW( SPI_CH, buffer )
    
    # 値が2バイトに分かれて送られるので、1つの値にまとめる
    input_value = ( buffer[0] * 256 + buffer[1] ) & 0x3ff
    
    # 入力値を電圧に変換
    volt = input_value * 3.3 / 1023
    
    # 取得した電圧に100をかけると温度が求められる
    temperature = volt * 100
    
    # 表示
    print ("温度 : ", temperature, " 電圧 : ", volt)
    
    # 1秒ずつ検出
    time.sleep(1)