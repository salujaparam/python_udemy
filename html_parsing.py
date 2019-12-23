from bs4 import BeautifulSoup
import re

ITEM_HTML = '''<html>
                    <head>
                    </head>
                    <body>
                        <li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
                            <article class="product_pod">
                                    <div class="image_container">
                                            <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
                                    </div>
                                    <p class="star-rating Three">
                                        <i class="icon-star"></i>
                                        <i class="icon-star"></i>
                                        <i class="icon-star"></i>
                                        <i class="icon-star"></i>
                                        <i class="icon-star"></i>
                                    </p>
                                    <h3>
                                        <a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">
                                            A Light in the ...
                                        </a>
                                    </h3>
                                    <div class="product_price">
                                        <p class="price_color">£51.77</p>
                                        <p class="instock availability">
                                            <i class="icon-ok"></i>
                                            In stock
                                        </p>
                                    <form>
                                        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
                                    </form>
                                    </div>
                            </article>
                        </li>
</body></html>
'''

class Locators:
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article div.product_price p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'

class ParsedItem:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    def find_item_name(self):
        locator = Locators.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    def find_item_link(self):
        locator = Locators.LINK_LOCATOR
        item_link = self.soup.select_one(locator)
        item_href = item_link.attrs['href']
        return item_href

    def find_price(self):
        locator = Locators.PRICE_LOCATOR
        price = self.soup.select_one(locator).string
        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, price)
        return matcher.group(0), float(matcher.group(1))

    def find_item_rating(self):
        locator = Locators.RATING_LOCATOR
        star_rating_tag = self.soup.select_one(locator)
        classes = star_rating_tag.attrs['class']
        clss = [clas for clas in classes if clas != 'star-rating']
        # clss = filter(lambda x: x != 'star-rating', classes)
        return clss[0]

parsing = ParsedItem(ITEM_HTML)
print(parsing.find_price())
print(parsing.find_item_rating())
print(parsing.find_item_name())
print(parsing.find_item_link())