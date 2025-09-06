from django.contrib import admin
from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):  
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "payment_method", "total", "is_paid", "is_completed", "created_at")
    list_filter = ("payment_method", "is_paid", "is_completed", "created_at")
    search_fields = ("user__username", "user__email", "id")
    inlines = [OrderItemInline]  # show items inside the order

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ("order", "product", "quantity", "price")
    search_fields = ("product__name", "order__id")
