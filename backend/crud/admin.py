from django.contrib import admin

from .models import Contas
  
# create a class for the admin-model integration
class ContasAdmin(admin.ModelAdmin):
  
    # add the fields of the model here
    list_display = ('id', 'fornecedor','vencimento_data','pago', 'notas')
  
# we will need to register the
# model class and the Admin model class
# using the register() method
# of admin.site class
admin.site.register(Contas,ContasAdmin)