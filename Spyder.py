from robobrowser import RoboBrowser
import string


class Spyder:


    def __init__(self, url, max_pages):
        self.url = url
        self.list = []
        self.max_pages = max_pages


    def spyder(self):
        browser = RoboBrowser()
        page = 0
        browser.open(self.url)

        while (page < self.max_pages):
            links = browser.get_links()

            if(page == 0):
                for link in links:
                    self.list.append(link)
            else:
                for link in links:
                     if(self.contains(link)): ##if(self.contains(link))
                        self.list.append(link)

            browser.follow_link(self.list[page])#browser.follow_link() parametre : un élément de ta liste (un lien)
            page+=1

    def contains(self, link):
        page = 0
        href = link.get("href")
        for tags in self.list:
            if(href not in tags.get("href")):
                return True
            else:
                return False


    def getList(self):
        return self.list