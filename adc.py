# GPIOを制御するライブラリ
import wiringpi
# タイマーのライブラリ
import time

# MCP3002（半固定抵抗）を接続したチャンネルを指定
SPI_CH = 0

# 読み込み対象のMCP3002（半固定抵抗）のアナログ入力チェンネルを指定
READ_CH = 0

# SPI初期化
wiringpi.wiringPiSPISetup( SPI_CH, 1000000 )

while True:
    # MCP3002（半固定抵抗）に送るデータを作成
    buffer = 0x6800 | ( 0x1800 * READ_CH )
    buffer = buffer.to_bytes( 2, byteorder='big' )
    
    # SPIを使ってCH0の値を取得
    wiringpi.wiringPiSPIDataRW( SPI_CH, buffer )
    # 値が2バイトに分かれて送られるので、1つの値にまとめる
    ch0_value = ( buffer[0] * 256 + buffer[1] ) & 0x3ff
    # 値を電圧に変換
    volt = ch0_value * 3.3 / 1023
    # 0.5秒ごと
    time.sleep(0.5)
    print ("値 :" , ch0_value , " 電圧 :", volt , "V")