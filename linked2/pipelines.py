# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import sqlite3

class Linked2Pipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()
    def create_connection(self):
        self.conn=sqlite3.connect("my_data.db")
        self.cursor=self.conn.cursor() 
    def create_table(self):
        self.cursor.execute("""DROP TABLE IF EXISTS my_data""")
        self.cursor.execute("""create table my_data(
                       Title text,
                       price text,
                       description text,
                       ProductID text,
                       Sellername text,
                       SellerID text,
                       URL text,
                       Image text,
                  
                       Date text
                  

        )
        """)
        
    def process_item(self, item, spider):
        self.cursor.execute ( """INSERT  INTO my_data VALUES(?,?,?,?,?,?,?,?,?)""",(
        item['Title'],
        item['Price'],
        item['Description'],
        item['ProductID'],
        item['Sellername'],
        item['SellerID'],
        item['URL'][0],
        item['Image'],
        
        item['Date']
        ))
        self.conn.commit()
        return item
    
        