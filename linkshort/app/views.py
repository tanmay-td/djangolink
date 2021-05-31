from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import shorturl
from  .forms import CreateNew
from  datetime import datetime
import random,string
# Create your views here.
def home(request):
    return render(request,'home.html')
def redirect(request,url):
    current_obj = shorturl.objects.filter(short =url)
    if len(current_obj) == 0:
        return render(request,'pagenotfound.html')
    else:
        context ={'obj':current_obj[0]}
        obj = current_obj[0].orignal_url
        return HttpResponseRedirect(obj)
        # return render(request,'redirect.html',context)


def create(request):
    if request.method == 'POST':
        form = CreateNew(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['orignal_url']
            random_char = list(string.ascii_letters)
            rand_char = ''
            for i in range(6):
                rand_char = rand_char + random.choice(random_char)
            while len(shorturl.objects.filter(short =rand_char)) != 0:
                for i in  range(6):
                    rand_char = rand_char + random.choice(random_char)
            d = datetime.now()
            s = shorturl(orignal_url = original_website,short =rand_char,time_date=d)
            s.save()
            return render(request,'urlcreated.html',{'chars':rand_char})
    else:
        form =CreateNew()
        context ={'form':form}
        return render(request,'create.html',context)