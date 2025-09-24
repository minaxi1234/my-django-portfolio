from django.urls import path
from .views import home_view, about_view,contact_view,message_view

urlpatterns = [
  path('', home_view, name='home'),
  path('about/', about_view, name='about'),
  path("contact/", contact_view, name='contact'),
  path("messages/", message_view, name='messages'),
]