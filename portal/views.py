from django.shortcuts import render
from django.core.mail import send_mail, EmailMultiAlternatives
from .models import posibleClient
from django.template.loader import get_template
from django.conf import settings
from django.template.loader import render_to_string


# Create your views here.
def index(request):
    # send_mail('Hello from mi casa', 'Hello this is an automatic message', 'olml12354@gmail.com', ['lopez.pablo2305@gmail.com'], fail_silently=False)

    if request.method == "POST":

        if request.POST.get('copia', False) == False:
            sendCopy = False
        else:
            sendCopy = True
        correo = posibleCliente.objects.create(nombre=request.POST['nombre'],
                                                telefono = request.POST['fono'],
                                                email = request.POST['mail'],
                                                mensaje=request.POST['mensaje'],
                                                copiaMensaje=sendCopy)
        
        context = {
            'user' : correo.nombre,
            'email' : correo.email, 
            'message' : correo.mensaje,
            'phone' : correo.telefono   
        }
        # contact_message = get_template('portal/contact_message.txt').render(context)
        subject = "El usuario {0} quiere contactarse contigo.".format(correo.nombre)
        to_email = ['palito2305@gmail.com']

        text_content = render_to_string('portal/contact_message.txt', context, request=request)
        html_content = render_to_string('portal/plantillamensaje.html', context, request=request)

        
        if correo.copiaMensaje == False:
            emailMessage = EmailMultiAlternatives(subject=subject, body=text_content, from_email=settings.EMAIL_HOST_USER, to=[to_email])
            emailMessage.attach_alternative(html_content, "text/html")
            emailMessage.send(fail_silently=True)
        else:
            emailMessage = EmailMultiAlternatives(subject=subject, body=text_content, from_email=settings.EMAIL_HOST_USER, cc=[correo.email], to=[to_email])
            emailMessage.attach_alternative(html_content, "text/html")
            emailMessage.send(fail_silently=True)
            
        
        
        # from_email = settings.EMAIL_HOST_USER
        
        # send_mail(subject, contact_message, from_email, to_email, fail_silently=True )
        return render(request, "portal/index.html", {})
    else:
        print('ADIOS mundo')
        return render(request, "portal/index.html", {}) 
    return render(request, "portal/index.html", {})