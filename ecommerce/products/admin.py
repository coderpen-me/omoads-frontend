from django.contrib import admin

# Register your models here.
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User




class ImageInLine(admin.StackedInline):
	model = BannerImage

class PricePeriodInline(admin.TabularInline):
    model = PricePeriod
    readonly_fields = ('startDate','endDate', 'price', 'numberDays')
    can_delete = False

class BookingDetailsInline(admin.TabularInline):
    readonly_fields = ('bookingDate','numberDays')
    model = BookingDetails
    def get_extra(self, request, obj=None, **kwargs):
        extra = 1
        return extra

class BannerAdmin(admin.ModelAdmin):
    inlines = [ImageInLine, PricePeriodInline, BookingDetailsInline, ]
    def get_fieldsets(self, request, obj=None):
        fields = list()
        if request.user.is_superuser:
            fields = ['agency','zone', 'banner_facing', 'banner_type', 'banner_lighted', 'banner_dimensions',
                     'banner_cost', 'banner_lattitude', 'banner_longitude', 'banner_landmark', 'banner_status', 'banner_bookingStatus']
            return [(None, {'fields': tuple(fields)})]
        else:
            fields = ['agency', 'banner_facing', 'banner_landmark','zone']
            self.readonly_fields = fields
            return [(None, {'fields': tuple(fields)})]
    


class ProfileInline(admin.StackedInline):
    model = ExtendedUser
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

class BannerInline(admin.TabularInline):
    fields = ('banner_facing', 'zone', 'banner_landmark', 'admin_edit_link')
    readonly_fields = fields
    model = Banner



class BookingAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email')
    inlines = [BannerInline]

admin.site.register(Agency, BookingAdmin)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)



admin.site.register(Banner, BannerAdmin)

admin.site.register(BookingDetails)
admin.site.register(PricePeriod)
admin.site.register(Zone)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Payments)
admin.site.register(ExtendedUser)
admin.site.register(Favourite)