from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=30)
    img=models.ImageField(upload_to="photo",null=True)
    def __str__(self) -> str:
        return self.name
    
class topservice(models.Model):
    opt=models.CharField(max_length=20, verbose_name="آپشن بالا صفحه اصلی")
    optd=models.CharField(max_length=50, verbose_name="جزئیات آپشن  بالا صفحه اصلی")
    color=models.CharField(max_length=20, verbose_name="لطفا تم رنگی را تغییر ندهید")
    def __str__(self) -> str:
        return( "opt"+str(self.id))
    
class fquestion(models.Model):
    question=models.CharField(max_length=100, verbose_name="پرسش")
    answer=models.TextField(verbose_name="پاسخ ")
    g=[("1","مشکلات پرداخت"),("2","تحویل سفارش"),("3"," عمومی")]
    group=models.CharField(max_length=30 , default="انتخاب کنید..." , choices=g , verbose_name="دسته بندی")
    def __str__(self) -> str:
        return( "q"+str(self.id))

    


class advertisement(models.Model):
    add=models.CharField(max_length=30, verbose_name="عنوان تبلیغ")
    exp=models.CharField(max_length=100, verbose_name="توضیحات")
    delay=models.CharField(max_length=10, verbose_name="لطفا تاخیر در نمایش را تغییر ندهید")
    img=models.ImageField(upload_to="photo")    
    def __str__(self) -> str:
        return( "add"+str(self.id))

class service(models.Model):
    specialnews=models.CharField(max_length=100 , null=True, verbose_name="خبر متحرک بالای صفحه")

    follower=models.CharField(max_length=10 ,verbose_name="تعداد دنبال کنندگان")
    customer=models.IntegerField(verbose_name="تعداد مشتریان")
    dailyparcel =models.IntegerField(verbose_name="تعداد سفارشات روزانه")
    dailyview=models.IntegerField(verbose_name="تعداد بازدیدهای روزانه از سایت")
    rising=models.CharField(max_length=10 , verbose_name="درصد رشد در سال")
    variety=models.IntegerField(verbose_name="تنوع محصولات")
   
    service1=models.CharField(max_length=30 , verbose_name="خدمت 1 صفحه درباره ما")
    service1detail=models.CharField(max_length=200  , verbose_name="جزئیات خدمت 1")
    service2=models.CharField(max_length=30 , verbose_name="خدمت 2 صفحه درباره ما")
    service2detail=models.CharField(max_length=200 , verbose_name="جزئیات خدمت 2")
    service3=models.CharField(max_length=30 , verbose_name="خدمت 3 صفحه درباره ما")
    service3detail=models.CharField(max_length=200 , verbose_name="جزئیات خدمت 3")
    service4=models.CharField(max_length=30 , verbose_name="خدمت 4 صفحه درباره ما")
    service4detail=models.CharField(max_length=200 , verbose_name="جزئیات خدمت 4")
       
    boldtitle=models.CharField(max_length=200 , verbose_name="عنوان درباره ما" )
    description=models.TextField(null=True, verbose_name="معرفی یولو صفحه درباره ما")
    img=models.ImageField(upload_to="photo",null=True,  verbose_name="تصویر یولو صفحه درباره ما")

class shop_prd(models.Model):
    title=models.CharField(max_length=30)
    preprice=models.IntegerField()
    curprice=models.IntegerField()
    description=models.CharField(max_length=100 , verbose_name="شرح مختصر محصول")
    details=models.TextField( null=True, verbose_name="شرح کامل محصول")
    img=models.ImageField(upload_to="photo", verbose_name="تصویر اصلی ")
    img1=models.ImageField(upload_to="photo",null=True, verbose_name="تصویر فرعی 1 ")
    img2=models.ImageField(upload_to="photo",null=True, verbose_name="تصویر فرعی 2 ")
    img3=models.ImageField(upload_to="photo",null=True, verbose_name="تصویر فرعی 3 ")
    category=models.ForeignKey(category , on_delete=models.CASCADE,related_name="pp")
    date=models.DateField(auto_now=True , verbose_name="تاریخ بارگذاری")
    def __str__(self) -> str:
        return self.title
    
class employee(models.Model):
    name=models.CharField(max_length=30, verbose_name="نام و نام خانوادگی")
    g=[("1","مرد"),("2","زن")]
    gender=models.CharField(max_length=30 , default="انتخاب کنید..." , choices=g)

    responsibility=models.CharField(max_length=30 , default="کارشناس")
    email=models.EmailField(help_text="ایمیل معتبر وارد کنید" , null=True, blank=True)
    start_day=models.DateField(auto_now=True)
    username=models.SlugField(db_index=True,unique=True,primary_key=True,error_messages={"unique":"این نام کاربری قبلا توسط شخص دیگیری انتخاب شده."})
    img=models.ImageField(upload_to="photo",null=True,  verbose_name="عکس پرسنلی")

    t=[("bg-theme-blue","blue"),("bg-theme-yellow","yellow"),("bg-theme-orange","orange"),("bg-theme-pink","pink")]
    theme=models.CharField(max_length=30 , default="انتخاب کنید..." , choices=t,  verbose_name="تم رنگی" , null=True)
    def __str__(self) -> str:
        return self.name

class article(models.Model):
    title=models.CharField(max_length=35, verbose_name="عنوان مقاله")
    subject=models.CharField(max_length=10, verbose_name="موضوع مقاله")
    keyword=models.CharField(max_length=10, verbose_name="کلید واژه مقاله")
    date=models.DateField(auto_now=True , verbose_name="تاریخ بارگذاری")
    writer=models.CharField(max_length=30 , verbose_name="نویسنده")
    summary=models.CharField(max_length=100 , verbose_name="چکیده" )
    description=models.TextField(verbose_name="متن مقاله")
    img=models.ImageField(upload_to="photo" , verbose_name="تصویر اصلی مقاله")
    img1=models.ImageField(upload_to="photo" ,null=True, verbose_name=" تصویر نمایشی مقاله در خانه")
    wimg=models.ImageField(upload_to="photo" , verbose_name="تصویر نویسنده مقاله")
    def __str__(self) -> str:
        return self.title
    
class identity(models.Model):
    address=models.CharField(max_length=100, verbose_name="آدرس")
    call=models.CharField(max_length=20, verbose_name="شماره تماس")
    email=models.EmailField(help_text="ایمیل معتبر وارد کنید" , null=True)
    open=models.CharField(max_length=100 , verbose_name="روز و ساعات کاری")
    img=models.ImageField(upload_to="photo" , verbose_name="لوگو" ,null=True)
    
class commentblog(models.Model):
    name=models.CharField(max_length=50, verbose_name="نام و نام خانوادگی")
    email=models.EmailField(help_text="ایمیل معتبر وارد کنید" , null=True)
    comment=models.TextField( verbose_name="نظر")  
    date=models.DateField(auto_now=True , verbose_name="تاریخ بارگذاری" ,null=True)
    num=models.IntegerField( verbose_name="شماره مقاله" ,null=True)
    def __str__(self) -> str:
        return self.name 
    

class newsletter(models.Model):
    email=models.EmailField(help_text="ایمیل معتبر وارد کنید")
    date=models.DateField(auto_now=True ,null=True) 
    def __str__(self) -> str:
        d=str(self.date)
        return d
    

class message(models.Model):
    fname=models.CharField(max_length=20, verbose_name="نام")
    lname=models.CharField(max_length=30, verbose_name="نام خانوادگی")
    email=models.EmailField(help_text="ایمیل معتبر وارد کنید", verbose_name="آدرس ایمیل")
    call=models.CharField(max_length=11, verbose_name="شماره تماس")
    comment=models.TextField( verbose_name="نظر")
    date=models.DateField(auto_now=True) 
    def __str__(self) -> str:
        d=str(self.date)
        return d
    
class user_address(models.Model):
    name=models.CharField(max_length=100, verbose_name="نام تحویل گیرنده")
    call=models.CharField(max_length=20, verbose_name="شماره تماس")
    email=models.EmailField(help_text="ایمیل معتبر وارد کنید" , null=True)
    city=models.CharField(max_length=20, verbose_name=" استان")
    address=models.CharField(max_length=500, verbose_name="آدرس")
    zip=models.CharField(max_length=20, verbose_name=" کدپستی")
    #username=models.ForeignKey(user_account , on_delete=models.CASCADE, related_name="pp")
    def __str__(self) -> str:
        return self.name
    
class banner(models.Model):
    img1=models.ImageField(upload_to="photo" , verbose_name="بنر 1" ,null=True)
    img2=models.ImageField(upload_to="photo" , verbose_name="بنر 2" ,null=True)
    msg1=models.CharField(max_length=500, verbose_name="توضیحات بنر 1")
    msg2=models.CharField(max_length=100, verbose_name="  خبر مشکی بنر 2")
    msg3=models.CharField(max_length=100, verbose_name="  خبر آبی بنر 2")
    msg4=models.CharField(max_length=500, verbose_name="توضیحات بنر 2")


class product_comment(models.Model):
    name=models.CharField(max_length=50, verbose_name="نام و نام خانوادگی")
    email=models.EmailField(help_text="ایمیل معتبر وارد کنید" )
    comment=models.TextField( verbose_name="نظر")  
    date=models.DateField(auto_now=True , verbose_name="تاریخ بارگذاری")
    num=models.IntegerField( verbose_name="شماره محصول" )
    def __str__(self) -> str:
        return self.name

roleitems=(("normal","عادی"),("vip","ویژه"))   
class CustomUser(AbstractUser):
    role=models.CharField(max_length=20, choices=roleitems, default="normal")