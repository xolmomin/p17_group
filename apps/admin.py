from django.contrib import admin

from apps.models import Post, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
    # fields = ['']
    # list_display = ['id', 'custom_title']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'custom_title']

    def custom_title(self, obj):
        return ' '.join(obj.title.split()[:4])

    custom_title.short_description = 'Sarlavha'
    #
    # def has_delete_permission(self, request, obj=None):
    #     return False
    #
    # def has_add_permission(self, request):
    #     return False

#
# class PostAdmin(admin.ModelAdmin):
#     pass
#
# admin.site.register(Post, PostAdmin)
