from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('home.urls')),
    path('Contact_us/', include('Contact.urls')),
    path('post_detail/', include('post_detail.urls')),
    path('', include('accounts.urls')),
    path('order/', include('order.urls')),

]
