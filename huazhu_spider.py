# -*- coding:utf-8 -*-

import encode_util

import requests
import json
import re
import sys



reload(sys)
sys.setdefaultencoding("utf-8")


headers ={'Accept':'*/*',
'Accept-Encoding':'gzip, deflate',
'Accept-Language':'zh-CN,zh;q=0.8',
'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}

class PriceSpider:
    def __init__(self):
        pass
 

    '''
    获取城市列表及id的函数，只需要调用一次，然后存储到文件，以后每次从文件中读取即可
    '''
    def getHotelCity(self):
        
        url = 'http://m.huazhu.com/Hotel/City'
        req = requests.get(url, headers = headers)
        content = req.content

        pattern = r'ndoo.vars.cities = (?P<data>.*?);'
        m = re.search(pattern,content)
        if m:
            cityInfo = m.group('data').encode('utf8')
            city_dict = json.loads(cityInfo, object_hook=encode_util.decode_dict)
            #格式转换,然后存到磁盘
            




    def getHotelPage(self,hotelId,inDate,outDate):
        url = 'http://m.huazhu.com/hotel/detail/'+hotelId+'?&CheckInDate='+inDate+'&CheckOutDate='+outDate


        url2 = 'https://api.growingio.com/v2/8f6e3e7f89d647cab9784afa81ea87bd/web/action'

        url3 = 'http://m.huazhu.com/Hotel/Price'

        headers ={'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36'}

        req = requests.get(url,headers=headers)
        _cookies = req.cookies

        postData = {'roomTypeID':'TRA'}

        price = requests.post(url3,data=postData,cookies=_cookies).content
        
        data = json.loads(price)['Data']['PriceCalender']
        for lev in data:
            print '%s\t%s' % (lev['MemberLevelDescript'],lev['DailyRoomPriceOfMemberList'][0]['Price'])
        


if __name__ == '__main__':
    #hotelId = '3001901'
    #inDate = '05/04/2016 00:00:00'
    #outDate = '05/05/2016 00:00:00'
    spider = PriceSpider()
   # spider.getHotelPage(hotelId, inDate, outDate)
    spider.getHotelCity()

