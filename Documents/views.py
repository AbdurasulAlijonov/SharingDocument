from datetime import date
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from Documents.models import Signup,Documents


def index(request):
    return render(request,'Documents/index.html')

def about(request):
    return render(request,'Documents/about.html')

def contact(request):
    return render(request,'Documents/contact.html')

def user_login(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        print(user)
        try:
            if user is not None:
                login(request, user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'
    context = {'error': error}
    return render(request,'Documents/login.html',context)

def login_admin(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        try:
            if user.is_staff:
                login(request,user)
                error = 'no'
            else:
                error = 'yes'
        except:
            error = 'yes'
    d = {'error':error}
    return render(request,'Documents/login_admin.html',d)

def signupUser(request):
    error = ''
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        password1 = request.POST['password1']
        branch = request.POST['branch']
        role = request.POST['role']

        try:
            user = User.objects.create_user(username=username,first_name=firstname,
                                            last_name=lastname,
                                            email=email,
                                            password=password)
            print('created user')
            Signup.objects.create(user=user,branch=branch,contact=contact,role=role)
           # Signup.save(user)
            error = 'no'
        except:
            error = 'yes'
    context = {'error' : error}
    return render(request,'Documents/signup.html', context=context)


def admin_home(request):
    if not request.user.is_staff:
        return redirect('login_admin')
    return render(request,'Documents/admin_home.html')

def Logout(request):
    logout(request)
    return redirect('index')

def profile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    context = {'data':data,'user':user}
    return render(request,'Documents/profile.html', context=context)

def changepassword(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ''
    if request.method == 'POST':
        oldpassword = request.POST['oldpassword']
        newpassword = request.POST['newpassword']
        conpassword = request.POST['confirmpassword']
        if newpassword == conpassword:
            user = User.objects.get(username__exact=request.user.username)
            user.set_password(newpassword)
            user.save()
            error = 'no'
        else:
            error = 'yes'
    context = {'error' : error}
    return render(request,'Documents/changepassword.html', context)


def editprofile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    data = Signup.objects.get(user=user)
    error = False
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        contact = request.POST['contact']
        user.first_name = firstname
        user.last_name = lastname
        user.username = username
        data.contact = contact
        user.save()
        data.save()
        error = True
    context = {'data':data,'user':user, 'error' : error}
    return render(request,'Documents/editprofile.html',context)

def upload_documents(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ''
    if request.method == 'POST':
        branch = request.POST['branch']
        subject = request.POST['subject']
        documentfile = request.POST['documentfile']
        filetype = request.POST['filetype']
        description = request.POST['description']

        user = User.objects.filter(username=request.user.username).first()
        try:
            document = Documents.objects.create(user=user,
                                                uploadingdate=date.today(),
                                                branch=branch,
                                                subject=subject,
                                                documentfile=documentfile,
                                                filetype=filetype,
                                                description=description,
                                                status='Pending')
            error = 'no'
        except:
            error = 'yes'
    context = {'error': error}
    return render(request, 'Documents/upload_document.html', context=context)