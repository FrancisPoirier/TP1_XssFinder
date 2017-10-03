from robobrowser import RoboBrowser

class InFormsXssFinder:

    def __init__(self, url):
        self.url = url


    def findXss(self):
        browser = RoboBrowser()

        browser.open(self.url)

        forms = browser.get_forms()
        formCount = len(forms)

        #Code to travel all links

        self.findXssInCurrentPage(browser, forms, formCount)


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
