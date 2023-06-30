from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class CreateBlog(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    image = models.ImageField(upload_to='media')
    date_added = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.titre
    
    #pour classer les poste en fonction des date les plus recent
    class Meta:
        ordering = ['-date_added']
        
class Comment(models.Model):
    post = ForeignKey(CreateBlog,related_name='comments',on_delete=models.CASCADE)
    email = models.EmailField()
    body = models.TextField()
    name = models.CharField(max_length=100,default="inconnu") 
    date_added = models.DateTimeField(auto_now=True)
    
    #pour classer les commentaire en fonction des date les plus recent
    class Meta:
        ordering = ['-date_added']
            