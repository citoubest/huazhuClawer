# -*- coding:utf-8 -*-

import requests
import json
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

class PriceSpider:
    def __init__(self):
    
    def GetHotelPage(self,hotelId,inDate,outDate):
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
    hotelId = '3001901'
    inDate = '05/04/2016 00:00:00'
    outDate = '05/05/2016 00:00:00'
    spider = PriceSpider()
    spider.GetHotelPage(hotelId, inDate, outDate)


