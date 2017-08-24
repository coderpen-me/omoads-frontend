from django.contrib import admin

# Register your models here.
from .models import Banner, Agency, BookingDetails,PricePeriod, Zone,BannerImage


class ImageInLine(admin.StackedInline):
	model = BannerImage
class BannerAdmin(admin.ModelAdmin):
	inlines = [ImageInLine, ]

admin.site.register(Banner, BannerAdmin)
admin.site.register(Agency)
admin.site.register(BookingDetails)
admin.site.register(PricePeriod)
admin.site.register(Zone)
admin.site.register(BannerImage)