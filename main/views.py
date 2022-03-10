from django.shortcuts import render, redirect
from main.models import Movie, Category
from main.forms import MovieCreateForm


# Create your views here.

def index(request):
    movie = Movie.objects.all()
    data = {
        'movie_list': movie
    }
    return render(request, 'index.html', context=data)


def test(request):
    data = {
        "title": 'Matrix 4',
    }
    return render(request, 'test.html', context=data)


def detail(request, id):
    movie = Movie.objects.get(id=id)
    data = {
        'movie': movie
    }
    return render(request, 'detail.html', context=data)


def search(request):
    word = request.GET.get('search', '')
    if request.GET.get('from_price', '') == '':
        from_price = 0
    else:
        from_price = int(request.GET.get('from_price'))
    if request.GET.get('to_price', '') == '':
        to_price = 1000000000
    else:
        to_price = int(request.GET.get('to_price'))
    category_id = None
    try:
        category_id = int(request.GET.get('category_id'))
    except:
        pass
    movie = Movie.objects.filter(title__contains=word,
                                 price__gte=from_price,
                                 price__lte=to_price)
    if category_id:
        movie = movie.filter(category_id=category_id)
    data = {
        'movie_list': movie,
        'categories': Category.objects.all()
    }
    return render(request, 'search.html', context=data)


def create_movie(request):
    if request.method == 'POST':
        form = MovieCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'create.html', context={'form': form})
    context = {
        'form': MovieCreateForm
    }
    return render(request, 'create.html', context=context)
