from django.shortcuts import render

posts=[
    {
        'title': 'التدوينة الأولى ',
        'content' : 'نص التدوينة التدوينة كنص تجريبي ',
        'post_date': '15-10-2020',
        'author':'عبد الحكيم ',
    },
    {
        'title': 'التدوينة الثانية ',
        'content' : 'نص التدوينة التدوينة كنص تجريبي ',
        'post_date': '15-10-2020',
        'author':'نسيبة ',
    },
    {
        'title': 'التدوينة الثالثة ',
        'content' : 'نص التدوينة التدوينة كنص تجريبي ',
        'post_date': '15-10-2020',
        'author':'تقوى ',
    },
    
    
]
# Create your views here.
def blogs_home (request):
    context = {
        'title': 'صفحة التدوينات',
        'posts' : posts
    }
    return render(request , 'blog/blogs_page.html' , context)
