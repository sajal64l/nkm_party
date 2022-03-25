from django.contrib import admin
from .models import History, Member, Gallery, Speech, FAQ, Facebook
from parler.admin import TranslatableAdmin

admin.site.register(Member)
admin.site.register(Facebook)
admin.site.register(FAQ, TranslatableAdmin)
admin.site.register(Gallery)
admin.site.register(Speech, TranslatableAdmin)
admin.site.register(History, TranslatableAdmin)
