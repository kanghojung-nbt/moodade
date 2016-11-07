from django.contrib import admin

from .models import  Stock,KaKAoMood


class StockAdmin(admin.ModelAdmin):
    list_display = ('ticker', 'open','close', 'volume')
class KaKaoAdmin(admin.ModelAdmin):
    list_display = ('mood', 'category')

admin.site.register(Stock , StockAdmin)
admin.site.register(KaKAoMood , KaKaoAdmin)



