from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.contrib import messages, auth
from paytm import checksum
from . models import Orders
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from .models import pma     

def checkout(request):
   
    return render(request,'payment/checkout.html')

def exam_checkout(request):
    return render(request,'payment/exam_checkout.html')

def payment(request):
        detail = pma.objects.all()[:1].get()
      
        MERCHANT_KEY =  detail.merchant_key
        if request.method == 'POST':
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            state = request.POST.get('state', '')
            city = request.POST.get('city', '')
            phone = request.POST.get('phone', '')
            orders = Orders(name=name, email=email,phone=phone,state=state,city=city)
            orders.save()
        
            id = orders.order_id
            param_dict = {
                'MID':detail.merchant_id,
                'ORDER_ID':str(orders.order_id), 
                'TXN_AMOUNT':'200',
                'CUST_ID':orders.email,
                'INDUSTRY_TYPE_ID':'Retail',
                'WEBSITE':'worldpressplg',
                'CHANNEL_ID':'WEB',
                'CALLBACK_URL':'http://165.22.254.36/payment/handlerequest',
            }
            param_dict['CHECKSUMHASH'] = checksum.generate_checksum(param_dict, MERCHANT_KEY)
            return render(request, 'payment/payment_form.html', {'param_dict': param_dict})
        return render(request, 'payment/checkout.html')
        

   


@csrf_exempt
def handlerequest(request):
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            checksum = form[i]
    order = Orders.objects.get(order_id=response_dict['ORDERID'])

    verify = True
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('order successful')

            order.status = "Placed"  # change field
            order.save()
            messages.success(request, 'Congrats Your Order Has Been Placed You Will Get Email Soon With Notes ...')
            # Send Mail
         
            send = [order.email]
            context = {
            'news': 'We have good news!'
            }
            send_html_email(send, 'Order Placed Successfully', 'email.html', context)
            #orders.status = "Sent" 
            #orders.save()  
        else:
            order.status = "Failed" 
            order.save() 
            print('order was not successful because' + response_dict['RESPMSG'])
    return render(request, 'payment/paymentstatus.html', {'response': response_dict})



def send_html_email(to_list, subject, template_name, context, sender='help.ccatcracker@gmail.com'):
    msg_html = render_to_string(template_name, context)
    msg = EmailMessage(subject=subject, body=msg_html, from_email=sender, bcc=to_list)
    msg.content_subtype = "html"  # Main content is now text/html

    return msg.send()


