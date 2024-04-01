from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from .models import Post, Category, Comment
from .forms import CommentForm, SearchForm

class home(ListView):
    model = Post
    template_name = 'blog_app/home.html'
    context_object_name = 'posts'
    paginate_by = 3
    ordering = ['-publish_date']

class post_detail(DetailView):
    model = Post
    template_name = 'blog_app/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = Comment.objects.filter(post=self.object)
        return context

class cine(ListView):
    model = Post
    template_name = 'blog_app/cine.html'
    context_object_name = 'posts'
    paginate_by = 6
    ordering = ['-publish_date']

    def get_queryset(self):
        cine_category = Category.objects.get(name='Cine')
        return Post.objects.filter(category=cine_category).order_by('-publish_date')

class tv(ListView):
    model = Post
    template_name = 'blog_app/tv.html'
    context_object_name = 'posts'
    paginate_by = 6
    ordering = ['-publish_date']

    def get_queryset(self):
        tv_category = Category.objects.get(name='TV')
        return Post.objects.filter(category=tv_category).order_by('-publish_date')

class videojuegos(ListView):
    model = Post
    template_name = 'blog_app/videojuegos.html'
    context_object_name = 'posts'
    paginate_by = 6
    ordering = ['-publish_date']

    def get_queryset(self):
        videojuegos_category = Category.objects.get(name='Videojuegos')
        return Post.objects.filter(category=videojuegos_category).order_by('-publish_date')

class literatura(ListView):
    model = Post
    template_name = 'blog_app/literatura.html'
    context_object_name = 'posts'
    paginate_by = 6
    ordering = ['-publish_date']

    def get_queryset(self):
        literatura_category = Category.objects.get(name='Literatura') #literatura_category
        return Post.objects.filter(category=literatura_category).order_by('-publish_date')

class podcasts(ListView):
    model = Post
    template_name = 'blog_app/podcasts.html'
    context_object_name = 'posts'
    paginate_by = 6
    ordering = ['-publish_date']

    def get_queryset(self):
        podcasts_category = Category.objects.get(name='Podcasts')
        return Post.objects.filter(category=podcasts_category).order_by('-publish_date')

def about(request):
    return render(request, 'blog_app/about.html')

def search(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data.get('query')
            results = Post.objects.filter(title__icontains=query)
            return render(request, 'blog_app/search.html', {'results': results, 'query': query})
    else:
        form = SearchForm()
    return render(request, 'blog_app/search.html', {'form': form})

@require_POST
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.author = request.user
        comment.save()
    return redirect('blog_app:post_detail', pk=post.pk)





