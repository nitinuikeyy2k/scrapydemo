# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scrapydemo.items import ScrapydemoItem

class NyusatsuSpider(scrapy.Spider):
    name = 'nyusatsu'
    allowed_domains = ['www.mod.go.jp']
    start_urls = ['https://www.mod.go.jp/gsdf/eae/kaikei/eafin/nyusatsu_gyousyu.html#buppinn/']

    def _check_blank(self, data):
        if data is None:
            return ""
        return data

    def _make_absoluteURL(self, response, link):
        print("link - ", link)
        if link:
            data = response.urljoin(link.get())
        else:
            data = None
        return data

    def parse(self, response):
        rows = response.xpath("//table[@class='left_caption'][1]/tbody/tr")
        for row in rows:
            loader = ItemLoader(item=ScrapydemoItem())
            data1 = self._check_blank(row.xpath(".//td[1]/text()").get())
            data2 = self._check_blank(row.xpath(".//td[2]/text()").get())

            data3 = self._make_absoluteURL(
                response, row.xpath(".//td[3]//@href"))            
            loader.add_value("file_urls", data3)

            data4 = self._make_absoluteURL(
                response, row.xpath(".//td[4]//@href"))
            loader.add_value("file_urls", data4)
            data5 = self._make_absoluteURL(
                response, row.xpath(".//td[5]//@href"))
            loader.add_value("file_urls", data5)
            data6 = self._make_absoluteURL(
                response, row.xpath(".//td[6]//@href"))
            loader.add_value("file_urls", data6)
            data7 = self._make_absoluteURL(
                response, row.xpath(".//td[7]//@href"))
            loader.add_value("file_urls", data7)
            data8 = self._make_absoluteURL(
                response, row.xpath(".//td[8]//@href"))
            loader.add_value("file_urls", data8)

            data9 = self._check_blank(row.xpath(".//td[9]/text()").get())

            yield{
                '駐屯地名': data1,
                '実施会計隊': data2,
                '品　　名': data3,
                '内訳書・仕様書等1': data4,
                '内訳書・仕様書等2': data5,
                '内訳書・仕様書等3': data6,
                '内訳書・仕様書等4': data7,
                '内訳書・仕様書等5': data8,
                '入札日': data9
            }
            yield loader.load_item()

