from robobrowser import RoboBrowser
import string

class InFormsXssFinder:

    def __init__(self, url):
        self.url = url
        self.listOfLinks = []

    ##Form generaly means inputs where you can write some text to send to the server in this code.


    def findXss(self):
        browser = RoboBrowser()

        browser.open(self.url)

        #links = browser.follow_link("")

        #Code to travel all links
        failures = self.goThroughAvailableHyperlinks(browser, browser.url)
        var = 1

    #Recursive
    #Pas fini
    def goThroughAvailableHyperlinks(self, browser, previousHref):

        if (len(browser.get_links()) == 0):
            # self.findXssInCurrentPage()
            # return the number of xss failures found
            pass
        else:
            links = browser.get_links()
            for elements in links:
                #traitement de string
                #href = self.getHref(elements)

                #Ouvre un nouveau lien

                browser.follow_link(elements)

                currentHref = self.getHref(elements)

                self.goThroughAvailableHyperlinks(browser, currentHref)


    def findXssInCurrentPage(self, browser):
        # if there is more than one form in one page, we got to try them all.
        forms = browser.get_forms()
        formCount = len(forms)

        if (formCount >= 1):

            for form in forms:

                # Code to treat XSS
                self.findXssFailuresInAForm(browser, form)

        else:
            # Code to change page and get new forms
            pass

    def findXssFailuresInAForm(self, browser, form):
        xssFailureTestString = '<script>alert("bonjour")</script>'

        fieldNames = self.getAllFieldNamesFromAForm(form)

        for fields in fieldNames:
            form[fields] = xssFailureTestString

        browser.submit_form(form)
        browser.update_state()
        response = str(browser.response._content)

        if (xssFailureTestString in response):
            requestType = browser.response.request.method
        else:
            pass


        # Gets the correct string format to proceed
    def getHref(self, linkToFormat):

        href = linkToFormat.get("href")
        if (href.startswith("../")):
            link = href[2:]
        elif (href.startswith("/") == False):
            link = "/" + href
        else:
            link = href

        return link


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



