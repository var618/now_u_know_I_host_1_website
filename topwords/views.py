from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup as BS
# Create your views here.


def index(request):
    context = {'title':'topwords'.upper(),
               'header':'lot is not ioT'.capitalize(),
               'messages': ['pig','rabbit','nose','donkey','mule']}
    return render(request=request, template_name='topwords/layout.html', context=context)


def query(url):
    if url:
        r = requests.get(url)
        r.encoding = 'utf-8'
    if r.status_code == 200:
        soup = BS(r.text, 'html5lib')
        lsa = soup.select('ol li a')
        return [x.text for x in lsa]
    return


def see(request):
    return HttpResponse('<p>'.join(query('http://weixin.sogou.com')) + '<p><a href="topwords/save/"></a>')


def save(request):
    pass


def login(request):
    pass


def logout(request):
    pass
