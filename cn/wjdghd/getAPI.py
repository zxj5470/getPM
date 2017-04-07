import requests
import os
from bs4 import BeautifulSoup
from ReadCityNameForList import get_all
from getTime import get_time

time = str(get_time())
name = str('../temp_' + time + '_PM.csv')
f = open(name, 'w', encoding='GBK')
url = 'http://www.pm25.in/'
cityName = ''
lis = get_all()
page = 0
flag = 0
for each in lis:
    page += 1
    if page % 30 == 0:
        print(page)
    cityName = lis[each]
    r = requests.get(url + cityName)
    r.encoding = 'utf-8'
    b = BeautifulSoup(r.text, 'html.parser')
    cityName = str(b.select('.city_name')[0].select('h2')[0].get_text())
    dataTime = str(b.select('.live_data_time')[0].select('p')[0].get_text()[7:])
    averLevel = str(b.select('.level')[0].get_text().replace(' ', '', 10000).replace('\n', '', 10000))
    AQI = b.select('.span12 > .span1')
    length = AQI.__len__()
    i = 0
    averInfo = {}
    while i < length - 1:
        temp = AQI[i]
        value = str(temp.find_all('div', {'class': 'value'})[0].get_text()).replace(' ', '', 10000)
        value = value.replace('\n', '', 10000).replace('\r\n\r\n', '\r\n', 10000)
        caption = str(temp.find_all('div', {'class': 'caption'})[0].get_text()).replace(' ', '', 10000)
        caption = caption.replace('\n', '', 10000).replace('\r\n\r\n', '\r\n', 10000)
        averInfo[caption] = value
        i += 1
    table = b.select('tr')
    inl = table.__len__()
    trLength = table[0].select('th')

    info = {}
    valueList = {}
    list = {}
    captionList = {}

    if flag == 0:
        captionList[0] = '城市名称'
        captionList[1] = '获取时间'
        captionList[2] = '空气质量'
        i = 3
        for e in trLength:
            captionList[i] = e.get_text()
            i += 1
        flag = 1
        for eachrow in captionList:
            f.write(str(captionList[eachrow]) + ',')
    i = 1
    while i < inl:
        trLength = table[i].select('td')
        valueList = {}
        if i == 1:
            valueList[0] = cityName
            valueList[1] = dataTime
            valueList[2] = averLevel
        else:
            valueList[0] = ''
            valueList[1] = ''
            valueList[2] = ''
        j = 3
        for e in trLength:
            valueList[j] = e.get_text()
            j += 1
        list[i] = valueList
        i += 1
    for eachCon in list:
        f.write('\r')
        for eachOne in list[eachCon]:
            f.write(str(list[eachCon][eachOne]) + ',')
    f.write('\r')
f.close()
f = open(name, 'rb')
f2 = open('../' + time + '_PM.csv', 'wb')
try:
    all_the_text = f.read()
    strall = str(all_the_text, encoding='gbk')
    strall = strall.replace("\r\n", "", 100000000).replace('\r\r', '\r', 100000000).replace('  ', '', 100000000)
    f2.write(bytes(strall, encoding='gbk'))
finally:
    f.close()
    os.remove(name)
    f2.close()
