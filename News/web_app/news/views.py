from django.shortcuts import render
from .models import News
from .forms import NewsForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = News.objects.order_by('-date')
    return render(request, 'news/home.html', {'news': news})


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/detail.html'
    context_object_name = 'detail'


class NewsUpdateView(UpdateView):
    model = News
    success_url = '/news/'
    template_name = 'news/update.html'
    form_class = NewsForm


class NewsDeleteView(DeleteView):
    model = News
    success_url = '/news/'
    template_name = 'news/delete.html'

    context_object_name = 'detail'


def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Вы написали какую-то дичь'

    form = NewsForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)
