from django.contrib import admin

from posts.models import Post, Love, Comment, Attachment,CommentReplay

admin.site.register(Post)
admin.site.register(Love)
admin.site.register(Comment)
admin.site.register(Attachment)
admin.site.register(CommentReplay)



