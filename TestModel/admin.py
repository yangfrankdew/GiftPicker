from django.contrib import admin
from TestModel.models import Input, Send, Product, Tag, Feedback

# Register your models here.
admin.site.register([Input, Send, Product, Tag, Feedback])