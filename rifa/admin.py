from django.contrib import admin
from .models import Rifa,Number

class RifaAdmin(admin.ModelAdmin):
       list_display = ("id","quantity","value","pix_key","title","description","award","date_start","date_finish","active")
       search_fields = ("id", "title","description","award")

       

class NumberAdmin(admin.ModelAdmin):
       list_display =( "id", "rifa_id","number" ,"status" ,"date")
       search_fields = ("id","rifa_id","status")


admin.site.register(Rifa,RifaAdmin)
admin.site.register(Number,NumberAdmin)