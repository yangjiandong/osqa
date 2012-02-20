#!/usr/bin/envs python
#-*- coding: utf-8 -*-#
# 秒杀卓越apple
# HTMLParser.HTMLParseError: malformed start tag, at line 850, column 700 

import winsound
import urllib2
import time
from BeautifulSoup import *
from urlparse import urljoin
 
def monitor(url):
    lastPrice=0
    mp3 = r"C:\maimai.wav"
    while True:
        try:
            page = urllib2.urlopen(url)
        except:
            print "could not open page %s" % url
            continue
        soup = BeautifulSoup(page.read())
        priceTag = soup('b',"priceLarge")
        price = priceTag[0].string
        print price
        if lastPrice == 0:
            lastPrice = price
        if price != lastPrice:
            winsound.PlaySound(mp3, winsound.SND_ASYNC)
        lastPrice = price
    

        time.sleep(30)

if __name__ == '__main__':
    monitor("http://www.amazon.cn/gp/product/B004PYEGE8/ref=s9_simh_gw_p147_d0_i1?pf_rd_m=A1AJ19PSB66TGU&pf_rd_s=center-1&pf_rd_r=0JW1WWYZ20YWJ1A7A29B&pf_rd_t=101&pf_rd_p=58840952&pf_rd_i=899254051")

 

