from django.db import models
from account.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering =['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    image = models.ImageField(upload_to="news/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    image_url = models.URLField(null=True,blank=True)

    class Meta:
        ordering =['title']
        verbose_name = 'News'
        verbose_name_plural = 'News'
