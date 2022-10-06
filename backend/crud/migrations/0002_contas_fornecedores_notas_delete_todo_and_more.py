# Generated by Django 4.1.1 on 2022-10-05 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vencimento_data', models.DateField()),
                ('pago', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Fornecedores',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=150)),
                ('cnpj', models.IntegerField(max_length=14)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Notas',
            fields=[
                ('id', models.UUIDField(auto_created=True, editable=False, primary_key=True, serialize=False)),
                ('numero_nota', models.IntegerField(max_length=150)),
                ('emissao_data', models.DateField()),
                ('nome_produto', models.CharField(max_length=150)),
                ('categoria_produto', models.CharField(max_length=150)),
                ('quantidade', models.DecimalField(decimal_places=2, max_digits=2)),
                ('total', models.DecimalField(decimal_places=2, max_digits=2)),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.fornecedores')),
            ],
        ),
        migrations.DeleteModel(
            name='Todo',
        ),
        migrations.AddField(
            model_name='contas',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.fornecedores'),
        ),
        migrations.AddField(
            model_name='contas',
            name='notas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crud.notas'),
        ),
    ]
