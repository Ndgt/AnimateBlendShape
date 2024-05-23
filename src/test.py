# coding: shift-jis

import sys
# rye���Ȃ̂Œǉ�
sys.path.append(r"C:\Users\owner\AppData\Local\Programs\Python\Python311\Lib\site-packages")
from pykakasi import kakasi

args = sys.argv

if len(args) > 1:
    kks = kakasi()
    f = open(args[1],"r")
    data = f.readlines()
    for words in data:
        if not words == '\n':
            line = words.strip().replace(" ", "").replace("�H","")
            result = kks.convert(line)
            dst_str = ""
            for j in range(len(result)):
                if len(args) > 2 and args[2] == "hira":
                    dst_str += result[j]["hira"] # ������
                else:
                    dst_str += result[j]["hepburn"] # �A���t�@�x�b�g
            print(dst_str)
else:
    print("no arguments")