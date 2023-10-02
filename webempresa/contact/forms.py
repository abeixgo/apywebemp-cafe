from django import forms

#creamos n nuestri formulariuo
class ContactForm(forms.Form):
    name=forms.CharField(label='Nombre', required=True,
            widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Escriba tu nombre'}))#widget sirve para extender la ocnfiguracion
    
    email=forms.EmailField(label='Email', required=True, 
            widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Escriba su email'}))#widget sirve para extender la ocnfiguracion)
    
    content=forms.CharField(label='Contenido', required=True,
            widget=forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'Escriba su mensaje', 'min_length':20, 'max_lenght':100}))#widget sirve para extender la ocnfiguracion)