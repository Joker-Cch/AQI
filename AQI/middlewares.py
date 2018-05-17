from selenium import webdriver
from scrapy.http import HtmlResponse
import scrapy
import time


class AqiSeleniumMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def process_request(self, request, spider):

        if "daydata" in request.url or "monthdata" in request.url:
            # driver = webdriver.Chrome()
            self.driver.get(request.url)
            for count in range(18):
                try:
                    self.driver.find_element_by_xpath("//div[@class='row']//tbody/tr//td[1]")
                    html = self.driver.page_source
                    return HtmlResponse(url=request.url, body=html.encode("utf-8"), encoding="utf-8", request=request)
                except:
                    time.sleep(0.5)

    def __del__(self):
        self.driver.quit()
