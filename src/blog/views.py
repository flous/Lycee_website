from django.shortcuts import render , get_object_or_404
from .models import Post , Comment


# Create your views here.
def blogs_home (request):
    context = {
        'title': 'مدونة',
        'posts' : Post.objects.all(),
    }
    return render(request , 'blog/blogs_page.html' , context)

def about(request):
    return render(request,'blog/about.html',{'title':'من أنا'})


def post_detail(request , post_id):
    post=get_object_or_404(Post , pk=post_id)
    context={
        'title' :post.title,
        'post': post,
        'comments':post.comments.filter(active=True)
    }
    return render(request , 'blog/post_detail.html', context)