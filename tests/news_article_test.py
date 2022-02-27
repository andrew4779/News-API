import unittest
from ..app.models import news_article
NewsArticle = news_article.NewsArticle


class NewsArticleTest(unittest.TestCase):
  def setUp(self):
    self.news_article = NewsArticle(
      "Andrew",
      "Progmamers Life",
      "day to day life of a coder",
      "https://www.fool.com.au/2022/02/27/are-these-2-leading-etfs-great-buys-in-march-2022/",
      "https://www.fool.com.au/wp-content/uploads/2022/02/etf-18-16.9.jpg",
      "2022-01-30T08:25:00Z",
    )
  

  def test_instance(self):
    self.assertTrue(isinstance(self.news_article, NewsArticle))


if __name__ == '__main__':
  unittest.main()