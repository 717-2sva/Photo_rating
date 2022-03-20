from django.contrib import auth
from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.models import User

def news_home (request):
    news = Articles.objects.order_by('-data')
    return render(request, 'news/news_home.html', {'news': news, 'user':auth.get_user(request)})

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm

def create (request):
    user_name = auth.get_user(request).username
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST, request.FILES)
        if form.is_valid():

            post = form.save(commit=False)
            post.author = User.objects.get(username = user_name)
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма не корретна'
    form = ArticlesForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)
