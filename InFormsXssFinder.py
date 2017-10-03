from robobrowser import RoboBrowser

class InFormsXssFinder:

    def __init__(self, url):
        self.url = url


    def findXss(self):
        browser = RoboBrowser()

        browser.open(self.url)

        stock = browser.get_forms()
        formFields = stock[1].fields
        formNames = formFields.to_dict().items()

        if (formNames.__len__ > 1):
            pass



