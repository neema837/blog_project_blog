from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Blog
from .forms import Blogforms


# Create your views here.
def home(request):
    blogview = Blog.objects.all()
    return render(request, 'index.html', {'blogview': blogview})


def reg(request):
    if request.method == 'POST':
        firstname = request.POST['fn']
        lastname = request.POST['ln']
        username = request.POST['uname']
        password1 = request.POST['p1']
        password2 = request.POST['p2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username already exists ")
            elif User.objects.filter(email=email).exists():
                messages.info(request, " Email Already Taken")
            else:
                user = User.objects.create_user(password=password1, username=username, email=email,
                                                first_name=firstname,
                                                last_name=lastname)
                user.save()
                print("User Created")
                return redirect("login")
    else:
        print("password not match")
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST["uname"]
        password = request.POST["p1"]
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Invalid User")
            return redirect('reg')
    return render(request, 'login.html')


def add(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        date = request.POST.get('date')
        # img = request.POST.get('img')
        obj = Blog(title=title, desc=desc, date=date)
        obj.save()
    return render(request, 'addblog.html')


def delete(request, blogid):
    blog = Blog.objects.get(id=blogid)
    if request.method == "POST":
        blog.delete()
        return redirect('/')
    return render(request, 'delete.html', {'blog': blog})


def update(request, id):
    blog = Blog.objects.get(id=id)
    form = Blogforms(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update.html', {'blog': blog,'form':form})
