from django.utils.text import slugify
import random, string
def generate_rendom_string(N):
    return("".join(random.choices(string.ascii_uppercase+string.digits,k=N)))
def generate_slug(x):
    y=slugify(x)
    from .models import BlogModel
    if BlogModel.objects.filter(slug=y).exists(): 
        y=generate_slug(x+generate_rendom_string(5))
    return y
        

