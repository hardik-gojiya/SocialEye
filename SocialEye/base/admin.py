from django.contrib import admin
from .models import Post, Reel, Comment_For_Reel, Comment_For_Post, Follow, Like_For_Post,Like_For_Reel

# Register your models here.
admin.site.register(Post)
admin.site.register(Reel)
admin.site.register(Comment_For_Post)
admin.site.register(Comment_For_Reel)
admin.site.register(Follow)
admin.site.register(Like_For_Post)
admin.site.register(Like_For_Reel)
