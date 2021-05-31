from django.urls import path,include
from .views import home ,create ,redirect

urlpatterns =[
    path('',home,name = 'home'),
    path('create/',create,name ='create'),
    path('<str:url>',redirect,name ='redirect')
]