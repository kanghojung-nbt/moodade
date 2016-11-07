from django.contrib import admin

from .models import  Stock,KaKAoMood,Keyboard


class StockAdmin(admin.ModelAdmin):
    list_display = ('ticker', 'open','close', 'volume')
class KaKaoAdmin(admin.ModelAdmin):
    list_display = ('mood', 'category')
class KeyboardAdmin(admin.ModelAdmin):
    list_display = ['button']

admin.site.register(Stock , StockAdmin)
admin.site.register(KaKAoMood , KaKaoAdmin)
admin.site.register(Keyboard , KeyboardAdmin)



