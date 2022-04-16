from django.contrib import admin
from .models import Product, certificatsM,clientsM

# Register your models here.


admin.site.register(Product)

@admin.register(clientsM)
class clinetsAdmin(admin.ModelAdmin):
    list_display = ('id', 'logo', 'companyName')

@admin.register(certificatsM)
class certificatesAdmin(admin.ModelAdmin):
    list_display = ('id', 'certificateInfo','certificateimage','certificatePDF')
    

