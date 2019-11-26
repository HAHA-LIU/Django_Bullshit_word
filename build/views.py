import os
from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import json,random

from BuildArticle import settings


def article(request):
    if request.method == 'GET':
        return render(request,'build/word.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        if not title:
            title_error = 'please give me title'
            return render(request, 'build/word.html', locals())
        print(222)
        print(settings.STATICFILES_DIRS)
        print(222)
        dir_ = settings.STATICFILES_DIRS[0]
        data1 = json.load(open(dir_+'/data.json', encoding="utf-8"))
        print(11111)
        print(data1)
        print(1111)
        body = ""
        while len(body) < 2000:
            num = random.randint(0, 100)
            if num < 10:  # 换行
                body += "\r\n"
            elif num < 20:  # 穿插名言
                body += random.choice(data1["famous"]).replace('a', random.choice(data1["before"])).replace('b',random.choice(data1['after']))
            else:
                body += random.choice(data1["bosh"])  # 加废话
            body = body.replace("x", title)
            content = body
        return render(request,'build/word.html',locals())