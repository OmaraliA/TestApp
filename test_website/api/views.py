from django.shortcuts import render
from api.models import Lecture, User, Test
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from rest_framework.decorators import action
from api.serializer import TestSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

def register(request):
    form = UserCreationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('lecture')
        else:
            error = "username or password incorrect"
            return render(request, 'login.html', {'error': error})
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('home')

def lecture_list(request):
  lectures = Lecture.objects.all()
  return render(request, 'lecture.html', {'lectures': lectures})

def lecture_details(request, pk):
  lecture = Lecture.objects.get(pk=pk)
  return render(request, 'singleLecture.html', {'lecture': lecture})

def user_list(request):
  users = User.objects.all()
  return render(request, 'index.html', {'users': users})

def user_details(request, pk):
  user = User.objects.get(pk=pk)
  return render(request, 'index.html')

@action(methods=['get'], detail=True)
def testing(request):
  tests = Test.objects.all()
  context = {'tests': TestSerializer(tests, many=True).data}
  return render(request,'test.html',context)

def test_details(request, pk):
  tests = Test.objects.filter(lecture_id=pk)
  return render(request, 'test.html',{'tests': tests})

def home(request):
    return render(request, 'home.html')


