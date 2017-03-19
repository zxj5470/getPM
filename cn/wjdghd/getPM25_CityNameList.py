# import requests
# import re
# from bs4 import BeautifulSoup
#
# url = 'http://www.pm25.in/'
# content = requests.get(url).content
# s = BeautifulSoup(content, 'html.parser')
# # find 1~22
# i = 1
# bottom = s.select('.unstyled')
# f = open('cityNameList.txt', 'w', encoding='utf-8')
# while i < 23:
#     b = bottom[i]
#     s = b.contents[3]
#     for each in s.find_all('a'):
#         st = str(each['href'][1:]) +','+ str(each.get_text())
#         f.write(st + '\r')
#     i += 1
# f.close()
