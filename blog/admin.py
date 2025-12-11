from django.contrib import admin
from .models import Category, Location, Post

# Перевод названия приложения Blog
admin.site.site_header = 'Панель администратора'
admin.site.index_title = 'Блог'
admin.site.site_title = 'Администрирование Блога'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_published', 'created_at')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}


class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'created_at')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    search_fields = ('name',)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'category',
        'location',
        'is_published',
        'created_at'
    )
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category', 'location')
    search_fields = ('title', 'text')
    filter_horizontal = ()
    date_hierarchy = 'pub_date'
    ordering = ('-pub_date',)
    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'author')
        }),
        ('Дополнительные опции', {
            'fields': ('category', 'location', 'pub_date', 'is_published'),
            'classes': ('collapse',)
        }),
    )


# Регистрация моделей
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
