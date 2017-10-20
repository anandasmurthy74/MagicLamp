import bs4 as bs
import urllib.request


class scrapertest:
    def __init__(self, topic):
        self.topic = topic
        url = 'https://en.wikipedia.org/wiki/' + topic
        print(url)
        sauce = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(sauce, "lxml")
        images = soup.find_all('a', class_="image")
        # Get the list of images and their link
        tags = images[0].children
        print("The images are : ", len(images))
        for tag in tags:
            print(tag['src'])


nImg = scrapertest('Chennai')
