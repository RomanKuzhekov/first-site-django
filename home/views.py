from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *
from .forms import *
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import *
from django.conf import settings
from django.core.mail import send_mail


def index(request):
    posts = Post.objects.filter(url='index')
    slider_up = Photos.objects.filter(Slider_Up=True).order_by('created_date')
    slider_down = Photos.objects.filter(Slider_Down=True).order_by('created_date')
    errors = []
    form = {}
    if request.POST:
        form['author'] = request.POST.get('author')
        form['phone'] = request.POST.get('phone')

        if not form['author']:
            errors.append('Заполните имя')
        if not form['phone']:
            errors.append('Заполните телефон')

        if not errors:
            form_orders = OrdersForm(request.POST)
            if form_orders.is_valid():
                comment = form_orders.save(commit=False)
                comment.save()
            message ='Имя: ' + form['author'] + '\nТелефон: '+ form['phone']
            send_mail('Новый заказ с сайта - Строительство домов в Волгограде', message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
            return redirect('thanks')
    return render(request, 'home/index.html', {'posts':posts, 'slider_up': slider_up, 'slider_down': slider_down, 'errors': errors, 'form': form})

def company(request):
    posts = Post.objects.filter(url=request.path)
    return render(request, 'home/support.html', {'posts':posts})

def articles_list(request):
    articles = Articles.objects.filter(approwed_article=True).order_by('created_date')
    return render(request, 'home/articles_list.html', {'articles':articles})

def articles_detail(request, pk):
    article = get_object_or_404(Articles, pk=pk)
    articles = Articles.objects.order_by('-created_date')[:5]
    return render(request, 'home/articles_detail.html', {'article': article, 'articles':articles})

def guestbook(request):
    comments = Comment.objects.filter(approwed_comment=True).order_by('created_date')
    errors = []
    form = {}
    if request.POST:
        form['text'] = request.POST.get('text')
        form['author'] = request.POST.get('author')

        if not form['text']:
            errors.append('Заполните текст')
        if not form['author']:
            errors.append('Заполните имя')

        if not errors:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.save()
            return redirect('guestbook_thanks')
    return render(request, 'home/guestbook.html', {'comments':comments, 'errors': errors, 'form': form})

def guestbook_thanks(request):
    return render(request, 'home/guestbook_thanks.html')

def thanks(request):
    return render(request, 'home/thanks.html')

def photos(request):
    photos = Photos.objects.filter(Photo=True).order_by('created_date')
    return render(request, 'home/photos.html', {'photos':photos})
