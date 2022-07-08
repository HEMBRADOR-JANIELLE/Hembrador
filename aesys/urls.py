"""mahaba
"""
from django.contrib import admin
from django.urls import path
from aesys import views
from django.urls import re_path as url

urlpatterns = [

    url(r'^customerlist/$', views.customerpageList, name='customerlist/'),
    url(r'^(\d+)/showpage/', views.showPage, name='showpage/'),
    url(r'^(\d+)/addCart/', views.addCart, name='addCart/'),
    url(r'^(\d+)/summary/', views.summarypage, name='summary/'),
    url(r'^None/summary/', views.summarypage2, name='summary/'),
    url(r'^(\d+)/cancelorder/', views.cancelOrder, name='cancelorder'),
    url(r'^edit/(\d+)', views.editCustInfo, name='edit/'),
    url(r'^edit/update/(\d+)', views.updateCustInfo, name='update/'),
   

    # path('storepage/', views.storepage, name='storepage/'),
    # path('customerpage/',views.customerpage, name='customerpage/'),
    path('customerpage/',views.customerpage, name='customerpage/'),
   


# webdev1
    path('product/', views.product, name='product/'),
    path('product2/', views.product2, name='product2/'),
    path('product3/', views.product3, name='product3/'),
    path('product4/', views.product4, name='product4/'),
    path('product5/', views.product5, name='product5/'),
    path('product6/', views.product6, name='product6/'),
]
