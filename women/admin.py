from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from .models import Women, Category

@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    fields = ['title', 'slug', 'content', 'img_show', 'img_file', 'cat', 'tag']
    prepopulated_fields = {'slug': ('title', )}
    filter_vertical = ['tag']
    list_display = ('id', 'title', 'img_show', 'time_created', 'is_published', 'cat')
    list_display_links = ('id', 'title')
    readonly_fields = ['img_show']
    list_editable = ['is_published']
    list_per_page = 5
    actions = ['set_published', 'set_draft']
    search_fields = ['title', 'cat__name']
    list_filter = ['cat__name', 'is_published']
    save_on_top = True

    @admin.display(description='Изображение')
    def img_show(self, women: Women):
        if women.img_file:
            return mark_safe(f"<img src='{women.img_file.url}' width='45'>")
        return 'Отсуствует Изображение'
    @admin.action(description='Опубликовать записи')
    def set_published(self, request, queryset):
        count = queryset.update(is_published=Women.Publisherdraft.PUBLISHED)
        self.message_user(request, f"Были опубликованы {count} записей.")

    @admin.action(description='Снять с публикации')
    def set_draft(self, request, queryset):
        count = queryset.update(is_published=Women.Publisherdraft.DRAFT)
        self.message_user(request, f"{count} было снято с публикации.", messages.WARNING)


@admin.register(Category)
class WomenAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')