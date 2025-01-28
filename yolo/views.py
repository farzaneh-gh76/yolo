from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import  authenticate,login as lg , logout as lo
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
    b=banner.objects.all()
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
    return render(request , "yolo/html/index.html", context={"s":s  ,"c":c, "i":i , "ts":ts , "np":np, "p":p, "add":add, "a":a , "b":b})

def error(request):
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")

    return render(request , "yolo/html/404.html", context={ "s":s ,"c":c, "i":i})

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
    #u=user_address.objects.filter(user_account_id=adad)
    u=user_address.objects.all()
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl")
        n=request.POST.get("name")
        em=request.POST.get("email")
        m=request.POST.get("mobile")
        a=request.POST.get("address1")
        cp=request.POST.get("zip")
        co=request.POST.get("country") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")               
        if (n and m and a and cp and co):
            user_address.objects.create(name=n , email=em , call=m , city=co , address=a ,zip=cp)
            return redirect("/success")    
        
    return render(request , "yolo/html/address.html", context={"s":s  ,"c":c, "i":i , "u":u})

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

@login_required
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
    return render(request , "yolo/html/faqs.html", context={"s":s  ,"c":c, "i":i , "q1":q1 ,"q2":q2 ,"q3":q3})


def forgot(request):
    return render(request , "yolo/html/forgot-password.html")

def login(request):
    if (request.method=="POST"):
        usr=request.POST.get("email")
        pass1=request.POST.get("password")
        u=authenticate(username=usr,password=pass1)
        if u is not None:
            lg(request,u)
            if (u.role=="normal"):
                return redirect("/user")
            else:
                return redirect("/uservip")
            
        else:
            return render(request , "yolo/html/login.html" , context={"msg":"نام کاربری و یا رمز عبور اشتباه است"})

    return render(request , "yolo/html/login.html")

def logout(request):
    lo(request)
    return redirect('/login')

def onsale(request):
    p=[]
    pw=shop_prd.objects.all( )
    for i in range(len(pw)):
        pp=pw[i]
        if (int(pp.curprice) / int(pp.preprice))<0.9:
            p.append(pp)

    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/onsale.html" , context={"p":p ,"s":s  ,"c":c, "i":i})

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
    cp=product_comment.objects.filter(num=adad)
    p=shop_prd.objects.filter(id=adad)
    q=p[0].category_id
    sug=shop_prd.objects.filter(category_id=q)
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
         
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
        
    if (request.method=="GET"):
        n=request.GET.get("name") 
        em=request.GET.get("email") 
        msg=request.GET.get("comment")
        if(n and em and msg):
            product_comment.objects.create(name=n , email=em , comment=msg ,num=adad)
            return redirect("/success")
        
    return render(request , "yolo/html/product.html" , context={"p":p , "s":s  ,"c":c, "i":i , "cp":cp ,"sug":sug})

def register(request):
    if(request.method=="POST"):
        usr=request.POST.get("email")
        eml=request.POST.get("email")
        name=request.POST.get("full-name")
        pass1=request.POST.get("password")
        CustomUser.objects.create_user(usr,eml,pass1,first_name=name,is_staff=False)
        return redirect("/login")        
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
    if (request.method=="GET"):
        r=request.GET.get("key") 
        if (r):
            sr=shop_prd.objects.filter(title__contains=r)
            return render(request , "yolo/html/search.html" ,  context={ "s":s  ,"c":c, "i":i , "sr":sr})
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

@login_required
def user(request):
    u=user_address.objects.all()
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl")
        n=request.POST.get("name")
        em=request.POST.get("email")
        m=request.POST.get("mobile")
        a=request.POST.get("address1")
        cp=request.POST.get("zip")
        co=request.POST.get("country") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")               
        if (n and m and a and cp and co):
            user_address.objects.create(name=n , email=em , call=m , city=co , address=a ,zip=cp)
            return redirect("/success")    
        
    if(request.user.role=="normal"):
        return render(request , "yolo/html/user-dashboard.html", context={"s":s  ,"c":c, "i":i , "u":u})
    else:
        return redirect("/login")

@login_required
def uservip(request):
    u=user_address.objects.all()
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl")
        n=request.POST.get("name")
        em=request.POST.get("email")
        m=request.POST.get("mobile")
        a=request.POST.get("address1")
        cp=request.POST.get("zip")
        co=request.POST.get("country") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")               
        if (n and m and a and cp and co):
            user_address.objects.create(name=n , email=em , call=m , city=co , address=a ,zip=cp)
            return redirect("/success")    
    if(request.user.role=="vip"):
        return render(request , "yolo/html/user-dashboard-vip.html", context={"s":s  ,"c":c, "i":i , "u":u})
    else:
        return redirect("/login")

       

@login_required
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
