from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import re
from getpass import getpass
import unittest
import os
from smtplib import SMTP_SSL
from email.mime.text import MIMEText

# sender and receiver are discussed in README.md
sender = 'makeswell@gmail.com'
receiver = 'maxwell.pietsch@gmail.com'

def create_courses_of_interest():
	courses_of_interest = []
	with open('courses_of_interest.txt', 'r') as f:
		just_read_course_name = False
		for line in f:
			if line[0] != '#':
				if just_read_course_name == False:
					course = line.strip()
					just_read_course_name = True
				else:
					section_num = line.strip()
					courses_of_interest.append((course,section_num))
	return courses_of_interest

def start_from_first_page(driver, definitely_started_from_first_page=False):
	#if we're not sure if we started from the first page or not, we'll keep clicking on the first page button until we can no longer find the Previous button. at this point we'll assume we're at the first page and call the function again with definitely_started_from_the_first_page equal to True.
	if not definitely_started_from_first_page:
		try:
			driver.find_element_by_xpath("//a[@title='Previous page of results']").click()
			start_from_first_page(driver, False)
		except NoSuchElementException:
			print("Should be at the first page now.")


def seats_available(course_title, section_num, driver, definitely_started_from_first_page_for_this_course=False):	
	if not definitely_started_from_first_page_for_this_course:
		start_from_first_page(driver)
		definitely_started_from_first_page_for_this_course = True
	try:
		seatz = int(driver.find_element_by_xpath(u'//td[contains(text(), "' + course_title + '")]/preceding-sibling::td[contains(text(), "' + section_num + '")][1]/following-sibling::td[5]').text)
		print(str(seatz) + ' seats available in ' + course_title + ' section #' + section_num)
		return seatz
	except NoSuchElementException:
		try:
			driver.find_element_by_xpath("//a[@title='Next page of results']").click()
		except NoSuchElementException:
			print("Reached the last page without finding the course.")
		else:
			seats = seats_available(course_title, section_num, driver, definitely_started_from_first_page_for_this_course)
			return seats

def send_email_if_available(course, section_num, sender, password, receiver, driver):
	seats = seats_available(course, section_num, driver)
	if (seats > 0):
		msg_text = str(seats) + ' seat(s) is available in ' + course + ' with section #' + section_num
		print(msg_text)
		print('Sending email from ' + sender + ' to ' + receiver)
		msg = MIMEText(msg_text)
		msg['Subject'] = 'Seat open in ' + course
		msg['From'] = sender
		msg['To'] = receiver

		s = SMTP_SSL('smtp.gmail.com', 465, timeout=10)
		s.set_debuglevel(1)
		s.login(sender, password)
		s.sendmail(msg['From'], msg['To'], msg.as_string())
		s.quit()

def submit_search_open_results():
	driver = webdriver.Firefox()
	driver.get("http://www.registrar.usf.edu/ssearch/search.php")
	driver.find_element_by_xpath(u'//option[contains(text(), "Tampa")]').click()
	driver.find_element_by_xpath(u'//option[contains(text(), "Engineering Computer Science")]').click()
	driver.find_element_by_xpath(u'//option[contains(text(), "ALL")]').click()
	driver.find_element_by_name("search").click()
	return driver

if __name__ == "__main__":
	#import test_seats
	driver = submit_search_open_results()
	print('Not sure this works with email providers other than Gmail')
	#password = getpass('Email password:')
	courses_of_interest = create_courses_of_interest()
	with open('appp.txt') as p:
		p.readline() # do away with the comment line
		app_password = p.readline().strip()
	for course, section_num in courses_of_interest:
		send_email_if_available(course, section_num, sender, app_password, receiver, driver)
	driver.close()

