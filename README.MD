Simple test task for MARAKAS Design Studio

# Requirements
`Docker`
`Python3.8`
# Install
```
git clone 
poetry install
sudo docker pull scrapinghub/splash
```  

#Run
Put your keywords line by line to `amazon_scraper/input.txt`
###Run Splash
```
docker run -p 8050:8050 scrapinghub/splash
```
###Run Spiders
```
cd amazon_scraper
scrapy crawl amazon
```
