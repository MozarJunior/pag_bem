from django.contrib import admin
from .models import Cliente, Estabelecimento, EstabelecimentoCliente, Plano, PlanoControle, Admin
# Register your models here.

admin.site.register(Admin)
admin.site.register(Cliente)
admin.site.register(Estabelecimento)
admin.site.register(EstabelecimentoCliente)
admin.site.register(Plano)
admin.site.register(PlanoControle)