from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.mail import send_mail
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from .models import Center
from .models import Ranks,Aptitude,CCAT_Question
from .models import Send,question,SendEmail
from django.contrib import messages, auth
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator

def index(request):
  
    return render(request,'pages/index.html')

def about(request):
    return render(request,'pages/about.html')


def ccat(request):
   # emails = ['abhijeets7661@gmail.com','abhijeets762@hmail.com']
    #context = {
    #   'news': 'We have good news!'
    #}
    #send_html_email(emails, 'Good news', 'email.html', context)  
    return render(request,'pages/ccat.html')

def cdac(request):
    return render(request,'pages/cdac.html')

def ads(request):
    return HttpResponse("google.com, pub-9052038674902514, DIRECT, f08c47fec0942fa0")
def ccee(request):
    return render(request,'pages/ccee.html')

def test(request):
    return render(request,'pages/test.html')
def interview(request):
    return render(request,'pages/interview.html')

def questions(request):
    queryset_list =  question.objects.order_by('-qno')[:1]
    apti_question = Aptitude.objects.order_by('-qno')[:1]
    context = {
       
       'question':queryset_list,
       'apti':apti_question
       
  }
    return render(request,'pages/questions.html',context)

def ccat_questions(request):
    queryset_list =  Aptitude.objects.order_by('-qno')
    #queryset_list =  CCAT_Question.objects.filter(display__contains='Yes');
    paginator = Paginator(queryset_list,4)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
 #   apti_question = Aptitude.objects.order_by('-qno')


    context = {
       
        'listings':paged_listings,
       
       
    }
  
    return render(request,'pages/ccat_questions.html',context)
def crashcourse(request):
    return render(request,'pages/ccat-course.html')

def notify(request):
    if request.method == 'POST':
      
        email = request.POST.get('email', '')
        try:

            n = Send(email=email)
            n.save()
            messages.success(request, 'You are now registered For Daily Updates ')
        except:
             messages.success(request,"This Email Already Exist If you didnt get email Contact Us .")


    return redirect('questions')

def ccat_notify(request):
    if request.method == 'POST':
      
        email = request.POST.get('email', '')
        send = [email]
        try:
            n = SendEmail(email=email)
            n.save()
            context = {
                'news': 'We have good news!'
                
                }
            #send_html_email(send, 'Welcome To ccatcracker ', 'ccat_mail.html', context)

            messages.success(request, 'You are now registered For Daily Updates ')

        except:
          
         

            messages.success(request,"Thank you you are now subscribed for ccatcracker  .")
       

    return  render(request,'pages/course.html')

def search(request):
    
    queryset_list =  Center.objects.all();

   
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact = city)
    
    #lte is less than eqyual to
    
    if 'course' in request.GET:
        course = request.GET['course']
        if course:
            queryset_list = queryset_list.filter(course__iexact = course)

    context = {
       
        'courses':queryset_list,
        'values' : request.GET
    }
    
    return render(request,'pages/search.html',context)


def rank(request):
    queryset_list =  Ranks.objects.all();

   
    if 'rank' in request.GET:
        rank = request.GET['rank']
        if rank:
            queryset_list = queryset_list.filter(rank__gte = rank)
    
    #lte is less than eqyual to
    
    if 'course' in request.GET:
        course = request.GET['course']
        if course:
            queryset_list = queryset_list.filter(course__iexact = course)

    context = {
       
        'courses':queryset_list,
        'values' : request.GET
    }
    
    return render(request,'pages/get_college.html',context)
def dac_interview(request):
    return render(request,'pages/dac.html')


def bd_interview(request):
    return render(request,'pages/bd.html')


def prev_questions(request):
    queryset_list =  question.objects.order_by('-qno');
    paginator = Paginator(queryset_list,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    apti_question = Aptitude.objects.order_by('-qno')
    context = {

        'listings':paged_listings,
        'apti':apti_question

    }


    return render(request,'pages/previous_questions.html',context)

def eng(request):
    return render(request,'pages/english.html')

def apti(request):
    return render(request,'pages/apti.html')


def send_html_email(to_list, subject, template_name, context, sender='help@ccatcracker.in'):

    msg_html = render_to_string(template_name, context)
    msg = EmailMessage(subject=subject, body=msg_html, from_email=sender, bcc=to_list)
    msg.content_subtype = "html"  # Main content is now text/html

    try:

        msg.send()
    except:
        return 1
    
