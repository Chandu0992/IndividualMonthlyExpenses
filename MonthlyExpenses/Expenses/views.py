from django.shortcuts import render
from .models import Register,Expenses
import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect,HttpResponse

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
#from django import db

# Create your views here.
def index(request):
    return render(request,"index.html")

def signup(request):
    return render(request,'register.html')

def user_logout(request):
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    mob_email = request.POST.get('log_mob')
    pwd = request.POST.get('log_pwd')
    if len(mob_email) == 10 and ('@' not in list(mob_email)):
        log_res = Register.objects.filter(mobile = int(mob_email)).all()
        if len(log_res) == 0:
            return render(request,"index.html",{'msg':'Account Not Exist Please Signup'})
    else:
        log_res = Register.objects.filter(email = mob_email).all()
        if len(log_res) == 0:
            return render(request,"index.html",{'msg':'Account Not Exist Please Signup'})

    res = list(log_res)[0]
    if pwd == res.password:
        show_per = Register.objects.all()
        per_lst = list(show_per)
        return render(request,"home.html",{'res':res,'per_lst':per_lst})
    else:
        return render(request,"index.html",{'msg':'Login Credientials Wrong !'})

def myExpenses(request):
    lst_per = request.POST.getlist('per_lst')
    my_mob = request.POST.get('mymob')
    amt = int(request.POST.get('uamt'))
    #print(amt,type(amt))
    dt = request.POST.get('udate')
    type_exp = request.POST.get('expense_type')
    desc = request.POST.get('udesc')
    if len(lst_per) == 0:
        lst_per.append(my_mob)
        amount = amt/1
    else:
        amount = amt/len(lst_per)
    log_res = Register.objects.filter(mobile = int(my_mob)).all()
    res = list(log_res)[0]
    show_per = Register.objects.all()
    per_lst = list(show_per)
    number = res.mobile
    for x in lst_per:
        res_exp = Expenses(mobile=x,dt=dt,type_exp=type_exp,desc=desc,amount=amount)
        res_exp.save()
    return render(request,"home.html",{'res':res,'per_lst':per_lst,'msg':'Saved Data Sucessfully !','number':number})


def registerNew(request):
    uname = request.POST.get('uname')
    umob = request.POST.get('umobile')
    umail = request.POST.get('uemail')
    ugen = request.POST.get('ugen')
    upwd = request.POST.get('upassword')
    mob_check = Register.objects.filter(mobile = umob).all()
    email_check = log_res = Register.objects.filter(email = umail).all()
    if len(mob_check) == 1 or len(email_check) == 1:
        return render(request,"register.html",{'msg':'Mobile or Email already Exist !'})
    else:
        res = Register(name=uname,mobile=umob,email=umail,gen=ugen,password=upwd)
        res.save()
        return render(request,"register.html",{'msg':'Signup Sucessfully !'})

def showDetails(request):
    exp = request.POST.get('expenses')
    mob = request.POST.get('myMobile')
    sdt = request.POST.get('sdt')
    edt = request.POST.get('edt')
    format_str = '%Y-%m-%d'
    sdate_obj = datetime.datetime.strptime(sdt,format_str).date()
    edate_obj = datetime.datetime.strptime(edt,format_str).date()
    if exp == 'all':
        res_details = Expenses.objects.filter(mobile=mob).all()
    else:
        res_details = Expenses.objects.filter(mobile=mob,type_exp=exp).all()
    res = list(res_details)
    res_lmt = []
    sum = 0
    for x in res:
        #print(x.dt)
        if x.dt>=sdate_obj and x.dt<=edate_obj:
            sum += x.amount
            res_lmt.append(x)
    return render(request,"details.html",{'mobile':mob,'res_details':res_lmt,'sum':sum})
    #return render(request,"details.html")
