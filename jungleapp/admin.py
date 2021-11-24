# Register your models here.

from django.contrib import admin
from .models import crags, gallery_acid, Author, category, grade, post, comment, commentcrag, commentsector, commentroute, sectors, dificulty, routes, grade, type_of_climb

admin.site.register(crags)
admin.site.register(gallery_acid)
admin.site.register(Author)
admin.site.register(category)
admin.site.register(post)
admin.site.register(comment)
admin.site.register(commentcrag)
admin.site.register(sectors)
admin.site.register(dificulty)
admin.site.register(routes)
admin.site.register(grade)
admin.site.register(type_of_climb)
admin.site.register(commentsector)
admin.site.register(commentroute)