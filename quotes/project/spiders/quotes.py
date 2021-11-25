import scrapy
from scrapy.http import FormRequest
from project.items import QuoteItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    base_url = 'https://quotes.toscrape.com/page/'
    page_number = 2
    start_urls = ['https://quotes.toscrape.com/login']

    def start(self, response):
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

        next_page = self.base_url + str(self.page_number) + '/'
        if self.page_number < 11:
            self.page_number += 1
            yield response.follow(next_page, callback=self.start)

    def parse(self, response):
        token = response.css('form input::attr(value)').extract_first()
        return FormRequest.from_response(response, formdata=dict(
            csrf_token=token,
            username='matheus@email.com',
            password='123123'
        ), callback=self.start)
