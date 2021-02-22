from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class Article(models.Model):
    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title=models.CharField(max_length=50,verbose_name="Başlık")
    created_date=models.DateTimeField(auto_now_add=True,verbose_name="Yayınlanma Tarihi")
    content=RichTextField(verbose_name="İçerik")
    article_image=models.FileField(blank=True,null=True,verbose_name="Fotoğraf ekle")
    def __str__(self):
        return self.title
class Comment(models.Model):
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Makale")
    