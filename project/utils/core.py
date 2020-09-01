from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count

def get_object_by_id(instance, id):
    try:
        obj = instance.objects.get(id = id)    
    except ObjectDoesNotExist:
        obj = None
    
    return obj

def get_object_by_user(instance, user):
    
    try:
        obj = instance.objects.get(user = user)
         
    except ObjectDoesNotExist:
        obj = None
         
    return obj

def get_object_by_username(instance, username):
    try:
        obj = instance.objects.get(user__username = username)
    except ObjectDoesNotExist:
        obj = None
    
    return obj


def get_count_object(instance, profile):
    try:
        following = instance.objects.get(user=profile)
        following = following.following.count()
        
    except ObjectDoesNotExist:
        following = 0
    
    return following

    # try:
    #     queryset = instance.objects.annotate(num_ = Count(attribute_name))

    #     return queryset[0].num_
    # except IndexError:
    #     return 0
    
def get_object_by_slug(instance, slug):
    try:
        obj = instance.objects.get(slug = slug)
    except ObjectDoesNotExist:
        obj = None
    return obj

def get_object_by_post(instance, post):
    try:
        obj = instance.objects.get(post = post)
    except ObjectDoesNotExist:
        obj = None
    return obj


def get_all_objects(instance):
    return instance.objects.all()