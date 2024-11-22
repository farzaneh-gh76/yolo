from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def catg(request, adad):
    p=shop_prd.objects.filter(category_id=adad)
    c=category.objects.all()
    return render(request , "yolo/html/shop.html" , context={"p":p , "c":c})


def home(request):
    p=shop_prd.objects.all()
    lp=len(p)
    if lp>20:
        np=p[lp-20:]
    else:
        np=p
    a=article.objects.all()
    la=len(a)
    a=a[la-2:]
    add=advertisement.objects.all()    
    ts=topservice.objects.all()
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/index.html", context={"s":s  ,"c":c, "i":i , "ts":ts , "np":np, "p":p, "add":add, "a":a})

def error(request):
    return render(request , "yolo/html/404.html")

def about(request):
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    e=employee.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/about-us.html" , context={"e":e , "s":s ,"c":c, "i":i})

def address(request):
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/address.html", context={"s":s  ,"c":c, "i":i})

def blog(request):
    s=service.objects.all()
    c=category.objects.all()
    a=article.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/blog-grid.html", context={"s":s  ,"c":c, "a":a , "i":i})

def blogd(request, adad): 
    msg=commentblog.objects.filter(num=adad)
    s=service.objects.all()
    c=category.objects.all()
    a=article.objects.filter(id=adad)
    i=identity.objects.all()

    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
      
    if (request.method=="GET"):
        n=request.GET.get("name")
        e=request.GET.get("email")
        m=request.GET.get("comment")        
        if (n  and m and e):
            commentblog.objects.create(name=n , email=e , comment=m , num=adad)
            return redirect("/success")
    
    return render(request , "yolo/html/blog-detail.html",context={"s":s  ,"c":c, "a":a , "i":i , "msg":msg})


def cart(request):
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/cart.html", context={"s":s  ,"c":c, "i":i})


def comingsoon(request):
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")  
    return render(request , "yolo/html/coming-soon.html",context={"s":s  ,"c":c, "i":i})


def compare(request):
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/compare.html", context={"s":s  ,"c":c, "i":i})


def contact(request):
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        f=request.POST.get("fName")
        l=request.POST.get("lName")   
        em=request.POST.get("email")
        n=request.POST.get("call")
        msg=request.POST.get("comment")
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
        
        if (f and l and em and n and msg):
            message.objects.create(fname=f ,lname=l, email=em, call=n , comment=msg)
            return redirect("/success")   

    return render(request , "yolo/html/contact-us.html" , context={"s":s  ,"c":c, "i":i})

def faqs(request):
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    q1=fquestion.objects.filter(group=1)
    q2=fquestion.objects.filter(group=2)
    q3=fquestion.objects.filter(group=3)
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/faqs.html", context={"s":s  ,"c":c, "i":i , "q1":q1 ,"q2":q2 ,"q3":q3})


def forgot(request):
    return render(request , "yolo/html/forgot-password.html")

def login(request):
    return render(request , "yolo/html/login.html")

def onsale(request):
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/onsale.html", context={"s":s  ,"c":c, "i":i})

def ordersuccess(request):
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/order-success.html", context={"s":s  ,"c":c, "i":i})

def otp(request):
    return render(request , "yolo/html/otp.html")

def payment(request):
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/payment.html", context={"s":s  ,"c":c, "i":i})


def product(request, adad):
    p=shop_prd.objects.filter(id=adad)
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/product.html" , context={"p":p , "s":s  ,"c":c, "i":i})

def register(request):
    return render(request , "yolo/html/register.html")

def resetpassword(request):
    return render(request , "yolo/html/reset-password.html")


def search(request):
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/search.html" ,  context={ "s":s  ,"c":c, "i":i})


def shop(request):
    p=shop_prd.objects.all()
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/shop.html" , context={"p":p ,"s":s  ,"c":c, "i":i})

def success(request):
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/success.html" ,  context={ "s":s  ,"c":c, "i":i})


def user(request):
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/user-dashboard.html" ,  context={ "s":s  ,"c":c, "i":i})


def wishlist(request):
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/wishlist.html" ,  context={ "s":s  ,"c":c, "i":i})
