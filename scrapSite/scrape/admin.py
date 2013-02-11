from django.contrib import admin
from scrape.models import scraper

class scraperAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['weighted_avg']}),
        ('Date information', {'fields': ['spot_date','hour'], 'classes': ['collapse']}),
    ]
    
admin.site.register(scraper,scraperAdmin)
