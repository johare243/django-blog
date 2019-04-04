import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
			'jmo.settings')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'static')
framework = os.path.join(STATIC_DIR, '/images/framework.jpg')
python = os.path.join(STATIC_DIR, '/images/python.jpg')

import django
django.setup()

from pages.models import Category, Post

def populate():
	#first create lists of dicts containing pages
	#we want to add into each category (cat)
    python_pages = [
        {"title": "Official Python Tutorial",
         "url": "http://docs.python.org/2/tutorial/",
         "views": 95},
        {"title": "How to think like a scientist",
         "url": "http://www.greenteapress.com/thinkpython/",
         "views": 15},
        {"title": "Learn Python in 10 Minutes",
         "url": "http://www.korokithakis.net/tutorials/python/",
         "views": 75},
    ]
    print(python)

    django_pages = [
		{"title": "Official Django Tutorial",
         "url": "http://docs.djangoproject.com/en/1.9.intro/tutorial01/",
         "views": 45},
		{"title": "Django Rocks",
         "url": "http://www.djangorocks.com/",
         "views": 15},
		{"title": "How to Tango with Django",
         "url": "http://www.tangowithdjango.com/",
         "views": 45},
	]

    other_pages = [
		{"title":"Youtube",
		 "url": "https://youtube.com/",
         "views": 145},
		{"title":"Flask",
		 "url": "http://flask.pocoo.org",
         "views": 122},
	]

    cats = {"Python": {"pages": python_pages,
			   "views": 128,
			   "likes": 64,
               "cat_image": python},
		"Django": {"pages": django_pages,
			   "views": 64,
			   "likes": 32,
               "cat_image": framework},
		"Others": {"pages": other_pages,
			   "views": 32,
			   "likes": 44,
               "cat_image": framework},
	}

	# iterate through each dict & add category
	# then add all associated pages for that cat
    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['views'], cat_data["likes"])
        print(c.views)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"], p["views"])
# Print out the cats that were added
        for c in Category.objects.all():
            for p in Post.objects.filter(category=c):
                print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views=0):
    p = Post.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, views=0, likes=0,):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes,)[0]
    c.views = views
    c.likes=likes
    c.save()
    return c

if __name__ == '__main__':
	print("Starting the population script...")
	populate()
