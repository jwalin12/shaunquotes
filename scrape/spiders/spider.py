import scrapy
import csv

class Spider(scrapy.Spider):
    name = "spid"
    start_urls = ['https://bestoflifemag.com/shaun-week-quotes-workout-motivation/']

    def parse(self, response):

        page = response.url.split('/')[-3]
        file_name = 'spid-%s.csv' % page
        with open(file_name, 'w') as f:

            quotes = response.css('h3::text').getall()[:-5]
            for i in quotes:
                i = i.replace(',', '')
                f.write(i)
                f.write("\n")



