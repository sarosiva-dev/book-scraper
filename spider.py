import scrapy
class scarpy(scrapy.Spider):
    name="nameprice"
    start_urls=["https://books.toscrape.com"]
    def parse(self, response):
        print("STATUS:", response.status)
        print("URL:", response.url)

        articles = response.css("article.product_pod")

        print("BOOKS FOUND:", len(articles))

        for article in articles:
            bookname = article.css("h3 a::attr(title)").get()
            price = article.css("p.price_color::text").get()
            price=price.replace("£", "$")
            availability = article.css("p.instock.availability::text").getall()
            availability=" ".join(availability).split()
            availability=" ".join(availability)
            star_rating = article.css("p.star-rating::attr(class)").get().strip()
            star_rating=star_rating.replace("star-rating","").strip()
            ratings={
                "One":1,
                "Two":2,
                "Three":3,
                "Four":4,
                "Five":5
            }
            star_rating=ratings.get(star_rating)

            yield{"bookname":bookname,
                  "price":price,
                  "availability":availability,
                  "star_rating":star_rating
                  }