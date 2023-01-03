from .models import Post, Category, Comment
from django.views.generic import DetailView, TemplateView, ListView
from django.views.generic.edit import CreateView

# Home
class HomeView(TemplateView):
    template_name = 'blog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["latest_posts"] = Post.objects.filter(status=Post.STATUS_PUBLISHED).order_by("-date_available")
        context["categories"] = Category.objects.filter(status=True).order_by("sort_order")
        return context
    

# Post
class PostView(DetailView):
    template_name = 'blog/post.html'
    model = Post

# Comment
class CommentCreateView(CreateView):
    model = Comment
    fields = ('name', 'description',)
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        post = Post.objects.get(slug = self.kwargs['slug'])
        form.instance.post = post
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = Post.objects.get(slug = self.kwargs['slug'])
        context["post"] = post
        return context
    
    
# Category
class CategoryView(ListView):
    template_name = 'blog/category.html'
    context_object_name = 'posts'

    def get_queryset(self):
        category = Category.objects.get(slug = self.kwargs['slug'], status = True)
        return category.posts.filter(status = Post.STATUS_PUBLISHED)

    def get_context_data(self, **kwargs):
        category = Category.objects.get(slug = self.kwargs['slug'], status = True)
        context = super().get_context_data(**kwargs)
        context["category"] = category
        context["categories"] = Category.objects.filter(status=True).order_by("sort_order")
        return context

# Search
class SearchView(ListView):
    template_name = 'blog/search.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        query = super().get_queryset()

        if 'search' in self.request.GET:
            return query.filter(status = Post.STATUS_PUBLISHED, title__contains = self.request.GET['search'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["search"] = self.request.GET.get('search')
        return context
    
    