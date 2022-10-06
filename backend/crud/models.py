from django.db import models

class Fornecedores(models.Model):
    id=models.UUIDField(primary_key=True)
    nome=models.CharField(max_length=150)
    cnpj=models.IntegerField()
    telefone=models.CharField(max_length=15)

    def __str__(self):
  
        return self.id

class Notas(models.Model):
    id=models.UUIDField(primary_key=True, editable=False, auto_created=True)
    numero_nota=models.IntegerField()
    fornecedor=models.ForeignKey('Fornecedores', on_delete=models.CASCADE,)
    emissao_data=models.DateField()
    nome_produto=models.CharField(max_length=150)
    categoria_produto=models.CharField(max_length=150)
    quantidade=models.DecimalField(decimal_places=2, max_digits=2)
    total=models.DecimalField(decimal_places=2, max_digits=2)
    
    def __str__(self):
  
        return self.id


class Contas(models.Model):
    id=models.UUIDField(primary_key=True, editable=False, auto_created=True)
    fornecedor=models.ForeignKey('Fornecedores', on_delete=models.CASCADE, blank=True, null=True)
    vencimento_data=models.DateField()
    pago=models.BooleanField(default=False)
    notas=models.ForeignKey('Notas', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
  
        return self.id