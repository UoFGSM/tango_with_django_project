import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {'title': 'OfficialPython Tutorial', 'url': 'http://docs.python.org/3/tutorial/','views': 145},
        {'title': 'HowtoThinklike aComputerScientist', 'url': 'http://www.greenteapress.com/thinkpython/','views': 60},
        {'title': 'LearnPythonin10 Minutes', 'url': 'http://www.korokithakis.net/tutorials/python/','views': 85}
    ]
    
    django_pages = [
        {'title': 'OfficialDjangoTutorial', 'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/','views': 95},
        {'title': 'DjangoRocks', 'url': 'http://www.djangorocks.com/','views': 160},
        {'title': 'HowtoTangowith Django', 'url': 'http://www.tangowithdjango.com/','views': 45}
    ]
    
    other_pages = [
        {'title': 'Bottle', 'url': 'http://bottlepy.org/docs/dev/','views': 65},
        {'title': 'Flask', 'url': 'http://flask.pocoo.org','views': 100}
    ]
    
    cats = {
        'Python': {'pages': python_pages,'views': 128,'likes': 64},
        'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
        'OtherFrameworks': {'pages': other_pages, 'views': 32, 'likes': 16}
    }

    # If you want to add more categories or pages,
    # add them to the dictionaries above.
    
    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'-{c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
