from django.contrib import admin
from mainapp.models import *
from django_summernote.admin import SummernoteModelAdmin


class PostClassAdmin(SummernoteModelAdmin):
    list_display = ('id', 'cat', 'title', 'photo', 'document', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {"slug": ("title",)}
    summernote_fields = ('content',)


class CategoryClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class BookingHouseClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'day', 'holidayhouse', 'booking_wish', 'time', 'time_ordered', 'user')
    list_display_links = ('id', 'day', 'user')
    search_fields = ('time_ordered', 'user')
    # list_editable = ('is_published',)
    # list_filter = ('is_published', 'time_create')


class HolidayHouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    # prepopulated_fields = {"slug": ("name",)}


admin.site.register(PostClass, PostClassAdmin)
admin.site.register(CategoryClass, CategoryClassAdmin)
admin.site.register(BookingHouseClass, BookingHouseClassAdmin)
admin.site.register(HolidayHouse, HolidayHouseAdmin)
