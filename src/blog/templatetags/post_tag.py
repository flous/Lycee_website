from django import template
from blog.models import Post , Comment
from ECAs.models import Activities , ImagesActivities
from django.contrib.auth.models import User ,Group

register=template.Library()
@register.inclusion_tag('blog/latest_posts.html')
def latest_posts():
    context={
        'l_posts':Post.objects.all()[0:5]
    }
    return context
 
@register.inclusion_tag('blog/latest_comments.html')
def latest_comments():
    context={
        'l_comments':Comment.objects.filter(active=True)[0:5],
    }
    return context
@register.inclusion_tag('ECAs/latest_activities.html')
def latest_activities():
    context={
        'l_acts':Activities.objects.all()[0:5],
    }
    return context
@register.inclusion_tag('ECAs/regroup_activities.html')
def regroup_activities(id_act):
    act=Activities.objects.get(id=id_act)
    context={
        'act':act,
        'imgs_activiti' :ImagesActivities.objects.filter(activitie=act),
    }
    return context
@register.inclusion_tag('ECAs/images_activities.html')
def consult_images_activities(id_act):
    act=Activities.objects.get(id=id_act)
    context={
        'act':act,
        'imgs_activiti' :ImagesActivities.objects.filter(activitie=act),
    }
    return context
@register.filter(name='has_group')
def has_group(user, group_name):
    try:
        group =  Group.objects.get(name=group_name)
    except Group.DoesNotExist:
        return False

    return group in user.groups.all()