from django.contrib import admin
from django.utils.safestring import mark_safe
from mptt.admin import MPTTModelAdmin

from . import models

#используемый для последовательного отображения данных рецепта в интерфейсе редактирования поста
#Он наследуется от admin.StackedInline, который является подклассом admin
#Атрибут extra определяет количество дополнительных форм, которые должны отображаться для добавления новых рецептов.
class RecipeInline(admin.StackedInline):
    model = models.Recipe
    extra = 1

#PostAdmin: Управление и отображение записей в блоге
@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    #list_display: Этот атрибут определяет поля, которые должны отображаться в представлении списка для записей
    list_display = ["title", "category", "author", "get_html_photo", "create_at", "id"]
    inlines = [RecipeInline]
    save_as = True
    save_on_top = True
    fields = ['title', 'slug', 'category', 'tags', 'author', 'create_at', 'image', 'get_html_photo' ,'text']
    readonly_fields = ['create_at', 'get_html_photo']

    #Метод get_html_photo - это пользовательский метод, который возвращает HTML-тег <img> для отображения изображения публикации.
    def get_html_photo(self, object):
        if object.image:
            return mark_safe(f"<img src='{object.image.url}' width=50>")

    get_html_photo.short_description = "image"



#RecipeAdmin: Управление и отображение рецептов
@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ["name", "prep_time", "cook_time", "post"]


#CommentAdmin: Управление и отображение комментариев
@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'website', 'id', 'create_at']


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)


admin.site.site_title = 'Главный Админ'
admin.site.site_header = 'Я админ'

