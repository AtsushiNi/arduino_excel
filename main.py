import serial # シリアル通信用ライブラリ
import re # データを正規表現で切り分けるのに使うライブラリ
import numpy as np # 配列の操作用ライブラリ

# 定数
PORT = 'COM5' # ArduinoのCOMポート

# データを格納する配列
number = np.empty(0)
time = np.empty(0)
value1 = np.empty(0)
value2 = np.empty(0)

ser = serial.Serial(PORT, 9600) # ボーレートは9600にしている

while True:
  line = ser.readline()
  try:
    # ここからは状況次第で書き換えて!
    string_line = line.decode().rstrip('\r\n') # バイト文字から文字列へ変換した後、改行コードを削除
    data_sets = re.split(',', string_line) # data_sets: 1行分のデータの配列
    print(data_sets)

    for data_set in data_sets:
      data = re.split(':', data_set) # data[0]: 値の名前, data[1]: 値

      if data[0] == 'number':
        np.append(number, int(data[1]))
      elif data[0] == 'time':
        np.append(time, int(data[1]))
      elif data[0] == 'value1':
        np.append(value1, float(data[1]))
      elif data[0] == 'value2':
        np.append(value2, float(data[1]))

  except UnicodeDecodeError: # 受信したデータがおかしいときのエラー処理
    print('ERROR!!!')
    print(line)