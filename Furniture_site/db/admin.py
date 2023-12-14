from django.contrib import admin
from .models import Articles, Clients, Deposites, DepositsRegistration, ExchangeRates, Persons
# Register your models here.
admin.site.register(Articles)
admin.site.register(Persons)
admin.site.register(Deposites)
admin.site.register(ExchangeRates)
admin.site.register(Clients)
admin.site.register(DepositsRegistration)