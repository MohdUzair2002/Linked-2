from dataclasses import replace
from os import link
from re import I
from turtle import title
from numpy import product
from pytest import Item
import scrapy
from scrapy.selector import Selector
from ..items import Linked2Item
import math
from datetime import datetime
# class SpidernameSpider(scrapy.Spider):
#     name = 'spidername'
#     product="maos"
#     # allowed_domains = ['www.americanas.com.br']
#     start_urls = ['https://www.americanas.com.br/busca/maos']
#     page_number=2
    

#     def parse(self, response):
    
#     links=response.xpath("/html/body/div[1]/div/div/main/div/div[3]/div[2]")
#     ULinks=links.xpath(".//a[@aria-current='page']")
#     for link in ULinks:
#         link=link.xpath(".//@href").get()
#         FLink=response.urljoin(link)

#         yield scrapy.Request(url=FLink,callback=self.GetData)


#     def GetData(self,response):
#         i=0
#         items=Linked2Item()
#         now = datetime.now()
#         Date=now.strftime("%d/%m/%Y %H:%M:%S")
#         name1=response.xpath("/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/h1/text()").get()
#         try:
#         if name1==[]:
#             name1=response.xpath("/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/h1/text()").get()
#         else:
#             name1=response.xpath("/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/h1//text()").get()
#         except:
#                 name1="nill"
#         discription=response.xpath("/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/div[3]/p/text()").get()
#     #     if discription==None:
#     #           i=0
#     #           t=[]
#     #           discription1=response.xpath("(/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/div[4]/p)//text()[i]")

#     #           while(discription1!=None):
#     #            discription1=response.xpath("(/html/body/div[1]/div/div/main/div[2]/div[1]/div[2]/div[4]/p)//text()[i]")
#     #            if discription1!=None:
#     #             t.append(discription1)
#     #            i+=1
#     #           t= ("".join(t))
#     #           discription=t
#         pricecurrency=response.xpath("/html/body/div/div/div/main[3]/div/div[1]/div[2]/div[2]/div[2]/div/div/a/div[2]/div[2]/div[2]/span[1]//text()").get()
#         url=response.url,
#         price1=response.xpath("(/html/body/div[1]/div/div/main/div[2]/div[2]/div[1]/div[1]/div//text())[2]").get()
#         productid=(response.url.split("/")[4]).split("?")[0]
#         seller_name=response.xpath("//*[@id='rsyswpsdk']/div/main/div[2]/div[2]/div[4]/p/a[1]//text()").get()
#     #     if pricecurrency[1] =="%" or pricecurrency[2] =="%" :
#     #       pricecurrency=response.xpath("/html/body/div[1]/div/div/main/div[2]/div[2]/div[1]/div[2]/div/text()[1]").get()
#     #       price1=response.xpath("/html/body/div[1]/div/div/main/div[2]/div[2]/div[1]/div[2]/div/text()[2]").get()
#         try:
                
#                 seller_name=response.xpath("//*[@id='rsyswpsdk']/div/main/div[2]/div[2]/div[4]/p/a[1]//text()").get()
#                 sellerid=response.xpath("/html/body/div[1]/div/div/main/div[2]/div[2]/div[4]/p/a[1]/@href").get().split("/")[-1]
#         except: 
#         seller_name="Americanas"
#         sellerid="Americanas"
        
#         price=price1
#         image=response.xpath("/html/body/div[1]/div/div/main/div[2]/div[1]/div[1]/div[2]/div/div[1]/div/picture/img/@src").get()
#     #     shipping=response.xpath("/html/body/div[1]/div/div/main[3]/div/div[1]/div[2]/div[2]/div/div/div/a/div[3]/div/p/font/font/text()")
    
#         items['Title']=name1
#         items['Price']=price
#         items['Description']=discription
#         items['ProductID']=productid
#         items['Sellername']=seller_name
#         items['SellerID']=sellerid
#         items['URL']=url
#         items['Image']=image
#     #     items['shipping']=shipping
#         items['Date']=Date
#         yield items
        
#         offset=24*SpidernameSpider.page_number
#         next_page="https://www.americanas.com.br/busca/maos?limit=24&offset=24"
#     #     if int(SpidernameSpider.a )>24:
#     #      if int(SpidernameSpider.a) <=9976:
#         if SpidernameSpider.page_number<=2:
#             SpidernameSpider.page_number+=1
#             yield  response.follow(next_page,callback=self.parse)
#             # else:
#             #     if SpidernameSpider.page_number<=416:
#             #       SpidernameSpider.page_number+=1
#             #       yield  response.follow(next_page,callback=self.parse)  
            
               
class SpidernameSpider(scrapy.Spider):
    name = 'spidername'
    product="maos"
    # allowed_domains = ['www.americanas.com.br']
    start_urls = ['https://www.mastersportal.com/studies/289722/computer-engineering.html?ref=search_card']
    page_number=2
    

    def parse(self, response):
        print(response)
    #   links=response.xpath("/html/body/div[1]/div/div/main/div/div[3]/div[2]")
          

    