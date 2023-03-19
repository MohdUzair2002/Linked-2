# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from traceback import print_exception
import scrapy
from scrapy.loader.processors import Join, MapCompose, TakeFirst

class Linked2Item(scrapy.Item):
    Title = scrapy.Field()
    Price = scrapy.Field()
    Description = scrapy.Field()
    ProductID = scrapy.Field()
    Sellername = scrapy.Field()
    SellerID = scrapy.Field()
    URL = scrapy.Field()
    Image=scrapy.Field()
    # shipping=scrapy.Field()
    Date=scrapy.Field()
    pass
