from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('route/<id>/', views.route, name = 'route'),
    path('about_us', views.about_us, name = 'about_us'),
    path('crag/<id>/', views.crag, name = 'crag'),
    path('Beta_blog_post/<id>/', views.Beta_blog_post, name = 'Beta_blog_post'),
    path('Beta_blog_post_create/', views.Beta_blog_post_create, name = 'Beta_blog_post_create'),
    path('Beta_blog_post_create_cat/', views.Beta_blog_post_create_cat, name = 'Beta_blog_post_create_cat'),
    path('Beta_blog_post_update/<id>/', views.Beta_blog_post_update, name = 'Beta_blog_post_update'),
    path('Beta_blog_post_delete/<id>/', views.Beta_blog_post_delete, name = 'Beta_blog_post_delete'),
    path('Beta_blog', views.Beta_blog, name = 'Beta_blog'),
    path('Beta_guidebooks', views.Beta_guidebooks, name = 'Beta_guidebooks'),
    path('Beta_videos_acid', views.Beta_videos_acid, name = 'Beta_videos_acid'),
    path('Beta_videos', views.Beta_videos, name = 'Beta_videos'),
    path('sector/<id>/', views.sector, name = 'sector'),
    path('cragsite', views.cragsite, name = 'cragsite'),
    path('gallery/<id>/', views.gallery, name = 'gallery'),
    path('gallery_display/<id>/', views.gallery_display, name = 'gallery_display'),
    path('search/', views.search, name = 'search'),
    path('search_general/', views.search_general, name = 'search_general'),
    path('profile/', views.profile_view, name='account_profile'),
] 