from django.test import TestCase
from aesys.views import MainPage
from .models import Contact_Us
'''
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.urls import resolve
'''

class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')

	# def test_responding_post_request(self):
	# 	resp = self.client.post('/', data={'name' :'newName',
	# 		'email': 'newEmail',
	# 		'concern': 'newConcern',
	# 		'review': 'newReview'})
	# 	self.assertIn('newName', resp.content.decode())
	# 	self.assertTemplateUsed(resp, 'mainpage.html')

	def test_save_POST_request(self):
		response = self.client.post('/', {'name' :'Janielle',
	 		'email': 'janiellehembrador@gmail.com',
	 		'concern': 'Complaints',
	 		'review': 'Great product!'})
		self.assertEqual(Contact_Us.objects.count(),1)
		inputData = Contact_Us.objects.first()
		self.assertEqual(inputData.name_m, 'Janielle')
		self.assertEqual(inputData.email_m, 'janiellehembrador@gmail.com')
		self.assertEqual(inputData.concern_m, 'Complaints')
		self.assertEqual(inputData.review_m, 'Great product!')

	def test_only_saves_items_uf_necessary(self):
		self.client.get('/')
		self.assertEqual(Contact_Us.objects.count(), 0)

	def test_post_redirect(self):
		response = self.client.post('/', {'name' :'Janielle',
	 		'email': 'janiellehembrador@gmail.com',
	 		'concern': 'Complaints',
	 		'review': 'Great product!'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')


class ORMTEST(TestCase):
	def test_saving_retrive(self):
		Contact_Us_copy = Contact_Us()
		Contact_Us_copy.name_m = 'Janielle'
		Contact_Us_copy.email_m = 'janiellehembrador@gmail.com'
		Contact_Us_copy.concern_m = 'Complaints'
		Contact_Us_copy.review_m = 'Great product!'
		Contact_Us_copy.save()

		Contact_Us_copy2 = Contact_Us()
		Contact_Us_copy2.name_m = 'jaji'
		Contact_Us_copy2.email_m = 'jajiembrador@gmail.com'
		Contact_Us_copy2.concern_m = 'Feedback'
		Contact_Us_copy2.review_m = 'Nice product!'
		Contact_Us_copy2.save()

		Contact_Us_list = Contact_Us.objects.all()
		self.assertEqual(Contact_Us_list.count(), 2)

		info1 = Contact_Us_list[0]
		info2 = Contact_Us_list[1]

		self.assertEqual(info1.name_m, 'Janielle')
		self.assertEqual(info1.email_m, 'janiellehembrador@gmail.com')
		self.assertEqual(info1.concern_m, 'Complaints')
		self.assertEqual(info1.review_m, 'Great product!')

		self.assertEqual(info2.name_m, 'jaji')
		self.assertEqual(info2.email_m, 'jajiembrador@gmail.com')
		self.assertEqual(info2.concern_m, 'Feedback')
		self.assertEqual(info2.review_m, 'Nice product!')


	def test_template_display_list(self):
		Contact_Us.objects.create(name_m = 'Jaja',
			email_m = 'jajahembrador@gmail.com',
			concern_m = 'Others',
			review_m = 'Love the product!')

		Contact_Us.objects.create(name_m = 'Shan',
			email_m = 'shanhembrador@gmail.com',
			concern_m = 'Others',
			review_m = 'Love it')

		response = self.client.get('/')
		self.assertIn('Jaja, jajahembrador@gmail.com, Others, Love the product!', response.content.decode())
		self.assertIn('Shan, shanhembrador@gmail.com, Others, Love it', response.content.decode())

