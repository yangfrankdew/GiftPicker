from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from TestModel.models import Input, Send, Product, Tag, Feedback

class InputForm(forms.Form):
    inputID = forms.IntegerField()
    receiverID = forms.IntegerField()
    hobby = forms.CharField(max_length=50)
    age = forms.IntegerField()
    relationship = forms.CharField(max_length=50)
    budget = forms.FloatField()
    ocassion = forms.CharField(max_length=50)
    customerID = forms.IntegerField()

class SendForm(forms.Form):
    sendID = forms.IntegerField()
    receiverID = forms.IntegerField()
    customerID = forms.IntegerField()
    productID = forms.IntegerField()
    inputID = forms.IntegerField()

class ProductForm(forms.Form):
    productID = forms.IntegerField()
    tagID = forms.IntegerField()
    shoppingplatform = forms.CharField(max_length=50)
    price = forms.FloatField()
    weblink = forms.CharField(max_length=255)
    productname = forms.CharField(max_length=100)
    imagelink = forms.CharField(max_length=255)

class TagForm(forms.Form):
    tagID = forms.IntegerField()
    hobby = forms.CharField(max_length=50)
    age = forms.IntegerField()
    relationship = forms.CharField(max_length=50)
    budget = forms.FloatField()
    ocassion = forms.CharField(max_length=50)

class FeedbackForm(forms.Form):
    feedbackID = forms.IntegerField()
    satisfactionvalue = forms.IntegerField()
    sendID = forms.IntegerField()
    receiverID = forms.IntegerField()
    customerID = forms.IntegerField()
    productID = forms.IntegerField()