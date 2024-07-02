from django.db import models
from account.models import User
from auditlog.registry import auditlog
from auditlog.models import AuditlogHistoryField



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
    image = models.ImageField(upload_to="news/" , null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    image_url = models.URLField(null=True,blank=True)
    views = models.IntegerField(default=0)
    history = AuditlogHistoryField()

    class Meta:
        ordering =['title']
        verbose_name = 'News'
        verbose_name_plural = 'News'


class Ads(models.Model):

    about =models.TextField()
    image = models.ImageField(upload_to='ads/',null=True)
    IMAGE_TYPE = [
        ('headerimg','Headerimg'),
        ('whatnewimage', 'WhatsNewImage'),
        ('mostpopularimg','MostPopularImg'),
        ('endpageimg','EndPageimg'),
        ('footerimg','FooTerimg'),
        ('detailsimg','Detailsimg')
    ]
    image_type = models.CharField(choices=IMAGE_TYPE, max_length=200, default='whatnewimage')
    

    history = AuditlogHistoryField()
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='inactive')


    def __str__(self):
        return self.about
    


class Systemsetting(models.Model):
    sys_name = models.CharField(max_length=150)
    logo = models.ImageField(upload_to='SysLogo')
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    address = models.CharField(max_length=250)
    slogan = models.TextField()
    facebooklink = models.URLField(null=True,blank=True)
    youtubelink = models.URLField(null=True,blank=True)
    history = AuditlogHistoryField()

    def __str__(self):
        return self.sys_name
    

class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    mess = models.TextField()
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    history = AuditlogHistoryField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    author = models.TextField()
    mess = models.TextField()
    email = models.EmailField(default='user@user.com')
    created_at = models.DateTimeField(auto_now_add=True)
    history = AuditlogHistoryField()
    
    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

auditlog.register(Category,serialize_data=True)
auditlog.register(News)
auditlog.register(Comment)