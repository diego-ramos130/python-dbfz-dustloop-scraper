# -*- coding: utf-8 -*-
import scrapy


class dustloopDBFZSpider(scrapy.Spider):
    name = 'dustloopDBFZ'

    start_urls = [
                  'http://www.dustloop.com/wiki/index.php?title=DBFZ/Fused_Zamasu/Frame_Data',
            ]

    def parse(self, response):
        for row in response.xpath('//*[@class="wikitable"]//tbody//tr'):
            yield {
                'Version': row.xpath('th//text()').extract_first(),
                'Damage': row.xpath('td[1]//text()').extract_first(),
                'Attribute': row.xpath('td[2]//text()').extract_first(),
                'Guard': row.xpath('td[3]//text()').extract_first(),
                'Startup': row.xpath('td[4]//text()').extract_first(),
                'Active': row.xpath('td[5]//text()').extract_first(),
                'Recovery': row.xpath('td[6]//text()').extract_first(),
                'Frame Adv.': row.xpath('td[7]//text()').extract_first(),
                'Level': row.xpath('td[8]//text()').extract_first(),
                'Blockstun': row.xpath('td[9]//text()').extract_first(),
                'Hitstun': row.xpath('td[10]//text()').extract_first(),
                'Untech': row.xpath('td[11]//text()').extract_first(),
                'Invul': row.xpath('td[12]//text()').extract_first(),
                'Hitbox': row.xpath('td[13]//text()').extract_first(),
                'Notes': '',
            }


# scraping normal moves: 
# 1. skip first row of every wikitable.
# 2. if the iterated row doesn't have 14 td+th, skip it.
# 3. assuming that both above criteria are satisfied, save the text content of each td/th in a single JSON object, making a JSON object with 14 properties. 
# this is one move.

