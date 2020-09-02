import os
import random 
import string
from random import choice
from django.utils.text import slugify

def get_file_extension(filename):
    basename = os.path.basename(filename)
    base, ext = os.path.splitext(basename)
    return base, ext

def get_class_name(instance):
    return instance.__class__.__name__

def upload_directory_path(instance,filename):    
    new_file = random.randint(1, 39515623)        
    basename, ext = get_file_extension(filename)
    filename = "{new_file_name}{ext}".format(new_file_name=new_file,ext=ext)

    class_name = get_class_name(instance)
    print('class name',class_name)
    
    if class_name == 'PostExtraImage':

        folder_name =  'post'
        return "{folder_name}/{username}/{new_filename}/{filename}".format(
            folder_name=folder_name, username = instance.post.user, new_filename=new_file, filename=filename
        )
    
    elif class_name == "Post": 
               
        folder_name = 'post'

    elif class_name == "Profile":

        folder_name = 'profile'
    
            
    return "{folder_name}/{username}/{new_filename}/{filename}".format(
        folder_name=folder_name, username = instance.user, new_filename=new_file, filename=filename
    )
    
def generate_slug():    
    random = string.ascii_uppercase + string.ascii_lowercase + string.digits  
    return ''.join(choice(random) for _ in range(15))

def get_absolute_uri(self,post):
    request = self.context.get('request')
    attribute_url = post.image.url    
    return request.build_absolute_uri(attribute_url)


def is_valid(args={}, username=None, current_username=None):
    
    is_user_exist = True
    for user in username:
        if user != args['username'] and args['username'] != current_username:
            is_user_exist = False
      
    if args['password'] == args['confirm'] and is_user_exist:       
        return True
     
    return False
        
    
