from django.shortcuts import render,redirect
from django.views.generic import ListView # puisque on va utiliser la pagination pour les differant page
from .models import *
from .forms import BlogForm


class List(ListView):
    template_name='blog/index.html'
    queryset=CreateBlog.objects.all() # on vien de tout recuperer dans la bd et metre dans la variable queryset qui est un tablea
    paginate_by = 3
    
def DetailView(request,slug):
    post = CreateBlog.objects.get(slug=slug)
    # chaque commentaire est relier  a un article
    comments = post.comments.all() # on recupere tout les commentaire lie a un article
    if request.method == 'POST':
        form = BlogForm(request.POST) # ce que on recupere doit etre dans le formulaire
        if form.is_valid():
            form.save(commit=False) # commit=false pour sire que on ne seveugarde pas le fichier sans le champ post du moel comment
            form.instance.post=post 
            form.save()
            return redirect('detailView',slug=post.slug)
    else:
        form=BlogForm()    
 
    content={ 
        'article':post,
        'comments':comments,
        'form':form
    }
    
    return render(request,'blog/update.html',content)
    
    

    