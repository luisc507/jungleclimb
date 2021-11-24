from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.db.models.aggregates import Count
from django.db.models import Q
from django.http import request
from django.shortcuts import redirect, render, get_object_or_404, redirect, reverse
from django.db.models import Count
from .models import crags, gallery_acid, post, sectors, routes
from marketing.models import Signup, Contact
from .forms import CommentForm, CommentCragForm, CommentRouteForm, CommentSectorForm, CreateCat, CreatePost


# Create your views here.
def search(request):
    cragsinfo = crags.objects.all()
    queryset = post.objects.all()
    query = request.GET.get('q')
    if query:
        queryset= queryset.filter(
            Q(title__icontains=query) |
            Q(overview__icontains=query) |
            Q(content__icontains=query) 
        ).distinct()

    context= {
        'queryset' : queryset,
        'cragsinfo' : cragsinfo,
    }
    return render(request, 'search_results.html', context)


def search_general(request):
    cragsinfo = crags.objects.all()
    querysetwo = crags.objects.filter(Btn = True)
    querytwo = request.GET.get('k')
 
    if querytwo:
        querysetwo= querysetwo.filter(
            Q(name__icontains=querytwo) |
            Q(overview__icontains=querytwo) |
            Q(content__icontains=querytwo) 
        ).distinct()

    context= {
        'querysetwo' : querysetwo,
        'cragsinfo' : cragsinfo,
    }
    return render(request, 'search_general.html', context)


def get_category_count():
    quearyset = post.objects.values('categories__title').annotate(Count('categories__title'))
    return quearyset


def index(request):
    cragsinfo = crags.objects.all()
    context = {'cragsinfo' : cragsinfo}
    return render(request, 'index.html', context)

def route(request, id):
    cragsinfo = crags.objects.all()
    posts = get_object_or_404(routes, id=id)
    form = CommentRouteForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = posts
            form.save()
            return redirect(reverse("route", kwargs={
                'id': posts.id
            }))

    context = {
        'cragsinfo' : cragsinfo,
        'posts' : posts,
        'form' : form
        }
        
    return render(request, 'route.html', context)

def about_us(request):
    cragsinfo = crags.objects.all()

    if request.method == "POST":
        emailcontact = request.POST["emailcontact"]
        messagecontact = request.POST["messagecontact"]
        new_signup = Contact()
        new_signup.emailcontact = emailcontact
        new_signup.messagecontact = messagecontact
        new_signup.save()

        send_mail(
            'Contact form',
            messagecontact,
            emailcontact,
            [ 'jungleclimbpty@gmail.com'],
        )

    context = {'cragsinfo' : cragsinfo}

    return render(request, 'about_us.html', context)

def crag(request, id):
    cragsinfo = crags.objects.all()
    sectorpost = sectors.objects.all()
    text = get_object_or_404(crags, id=id)
    form = CommentCragForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = text
            form.save()
            return redirect(reverse("crag", kwargs={
                'id': text.id
            }))

    context = {
        'cragsinfo' : cragsinfo,
        'posts' : text,
        'form' : form,
        'sectorpost' : sectorpost,
        }
    return render(request, 'crag.html', context)

def Beta_blog_post(request, id):
    cragsinfo = crags.objects.all()
    category_count = get_category_count()
    text = get_object_or_404(post, id=id)
    form = CommentForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = text
            form.save()
            return redirect(reverse("Beta_blog_post", kwargs={
                'id': text.id
            }))

    context = {
        'posts': text,
        'category_count' : category_count,
        'form' : form,
        'cragsinfo' : cragsinfo
    }
    return render(request, 'Beta_blog_post.html', context)

def Beta_blog_post_create_cat(request):
    title = 'Create'
    form = CreateCat(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("index"))

    context = {
        'form': form,
        'title': title
    }
    return render(request, "Beta_blog_post_create_cat.html", context)

def Beta_blog_post_create(request):
    title = 'Create'
    form = CreatePost(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("Beta_blog_post", kwargs={
                'id': form.instance.id
            }))

    context = {
        'form': form,
        'title': title
    }
    return render(request, "Beta_blog_post_create.html", context)

def Beta_blog_post_update(request, id):
    title =  'Update'
    posts = get_object_or_404(post, id=id)
    form = CreatePost(request.POST, request.FILES, instance=posts)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect(reverse("Beta_blog_post", kwargs={
                'id': form.instance.id
            }))

    context = {
        'form': form,
        'title' : title,
    }
    return render(request, "Beta_blog_post_create.html", context)

def Beta_blog_post_delete(request, id):
    posts = get_object_or_404(post, id=id)
    posts.delete()
    return redirect(reverse("Beta_blog"))


def Beta_blog(request):
    cragsinfo = crags.objects.all()
    category_count = get_category_count()
    latest = post.objects.order_by('-timestamp')
    paginator = Paginator(latest, 2)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)


    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()

    context = {
        'queryset' : paginated_queryset,
        'page_request_var': page_request_var,
        'latest' : latest,
        'category_count' : category_count,
        'cragsinfo' : cragsinfo
        }
    return render(request, 'Beta_blog.html', context)

def Beta_guidebooks(request):
    cragsinfo = crags.objects.all()
    context = {'cragsinfo' : cragsinfo}
    return render(request, 'Beta_guidebooks.html', context)

def Beta_videos_acid(request):
    cragsinfo = crags.objects.all()
    context = {'cragsinfo' : cragsinfo}
    return render(request, 'Beta_videos_acid.html', context)

def Beta_videos(request):
    cragsinfo = crags.objects.all()
    context = {'cragsinfo' : cragsinfo}
    return render(request, 'Beta_videos.html', context)

def sector(request, id):
    cragsinfo = crags.objects.all()
    routesinfo = routes.objects.all()
    posts = get_object_or_404(sectors, id=id)
    form = CommentSectorForm(request.POST)

    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = posts
            form.save()
            return redirect(reverse("sector", kwargs={
                'id': posts.id
            }))

    context = {
        'cragsinfo' : cragsinfo,
        'posts' : posts,
        'routesinfo' : routesinfo,
        'form' : form
        }
    return render(request, 'sector.html', context)

def cragsite(request):
    cragsinfo = crags.objects.all()
    context = {'cragsinfo' : cragsinfo}
    return render(request, 'cragsite.html', context)

def cragsnavbar(request):
    cragsinfo = crags.objects.all()
    context = {'cragsinfo' : cragsinfo}
    return render(request, 'navbar.html', context)


def gallery(request, id):
    cragsinfo = crags.objects.all()
    posts = get_object_or_404(crags, id=id)
    gallerypics = gallery_acid.objects.all()
    context = {
        'gallerypics' : gallerypics,
        'cragsinfo' : cragsinfo,
        'posts' : posts
        }
    return render(request, 'gallery.html', context)

def gallery_display(request, id):
    cragsinfo = crags.objects.all()
    posts = get_object_or_404(gallery_acid, id=id)
    context = {
        'posts': posts,
        'cragsinfo' : cragsinfo
    }
    return render(request, 'gallery_display.html', context)

def profile_view(request):
    return render(request, 'account/profile.html')
