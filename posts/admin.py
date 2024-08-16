from django.contrib import admin
from posts.models import Post,Comment,Like,PostTag,Tag

admin.site.register(Post)
admin.site.register(PostTag)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Like)