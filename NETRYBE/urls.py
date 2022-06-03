from django.urls import path
from.import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('training/',views.training, name='courses'),
    path('coursedetails/',views.coursesdet,name='coursedetails'),
    path('contact/', views.contact, name='contact'),
    path('datasci/',views.datasci,name='datasci'),
    path('frontend/',views.frontend,name='frontend'),
    path('productdesign/',views.productdesign,name='productdesign'),
    path('backend/',views.backend, name='backend'),
    path('schprog/', views.schprog,name='schprog')
]