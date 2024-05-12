from django.contrib import admin
from .models import Post ,ContactModel

@admin.register(Post)
class Admin(admin.ModelAdmin):
    list_display = ('id' , 'title','desc' )




@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id' , 'email' )
    

