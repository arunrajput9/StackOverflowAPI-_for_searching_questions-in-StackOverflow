from time import sleep

from django.shortcuts import render
import requests
import datetime
count=0
time_first_search_min=datetime.datetime.today()
time_next_search=time_first_search_min+datetime.timedelta(minutes=1)

# Create your views here.

def home(request):
    global count,time_first_search_min,time_next_search
    count+=1
    time_first_search_min=datetime.datetime.today()
    time_next_search=time_first_search_min+datetime.timedelta(minutes=1)
    return render(request, 'home.html')

def search_questions(request):
    ques=request.GET['question']

    result = requests.get("https://api.stackexchange.com/2.3/search/excerpts?order=desc&sort=activity&title={}&site=stackoverflow".format(ques)).json()

    return render(request,'result.html',{'result': list(result["items"])})

def back(request):
    global count,time_first_search_min,time_next_search
    count+=1
    if time_first_search_min==0 or count>6:
        count=0
        time_first_search_min=datetime.datetime.today()
        time_next_search=time_first_search_min+datetime.timedelta(minutes=1)
    if count==6 and datetime.datetime.today()<time_next_search:
        count=0
        time_in_sec=(time_next_search-datetime.datetime.today()).seconds
        times=time_in_sec*1000
        time_first_search_min=0

        return render(request,'wait.html',{'time_in_sec': time_in_sec,'times':times})
    return render(request, 'home.html')


