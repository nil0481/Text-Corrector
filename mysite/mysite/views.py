# nilesh (now created)
from django.http import HttpResponse
from django.shortcuts import render
from django.conf.urls.static import static

def index(request):
    params={'name':'nilesh','place':'india'}
    return render(request,'index2.html',params)
    # return HttpResponse('''<a href="https://www.google.com/"><h1>google</h1> </a><br><a href="about">about</a>''')
def removepun(djtext):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    analysed=""
    for i in djtext:
        if i not in punctuations:
            analysed += i
    return analysed
def extrasp(djtext):
    analysed=''
    for i, s in enumerate(djtext):
        if djtext[i] == " " and djtext[i + 1] == " ":
            pass
        else:
            analysed += s

    return analysed

def about(request):

    djtext=request.POST.get('text', 'default')                    #getting the text entered by user
    removepunc=request.POST.get('removepunc', 'off')              #getting if checkbox removepunc is on/off
    is_upper=request.POST.get('capitaliseall', 'off')
    extraspace=request.POST.get('extraspace', 'off')
    params={}
    flag=0

    if removepunc=='on':
        analysed=removepun(djtext)
        djtext = analysed
        params = {'purpose': 'removed punctuation', 'analysed_text': djtext}
        flag=1
        # return render(request, 'analyse.html', params)
    if is_upper=='on':
        analysed=djtext.upper()
        djtext=analysed
        params = {'purpose': 'changed to uppercase', 'analysed_text': djtext}
        flag = 1
        # return render(request, 'analyse.html', params)
    if extraspace=='on':
        analysed=extrasp(djtext)
        djtext=analysed
        params = {'purpose': 'extraspace removed', 'analysed_text': djtext}
        flag = 1
    if flag==0:
        return HttpResponse("<h1>Unknown Response</h1>")
    return render(request, 'analyse.html', params)


    # return HttpResponse(file_content+'''\n\n<br><a href="goout">goout</a><br><a href="/">back</a>''')


def goout(request):
    f = open('mysite/file.txt', 'r')
    file_content = f.read()
    f.close()

    return HttpResponse(file_content+'''<br><a href="/">back</a>''')