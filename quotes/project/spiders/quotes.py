import scrapy
from project.items import QuoteItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response, **kwargs):
        quotes = response.css('div.quote')


        for quote in quotes:
            title = quote.css('span.text::text').extract_first()
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tag::text').extract()
            yield QuoteItem(
                title=title,
                author=author,
                tags=tags
            )
