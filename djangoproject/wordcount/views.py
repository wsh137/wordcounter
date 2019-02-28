from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html' )

def about(request):
    return render(request, 'about.html')

def result(request):
    text=request.GET['fulltext'] #입력받는 원문 전체를 뜻함, text라는 변수에 담아준다
    words = text.split()#저거 자체가 리스트 / 문자열 관련 .split 함수/ text 문자열을 공백을 기준으로 나눠서 리스트로 저장해주는 함수
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            #increase
            word_dictionary[word]+=1
        else:
            #add to dictionary
            word_dictionary[word]=1

    return render(request, 'result.html', {'full':text, 'total': len(words), 'dictionary' : word_dictionary.items() })