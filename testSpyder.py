import unittest
from Spyder import Spyder


class MyTestCase(unittest.TestCase):
    def testMethod_gather_inAtLeastOnePage_shouldAddLinksIntoTheSpyderList(self):
        testUrl = "http://remikya.com"
        max_pages = 4
        spyder = Spyder(testUrl,max_pages)

        spyder.gather()
        spyderList = spyder.getList()
        listIsEmpty = True if (len(spyderList) == 0) else False

        EXPECTED_ANSWER = False
        self.assertEqual(EXPECTED_ANSWER, listIsEmpty)


    def testMethod_isInTheList_shouldReturnTrueIfTheLinkReceivedIsAlreadyInTheSpyderList(self):
        testUrl = "http://remikya.com"
        max_pages = 4
        spyder = Spyder(testUrl, max_pages)
        spyder.gather()

        spyderListElement = spyder.getList()[0]
        answer = spyder.isInTheList(spyderListElement)

        EXPECTED_ANSWER = True
        self.assertEqual(EXPECTED_ANSWER, answer)


if __name__ == '__main__':
    unittest.main()
