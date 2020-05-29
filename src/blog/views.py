from django.shortcuts import render , get_object_or_404
from .models import Post , Comment
from .forms import AddComment , AddPostForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage
from django.views.generic import CreateView ,UpdateView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.
def blogs_home (request):
    posts=Post.objects.all()
    paginator = Paginator(posts , 5)
    page = request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_page)
        


    context = {
        'title': 'مدونة',
        'posts' : posts,
        
    }
    return render(request , 'blog/blogs_page.html' , context)

def about(request):
    return render(request,'blog/about.html',{'title':'من أنا'})


def post_detail(request , post_id):
    post=get_object_or_404(Post , pk=post_id)
    comments=post.comments.filter(active=True)
#  التتحقق في حالة إرسال البيانات من أجل إضافة تعيق خاص بمنشور معين 
    if request.method=='POST':
        comment_form=AddComment(data=request.POST)
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.post=post
            new_comment.save()
            comment_form=AddComment()
    else:
        comment_form=AddComment()

    context={
        'title' :post.title,
        'post': post,
        'comments':comments,
        'comment_form' :comment_form,
    }
    return render(request , 'blog/post_detail.html', context)
class PosteCreateView(LoginRequiredMixin ,CreateView):
    model = Post
    template_name = 'blog/add_post.html'
    form_class =AddPostForm
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class PosteUpdateView(LoginRequiredMixin ,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    form_class =AddPostForm
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    def test_func (self):
        post =self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
class PosteDeletView(LoginRequiredMixin ,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func (self):
        post =self.get_object()
        if self.request.user == post.author:
            return True
        return False