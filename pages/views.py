from datetime import datetime
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login
from django.urls import reverse
from pages.models import Category, Post
from pages.forms import CategoryForm, PostForm, UserForm, UserProfileForm
#from django.contrib.sessions import session

# Create your views here.
def index(request):
    request.session.set_test_cookie()

    #grab top categories and posts from db
    category_list = Category.objects.order_by('-likes')
    post_list = Post.objects.order_by('views')[:5]

    paginator = Paginator(category_list, 5)
    page = request.GET.get('page')
    categories = paginator.get_page(page)

    context_dict = {'categories': categories, 'posts': post_list,}

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    response = render(request, 'pages/index.html', context_dict)

    return response


def about(request):
    #if request.session.test_cookie_worked():
        #print("TEST COOKIE WORKED")
        #request.session.delete_test_cookie()
    visitor_cookie_handler(request)
    context_dict2 = {'boldmessage': "This is the portfolio of James O'Hare"}
    context_dict2['visits'] = request.session['visits']
    return render(request, 'pages/about.html', context=context_dict2)

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        posts = Post.objects.filter(category=category)
        context_dict['posts'] = posts
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['posts'] = None
        context_dict['category'] = None

    return render(request, 'pages/category.html', context_dict)

def show_post(request, post_name_slug):
    context_dict = {}
    try:
        post = Category.objects.get(slug=post_name_slug)
        context_dict['post'] = post
    except Category.DoesNotExist:
        context_dict['post'] = None

    return render(request, 'pages/post.html', context_dict)

@login_required
def add_category(request):
    form = CategoryForm()

    # http post?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            #save new form to db
            cat = form.save(commit=True)
            print(cat, cat.slug)
            #redirect back to index page
            return redirect('index')
        else:
            #form has errors, so print them to the terminal
            print(form.errors)

    #render the form with error msgs or not
    return render(request, 'pages/add_category.html', {'form': form,})

@login_required
def add_post(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            if category:
                post = form.save(commit=False)
                post.category = category
                post.views = 0
                post.save()
                return show_category(request, category_name_slug)
            else:
                print(form.errors)

    context_dict = {'form':form, 'category': category}
    return render(request, 'pages/add_post.html', context_dict)

def register(request):
    #will be set to True on successful registration
    registered = False

    #if HTTP request, process the form data
    if request.method == 'POST':
        #grab the info from the form
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        #if the forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                 'pages/register.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        #check to see if the username/password is valid
        #if valid, return a User object
        user = authenticate(username=username, password=password)

        if user:
            #make sure account has not been disabled
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse('Your account is disabled')
        else:
            #bad credentials, so we cannot allow log in
            print("invalid login details: {0}, {1}".format(username,password))
            return HttpResponse("Invalid login credentials")
    #if not an HTTP POST, display the log in form
    else:
        return render(request, 'pages/login.html')

@login_required
def restricted(request):
    return render(request, 'pages/restricted.html')

@login_required
def user_logout(request):
    #since we know the user is logged in from the decorator
    #we can just log them out
    logout(request)
    #send back to hompage
    return HttpResponseRedirect(reverse('index'))

##HELPER FUNCTIONS
#COOKIES
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
        return val

def visitor_cookie_handler(request):
    #get number of visits to the site
    #use COOKIES.get() to obtain the visits cookie
    #if cookie exists, return value casted to an int
    #else, set default value to one
    visits = int(request.COOKIES.get('visits', '1'))

    last_visit_cookie = request.COOKIES.get('last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    #if it's been more than one day since the last visit
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        #update last visit cookie now that the count has been updated
        response.set_cookie('last_visit', str(datetime.now()))
    else:
        visits = 1
        #set the last visit cookie
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits

