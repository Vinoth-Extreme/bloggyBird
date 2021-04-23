from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comments
from django.urls import reverse_lazy, reverse
from .forms import AddPostForm, EditPostForm, CommentForm
import datetime
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.

# Normal views
class HomeView(ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-publication_date']
    ordering = ['-pk']

    def get_context_data(self, *args, **kwargs):
        cats = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cats"] = cats
        return context


class ArticleDetails(DetailView):
    model = Post
    template_name = 'article-detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetails, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.totalLikes()
        total_loves = stuff.totalLoves()

        is_liked = False
        is_loved = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            is_liked = True
        if stuff.loves.filter(id=self.request.user.id).exists():
            is_loved = True
        context['total_likes'] = total_likes
        context['is_liked'] = is_liked
        context['total_loves'] = total_loves
        context['is_loved'] = is_loved
        return context




# **********************************************************************************************
# Category
class AddCategoryView(CreateView):
    model = Category
    fields = '__all__'
    template_name = 'add_category.html'

class EditCategoryView(UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'edit_category.html'

class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'delete_category.html'
    success_url = reverse_lazy('home')

def CategoriesList(request):
    cats = Category.objects.all()
    context = { 'cats': cats, }
    return render(request, 'categories_list.html', context)

def CategoryView(request, cat):
    articles = Post.objects.filter(category=cat).order_by('publication_date').reverse()
    count = articles.count()
    context = {
        'cat': cat.title(),
        'posts': articles,
        'count': count,
    }
    return render(request, 'category_based_articles.html', context)



# **********************************************************************************************
#Posts
class AddPostView(CreateView):
    model = Post
    form_class = AddPostForm
    template_name = 'add_post.html'

class EditPost(UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'edit_post.html'

class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')





# ************************************************************************************************
# likes & loves
def LikeView(request, id):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(id)]))

def LoveView(request, id):
    post = get_object_or_404(Post, id=request.POST.get('post_id_love'))
    is_loved = False
    if post.loves.filter(id=request.user.id).exists():
        post.loves.remove(request.user)
        is_loved = False
    else:
        post.loves.add(request.user)
        is_loved = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(id)]))

#***************************************************************************************************
# Comments
class AddCommentView(CreateView):
    model = Comments
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.done_by_id = self.request.user.pk
        return super().form_valid(form)

    success_url = reverse_lazy('home')


def asyncComment(request):
    post = request.POST.get('post')
    user = request.POST.get('user')
    body = request.POST.get('body')
    new = Comments(post_id=post, done_by_id=user, body=body)
    new.save()
    return JsonResponse({'comment': model_to_dict(new)}, status=200)


def test(request):
    if request.method == 'POST':
        is_liked_test = False
        context = {
            'is_liked': is_liked_test,
        }
        return render(request, 'test.html', context)
    else:
        return render(request, 'test.html')



