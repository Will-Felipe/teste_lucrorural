from django.shortcuts import render

# import view sets from the REST framework
from rest_framework import viewsets
  
from .serializers import ContasSerializer
from .models import Contas

from .serializers import FornecedoresSerializer
from .models import Fornecedores
  
class ContasView(viewsets.ModelViewSet):
  
    # create a sereializer class and 
    # assign it to the ContasSerializer class
    serializer_class = ContasSerializer
  
    # define a variable and populate it 
    # with the Contas list objects
    queryset = Contas.objects.all()

class FornecedoresView(viewsets.ModelViewSet):
  
    # create a sereializer class and 
    # assign it to the ContasSerializer class
    serializer_class = FornecedoresSerializer
  
    # define a variable and populate it 
    # with the Contas list objects
    queryset = Fornecedores.objects.all()