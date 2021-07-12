from django.contrib import admin
from django.urls import path
from home import views

admin.site.site_header = "Manu Admin"
admin.site.site_title = "Manu Admin Portal"
admin.site.index_title = "Welcome to Manu Admin Portal"


urlpatterns = [

    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("summarizer", views.summarizer, name='summarizer'),
    path("generation", views.generation, name='generation'),
    path("sentiment", views.sentiment, name='sentiment'),
    path("question", views.question, name='question'),
    

]



