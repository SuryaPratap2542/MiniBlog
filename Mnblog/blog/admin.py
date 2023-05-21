from django.contrib import admin
from .models import Post,Contact

# Register your models here.
@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display=['id','title','desc']

@admin.register(Contact)
class ContactModelAdmin(admin.ModelAdmin):
    list_display=['id','name','email','message']