# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
from urllib.parse import urlparse

from scrapy.pipelines.files import FilesPipeline
from scrapydemo.spiders.nyusatsu import NyusatsuSpider
from datetime import datetime

class ScrapydemoPipeline(object):
    def process_item(self, item, spider):
        return item

class MyFilesPipelines(FilesPipeline):

    def file_path(self, request, response=None, info=None):
        print("request url :",request.url)
        print("os path :", os.path.basename(urlparse(request.url).path))
        now = datetime.now()
        time = now.strftime("%d-%b-%Y") + os.path.sep + NyusatsuSpider.name + os.path.sep 
        return time + os.path.basename(urlparse(request.url).path)
