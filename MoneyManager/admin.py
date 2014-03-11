from django.contrib import admin
from MoneyManager.models import Category,SubCategory,Owner,Creditcard

class SubCategoryInline(admin.TabularInline):
    model = SubCategory
    extra = 1

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category', {'fields': ['name']}),
    ]
    inlines = [SubCategoryInline]

admin.site.register(Category, CategoryAdmin)


class CreditcardInline(admin.TabularInline):
    model = Creditcard
    extra = 1

class OwnerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Owner', {'fields': ['name']}),
    ]
    inlines = [CreditcardInline]

admin.site.register(Owner, OwnerAdmin)

