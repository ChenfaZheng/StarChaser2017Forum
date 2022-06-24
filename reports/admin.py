from django.contrib import admin
from .models import Report, Review


class ReviewInline(admin.TabularInline):
    model = Review


class ReportAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline, 
    ]
    list_display = (
        "title", 
        "reporter", 
        "uploader", 
        "note", 
    )


admin.site.register(Report, ReportAdmin)