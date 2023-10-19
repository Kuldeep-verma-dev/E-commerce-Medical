from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import *
from django.db import connection


# Create your views here.


# THIS IS HOME PAGE RELATED VIEW CODE

def index(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    x = category.objects.all().order_by('-id')[0:6]
    pdata = myproduct.objects.all().order_by('-id')[0:7]
    mydict = {"data": x, "prodata": pdata, "cart": ct}
    return render(request, 'user/index.html', context=mydict)


# THIS IS ABOUT PAGE RELATED VIEW

def about(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    return render(request, 'user/aboutus.html', {"cart": ct})


# THIS IS ALL PRODUCT  VIEW

def product(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    return render(request, 'user/product.html', {"cart": ct})

# THIS IS MY ORDERS VIEW

def myorder(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    user = request.session.get('userid')
    oid = request.GET.get('oid')
    if user:
        if oid is not None:
            morder.objects.all().filter(id=oid).delete()
            return HttpResponse(
                "<script>alert('Your order has been cancelled..');location.href='/user/myorder/'</script>")
        cursor = connection.cursor()
        cursor.execute("select p.*,o.* from user_myproduct p, user_morder o where  p.id = o.pid and  o.userid='" + str(
            user) + "' and o.remarks='Pending'")
        pdata = cursor.fetchall()
        cursor.execute("select p.*,o.* from user_myproduct p, user_morder o where  p.id = o.pid and  o.userid='" + str(
            user) + "' and o.remarks='Delivered'")
        ddata = cursor.fetchall()
        mydict = {"pdata": pdata, "ddata": ddata, "cart": ct}
    else:
        return HttpResponse("<script>alert(' You have to Sign In first ..');location.href='/user/signin/'</script>")
    return render(request, 'user/myorder.html', mydict)


# THIS IS ENQUIRY PAGE VIEW

def enquiry(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    status = False
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('mob')
        c = request.POST.get('email')
        d = request.POST.get('msg')
        contactus(Name=a, Mobile=b, Email=c, Message=d).save()
        status = True
    msg = {"m": status, "cart": ct}
    return render(request, 'user/enquiry.html', context=msg)

#  THIS IS RAGISTRATION PAGE VIEW

def signup(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    status = False
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('phone')
        c = request.POST.get('email')
        d = request.POST.get('password')
        e = request.FILES.get('file')
        f = request.POST.get('msg')
        x = register.objects.all().filter(email=c).count()
        if x == 0:
            register(name=a, email=c, mobile=b, passwd=d, address=f, ppic=e).save()
            return HttpResponse(
                "<script>alert('You are registered successfully.....');location.href='/user/index/'</script>")
        else:
            return HttpResponse(
                "<script>alert('Your email id already  registered.....');location.href='/user/signup/'</script>")
    return render(request, 'user/signup.html', {"cart": ct})


# THIS IS PROFILE PAGE REALTED VIEW

def myprofile(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    user = request.session.get('userid')
    x = ""
    if user:
        if request.method == "POST":
            a = request.POST.get('name')
            b = request.POST.get('phone')
            d = request.POST.get('password')
            e = request.FILES.get('file')
            f = request.POST.get('msg')
            register(email=user, name=a, mobile=b, ppic=e, passwd=d, address=f).save()
            return HttpResponse(
                "<script>alert('Your Profile updated successfully...');location.href='/user/profile/' </script>")
        x = register.objects.all().filter(email=user)
    d = {"mdata": x, "cart": ct}
    return render(request, 'user/myprofile.html', d)

# THIS IS LOGIN PAGE VIEW

def signin(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    if request.method == "POST":
        Email = request.POST.get('email')
        Passwd = request.POST.get('passwd')
        x = register.objects.all().filter(email=Email, passwd=Passwd).count()
        y = register.objects.all().filter(email=Email, passwd=Passwd)
        if x == 1:
            request.session['userid'] = Email
            request.session['userpic'] = str(y[0].ppic)
            return HttpResponse("<script>alert('You are Login.....');location.href='/user/index/'</script>")
        else:
            return HttpResponse(
                "<script>alert('Your userid or password  is incorrect.....');location.href='/user/signin/'</script>")
    return render(request, 'user/signin.html', {"cart": ct})






# THIS IS PRODUCTS CATEGORY VIEW (MEDICINES)


def medicines(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    cid = request.GET.get('msg')
    cat = category.objects.all().filter(MainCategoryName='Medicines')
    d = myproduct.objects.all().filter(mcategory=8)
    if cid is not None:
        d = myproduct.objects.all().filter(mcategory=8, pcategory=cid)
    mydict = {"cats": cat, "data": d, "a": cid, "cart": ct}
    return render(request, 'user/medicines.html', mydict)

# THIS IS PRODUCTS CATEGORY VIEW (SYRUPS)

def syrups(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    cid = request.GET.get('msg')
    cat = category.objects.all().filter(MainCategoryName='Syrups')
    d = myproduct.objects.all().filter(mcategory=10)
    if cid is not None:
        d = myproduct.objects.all().filter(mcategory=10, pcategory=cid)
    mydict = {"cats": cat, "data": d, "a": cid, "cart": ct}
    return render(request, 'user/syrups.html', mydict)

# THIS IS PRODUCTS CATEGORY VIEW (SKIN CARE)

def herbal_skincare(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    cid = request.GET.get('msg')
    cat = category.objects.all().filter(MainCategoryName='Herbal & Skincare')
    d = myproduct.objects.all().filter(mcategory=9)
    if cid is not None:
        d = myproduct.objects.all().filter(mcategory=9, pcategory=cid)
    mydict = {"cats": cat, "data": d, "a": cid}
    return render(request, 'user/herbal&skincare.html', mydict)

# THIS IS PRODUCTS CATEGORY VIEW (BABY CARE)

def babycare(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    cid = request.GET.get('msg')
    cat = category.objects.all().filter(MainCategoryName='BabyCare')
    d = myproduct.objects.all().filter(mcategory=11)
    if cid is not None:
        d = myproduct.objects.all().filter(mcategory=11, pcategory=cid)
    mydict = {"cats": cat, "data": d, "a": cid, "cart": ct}
    return render(request,"user/BabyCare.html",mydict)

# THIS IS PRODUCTS CATEGORY VIEW (HEALTH NUTRITION)

def health_nutrition(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    cid = request.GET.get('msg')
    cat = category.objects.all().filter(MainCategoryName='Health & Nutrition')
    d = myproduct.objects.all().filter(mcategory=12)
    if cid is not None:
        d = myproduct.objects.all().filter(mcategory=12, pcategory=cid)
    mydict = {"cats": cat, "data": d, "a": cid, "cart": ct}
    return render(request,"user/Health&Nutrition.html",mydict)

# THIS IS PRODUCTS CATEGORY VIEW (WOMEN CARE)

def womencare(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    cid = request.GET.get('msg')
    cat = category.objects.all().filter(MainCategoryName='womencare')
    d = myproduct.objects.all().filter(mcategory=16)
    if cid is not None:
        d = myproduct.objects.all().filter(mcategory=16, pcategory=cid)
    mydict = {"cats": cat, "data": d, "a": cid, "cart": ct}
    return render(request,"user/WomenCare.html",mydict)

# THIS IS PRODUCTS CATEGORY VIEW (PERSONAL CARE)

def personalcare(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    cid = request.GET.get('msg')
    cat = category.objects.all().filter(MainCategoryName='PersonalCare')
    d = myproduct.objects.all().filter(mcategory=13)
    if cid is not None:
        d = myproduct.objects.all().filter(mcategory=13, pcategory=cid)
    mydict = {"cats": cat, "data": d, "a": cid, "cart": ct}
    return render(request,"user/PersonalCare.html",mydict)

# THIS IS PRODUCTS CATEGORY VIEW (AYURVEDA)

def ayurveda(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    cid = request.GET.get('msg')
    cat = category.objects.all().filter(MainCategoryName='Ayurveda')
    d = myproduct.objects.all().filter(mcategory=14)
    if cid is not None:
        d = myproduct.objects.all().filter(mcategory=14, pcategory=cid)
    mydict = {"cats": cat, "data": d, "a": cid, "cart": ct}
    return render(request,"user/Ayurveda.html",mydict)


# THIS IS PRODUCTS CATEGORY VIEW(HEALTH DEVICES)

def healthdevices(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    cid = request.GET.get('msg')
    cat = category.objects.all().filter(MainCategoryName='HealthDevices')
    d = myproduct.objects.all().filter(mcategory=15,)
    if cid is not None:
        d = myproduct.objects.all().filter(mcategory=15, pcategory=cid)
    mydict = {"cats": cat, "data": d, "a": cid, "cart": ct}
    return render(request,"user/HealthDevices.html",mydict)


# HEALTH TOPICS FOR READ

def healthnotes(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    hd = healthNote.objects.all().filter()
    return render(request,"user/HealthNotes.html",{"notes":hd})


# THIS IS PRODUCTS CATEGORY VIEW (OFF PRODUCTS)

def PriceLessProduct(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    cid = request.GET.get('msg')
    cat = category.objects.all().filter(MainCategoryName='Less_MRP_Product')
    d = myproduct.objects.all().filter(mcategory=17)
    if cid is not None:
        d = myproduct.objects.all().filter(mcategory=17, pcategory=cid)
    mydict = {"cats": cat, "data": d, "a": cid, "cart": ct}
    return render(request,"user/15_and_10_and_50_%_OFF.html",mydict)




# THIS IS A VIEW PAGE FOR PRODUCT

def viewproduct(request):
    a = request.GET.get('msg')
    x = myproduct.objects.all().filter(id=a)
    return render(request, 'user/viewproduct.html', {"pdata": x, })


# THIS IS LOGOUT RELATED VIEW

def signout(request):
    if request.session.get('userid'):
        del request.session['userid']
    return HttpResponse("<script>alert('You are signed out....');location.href='/user/index/'</script>")


# THIS VIEW IS USED TO ENTER IN MYORDER

def myordr(request):
    user = request.session.get('userid')
    pid = request.GET.get('msg')
    if user:

        if pid is not None:
            morder(userid=user, pid=pid, remarks="Pending", odate=datetime.now().date(), status=True).save()
            return HttpResponse("<script>alert('Your order confirmed....');location.href='/user/index/'</script>")

    else:
        return HttpResponse("<script>alert('You have to sign in first..');location.href='/user/signin/'</script>")
    return render(request, 'user/myordr.html')

# THIS VIEW IS USED TO ENTER IN CART

def mycart(request):
    p = request.GET.get('pid')
    user = request.session.get('userid')
    if user:
        if p is not None:
            mcart(userid=user, pid=p, cdate=datetime.now().date(), status=True).save()
            return HttpResponse("<script>alert('Your item is added cart..');location.href='/user/index/'</script>")
    else:
        return HttpResponse("<script>alert('You have signed in first...');location.href='/user/signin/'</script>")

    return render(request, 'user/mcart.html')


# THIS VIEW IS RELATED TO CART AND FOR SHOW

def showcart(request):
    user = request.session.get('userid')
    ct = ""
    if user:
        ct = mcart.objects.all().filter(userid=user).count()
    user = request.session.get('userid')
    md = {}
    a = request.GET.get('msg')
    cid = request.GET.get('cid')
    pid = request.GET.get('pid')
    if user:
        if a is not None:
            mcart.objects.all().filter(id=a).delete()
            return HttpResponse(
                "<script>alert(' your item are deleted from cart...');location.href='/user/showcart/'</script>")
        elif pid is not None:
            mcart.objects.all().filter(id=cid).delete()
            morder(userid=user, pid=pid, remarks="pending", status=True, odate=datetime.now().date())
            return HttpResponse(
                "<script>alert('Your order has been placed successfully.. ');location.href='/user/showcart/'</script>")
        cursor = connection.cursor()
        cursor.execute(
            "select p.*,c.* from user_myproduct p,user_mcart c where p.id = c.pid and c.userid='" + str(user) + "'")
        cdata = cursor.fetchall()
        md = {"cdata": cdata, "cart": ct}
    return render(request, 'user/showcart.html', md)

# THIS IS A SIMILER PRODUCT RELATED PAGE

def cpdetail(request):
    c = request.GET.get('cid')
    p = myproduct.objects.all().filter(pcategory=c)
    return render(request, 'user/cpdetail.html', {"pdata": p})

# THIS IS SEARCH BOX RELATED VIEW

def search(request):
    query=request.GET['qry']
    if len(query)>100 :
        allmyproduct=[]
    elif  len(query) == 0 :
        allmyproduct = []
    else:
        allmyproduct=myproduct.objects.filter(name__icontains=query)

    para={"alldata":allmyproduct,"q":query}
    return  render(request,'user/search.html',para)


def payment(request):
    return render(request,'user/Payment_and_Details.html')
