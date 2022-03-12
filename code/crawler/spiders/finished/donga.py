import scrapy

from crawler.items import Headline

class DongaSpider(scrapy.Spider):
    name = 'donga'
    allowed_domains = ['donga.com']
    start_urls = ['http://donga.com/']

    # 크롤링을 시작할 URL 리스트
    ## start_urls = ['http://www.donga.com/news/Economy/List']
    def start_requests(self):
        for part in ["Opinion", "Politics", "Economy", "Inter", "Society"]: # "Culture"]:
           
            print("Section :" + part, " page : ", index )
            for i in range(1, 600, 20): #page 1 == 1, page2 = 21, page3 = 41, page4 = 61, page5 = 81, page 6 = 101 ....
                yield scrapy.Request("http://www.donga.com/news/" + part + "/List?p=" + str(i))
                
                
    def parse(self, response):
        """
        메인 페이지의 토픽 목록에서 링크를 추출하고 출력합니다.
        """
        link = response.css('div.articleList a::attr("href")').extract()
        for url in link:
            # 광고 페이지 제외
            if url.find("products") == 1: 
                continue
            # 의미 없는 페이지 제외
            if url == "#": 
                continue
            
            yield scrapy.Request(url, self.parse_topics)

    def parse_topics(self, response):
        item = Headline()
        item['title'] = response.css('head title::text').extract_first()
        item['url'] = response.url
        # item['body'] = " ".join(response.css('.o-article_block p')\
        #     .xpath('string()')\
        #     .extract())
        item['body'] = response.css('.article_txt::text').extract()
        yield item
        
