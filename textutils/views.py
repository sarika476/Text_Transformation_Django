# created by --Vikrant
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'Vikrant', 'age': '20'}
    return render(request, 'index.html', params)


def analyze(request):
    djtext = request.POST.get('text', 'default')

    removepunc = request.POST.get('removepunc', 'off')
    fullcase = request.POST.get('fullcase', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcounter = request.POST.get('charcounter', 'off')

    if removepunc == 'on':

        #analyzed = djtext
        punctuatonlist = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuatonlist:
                analyzed = analyzed + char
        print(analyzed)
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if fullcase == 'on':
        analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.upper()

        params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if newlineremover =='on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.rstrip("\n\r")
        params = {'purpose': 'New Line Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if spaceremover =='on':
        analyzed = ""
        for char in djtext:
            if not char == " ":
                analyzed = analyzed + char
        params = {'purpose': 'Space Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    if charcounter == 'on':
        analyzed = 0
        for char in djtext:
            if not char == ' ':
                analyzed = analyzed + int(len(char))
        params = {'purpose': 'Char Counter', 'analyzed_text': 'TEXT =  ' + djtext + '\nChar Counts = ' + str(analyzed)}
        djtext = analyzed
        #return render(request, 'analyze.html', params)
    #else:
    #    return HttpResponse("Error.........!")

    return render(request, 'analyze.html', params)
    # HttpResponse('<h1>Analyze</h1> <a href="/">Back</a></br>')


