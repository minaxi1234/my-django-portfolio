from django.shortcuts import render
from django.http import HttpResponse
from .models import ContactMessage



def home_view(request):
  context = {
    'name':'Meenakshi',
    'course': 'django basics',
    'topics' : ['Templates','Views', 'URLs', "Models", 'Forms'],
    "goals": ["Learn Python basics", "Learn Django templates", "Build a project"]
  }
  return render(request, 'home/index.html',context)

def about_view(request):
  context = {
    'name': 'Meenakshi',
    'course': 'DJango',
    'bio':'This site is created by Meenakshi to learn Django step by step.',
    'skills': ['Python', 'Django Templates', 'Views', 'URLs', 'Models', 'Forms']
  }
  return render(request, 'home/about.html', context)

def contact_view(request):
  message_sent = False

  if request.method == 'POST':
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')

    ContactMessage.objects.create(name=name, email=email,message=message)

    message_sent = True
  context = {'message_sent': message_sent}
  return render(request, 'home/contact.html', context)

def message_view(request):
  messages = ContactMessage.objects.all().order_by('-created_at')
  context = {'messages': messages}
  return render(request, 'home/messages.html', context)




