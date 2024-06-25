# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class EditedPipeline:
    def process_item(self, item, spider):

        def clean_text(text):
            #crear \n in text
            if isinstance(text, str):
                return text.replace('\n', '').strip()
            elif isinstance(text, list):
                return [t.replace('\n', '').strip() for t in text]
            return text
        
        item['name'] = clean_text(item.get('name'))
        price = clean_text(item.get('price'))  # Clean the value
        item['price'] = float(price.split('BGN')[1]) # get float only
        item['colour'] = clean_text(item.get('colour'))
        sizes = clean_text(item.get('size'))
        del sizes[0] # pop unwanted text
        item['size'] = sizes
        item['reviews_count'] = int(item.get('reviews_count'))  
        item['reviews_score'] = float(item.get('reviews_score'))  
        
        return item

    
