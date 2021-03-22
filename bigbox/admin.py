from django.contrib import admin

# Register your models here.
from .models import Category, Reason, Activity, Box

class CategoryAdmin(admin.ModelAdmin):

    pass
admin.site.register(Category, CategoryAdmin)

class ReasonAdmin(admin.ModelAdmin):
    pass
admin.site.register(Reason, ReasonAdmin)

admin.site.register(Activity)

@admin.register(Box)
class BoxAdmin(admin.ModelAdmin):
    pass