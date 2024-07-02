from typing import Any
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views import View
from . models import News,Category,ContactUs,Comment
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.contrib import messages

import datetime

from django.http import HttpResponse
from django.utils import timezone

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trending'] =News.objects.all().order_by('-pub_date')[:3]
        context['rightcontent'] =News.objects.all().order_by('-pub_date')[3:5]
        context['recent'] =News.objects.all().order_by('pub_date')[:3]
        context['categories'] = Category.objects.all()[:5]
        context['mostpopular'] =News.objects.all().order_by('-views')[:4]
        context['mostrecent'] =News.objects.all().order_by('pub_date')[:6]

        context['news'] = {}
        for category in context['categories']:
            context['news'][category.id] =News.objects.filter(category=category).order_by('-pub_date')[:5]
        return context
    
    
    



class CategoryPageView(TemplateView):
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()[:5]
        context['mostpopular'] =News.objects.all().order_by('-views')[:4]
        context['mostrecent'] =News.objects.all().order_by('pub_date')[:6]
       
        context['news'] = {}
        for category in context['categories']:
            context['news'][category.id] =News.objects.filter(category=category).order_by('-pub_date')[10:16]
        return context
    

class AboutUsPageView(TemplateView):
    template_name = 'about.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

# class LatestNewsPageView(DetailView):
#     template_name = 'latest_news.html'
#     model = News
#     context_object_name = 'news'

#     def get_object(self, queryset=None):
#         news = super().get_object(queryset)
#         news.views += 1
#         news.save()
#         return news

class LatestNewsPageView(DetailView):
    template_name = 'latest_news.html'
    model = News
    context_object_name = 'news'

    def get_object(self, queryset=None):
        news = super().get_object(queryset)
        news.views += 1
        news.save()
        return news

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news = self.get_object()
        context['comments'] = Comment.objects.filter(post=news).all()
        
        return context



def Comments(request,id):
    posts = get_object_or_404(News, id=id)

    if request.method == 'POST':
        data = request.POST
        author = data.get('name')
        mes = data.get('message')
        email = data.get('email')
        created_at = timezone.now()

    # if not (author and mes and email):
    #     error_message = "All fields are required."
    #     query_params = f'?error_message={error_message}&name={author}&message={mes}&email={email}'
    #     return redirect(f'details{id}{query_params}')
        
    if author and mes and email :
        comment = Comment(post = posts, author = author, mess = mes,email= email,created_at=created_at )
        comment.save()
        return redirect('details', pk = posts.id)



def Contact(request):
    if request.method == "POST":
        data = request.POST
        db = ContactUs()
        db.name = data.get('name')
        db.subject = data.get('subject')
        db.mess = data.get('message')
        db.email = data.get('email')
        if not (db.name and db.subject and db.mess and db.email):
            error_message = "All fields are required."
            return render(request, 'contact.html', {'error_message': error_message, 'data': data})

        db.save()

        subject = db.subject
        from_email = 'info.demodjango@gmail.com'
        recipient_list = ['info.demodjango@gmail.com'] 
        
        context = {
            'name': db.name,
            'email': db.email,
            'subject':db.subject,
            'message': db.mess,
        }
        text_content = f"Name: {db.name}\nEmail: {db.email}\nMessage: {db.mess}\nSubject:{db.subject}"
        html_content = render_to_string('contact_email.html', context)

        # Send email
        email = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
        email.attach_alternative(html_content, "text/html")
        email.send()

        messages.success(request, 'This data has been sent to the admin.')
       
        return redirect('contact')
    return render(request,'contact.html')


def set_cookie(
        response: HttpResponse,
        key: str,
        value: str,
        cookie_host: str,
        days_expire: int = 365,
):
    max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(days=days_expire), "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    domain = cookie_host.split(":")[0]
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires,
        domain=domain,
        secure=False,
    )