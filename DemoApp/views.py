from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from django.contrib import messages
from requests import session
from .models import signr,publdata,playdata1,playdata2,playdata3
from django.contrib.auth import logout
import requests

# Create your views here.
def home(request):
    return render(request,"html/index.html")

def admins(request):
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        try:
            user = signr.objects.get(email=email)
            if (user.password==password):
                request.session["emails"]=email
                return redirect("vat")
            else:
                return render(request,"html/adminlogin.html",{"error":"Invalid Password"})
                
        except:
            return render(request,"html/adminlogin.html",{"error":"Account doesnt Exist"})
    return render(request,"html/adminlogin.html")

def candidate(request):
    return render(request, 'html/candidate.html')

def vot(request):
    query = request.GET.get('search_query')
    api_key = '655ead06'  # Replace with your actual API key
    movie_results = []
    if query:
        api_url = f'http://www.omdbapi.com/?s={query}&apikey={api_key}'
        response = requests.get(api_url)
        data = response.json()
        if data.get('Response') == 'True':
            for result in data.get('Search', []):
                imdb_id = result.get('imdbID')
                movie_info_url = f'http://www.omdbapi.com/?i={imdb_id}&apikey={api_key}'
                movie_response = requests.get(movie_info_url)
                movie_data = movie_response.json()
                movie_results.append({
                    'Title': movie_data.get('Title', ''),
                    'Year': movie_data.get('Year', ''),
                    'Type': movie_data.get('Type', ''),
                    'Poster': movie_data.get('Poster', ''),
                    'Actors': movie_data.get('Actors', ''),
                    'Plot': movie_data.get('Plot', '')
                })
    if request.method == 'POST':
        title = request.POST.get('title')
        year = request.POST.get('year')
        movie_type = request.POST.get('movie_type')
        actors = request.POST.get('actors')
        plot = request.POST.get('plot')
        poster_url = request.POST.get('poster_url')
        request.session["title"]=title
        request.session["year"]=year
        request.session["movies"]=movie_type
        request.session["actors"]=actors
        request.session["plot"]=plot
        request.session["poster"]=poster_url
        return redirect("bap")
    return render(request, 'html/fetch.html', {'movies': movie_results})

def bap(request):
    if request.method == 'POST':
        title=request.session.get("title")
        year=request.session.get("year")
        movies=request.session.get("movies")
        actors=request.session.get("actors")
        plot=request.session.get("plot")
        poster=request.session.get("poster")
        email=request.session.get("emails")
        database_choice = request.POST.get('database_choice')
        
        if database_choice == '1':
            n=publdata.objects.create(title=title,year=year,movie_type=movies,actors=actors,plot=plot,poster=poster)
        elif database_choice == '2':
            n=playdata1.objects.create(title=title,year=year,movie_type=movies,actors=actors,plot=plot,poster=poster,email=email)
        elif database_choice == '3':
            n=playdata2.objects.create(title=title,year=year,movie_type=movies,actors=actors,plot=plot,poster=poster,email=email)
        elif database_choice == '4':
            n=playdata3.objects.create(title=title,year=year,movie_type=movies,actors=actors,plot=plot,poster=poster,email=email)
        return redirect("vat")
    return render(request,"html/noreg.html")


def delse(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        country = request.POST.get('country')
        gender = request.POST.get('gender')
        languages = request.POST.get('languages')
        n=signr.objects.create(name=name,email=email,gender=gender,country=country,language=languages,password=password)
        return redirect('hm')
    else:
        return render(request,"html/candidate.html")
    
def vote(request):
    if request.method == 'POST':
        search_query = request.POST.get('search_query')
        if search_query:
            return redirect("/fetchmovie/?search_query={}".format(search_query))
        else:
            pass
    else:
        return render(request,"html/input.html")

def pap(request):
    movies_a = publdata.objects.all()
    context = {
        'movies_a': movies_a
    }
    return render(request, 'html/nsuc.html', context)

def paps(request):
    email=request.session.get("emails")
    movies_a = playdata1.objects.filter(email=email)
    context = {
        'movies_a': movies_a
    }
    return render(request, 'html/nsucv.html', context)

def papt(request):
    email=request.session.get("emails")
    movies_a = playdata3.objects.filter(email=email)
    context = {
        'movies_a': movies_a
    }
    return render(request, 'html/pollc.html', context)

def cts(request):
    email=request.session.get("emails")
    movies_a = playdata2.objects.filter(email=email)
    context = {
        'movies_a': movies_a
    }
    return render(request, 'html/pollb.html', context)

def logt(request):
    if request.method == 'POST':
        logout(request)
        return redirect("hm")
    return render(request,"html/res.html")

def prof(request):
    email=request.session.get("emails")
    profile = signr.objects.get(email=email)
    return render(request, 'html/rest.html', {"profile":profile})

