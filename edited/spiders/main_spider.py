from selenium import webdriver
from scrapy.http import HtmlResponse
import scrapy
from edited.items import EditedItem
class MySpider(scrapy.Spider):
    name = 'marksandspencer'

    def start_requests(self):
        url = 'https://www.marksandspencer.com/bg/easy-iron-geometric-print-shirt/p/P60639302.html'
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = EditedItem()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        try:
            driver = webdriver.Chrome(options=chrome_options)  #using default chromedriver directory //webdriver.Chrome('<your_path>', options=chrome_options)
        except Exception as e:
            print("Cannot load Chrome locally")
    
        try:
            driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", options=chrome_options)
        except:
            print("Cannot load Chrome remotely. \nPlease check installing steps again")

        driver.get(response.url)
        scrapy_response = HtmlResponse(url=driver.current_url, body=driver.page_source, encoding='utf-8')
        driver.quit()
        item['name'] = scrapy_response.xpath('//h1[@class="product-name"]/text()').get().strip()
        item['price'] = scrapy_response.xpath('//div[@class="price"]/span/span/span[@class="value"]/text()').get()
        item['colour'] = scrapy_response.xpath('//div[@class="colour-selector"]/div/@data-colorname').get()
        item['size'] = scrapy_response.xpath('//select[@class="custom-select form-control select-size"]/option/text()').getall()
        item['reviews_score'] = scrapy_response.xpath('//span[@class="review-summary__rating"]/text()').get()
        item['reviews_count'] = scrapy_response.xpath('//span[@class="review-summary__total-review review-summary-count"]/@data-value').get()
        yield item