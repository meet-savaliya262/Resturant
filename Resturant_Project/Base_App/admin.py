from django.contrib import admin
from django.utils.html import format_html
from Base_App.models import *

@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'Item_name', 'Price', 'get_category', 'description', 'edit_link')
    list_filter = ('Category',)
    search_fields = ('Item_name', 'Category__Category_name')
    list_display_links = None 

    def get_image(self, obj):
        if obj.Image:
            return format_html('<img src="{}" width="100" height="100" />', obj.Image.url)
        return "-"
    get_image.short_description = 'Image'

    def get_category(self, obj):
        return obj.Category.Category_name
    get_category.short_description = 'Category'

    def edit_link(self, obj):
        return format_html(
            '<a href="{}" class="button" '
            'style="color:#007bff;text-decoration:none;font-size:18px;">✏️ Edit</a>',
            f'/admin/Base_App/items/{obj.id}/change/'
        )
    edit_link.short_description = 'Edit'

@admin.register(ItemList)
class ItemListAdmin(admin.ModelAdmin):
    list_display = ('Category_name','edit_link')
    def edit_link(self, obj):
        return format_html(
            '<a href="{}" class="button" '
            'style="color:#007bff;text-decoration:none;font-size:18px;">✏️ Edit</a>',
            f'/admin/Base_App/itemlist/{obj.id}/change/'
        )
    edit_link.short_description = 'Edit'

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('Description','edit_link')
    def edit_link(self, obj):
        return format_html(
            '<a href="{}" class="button" '
            'style="color:#007bff;text-decoration:none;font-size:18px;">✏️ Edit</a>',
            f'/admin/Base_App/aboutus/{obj.id}/change/'
        )
    edit_link.short_description = 'Edit'

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('User_name', 'Description', 'Rating', 'get_image')
    def get_image(self, obj):
        if obj.Image:
            return format_html('<img src="{}" width="100" height="100" />', obj.Image.url)
        return "-"
    get_image.short_description = 'Image'

@admin.register(BookTable)
class BookTableAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Phone_number', 'Email', 'Total_person', 'Booking_date')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'email', 'phone', 'total_amount', 'created_at', 'get_items_images', 'status')
    list_filter = ('created_at', 'user', 'status')
    list_editable = ('status',)
    readonly_fields = ('user', 'name', 'email')  # cannot overwrite these in admin

    def get_items_images(self, obj):
        items = obj.food_items.all()
        if not items:
            return "-"
        html = '<div style="display:flex; overflow-x:auto;">'
        for item in items:
            if item.Image:
                html += f'<img src="{item.Image.url}" width="90" height="80" style="margin:2px; border-radius:6px;" title="{item.Item_name}" />'
        html += '</div>'
        return format_html(html)

    get_items_images.short_description = 'Ordered Items'


