import simplejson
import django.core.exceptions
from django.http import HttpRequest, HttpResponse, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from .models import User
from django.db.models import Q
import bcrypt
import jwt
import datetime
from django.conf import settings

AUTH = 60 * 60 * 8


def gen_token(user_id):
    ret = jwt.encode({'user_id': user_id, 'exp': int(datetime.datetime.now().timestamp()) + AUTH},
                     settings.SECRET_KEY, 'HS256').decode('utf-8')
    return ret


def validate(func):
    def wrapper(request: HttpRequest):
        try:
            token = request.META.get("HTTP_1");
            if not token:
                return HttpResponse("not login");
            payload = jwt.decode(token, settings.SECRET_KEY,'HS256');
            user_id = payload['user_id'];
            user = User.objects.filter(pk__exact=user_id);
            request.user = user[0];
            return func(request);
        except Exception as e:
            print(e)
            return HttpResponse(status=401);

    return wrapper


# Create your views here.
def reg(request: HttpRequest):
    try:
        payload = simplejson.loads(request.body);
        email = payload['email'];
        name = payload['name'];
        password = payload['password'];

        qs = User.objects.filter(email=email);
        if qs:
            return HttpResponseBadRequest("user exists");

        user = User();
        user.email = email;
        user.name = name;
        user.password = (bcrypt.hashpw(password.encode(), bcrypt.gensalt())).decode();
        print("~~~~~~~~~~~~~~~~")
        try:
            user.save()
            ret = JsonResponse({
                'token': gen_token(user.id)
            });
            return ret
        except Exception as e:
            print(e)
            return HttpResponseBadRequest();
    except Exception as e:
        print(e)
        return HttpResponseBadRequest();


def login(request):
    try:
        payload = simplejson.loads(request.body);
        email = payload['email'];
        user = User.objects.get(email=email);
        password = payload['password'];
        print(bcrypt.checkpw(password.encode("UTF-8"), user.password.encode("UTF-8")))


        if not user:
            return HttpResponse("not exists");
        if not bcrypt.checkpw(password.encode("UTF-8"), user.password.encode("UTF-8")):
            return HttpResponse("password is wrong");

        return JsonResponse({
            "user_id": user.id,
            "user_name": user.name,
            "user_email": user.email,
            "token": gen_token(user.id)
        })
    except django.core.exceptions.ObjectDoesNotExist as e:
        return HttpResponse("user does not exist");

    except Exception as e:
        print(e)
        return HttpResponseBadRequest("system error");
