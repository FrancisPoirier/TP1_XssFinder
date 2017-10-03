from robobrowser import RoboBrowser
import string

class InFormsXssFinder:

    def __init__(self, url):
        self.url = url


    def findXss(self):
        browser = RoboBrowser()

        browser.open(self.url)

        links = browser.get_links()
        newLink = self.getLink(links, n=0)
        #forms = browser.get_forms()
        #formCount = len(forms)

        #Code to travel all links
        #self.goThroughAvailableHyperlinks(browser)

        #self.findXssInCurrentPage(browser, forms, formCount)

    #Recursive
    #Pas fini
    def goThroughAvailableHyperlinks(self, browser, nextLink, n):

        if (len(browser.get_links()) == 0):
            # self.findXssInCurrentPage()
            # return the number of xss failures found
            pass
        else:
            prefixe = 'http://testfire.net'
            newBrowser = browser.open(nextLink)
            links = newBrowser.get_links()
            href = self.getLink(links, n)
            newLink = prefixe + href
            return self.goThroughAvailableHyperlinks(browser, newLink, n = n+1)

    #Gets the correct string format to proceed
    def getLink(self, links, n):

        href = links[n].get("href")
        if (href.startswith("../")):
            link = href[2:]
        elif (href.startswith("/") == False):
            link = "/" + href
        else:
            link = href

        return link



    def findXssInCurrentPage(self, browser, forms, formCount):
        # if there is more than one form in one page, we got to try them all.
        if (formCount > 1):

            formNumber = 0
            for form in forms:
                formFields = forms[formNumber].fields.to_dict()
                fieldNames = self.getAllFieldNames(formFields)


                # Code to treat XSS

                formNumber += 1

        elif (formCount == 1):
            formFields = forms[0].fields.to_dict()
            fieldNames = self.getAllFieldNames(formFields)

            # Code to treat XSS

        else:
            # Code to change page and get new forms
            pass



        #Return a list with the html attribute "name=" of all elements of the form.
    def getAllFieldNames(self, formFields):
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
