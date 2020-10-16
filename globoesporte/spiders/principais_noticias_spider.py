import scrapy


class UltimasNoticiasSpider(scrapy.Spider):
    
    name = 'ultimas_noticias_spider' 
    def __init__(self,time = '',*args, **kwargs):
               
        super(UltimasNoticiasSpider, self).__init__(*args, **kwargs)
        
        self.allowed_domains = ['globoesporte.globo.com/futebol/times/' + time ]      
        self.start_urls = ['https://globoesporte.globo.com/futebol/times/' + time]
    
    def parse(self, response):
        
        noticias = response.xpath("//div[contains(@class,'bstn-fd')]//div[@class = 'bastian-page']//div\
            [contains(@class,'bastian-feed')]//div[@class='feed-post-body-resumo']/text()").getall()       
        links = response.xpath("//div[contains(@class,'bstn-fd')]//div[@class = 'bastian-page']//div\
            [contains(@class,'bastian-feed')]//div[contains(@class,'feed-media')]//a/@href").getall()

        for noticia, link in zip(noticias,links):
            
            yield {
                'noticia':noticia,
                'link':link
            }