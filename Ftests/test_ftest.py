from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase

class PageTest(LiveServerTestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	
	def test_start_list_and_retrieve(self):
		self.browser.get(self.live_server_url)
		self.assertIn('abodeessentials', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Contact Us', headerText)

		ClientName = self.browser.find_element_by_id('applicantName')
		self.assertEqual(ClientName.get_attribute('placeholder'),'Enter your name here.')
		ClientName.send_keys('Janielle Hembrador')
		time.sleep(1)

		ClientEmail = self.browser.find_element_by_id('applicantEmail')
		self.assertEqual(ClientEmail.get_attribute('placeholder'),'Enter your e-mail here.')
		ClientEmail.send_keys('janiellehembrador@gmail.com')
		time.sleep(0.5)

		ClientConcern = self.browser.find_element_by_id('applicantConcern')
		self.assertEqual(ClientConcern.get_attribute('placeholder'),'Choose your concern.')
		selectClientConcern = Select(ClientConcern)
		selectClientConcern.select_by_visible_text('Complaints')
		time.sleep(0.5)

		ClientReview = self.browser.find_element_by_id('applicantReview')
		self.assertEqual(ClientReview.get_attribute('placeholder'),'Enter message here.')
		ClientReview.send_keys('Great product!')
		time.sleep(0.5)
      		
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		time.sleep(0.5)
		
		# inputbox.send_keys(Keys.ENTER)
		table = self.browser.find_element_by_tag_name('table')
		row_data = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Janielle Hembrador, janiellehembrador@gmail.com, Complaints, Great product!', [row.text for row in row_data])
		
# if __name__ == '__main__' :
# 	unittest.main(warnings='ignore')

	def test_start_list_and_retrieve_2(self):
		self.browser.get(self.live_server_url)
		self.assertIn('abodeessentials', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Contact Us', headerText)

		ClientName = self.browser.find_element_by_id('applicantName')
		self.assertEqual(ClientName.get_attribute('placeholder'),'Enter your name here.')
		ClientName.send_keys('Jaji Hembrador')
		time.sleep(1)

		ClientEmail = self.browser.find_element_by_id('applicantEmail')
		self.assertEqual(ClientEmail.get_attribute('placeholder'),'Enter your e-mail here.')
		ClientEmail.send_keys('jaji@gmail.com')
		time.sleep(0.5)

		ClientConcern = self.browser.find_element_by_id('applicantConcern')
		self.assertEqual(ClientConcern.get_attribute('placeholder'),'Choose your concern.')
		selectClientConcern = Select(ClientConcern)
		selectClientConcern.select_by_visible_text('Question')
		time.sleep(0.5)

		ClientReview = self.browser.find_element_by_id('applicantReview')
		self.assertEqual(ClientReview.get_attribute('placeholder'),'Enter message here.')
		ClientReview.send_keys('Nice product!')
		time.sleep(0.5)
      		
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		time.sleep(0.5)
		
		# inputbox.send_keys(Keys.ENTER)
		# table = self.browser.find_element_by_tag_name('table')
		# row_data = table.find_element_by_tag_name('td')
		#self.assertIn('1: Jaji Hembrador, jaji@gmail.com, Question, Nice product!', row_data.text)
		
		self.browser.get(self.live_server_url)
		self.assertIn('abodeessentials', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Contact Us', headerText)

		ClientName = self.browser.find_element_by_id('applicantName')
		self.assertEqual(ClientName.get_attribute('placeholder'),'Enter your name here.')
		ClientName.send_keys('Jaja Hembrador')
		time.sleep(1)

		ClientEmail = self.browser.find_element_by_id('applicantEmail')
		self.assertEqual(ClientEmail.get_attribute('placeholder'),'Enter your e-mail here.')
		ClientEmail.send_keys('jaja@gmail.com')
		time.sleep(0.5)

		ClientConcern = self.browser.find_element_by_id('applicantConcern')
		self.assertEqual(ClientConcern.get_attribute('placeholder'),'Choose your concern.')
		selectClientConcern = Select(ClientConcern)
		selectClientConcern.select_by_visible_text('Feedback')
		time.sleep(0.5)

		ClientReview = self.browser.find_element_by_id('applicantReview')
		self.assertEqual(ClientReview.get_attribute('placeholder'),'Enter message here.')
		ClientReview.send_keys('Love the product!')
		time.sleep(0.5)
      		
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		time.sleep(0.5)
		
		# inputbox.send_keys(Keys.ENTER)
		table = self.browser.find_element_by_tag_name('table')
		row_data = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Jaji Hembrador, jaji@gmail.com, Question, Nice product!', [row.text for row in row_data])
		self.assertIn('2: Jaja Hembrador, jaja@gmail.com, Feedback, Love the product!', [row.text for row in row_data])