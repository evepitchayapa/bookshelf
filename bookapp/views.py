from django.shortcuts import render,get_object_or_404,Http404
from .models import Bookwriter,Author,Publisher
from django.contrib.auth.models import User,auth
from django.shortcuts import render, redirect
from django.contrib import messages
import time

# Create your views here.

def homepage (request):
    firstbook = Bookwriter.objects.all()
    book5order =[]
    for i in firstbook:
        if len(book5order) < 5:
            book5order.append(i)
    context= {'firstbook':book5order}
    return render(request,'homepage.html',context)

def search (request):
    flide = str (request.POST.get('flide'))
    check = str(request.POST.get('num1'))
    book = Bookwriter.objects.all()
    author = Author.objects.all()
    publisher = Publisher.objects.all()
    result = []
    print (check)
    if check == '10':
        order = 10
    elif check == '100':
        order =100
    elif check == 'all':
        order =-1
        
    if flide == 'book':
        if order == -1:
            result = book
        else:
            for i in book:
                if len(result)< order :
                    result.append(i)
    elif flide == 'author':
        if order == -1:
            result = author
        else:
            for i in author:
                if len(result)<order:
                    result.append(i)
    elif flide == 'publisher':
        if order == -1:
            result = publisher
        else:
            for i in publisher:
                if len(result)<order:
                    result.append(i)
   
    context = {"result":result,"flide":flide}
    return render(request,'search.html',context)


def signup (request):
    return render(request,'signup.html')

def createuser (request):
    firstname = request.POST.get("firstname")
    lastname = request.POST.get("lastname")
    username = request.POST.get("username")
    password = request.POST.get("password")
    rpassword = request.POST.get("rpassword")
    email1 = request.POST.get("email1")

    if password == rpassword:
        if User.objects.filter(username=username).exists():
            # print("UserName already used")
            messages.info(request,"UserName already used")
            return redirect('/signup')
        elif User.objects.filter(email=email1).exists():
            # print("Email already used")
            messages.info(request,"Email already used")
            return redirect('/signup')
        else:
            user = User.objects.create_user(
                username = username,
                password = password,
                email = email1,
                first_name = firstname,
                last_name = lastname
            )
            user.save()
            return render(request,'createuser.html')
    else :
        # print("Password not match")
        messages.info(request,"Password not match")
        return redirect('/signup')
def logout(request):
    auth.logout(request)
    return redirect('/accounts/login')

def querybyuser (request):
    timestart = time.time()
    flide = str(request.POST.get("flide-1"))
    searchboth = str(request.POST.get("searchboth"))
    searchbook = str (request.POST.get("searchbook"))
    at = ''
    resultid = []
    resultbook = []
    keepbook=[]
    if flide == 'author':
        at = 'author'
        a = Author.objects.filter(a_name__startswith = searchboth)
        for i in a:
            resultid.append(i.id) 
        if len(searchbook) != 0 :
            for i in resultid:                
                au = Author.objects.get(id=i)
                keepbook.append(au.bookwriter_set.all())
            for i in keepbook:
                resultbook.append(i.filter(b_name__startswith = searchbook))             
        else:
            for i in resultid:
                au = Author.objects.get(id=i)
                resultbook.append(au.bookwriter_set.all())
    elif flide == 'publisher':
        at = 'publisher'
        p = Publisher.objects.filter(p_name__startswith = searchboth)
        for i in p:
            resultid.append(i.id)
        if len(searchbook) != 0:
            for i in resultid:                
                publish = Publisher.objects.get(id=i)
                keepbook.append(publish.bookwriter_set.all())
            for i in keepbook:
                kept = i.filter(b_name__startswith = searchbook)
                resultbook.append(kept)  
                print (resultbook)  
        else:
            for i in resultid:
                pub = Publisher.objects.get(id=i)
                resultbook.append(pub.bookwriter_set.all())
    elif len(searchbook) != 0 and flide == '':
        at = 'book'
        resultbook = Bookwriter.objects.filter(b_name__startswith = searchbook)
    timestop = time.time()
    timeall = timestop-timestart
    context = {'at':at,'setbook':resultbook,'time':timeall}
    return render (request,'querybyuser.html',context)


