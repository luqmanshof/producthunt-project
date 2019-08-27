
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
# from products import views
import products.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',products.views.home, name='home'),
    path('accounts/',include('accounts.urls')),
]
