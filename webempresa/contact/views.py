from django.shortcuts import render, redirect#para recireccionar e envar mensaje que se ha enviado correctamente
from  .forms import ContactForm#importamos la clase ContactForm
from django.urls import reverse#para no poner el url en crudo
from django.core.mail import EmailMessage#crear estructura de mail

# Create your views here.
def contact(request):
   # print("Tipo de peticion: ", request.method)#tipo de peticion al formulario contact o la pagina contact 
    #Instaciamos la clase ContactForm, osea creamos un objeto damos vida a esa clase
    contact_form=ContactForm()
    #procesamos si la peticin es POST
    if request.method=='POST':
        contact_form=ContactForm(data=request.POST)#1: crear platnilla vacia, 2: si es POST rellenar los datos con requestPOST  a la plantilla vacia contactFORM
        if contact_form.is_valid():#Si todos los campos son válidos procederemos a recuperarlos
            name=request.POST.get('name', '')#asignación de variable para procesar datos enviados a través de un formulario POST en Django.
            email=request.POST.get('email', '')#asignación de variable para procesar datos enviados a través de un formulario POST en Django.
            content=request.POST.get('content', '')#asignación de variable para procesar datos enviados a través de un formulario POST en Django.

            #supongamos que toda va bien, entonces redireccionaremos
            #return redirect('/contact/?ok')#mala practoca poner ya que cunado cambia la pagina de contact se tiene que volver aqui y cambiat aqui
            #return redirect(reverse('contact'), "?ok")
        
            #enviamos el correo y redireccionamos
            email=EmailMessage(#asunto, cuerpo, eamil_origen, email:destino, reply_to
                'Abeixgo: nuevo mensaje de contacto', 
                'De {} <{}>\n\n Escribio: \n\n{}'.format(name, email, content),
                'no.constestar@inbox.mailtrap.io',
                ['abxmee@gmail.com'],
                reply_to=[email],
            )
            try:
                email.send()
                #todo a ido bieen redicciormaoa al ok
                return redirect(reverse('contact') + "?ok")
            except:
                #Alkgo no hga ido bien rediccionamos a Fail
                return redirect(reverse('contact') + "?fail")


    return render(request, 'contact/contact.html', {'contact_form1':contact_form})#enviados el objeto en dicionario de ocntexto