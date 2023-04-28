from scrapy import  Scrapy;


scrapy = Scrapy('https://socio5estrelas.com.br/experiencias/catalogo','user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36');

scrapy.start();
scrapy.compare();
scrapy.sendEmail();