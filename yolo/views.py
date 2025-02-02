from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.contrib.auth.decorators import  login_required
from django.contrib.auth import  authenticate,login as lg , logout as lo
import jdatetime
# Create your views here.

def catg(request, adad):
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()
         
         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]
    p=shop_prd.objects.filter(category_id=adad)
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")     
      
    return render(request , "yolo/html/shop.html" , context={"p":p ,"s":s  ,"c":c, "i":i,"w":w ,"can":can , "ca":ca})


def home(request):
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()

         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]

    pw=[]
    p=shop_prd.objects.all()
    for i in range(len(p)):
        pp=p[i]
        if (int(pp.curprice) / int(pp.preprice))<0.9:
            pw.append(pp)
    
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
    return render(request , "yolo/html/index.html", context={"s":s  ,"c":c, "i":i , "ts":ts , "np":np, "p":p, "pw":pw, "add":add, "a":a , "b":b,"w":w ,"can":can , "ca":ca})

def error(request):
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()

         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")

    return render(request , "yolo/html/404.html", context={ "s":s ,"c":c, "i":i,"w":w ,"can":can , "ca":ca})

def about(request):
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()
         
         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]
    
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    e=employee.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/about-us.html" , context={"e":e , "s":s ,"c":c, "i":i,"w":w ,"can":can , "ca":ca})


@login_required
def address(request):
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()
         
         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]
    u=user_address.objects.filter(user=request.user)
    #u=user_address.objects.all()
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    ord=order.objects.filter(user=request.user,status="cart").first()    
    if ord.address is not None:
        odrs=ord.address
    else:
        odrs=None
        
        
    num=0
    ben=0
    to=0
    
    for itm in ord.items.all():
        to+=itm.product.preprice * itm.qnt
        num+=itm.qnt
        ben+=((itm.product.preprice * itm.qnt)-(itm.product.curprice * itm.qnt))
    
    sm=20000+to-ben
    if (request.method=="POST"):
        e=request.POST.get("eml-nl")
        n=request.POST.get("name")
        m=request.POST.get("mobile")
        a=request.POST.get("address1")
        cp=request.POST.get("zip")
        co=request.POST.get("country") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")               
        if (n and m and a and cp and co):
            user_address.objects.create(name=n  , call=m , city=co , address=a ,zip=cp,user=request.user)
            return redirect("/address")    
        
    return render(request , "yolo/html/address.html", context={"s":s  ,"c":c, "i":i , "u":u,"ord":ord , "sm":sm , "num":num , "ben":ben ,"to":to,"w":w ,"can":can , "ca":ca, "odrs":odrs})

def blog(request):
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()
         
         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]
    s=service.objects.all()
    c=category.objects.all()
    a=article.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/blog-grid.html", context={"s":s  ,"c":c, "a":a , "i":i,"w":w ,"can":can , "ca":ca})

def blogd(request, adad): 
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()
         
         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]
    msg=commentblog.objects.filter(num=adad)
    s=service.objects.all()
    c=category.objects.all()
    a=article.objects.filter(id=adad)
    i=identity.objects.all()
    for itm in a:
        date_gregorian=itm.date
        date_jalali=jdatetime.datetime.fromgregorian(datetime=date_gregorian)
        date_jalali_str=date_jalali.strftime("%Y/%m/%d")
 
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
    
    return render(request , "yolo/html/blog-detail.html",context={"s":s  ,"c":c, "a":a , "i":i , "msg":msg,"dj":date_jalali_str,"w":w ,"can":can , "ca":ca})

@login_required
def cart(request):
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()
         
         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    ord=order.objects.filter(user=request.user,status="cart").first()    
    num=0
    ben=0
    to=0
    if ord is not None:
        for itm in ord.items.all():
          to+=itm.product.preprice * itm.qnt
          num+=itm.qnt
          ben+=((itm.product.preprice * itm.qnt)-(itm.product.curprice * itm.qnt))
    
    sm=20000+to-ben

    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/cart.html", context={"s":s  ,"c":c, "i":i,"ord":ord , "sm":sm , "num":num , "ben":ben ,"to":to,"w":w ,"can":can , "ca":ca})


def comingsoon(request):
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()
         
         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")  
    return render(request , "yolo/html/coming-soon.html",context={"s":s  ,"c":c, "i":i,"w":w ,"can":can , "ca":ca})





def contact(request):
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()
         
         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]
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

    return render(request , "yolo/html/contact-us.html" , context={"s":s  ,"c":c, "i":i,"w":w ,"can":can , "ca":ca})

def faqs(request):
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()
         
         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]
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
    return render(request , "yolo/html/faqs.html", context={"s":s  ,"c":c, "i":i , "q1":q1 ,"q2":q2 ,"q3":q3,"w":w ,"can":can , "ca":ca})




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
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()
         
         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]
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
    return render(request , "yolo/html/onsale.html" , context={"p":p ,"s":s  ,"c":c, "i":i,"w":w ,"can":can , "ca":ca})

def ordersuccess(request):
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()
         
         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/order-success.html", context={"s":s  ,"c":c, "i":i,"w":w ,"can":can , "ca":ca})






def product(request, adad): 
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()
         
         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]   
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
        
    return render(request , "yolo/html/product.html" , context={"p":p , "s":s  ,"c":c, "i":i , "cp":cp ,"sug":sug,"w":w ,"can":can , "ca":ca})

def register(request):
    if(request.method=="POST"):
        usr=request.POST.get("email")
        eml=request.POST.get("email")
        name=request.POST.get("full-name")
        pass1=request.POST.get("password")
        CustomUser.objects.create_user(usr,eml,pass1,first_name=name,is_staff=False)
        return redirect("/login")        
    return render(request , "yolo/html/register.html")




def search(request):
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()
         
         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]
    sr=[]
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
            return render(request , "yolo/html/search.html" ,  context={ "s":s  ,"c":c, "i":i , "sr":sr,"w":w ,"can":can , "ca":ca})
    return render(request , "yolo/html/search.html" ,  context={ "s":s  ,"c":c, "i":i,"w":w ,"can":can , "ca":ca})


def shop(request):
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()
         
         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]
    p=shop_prd.objects.all()
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/shop.html" , context={"p":p ,"s":s  ,"c":c, "i":i,"w":w ,"can":can , "ca":ca})

def success(request):
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()
         
         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all() 
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/success.html" ,  context={ "s":s  ,"c":c, "i":i,"w":w ,"can":can , "ca":ca})

@login_required
def user(request):
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()
         
         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]
    ord=order.objects.filter(user=request.user,status="final").first()
    u=user_address.objects.all()
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl")
        
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")               
            
        
    if(request.user.role=="normal"):
        return render(request , "yolo/html/user-dashboard.html", context={"s":s  ,"c":c, "i":i , "u":u,"w":w ,"can":can , "ca":ca, "ord":ord})
    if(request.user.role=="vip"):
        return redirect("/uservip")
    else:
        return redirect("/login")

@login_required
def uservip(request):
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()
         
         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[]
    ord=order.objects.filter(user=request.user,status="final").first()
    u=user_address.objects.all()
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl")
         
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")               
         
    if(request.user.role=="vip"):
        return render(request , "yolo/html/user-dashboard-vip.html", context={"s":s  ,"c":c, "i":i , "u":u,"w":w ,"can":can , "ca":ca,"ord":ord})
    if(request.user.role=="normal"):
        return redirect("/user")
    else:
        return redirect("/login")

       

@login_required
def wishlist(request):
    if request.user.is_authenticated :
         ws=wish.objects.filter(user=request.user)
         ca=order.objects.filter(user=request.user,status="cart").first()
         
         if ws is not None:         
            w=len(ws)
         else:
             w=0
         if ca is not None:
            can=len(ca.items.all())
         else:
            can=0
    else:
        w=0
        can=0
        ca=[] 
    s=service.objects.all()
    c=category.objects.all()
    i=identity.objects.all()
    if (request.method=="POST"):
        e=request.POST.get("eml-nl") 
        if (e):
            newsletter.objects.create(email=e)
            return redirect("/success")
    return render(request , "yolo/html/wishlist.html" ,  context={ "s":s  ,"c":c, "i":i,"w":w ,"can":can , "ca":ca,"ws":ws})

@login_required
def addcart(request,pid):
    product=get_object_or_404(shop_prd,id=pid)
    ord,created=order.objects.get_or_create(user=request.user,status="cart")
    orditm,created=orderitem.objects.get_or_create(order=ord,product=product)
   
    orditm.qnt+=1
    orditm.save()
    return redirect("/cart")

@login_required
def deletecart(request,itmid):
    orditm=get_object_or_404(orderitem,id=itmid,order__user=request.user,order__status="cart")
    
    orditm.delete()
    return redirect("/cart")

@login_required
def minuscart(request,itmid):
    orditm=get_object_or_404(orderitem,id=itmid,order__user=request.user,order__status="cart")
    orditm.qnt-=1
    orditm.save()
    if (orditm.qnt==0):
        orditm.delete()
    return redirect("/cart")

@login_required
def pluscart(request,itmid):
    orditm=get_object_or_404(orderitem,id=itmid,order__user=request.user,order__status="cart")
    orditm.qnt+=1
    orditm.save()
    return redirect("/cart")

@login_required
def addwish(request,pid):
    product=get_object_or_404(shop_prd,id=pid)
    w,created=wish.objects.get_or_create(user=request.user , product=product)     
    
    return redirect("/wishlist")

@login_required
def deletewish(request,itmid):
    itm=get_object_or_404(wish,user=request.user,product__id=itmid)
    
    itm.delete()
    return redirect("/wishlist")

@login_required
def addaddress(request,aid):
    ord,created=order.objects.get_or_create(user=request.user,status="cart")
    a=user_address.objects.get(user=request.user , id=aid)
    ord.address=a
    ord.save()
    return redirect("/address" , message="آدرس انتخابی شما اعمال شد.")


