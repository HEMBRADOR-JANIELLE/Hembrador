from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

def customerpage(request):
	cuslist = Customer.objects.all()
	return render(request,'mainpage.html')

def showPage(request,customerId):
	addcust =  Customer.objects.get(id=customerId)
	if request.method=='POST':
		Order.objects.create(name_id=addcust,product=request.POST['product'], quantity=request.POST['quantity'], 
			order_date=request.POST['order_date'],delivery_type=request.POST['delivery_type'])
		return redirect(f'/aesys/{addcust.id}/addCart/')
	else:
		return render(request, 'storepage.html',{'addcust':addcust})


	# customerId = Customer.objects.get(id=customerId)
	# return render(request,'storepage.html',{'customerId':customerId})

def customerpageList(request):
	name = request.POST['customer_name']
	number = request.POST['contact_no']
	email = request.POST['customer_email']
	city = request.POST['City_or_Municipality']
	province = request.POST['Province']
	newCustomer =  Customer.objects.create(customer_name=name,contact_no=number,customer_email=email,
		City_or_Municipality=city,Province=province)
	return redirect(f'/aesys/{newCustomer.id}/showpage/')


def addCart(request,customerId):
	addcust =  Customer.objects.get(id=customerId)
	addOrder=Order.objects.filter(name_id=customerId)
	print (addOrder)
	# addMessage = Review.objects.filter(name=addcust)
	# print(addMessage)
	if request.method=='POST':
		Review.objects.create(name_id=customerId, 
			concern_type=request.POST['concern_type'],
			message=request.POST['message'])
		return redirect(f'/aesys/{addcust.id}/summary/')
	else:
		return render(request, 'deliverypage.html',{'addcust':addcust,'addOrder':addOrder})

def summarypage(request, customerId):
	addcust =  Customer.objects.get(id=customerId)
	addOrder=Order.objects.filter(name_id=customerId)
	print (addOrder)
	addMessage = Review.objects.filter(name_id=addcust)
	print(addMessage)
	return render(request, 'summarypage.html',{'addcust':addcust,'addOrder':addOrder, 'addMessage':addMessage})

def cancelOrder(request, customerId):
	addcust =  Customer.objects.get(id=customerId)
	addcust.delete()
	return redirect(f'/aesys/{None}/summary/')

def summarypage2(request):
	return render(request, 'summarypage.html')

def editCustInfo(request, customerId):
	addcust = Customer.objects.get(id=customerId)	
	return render(request,'editdetails.html', {'addcust':addcust})

def updateCustInfo(request, customerId):
	addcust = Customer.objects.get(id=customerId)
	addcust.customer_name = request.POST['customer_name']
	addcust.contact_no = request.POST['contact_no']
	addcust.customer_email = request.POST['customer_email']
	addcust.City_or_Municipality = request.POST['City_or_Municipality']
	addcust.Province = request.POST['Province']
	addcust.save()	

	return redirect(f'/aesys/{addcust.id}/summary/')


# webdev 1

def homepage(request):
	return render(request, 'homepage.html')

def product(request):
	return render(request, 'allprod.html')

def product2(request):
	return render(request, 'allprod_2.html')

def product3(request):
	return render(request, 'allprod_3.html')

def product4(request):
	return render(request, 'allprod_4.html')

def product5(request):
	return render(request, 'allprod_5.html')

def product6(request):
	return render(request, 'allprod_6.html')