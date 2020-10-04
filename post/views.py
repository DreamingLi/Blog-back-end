import math

import simplejson
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

from post.models import Post, Content
from user.views import validate


def fillter(d, name, conv_func, default, val_func):
    try:
        ret = conv_func(d.get(name))

        return val_func(ret, default)
    except:
        return default


# Create your views here.
@validate
def pub(request):
    try:
        payload = simplejson.loads(request.body)

        post = Post()
        content = Content()
        content.content = payload['content']
        post.title = payload['title']
        post.author = request.user
        post.content = content

        try:
            content.save()
            post.save()


        except Exception as e:
            print(e)
            return HttpResponse("pub content save error")

        try:
            post.save()
            return JsonResponse({
                'post_id': post.id,
                'title': post.title,
                'author': post.author.name,
                'content': post.content.content
            })
        except Exception as e:
            print(e)
            return HttpResponse("pub content save error")
    except Exception as e:
        print(e)
        return HttpResponse("pub content save error")


def get(request, id):
    post = Post.objects.get(pk__exact=int(id))
    print(post)
    return JsonResponse({
        "post_id": post.id,
        "title": post.title,
        "pubdate": post.pubdate,
        "author": post.author.name,
        "author_id": post.author_id,
        "content": post.content.content
    })


def getall(request):

    page = fillter(request.GET, 'page', int, 1, lambda x, y: x if x > 0 else y)
    size = fillter(request.GET, 'size', int, 10, lambda x, y: x if x > 0 else y)
    start = (page - 1) * size
    posts = Post.objects.all()
    count = posts.count()
    posts = posts.order_by('-id')[start:start + size]

    return JsonResponse({
        'posts': [{'post_id': post.id, 'title': post.title} for post in posts],
        'pagination': {
            'page': page,
            'size': size,
            'count': count,
            'pages': math.ceil(count / size),
        }
    })
