from django.contrib import admin
from myapp.models import BlogComment


# Register your models here.
#admin.site.register(Employee)


#to display entire table in admin we need to below steps
class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'comment']

admin.site.register(BlogComment, BlogCommentAdmin)
