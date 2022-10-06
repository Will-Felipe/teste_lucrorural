# import sereliazers from the REST framework
from rest_framework import serializers
  
# import the todo data model
from .models import Contas

from .models import Fornecedores
  
# create a sereliazer class
class ContasSerializer(serializers.ModelSerializer):
  
    # create a meta class
    class Meta:
        model = Contas
        fields = ('id', 'fornecedor','vencimento_data','pago', 'notas')

class FornecedoresSerializer(serializers.ModelSerializer):
  
    # create a meta class
    class Meta:
        model = Fornecedores
        fields = ('id', 'nome','cnpj','telefone')