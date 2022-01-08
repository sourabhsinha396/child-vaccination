import random
from django.utils.text import slugify

def random_slug(name="user",digits=10):
    lower = 10**(digits-1)
    upper = 10**digits - 1
    return slugify(name[:8] + str(random.randint(lower, upper)))