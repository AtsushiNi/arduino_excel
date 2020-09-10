# arduino_excel
ArduinoからPCへのシリアル通信の内容をExcelファイルに書き出し、保存するプログラム

# Files
main.py -- pythonのプログラムファイル
example/example.ino -- Arduinoのサンプルプログラム

# Installation
```
pip install pyserial
pip install numpy
pip install openpyxl
```
logs/にlog.xlsx(Excelファイル)を作る(空でなくてもいいが上書きされる)  
ArduinoをPCに接続する  
ArduinoのCOMポートを調べて、コード中のPORTに書く
```
python main.py
```

# Libraries
- pySerial: シリアル通信用ライブラリ  
参考URL: https://github.com/AtsushiNi/arduino_excel.git

- numpy: 配列の操作用ライブラリ  
参考URL: https://udemy.benesse.co.jp/ai/python-numpy.html

- openpyxl: Excel操作用のライブラリ  
参考URL: https://gammasoft.jp/support/how-to-use-openpyxl-for-excel-file/

# Note
- ボーレートは9600にしている(コードの該当箇所を編集すれば変更可能)
- ArduinoのコードでSerial.writeを使うとうまくいかない可能性あり。Serial.printlnを使うべし
- LOG_FILE_NAMEの名前のファイルは実行すると上書きされるので注意
- LOG_FILE_NAMEの名前のExcelファイルが存在しないとエラーになるので注意
- Excelファイルはgit・githubで管理しない方がいいかも

# Sample
example/example.inoをArduinoIDEで書き込み、pythonを実行  
データの順番・時間・値1・値2をそれぞれ,と:区切りで出力した場合のサンプル