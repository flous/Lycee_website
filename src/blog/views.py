from django.shortcuts import render , get_object_or_404
from .models import Post , Comment
from .forms import AddComment
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator , PageNotAnInteger , EmptyPage

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