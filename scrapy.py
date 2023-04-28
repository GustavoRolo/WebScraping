import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from sendEmail import EmailSettings

class Scrapy:

    url = "";
    userAgent = "";
    soup = "";
    newProduct = "";
    allProduct = "";

    def __init__(self,url, userAgent):
        self.url = url;
        self.userAgent = userAgent;

    def start(self):
        options = webdriver.ChromeOptions();
        options.add_argument(self.userAgent);
        driver = webdriver.Chrome(options=options);
        driver.get(self.url);
        time.sleep(5);
        html_content = driver.page_source;
        driver.quit();
        self.soup = BeautifulSoup(html_content, 'html.parser');
        return;

    def compare(self):
        with open('model.txt', 'r',encoding='utf-8') as arquivo:
            conteudo = arquivo.read()
            for produtos in self.soup.find_all("h1", attrs={"class": "fengstexperience-catalog-card-template-1__title"}):
                self.allProduct += "\n" + produtos.text
                if produtos.text in conteudo:
                    continue
                else:
                    self.newProduct += "\n" + produtos.text
        return;

    def sendEmail(self):
        if self.newProduct != "":
            EmailSettings.ProsendEmailduct(self.newProduct)
            self.updateModel();
        return;

    def updateModel(self):
        with open('model.txt', 'w',encoding='utf-8') as arquivo:
             arquivo.write(self.allProduct)