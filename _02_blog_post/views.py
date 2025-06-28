from django.shortcuts import render, redirect
import qrcode
from django.http import HttpResponse
from blogs.models import Blogs
from _02_blog_post.form import UserForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
import uuid
import os
from io import BytesIO
from django.core.files.storage import default_storage
from django.core.mail import send_mail


def index(request):
    data = Blogs.objects.all()
    for d in data:
        print(d.title)
    return render(request, "index.html", {"data": data})


def blog_page(request, id):
    data = Blogs.objects.get(id=id)

    bg_classes = [
        "from-blue-50 via-sky-100 to-blue-200",
        "from-teal-50 via-green-100 to-emerald-200",
        "from-indigo-50 via-purple-100 to-violet-200",
        "from-amber-50 via-yellow-100 to-orange-200",
        "from-slate-100 via-gray-200 to-zinc-200",
    ]
    selected_bg = bg_classes[data.id % len(bg_classes)]

    return render(request, "full-blog-page.html", {"data": data, "bg": selected_bg})


def login_user(request):
    form = UserForm
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "YOu have been success fully logged in ")
            return redirect("index")
        else:
            messages.warning(request, "please check your inputs")
            return redirect("loginUser")

    else:
        return render(request, "login.html", {"form": form})


def register(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, "You are successfully Registered to the Blog Account"
            )
            return redirect("index")
        else:
            messages.warning(
                request,
                "YOu have something error while registering please try again later",
            )
            return HttpResponse("PLease enter the correct data")

    else:

        return render(request, "register.html", {"form": form})


def filter(request):
    category = request.GET.get("category")
    blogs = Blogs.objects.all().filter(category=category)
    if blogs == None:
        return HttpResponse("There is no blogs on this category")

    return render(request, "index.html", {"data": blogs})


def search(request):
    title = request.GET.get("search")
    blogs = Blogs.objects.filter(title__icontains=title)
    if blogs == None:
        return HttpResponse("There is no blog of this title")

    return render(request, "index.html", {"data": blogs})


def paymentQr(request):
    if request.method == "POST":
        upi_id = request.POST.get("upi_id")
        amt = request.POST.get("amount")

        upi_url = (
            f"upi://pay?pa={upi_id}&pn=Recipient%20Name&am={amt}&cu=INR&tn=Payment"
        )

        # Unique filename to avoid reuse
        filename = f"paymentQr/upi_qr_{uuid.uuid4().hex}.png"
        qr = qrcode.make(upi_url)

        filepath = f"media/{filename}"
        qr.save(filepath)

        return render(
            request, "paymentQrCodeGenerator.html", {"qr_url": f"/media/{filename}"}
        )
    return render(request, "paymentQrCodeGenerator.html")


def logout_user(request):
    logout(request)
    messages.success(request, "YOu have been successfully Logged Out")
    return redirect("index")


from django.core.mail import send_mail


def donation(request):
    if request.method == "POST":
        purpose = request.POST.get("purpose")
        message = request.POST.get("message")

        send_mail(
            subject=purpose,
            message=message,
            from_email="prashu8511@gmail.com",  # Sender
            recipient_list=["prashu8511@gmail.com"],  # Receiver (your own email)
            fail_silently=False,
        )
        return render(request, "donation.html", {"success": True})
    else:
        return render(request, "donation.html")
