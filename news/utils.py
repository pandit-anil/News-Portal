from newsapi import NewsApiClient
from account.models import User
from  . models import News,Category


API_KEY = 'dcef03d78e164544a02719a7ed42d37b'

def fetch(date_from):

    newsapi = NewsApiClient(api_key=API_KEY)
    for category in Category.objects.all():
        response = newsapi.get_everything(q=category.name, language='en', from_param=date_from)
        articles = response.get('articles',[])

        if len(articles) == 0:
            print(f"No Articles found for Category {category.name}")
        
        for article in articles:
            db_news = News(
                title = article.get('title'),
                content = article.get('content'),
                image_url = article.get('urlToImage'),
                category = category,
                pub_date = article.get('published_at'),
                created_at = article.get('published_at'),
                created_by =User.objects.get(pk=1)

            )
            db_news.save()
            print('data saved')

