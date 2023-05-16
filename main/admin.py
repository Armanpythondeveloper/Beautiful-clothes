from django.contrib import admin

# Register your models here.
from .models import (AboutHeader,AboutSection,OurTeam,
                     AboutIconca,AboutPartners,Products,JarangProd,
                     Like,ContactHeader,Contact,ContactInfo,
                     ContactAside,ContactTitles,ProductTitle,
                     IndexHeader,HomeNews,
                                                      )

@admin.register(AboutHeader)

class AboutHeaderAdmin(admin.ModelAdmin):

    list_display = ['name_1']
    list_display_links = ['name_1']
    search_fields = ['name_1']


admin.site.register(AboutSection)
admin.site.register(OurTeam)
admin.site.register(AboutIconca)
admin.site.register(AboutPartners)
admin.site.register(Products)
admin.site.register(JarangProd)
admin.site.register(Like)
admin.site.register(ContactHeader)
admin.site.register(Contact)
admin.site.register(ContactInfo)
admin.site.register(ContactAside)
admin.site.register(ContactTitles)
admin.site.register(ProductTitle)
admin.site.register(IndexHeader)
admin.site.register(HomeNews)