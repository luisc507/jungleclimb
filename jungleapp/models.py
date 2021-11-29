from django.db import models
from django.db.models.deletion import CASCADE
from tinymce import models as tinymce_models 
from django.db.models.fields import AutoField, TextField
from django.contrib.auth import get_user_model
from django.urls import reverse 

User = get_user_model()

# Create your models here.
class crags(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to="post/", null=False, blank=False)
    location = models.CharField(max_length=500, null=False, blank=False)
    Btn = models.BooleanField()
    overview = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    content = tinymce_models.HTMLField(null=True, blank=True)
    gallery_btn = models.BooleanField(null=True, blank=True)
    comment_count = models.IntegerField(default=0)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('crag', kwargs={'id': self.id})

    @property
    def get_commentscrag(self):
        return self.commentscrag.all().order_by('-timestamp')


class type_of_climb(models.Model):
    type = models.CharField(max_length=30)

    def __str__(self):
        return self.type


class dificulty(models.Model):
    dificulty = models.CharField(max_length=20)

    def __str__(self):
        return self.dificulty


class sectors(models.Model):
    sector_name = models.CharField(max_length=100, null=False, blank=False)
    order = models.IntegerField(null=True, blank=True)
    crag = models.ForeignKey(crags, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to="post/", null=True, blank=True)
    overview = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    content = tinymce_models.HTMLField(null=True, blank=True)
    comment_count = models.IntegerField(default=0)
    guidebook = tinymce_models.HTMLField(null=True, blank=True)
    type_of_climb = models.ForeignKey(type_of_climb, on_delete=models.SET_NULL, null=True, blank=True)
    dificulty = models.ForeignKey(dificulty, on_delete=models.SET_NULL, null=True, blank=True)
    route_count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.sector_name

    def get_absolute_url(self):
        return reverse('sector', kwargs={'id': self.id})

    @property
    def get_commentsector(self):
        return self.commentsector.all().order_by('-timestamp')



class grade(models.Model):
    grades = models.CharField(max_length=10)

    def __str__(self):
        return self.grades


class routes(models.Model):
    route = models.CharField(max_length=100, null=False, blank=False)
    sector_name = models.ForeignKey(sectors, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.CharField(max_length=10, null=True, blank=True)
    grade = models.ForeignKey(grade, on_delete=models.SET_NULL, null=True, blank=True)
    topo = models.ImageField(upload_to="post/", null=True, blank=True)
    commentary = models.CharField(max_length=500, null=True, blank=True)
    comment_count = models.IntegerField(default=0)

    def __str__(self):
        return self.route

    def get_absolute_url(self):
        return reverse('route', kwargs={'id': self.id})

    @property
    def get_commentsroute(self):
        return self.commentsroute.all().order_by('-timestamp')



class gallery_acid(models.Model):
    crag = models.ForeignKey(crags, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(upload_to="post/", null=False, blank=False)
    description = models.CharField(max_length=500, null=True, blank=True)
    date = models.DateField(null=False, blank=False)
    previous_post = models.ForeignKey('self', related_name='previous',on_delete=models.SET_NULL, null=True, blank=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('gallery_display', kwargs={'id': self.id})


 
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username

class category(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class post(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    thumbnail = models.ImageField(upload_to="post/")
    categories = models.ManyToManyField(category)
    feature = models.BooleanField()
    content = tinymce_models.HTMLField()
    previous_post = models.ForeignKey('self', related_name='previous',on_delete=models.SET_NULL, null=True, blank=True)
    next_post = models.ForeignKey('self', related_name='next', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('Beta_blog_post', kwargs={'id': self.id})

    def get_update_url(self):
        return reverse('Beta_blog_post_update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('Beta_blog_post_delete', kwargs={'id': self.id})

    @property
    def get_comments(self):
        return self.comments.all().order_by('-timestamp')


class comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(post, related_name="comments",on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username 


class commentcrag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(crags, related_name="commentscrag",on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username 


class commentsector(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(sectors, related_name="commentsector",on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username 


class commentroute(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(routes, related_name="commentsroute",on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username 
