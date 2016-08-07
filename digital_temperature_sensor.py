# 準備
# $ sudo apt-get install libi2c-dev 
# $ sudo sh -c 'echo "options i2c_bcm2708 combined=1" >> /etc/modprobe.d/i2c.conf'

# GPIOを制御するライブラリ
import wiringpi
# タイマーのライブラリ
import time
# I2Cデバイスからの読み取りに必要なライブラリを呼び出す
import os
import struct

# I2Cのインスタンスを作成
wiringpi.wiringPiSetup()
i2c = wiringpi.I2C()

# I2Cの設定
# 通信する機器のI2Cアドレスを指定
temperture_dev = i2c.setup(0x48)

# 温度を16ビットのデータ取得
# その他めレジスタ0x03に設定
i2c.writeReg8(temperture_dev, 0x03, 0x80)

while True:
    # 温度センサーの2バイト分を読み取る
    temperture_data = struct.unpack('2B', os.read(temperture_dev, 2))

    # 値が2バイトずつ分かれるので1つにまとめる
    temperture = ( ( temperture_data[0] << 8 ) + temperture_data[1] )

    # 負の値の場合は数値を変換
    if ( temperture_data[0] >= 0x80 ):
        temperture = temperture - 65536

    # 取得した値を128で割って温度を算出
    temperture = temperture / 128

    # 温度表示
    print ( "温度 " , temperture , "C" )

    # 1秒ごと
    time.sleep(1)