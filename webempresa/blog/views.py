from django.shortcuts import render, get_object_or_404
from .models import Post#recuperamos la  entradas de blog del base de datos para inyectar en html
from .models import Category

# Create your views here.
def blog(request):
    posts=Post.objects.all()#obtener todas las entradas que ha recibido el modeloDB de Post|||| en retrun inyectamos estos datos al html
    return render(request, 'blog/blog.html', {'posts':posts})#inyectamos los datos con diciconario de contexto

#creamos una vista para ver el filtro de post por categorias
def list_category(request, category_id):
    # Obtener la categoría con el id proporcionado
    category = get_object_or_404(Category, id=category_id)

    #Filtrar los posts por la categoría seleccionada para pasar al html 
  #  posts = Post.objects.filter(categories=category)#forma rudimentaria podemos hacer con CONSULTA INVERSA
    
   # return render(request, 'blog/category.html', {'category':category,
    #                                               'posts':posts})

    return render(request, 'blog/category.html', {'category':category})


