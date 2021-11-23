import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response, **kwargs):
        quotes = response.css('div.quote')


        for quote in quotes:
            title = quote.css('span.text::text').extract()
            author = quote.css('.author::text').extract()
            tags = quote.css('.tag::text').extract()
            yield dict(
                title=title,
                author=author,
                tags=tags
            )
