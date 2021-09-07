import json
import os.path
from datetime import date

import scrapy
from ratelimiter import RateLimiter
from scrapy import signals
from scrapy.crawler import CrawlerProcess
from scrapy.signalmanager import dispatcher

# this mean to call 5 pages per 15 seconds . If scraping too fast, it could be blocked. Also, some lists might be skipped when scrapping too fast
rate_limiter = RateLimiter(max_calls=5, period=15)
results = []

# you can customize your file location
path1 = "C://realestatelist_"
date = date.today()
path2 = str(date)+"-1.txt"
file_path = path1+path2

if os.path.isfile(file_path):
    os.remove(file_path)
    file_object = open(file_path, "w+")
    file_object.close()
else:
    pass

# this help avoid failing when striping text if elment is none 
def strip_text(element):
    if element:
        return element.strip()
    return None


# create a class inherited from another class scrapy.Spider
class BlogSpider(scrapy.Spider):
    name = 'blogspider'

    def __init__(self, city_region):
        # this is the starting URL
        # the website only allows to scrape at most 25 pages for each city using below URL, so some lists from the cities are missing. 
        # If you want to scrape more lists of each city in Vancouver, consdier using another wbeside. Refer to this https://evaanalytics.wixsite.com/website/post/use-scrapy-to-real-estate-data
        # However, this above website does not allow to scrape land size for houses easily
        self.start_urls = [
            f'https://www.rew.ca/properties/areas/{city_region}/page/1']
            
    def parse(self, response):
        # print(response.text)
        # response is the scraped result
        for title in response.css('.displaypanel-body'):
            yield {
                # depending on what you want to collect, the detail is different
                'Price': title.css('.displaypanel-title::text').get().strip(),
                'Structure & size': title.css('.displaypanel-section.clearfix').css('.l-pipedlist').xpath(
                    'li/text()').getall(),
                'Address': title.css('.displaypanel-section::text').get().strip(),
                'City': title.css('.l-pipedlist.displaypanel-info').xpath('li/text()').getall(),
                'list_Type': strip_text(title.css('.clearfix.hidden-xs').css('.displaypanel-info::text').get()),
                # here @src means to get the value of parameter src
                'URL': title.css('.displaypanel-photo').css('img.img-responsive').xpath('@src').get()
            }  # yield is used to return the result

        # response.css('a[rel="next"]') is a value
        for next_page in response.css('a[rel="next"]'):
            with rate_limiter:
                # this is to ask to go through the pages
                yield response.follow(next_page, self.parse)


# below is a function to call after spider find content
def crawler_results(signal, sender, item, response, spider):
    results.append(item)  # item is the scraped result from yield


dispatcher.connect(crawler_results, signal=signals.item_passed)
process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36'

})  # A user agent is any software, acting on behalf of a user, which "retrieves, renders and facilitates end-user interaction with Web content. Sometimes you need to change it to avoid banning from your scrapying websites

process.crawl(BlogSpider, 'vancouver-bc')
process.crawl(BlogSpider, 'north-vancouver-bc')
process.crawl(BlogSpider, 'richmond-bc')
process.crawl(BlogSpider, 'langley-bc')

process.start()

json_result = {
    'listings': results
}
# to create called sample .
with open(file_path, 'w+') as outfile:
    outfile.write(json.dumps(json_result) + '\n')
