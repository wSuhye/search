from django.shortcuts import render,redirect
import requests
from bs4 import BeautifulSoup

# Create your views here.
def home(request):
    # return render(request, 'home.html')
    if request.method == 'POST':
        search_word = request.POST.get('search_word')
        url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='
        full_url = url + search_word
        data = requests.get(full_url).text
        soup = BeautifulSoup(data, 'html.parser')
        news_titles = soup.find_all(class_='_sp_each_title')
        title_list = []
        for title in news_titles:
            title_list.append({
            'url':title.get('href'),
            'title':title.get('title')
            })
        return render(request, 'result.html', {'title_list':title_list})
    else:
        return render(request, 'home.html')

    
        
   
def result(request):
    return render(request, 'result.html')