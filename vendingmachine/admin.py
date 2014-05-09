from django.contrib import admin
from vendingmachine.models import Caliber
from vendingmachine.models import Bullet
from vendingmachine.models import Purpose
from vendingmachine.models import GoodFor

# Register your models here.
admin.site.register(Caliber)
admin.site.register(Bullet)
admin.site.register(Purpose)
admin.site.register(GoodFor)