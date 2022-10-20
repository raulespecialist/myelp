from django.contrib import admin
from .models import Business, Review


# A class that displays Reviews in a table form
class ReviewInline(admin.TabularInline):
    model = Review

    # Don't add any extra blank form for new Reviews
    extra = 0


# A class that lets us customize the Business list
class BusinessAdmin(admin.ModelAdmin):
    # Embed reviews in related businesses
    inlines = [ReviewInline]

    # Show the below properties in the Business list
    list_display = ('name', 'city', 'stars', 'categories')

    # Add filters for state and stars
    list_filter = ['stars', 'state']

    # Make the Business list searchable by name
    search_fields = ['name']

    # We don't want ids showing up
    exclude = ('id',)


admin.site.register(Business, BusinessAdmin)