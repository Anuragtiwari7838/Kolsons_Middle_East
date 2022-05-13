from django.shortcuts import render
import smtplib
from .models import clientsM, certificatsM
# for certificate display
from django.http import FileResponse, Http404

from email.message import EmailMessage
from kolsons.models import Product



def enquiry(request):
    product = Product.objects.all()
    enquirytag = False
    return render(request, 'enquiry.html',{'product': product,'enquirytag':enquirytag})
def about(request):
    product = Product.objects.all()
    return render(request, 'about.html',{'product': product})
def contactus(request):
    product = Product.objects.all()
    return render(request, 'contactus.html',{'product': product})
def market(request):
    product = Product.objects.all()
    return render(request, 'market.html',{'product': product})
def processcontrol(request):
    product = Product.objects.all()
    return render(request, 'processcontrol.html',{'product': product})
def machinery(request):
    product = Product.objects.all()
    return render(request, 'machinery.html',{'product': product})
def lifting(request):
    product = Product.objects.all()
    return render(request, 'lifting.html',{'product': product})
def catalogue(request):
    product = Product.objects.all()
    return render(request, 'catalogue.html',{'product': product})

def product(request):
    product = Product.objects.all()
    return render(request, 'product.html',{'product': product})
def client(request):
    product = Product.objects.all()
    clients = clientsM.objects.all()
    return render(request, 'client.html',{'clients':clients,'product': product})



# following functions return instance of certificats on certifications page
def certifications(request):
    product = Product.objects.all()
    certificats = certificatsM.objects.all()
    return render(request, 'certifications.html',{'certificats':certificats,'product': product})
    

# following function open the requested certificate in browser
def certificateDoc(request,id):
    try:
        
        certificate = certificatsM.objects.get(id=id)
        return FileResponse(certificate.certificatePDF, content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

# enquiry form mailing function
def enquiry_form(request):
    product = Product.objects.all()
    name = request.POST['name']
    organisation = request.POST['organisation']
    address = request.POST['address']
    phone = request.POST['phone']
    email = request.POST['email']
    pii = request.POST['pii']
    quantity = request.POST['quantity']
    comments = request.POST['comments']
     
        
    
    EMAIL_ADDRESS = 'nerthinksjareen@gmail.com'
    EMAIL_PASSWORD = 'Ironman@12'

    msg = EmailMessage()
    msg['Subject'] = 'contacting from enquiry form'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] ="info@kolsons.com"
    mg = f"name:{name}\nOrganisation:{organisation}\nAdress:{address}\nPhone:{phone}\nEmail:{email}\nProduct intrested in:{pii}\nQuantity:{quantity}\nComments/Suggestions/feedback:{comments}\n"

    msg.set_content(mg)
    
   
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    enquirytag = True
   
    return render(request,'enquiry.html',{'product': product,'enquirytag': enquirytag})






def productpost(request,id):
    broduct = Product.objects.all()
    product = Product.objects.filter(part_no=id).first()
    
    flag=[]
    keyset = list(Product._meta.get_fields())
    for f in keyset:
        if getattr(product,f.name)=="" or f.name=='images' or f.name=='part_no' or f.name=='name':
            
            pass
        else:
            # flag[f.name]=True
            flag.append([f.name,getattr(product,f.name)])

    return render(request,'kolsons/productpost.html' , {'product':product,'flag':flag})
