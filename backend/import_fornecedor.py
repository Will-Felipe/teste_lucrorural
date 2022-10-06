import os
import csv
import django

#Troque o "library" pelo nome do seu projeto
if __name__ == "__main__":
    try:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
        django.setup()
    except ImportError:
        raise ImportError(
            "Não foi possível importar o Django.\n"
            "Verifique se o seu virtual environment está ativado.\n"
            "Verifique se está no mesma pasta do projeto.\n"
            "Verifique se o nome do seu projeto está correto.\n"
        )

    #Importe os seus models
    from crud.models import Fornecedores
    
    #Apaga todos os registros
    Fornecedores.objects.all().delete()

    fornecedores = []
    with open('fornecedor.csv', encoding='utf8') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            fornecedor = Fornecedores(id=row['id'], nome=row['nome'], 
                        cnpj=row['cnpj'], telefone=row['telefone'])
            fornecedores.append(fornecedor)

    Fornecedores.objects.bulk_create(fornecedores)