# -*- coding: utf-8 -*-
import scrapy


class Android16Spider(scrapy.Spider):
    name = 'android16'
    start_urls = ['http://www.dustloop.com/wiki/index.php?title=DBFZ/Android_16/Frame_Data']

    def parse(self, response):
        for row in response.css('.wikitable tr'):
            yield {
                'Version': row.css('th::text').extract(),
                'Damage': row.css('td:nth-child(1)::text').extract(),
                'Attribute': row.css('td:nth-child(2)::text').extract(),
                'Guard': row.css('td:nth-child(3)::text').extract(),
                'Startup': row.css('td:nth-child(4)::text').extract(),
                'Active': row.css('td:nth-child(5)::text').extract(),
                'Recovery': row.css('td:nth-child(6)::text').extract(),
                'Frame Adv.': row.css('td:nth-child(7)::text').extract(),
                'Level': row.css('td:nth-child(8)::text').extract(),
                'Blockstun': row.css('td:nth-child(9)::text').extract(),
                'Hitstun': row.css('td:nth-child(10)::text').extract(),
                'Untech': row.css('td:nth-child(11)::text').extract(),
                'Invul': row.css('td:nth-child(12)::text').extract(),
                'Hitbox': row.css('td:nth-child(13)::text').extract(),
                'Notes': '',



            }


# scraping normal moves: 
# 1. skip first row of every wikitable.
# 2. if the iterated row doesn't have 14 td+th, skip it.
# 3. assuming that both above criteria are satisfied, save the text content of each td/th in a single JSON object, making a JSON object with 14 properties. 
# this is one move.

