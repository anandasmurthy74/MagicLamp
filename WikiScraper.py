import bs4 as bs
import urllib.request
import pandas as pd


class scraper:
    def __init__(self, topic):
        self.topic = topic
        url = 'https://en.wikipedia.org/wiki/' + topic
        print(url)
        sauce = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(sauce, "lxml")
        contents = soup.find_all('span', class_='toctext')
        images = soup.find_all('a', class_="image")
        headlines = soup.find_all('span', class_="mw-headline")
        df_list = pd.read_html(url)

        # Get the topics and the associated paragraphs
        headings = []
        paragraphs = []
        for x in range(0, len(headlines)):
            for elt in headlines[x].parent.nextSiblingGenerator():
                if elt.name == 'h2':
                    break
                if elt.name == 'p':
                    headings.append(headlines[x].text)
                    paragraphs.append(elt.text)

        keytopics = dict(zip(headings, paragraphs))

        # Get the list of images and their link
        img = []
        for image in images:
            img_tags = image.children
            for img_tag in img_tags:
                img.append(img_tag['src'])

        # Get the contents and their links
        toclist = []
        for toc in contents:
            toclist.append(toc.text)
        pop_list = ["See also", "References", "Bibliography", "External links", "Primary sources", "Notes", "Notes and references", "Further reading"]

        for x in range(0, len(pop_list)):
            if pop_list[x] in toclist:
                toclist.remove(pop_list[x])

        # Get all the references
        ref = []
        references = soup.find_all('span', class_="reference-text")

        for reference in references:
            ref.append(reference.text)


if __name__ == "__main__":
    scrape = scraper("Roman_civilization")
