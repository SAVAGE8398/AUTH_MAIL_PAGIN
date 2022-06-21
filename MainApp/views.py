from django.http import HttpResponse
from django.shortcuts import redirect, render
from Crud_auth.settings import EMAIL_HOST_USER
from MainApp.models import UserModel
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
def index(request):
    params={}
    return render(request, 'index.html',params)
def register(request):
    if request.method == 'POST':
        # a=UserModel.objects.all()
        # b=UserModel.object.get(NameF=name)
        name = request.POST.get('nametxt')
        email=request.POST.get('emailtxt')
        password=request.POST.get('passwordtxt')
        document=UserModel(NameF=name, EmailF=email, PasswordF=password)
        document.save()
        sub="REGISTRATION SUCESSFULL"
        message=""
        from_mail=EMAIL_HOST_USER
        to_mail=[email]
        html_messages=render_to_string('msg.html')
        send_mail(sub, message,from_mail,to_mail,html_message=html_messages,fail_silently=True)
        return redirect(login)
    params={}
    return render(request, 'register.html', params)
def login(request):
    params={}
    if request.method=='POST':
        email = request.POST.get('emailtxt')
        password = request.POST.get('passwordtxt')
        try:
            A=UserModel.objects.get(EmailF=email, PasswordF=password)
        except UserModel.DoesNotExist:
            return redirect(register)
        else:
            request.session['lid']=A.id
            return redirect(crm)  
    return render(request, 'login.html', params)
def crm(request):
    if (request.session.get('lid')):
        A=UserModel.objects.all().order_by('id')
        params = {'data':A}
        return render(request, 'crm.html',params)
    else:
        return redirect('index')

def delete(request):
    obj=UserModel.objects.get(pk=request.GET['pk'])
    print(obj)
    obj.delete()
    return redirect('crm')
def edit(request):
    obj=UserModel.objects.get(pk=request.GET['pk'])
    print(obj)
    params = {'data':obj}
    return render(request, 'edit.html',params)
def update(request):
    id=request.POST.get('id')
    name=request.POST.get('name')
    email=request.POST.get('email')
    password=request.POST.get('password')
    A=UserModel.objects.get(pk=id)
    print(A)
    A.NameF=name
    A.EmailF=email
    A.PasswordF=password
    A.save()
    return redirect('crm')
def logout(request):
    if(request.session.get('lid')):
        try:
            del request.session['lid']
        except KeyError:
            pass 
    return HttpResponse("You're logged out.")