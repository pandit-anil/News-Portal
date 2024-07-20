from django.contrib import admin
from . models import Category,News,Ads,Systemsetting,ContactUs,Comment


# Register your models here.
admin.site.register(Category)
admin.site.register(ContactUs)

@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    list_display = ('id','author','email')

@admin.register(Systemsetting)
class SyastemAdmin(admin.ModelAdmin):
    list_display = ('id','sys_name','email')


@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ('id','about')

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display =('title','pub_date','created_by','created_at','category','views')