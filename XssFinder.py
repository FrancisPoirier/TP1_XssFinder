from robobrowser import RoboBrowser
from Spyder import Spyder

class XssFinder:

    def __init__(self, url):
        self.url = url
        self.listOfLinks = []

    ##Form generaly means inputs where you can write some text to send to the server in this code.


    def findXss(self):
        browser = RoboBrowser()

        browser.open(self.url)

        self.findXssInCurrentPage(browser)

        #self.goThroughAvailableHyperlinks(browser)

    def goThroughAvailableHyperlinks(self, browser):
        #Use Spyder to get links of the website we want to analyse
        NUMBER_OF_PAGE_TO_CRAWL = 5
        spyder = Spyder(self.url, NUMBER_OF_PAGE_TO_CRAWL)
        spyder.gather()

        links = spyder.getList()

        for link in links:
            browser.follow_link(link)
            self.findXssInCurrentPage(browser)


    def findXssInCurrentPage(self, browser):
        # if there is more than one form in one page, we got to try them all.
        forms = browser.get_forms()
        formCount = len(forms)

        activeUrl = browser.url

        if (formCount >= 1):

            for form in forms:

                # Code to treat XSS
                self.findXssFailuresInAForm(browser, form)
                browser.open(activeUrl)


    def findXssFailuresInAForm(self, browser, form):
        xssFailureTestString = '<script>alert("bonjour")</script>'

        fieldNames = self.getAllFieldNamesFromAForm(form)
        for fields in fieldNames:
            form[fields] = xssFailureTestString

        xssUrlBeforeTest = browser.url
        browser.submit_form(form)
        response = str(browser.response._content)

        if (xssFailureTestString in response):
            requestType = str(browser.response.request.method) ##Demeter is proud.
            formAction = form.action
            self.saveXssFailures(xssUrlBeforeTest, formAction, requestType)



    ###Register the failures in a list under the wanted format
    def saveXssFailures(self, failingUrl, formAction, requestType):
        if (self.isInTheList(failingUrl, formAction, requestType) == False):
            toSave = [failingUrl, formAction, requestType]
            self.listOfLinks.append(toSave)


    ###Test if the failure found isn't already in the list
    def isInTheList(self, failingUrl, formAction, requestType):
        combination = [failingUrl, formAction, requestType]
        if (len(self.listOfLinks) == 0):
            return False
        else:
            for failures in self.listOfLinks:
                if failures == combination:
                    return True
                else:
                    return False


        #Return a list with the html attribute "name=" of all elements of the form.
    def getAllFieldNamesFromAForm(self, form):
        formFields = form.fields.to_dict()
        fieldNames = []
        fieldAmount = len(formFields.keys())

        # if there is more than one field in one form, we got to try them all.
        if (fieldAmount > 1):

            formFieldKeys = formFields.keys()
            for keys in formFieldKeys:
                fieldNames.append(keys)

        else:
            fieldNames.append(formFields.popitem()[0])

        return fieldNames



