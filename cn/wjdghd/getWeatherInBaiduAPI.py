import requests

from cn.wjdghd.ReadCityNameForList import get_all

lis = get_all(1)
i = 0
for each in lis:
    cityName = lis[each]
    url = 'http://api.map.baidu.com/telematics/v3/weather'
    postParam = {
        'location': str(cityName),
        'output': 'json',
        'ak': 'ci3WuAddC7PzAuwshgZQA0db39frBF5a'
    }
    r = requests.get(url, postParam)
    r.encoding = 'utf-8'
    print(r.text)
