import unittest
from selenium import webdriver
import os

class TestWithLocalFile(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.files_dir = os.path.dirname(os.path.realpath(__file__))
    
    def seats_available(self, course_title, driver):
        i = int(driver.find_element_by_xpath(u'//td[contains(text(), "' + course_title + '")]/following-sibling::td[4]').text)
        return i

    def test_FindsZeroSeats(self):
            self.driver.get("file://" + self.files_dir + "/sch_data_mining_has_zero_seats_open.html")
            self.assertEqual(self.seats_available("Data Mining", self.driver), 0)

    def test_FindsOneSeat(self):
            self.driver.get("file://" + self.files_dir + "/sch_data_mining_has_one_seat_open.html")
            self.assertEqual(self.seats_available("Data Mining", self.driver), 1)
        
    def test_FindsTwoSeats(self):
            self.driver.get("file://" + self.files_dir + "/sch_data_mining_has_one_seat_open.html")
            self.assertEqual(self.seats_available("Intro to Comp-Aid Verification", self.driver), 2)

    def tearDown(self):
        self.driver.close()

suite = unittest.TestLoader().loadTestsFromTestCase(TestWithLocalFile)

runner = unittest.TextTestRunner()
runner.run(suite)
