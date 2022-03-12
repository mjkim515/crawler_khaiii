# -*- coding: utf-8 -*-

# - 경기도 : 중부 일보 -
# http://www.joongboo.com/
# http://www.joongboo.com/news/articleList.html?page=1

import scrapy

from crawler.items import Headline

class JoongbooSpider(scrapy.Spider):
    name = 'joongboo'
    allowed_domains = ['www.joongboo.com']
    start_urls = ['http://www.joongboo.com/']

    def start_requests(self):
        for i in range(1, 6): 
            yield scrapy.Request("http://www.joongboo.com/news/articleList.html?page=" + str(i))
            
            
    
    def parse(self, response):
        """
        메인 페이지의 토픽 목록에서 링크를 추출하고 출력합니다.
        """
        link = response.css('h4.titles a::attr("href")').extract()
        #link -> ''/news/articleView.html?idxno=363529219'

        # http://www.joongboo.com/news/articleView.html?idxno=363529171

        for urla in link:
            url = "http://www.joongboo.com"+ urla;

            # 광고 페이지 제외
            if url.find("products") == 1: 
                continue
            # 의미 없는 페이지 제외
            if url == "#": 
                continue
            
            print ("URL : " + url)
            yield scrapy.Request(url, self.parse_topics)


    def parse_topics(self, response):

        item = Headline()
        item['title'] = response.css('head title::text').extract_first()
        item['url'] = response.url

        #//*[@id="articleBody"]/p[5]/text()[2]
        item['body'] = response.css('.article-body p').xpath('string()').extract()


        yield item 