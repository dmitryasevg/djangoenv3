from django.shortcuts import render
from django.http.response import HttpResponse, Http404
#from django.core.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from django.core.exceptions import ObjectDoesNotExist
from models import Article, Comments
from django.shortcuts import render_to_response, redirect

# Create your views here.

def basic_one(request):
    view = "basic_one"
    html = "<html><body>This is %s view</body></html>" % view
    return HttpResponse(html)


def template_two(request):
    view = "template_two"
    t = get_template('myview.html')
    html = t.render(Context({'name':view}))
    return HttpResponse(html)

def template_three_simple(request):
    view = "template_three_simple"
    return render_to_response('myview.html',{'name':view})

def articles(request):
    return render_to_response('articles.html',{'articles':Article.objects.all()})

def article(request,article_id = 1):
    return render_to_response('article.html',{'article':Article.objects.get(id = article_id),'comments':Comments.objects.filter(comments_article_id = article_id)})

def addlike(request,article_id):
    try:
        article = Article.objects.get(id = article_id)
        article.article_likes +=1
        article.save()
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/')


    