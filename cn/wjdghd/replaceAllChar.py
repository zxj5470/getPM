# coding : utf-8
import os

f_list = os.listdir('../')
os.mkdir('../New')
for i in f_list:
    if os.path.splitext(i)[1] == '.csv':
        print(str(i))
        try:
            f = open('../' + str(i), 'rb')
            f2 = open('../New/'+str(i), 'wb')
            all_the_text = f.read()
            strall = str(all_the_text, encoding='gbk')
            strall = strall.replace("\n", "", 100000000).replace("\r\n", "", 100000000).replace('  ', '',100000000).replace('\r\r', '\r', 100000000)
            f2.write(bytes(strall, encoding='gbk'))
        finally:
            f.close()
            f2.close()
