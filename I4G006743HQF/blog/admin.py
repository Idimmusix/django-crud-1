from django.contrib import admin
from blog.models import Post

# Register your models here.


# class PostAdmin(admin.ModelAdmin):
    # ...

    # def get_readonly_fields(self, request, obj=None):
        # if obj: #This is the case when obj is already created i.e. it's an edit
            # return ['players']
        # else:
            # return []

admin.site.register(Post)
