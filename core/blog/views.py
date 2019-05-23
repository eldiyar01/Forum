from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import View, ListView, CreateView

from  user.models import User
from .forms import CommentForm
from .models import News, Category, Comment
from .utils import ObjDetailMixin


class NewsView(ListView):
    context_object_name = 'news'
    template_name = 'blog/blog_news.html'
    queryset = News.objects.all()

    def get_context_data(self, **kwargs):
        context = super(NewsView, self).get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['all_news'] = News.objects.all()
        return context



def newsdetail(request, pk):
    news = News.objects.get(id=pk)
    comments = Comment.objects.filter(news=pk, moderation=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.news = news
            form.save()
            return reverse('blog:news_detail', pk)
    else:
        form = CommentForm()
    return render(request, 'blog/news_detail.html', {'news': news, 'comments': comments, 'form': form})


class CategoryDetail(ObjDetailMixin, View):
    model = Category
    template = 'blog/category_detail.html'


def search_result(request):
    search_q = request.GET.get('search')
    if search_q:
        result_news = News.objects.filter(title__icontains=search_q)
    else:
        result_news = "Sorry we did'nt find"
    return render(request, 'blog/search_result.html', context={'r_news': result_news,
                                                               'search': search_q})


def author(request,pk):
    post_author = User.objects.get(id=pk)
    return render(request, context={'author': post_author})


