from . models import News,Ads,Systemsetting

def popular_news(request):
    popular = News.objects.all().order_by('-views')[:3]
    return {'popular': popular}

def ads(request):
    header_images = Ads.objects.filter(status = 'active')
    footer_image = Ads.objects.filter(image_type = 'footerimg')
    context = {
        'ads': header_images
    }
    return {'imgads':header_images}

def SystemSetting(request):
    sys = Systemsetting.objects.first()
    return {'sys':sys}