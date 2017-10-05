from robobrowser import RoboBrowser
import string


class Spyder:

    def __init__(self, url, max_pages):
        self.url = url
        self.max_pages = max_pages
        self.list = []

    def gather(self):
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
                     if(self.isInTheList(link)):
                        self.list.append(link)

            browser.follow_link(self.list[page])
            page+=1

    def isInTheList(self, link):

        href = link.get("href")
        for tags in self.list:
            if (href in tags.get("href")):
                var = tags.get("href")
                return True
            else:
                return False

    def getList(self):
        return self.list