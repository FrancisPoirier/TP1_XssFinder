import unittest
from XssFinder import XssFinder
from robobrowser import RoboBrowser


##All test are done on a test website with known source code and access.
##Using the test Website the same way as a Mock.
class MyTestCase(unittest.TestCase):
    def testMethod_findXss_inOnePage_shouldFindAndSaveAnyXssFailuresIntoTheObjectList(self):
        url = "http://www.remikya.com"
        xssFinder = XssFinder(url)

        xssFinder.findXss()
        xssFinderListLength = len(xssFinder.getListOfLinks())

        EXPECTED_ANSWER = 1
        self.assertEqual(EXPECTED_ANSWER, xssFinderListLength)

    def testMethod_findXssFailuresInAForm_shouldOnlySaveXssFailuresThatAreNotAlreadyInTheList(self):
        url = "http://www.remikya.com/Controllers/SearchController.php"
        xssFinder = XssFinder(url)
        browser = RoboBrowser()
        browser.open(url)
        form = browser.get_form(id="form")

        xssFinder.findXssFailuresInAForm(browser, form)
        xssFinder.findXssFailuresInAForm(browser, form)
        xssFinderListLength = len(xssFinder.getListOfLinks())

        EXPECTED_ANSWER = 1
        self.assertEqual(EXPECTED_ANSWER, xssFinderListLength)


    def testMethod_getAllFieldNamesInAForm_shouldReturnTheNameAttributeOfAllFormNodes(self):
        url = "http://www.remikya.com/Controllers/LoginController.php"
        xssFinder = XssFinder(url)
        browser = RoboBrowser()
        browser.open(url)
        form = browser.get_form(action="/Controllers/LoginController.php")

        fieldNames = xssFinder.getAllFieldNamesFromAForm(form)

        FIRST_EXPECTED_ANSWER = "nom_utilisateur"
        SECOND_EXPECTED_ANSWER = "mot_de_passe"
        THIRD_EXPECTED_ANSWER = "Connecter"
        self.assertEqual(FIRST_EXPECTED_ANSWER, fieldNames[0])
        self.assertEqual(SECOND_EXPECTED_ANSWER, fieldNames[1])
        self.assertEqual(THIRD_EXPECTED_ANSWER, fieldNames[2])


if __name__ == '__main__':
    unittest.main()
