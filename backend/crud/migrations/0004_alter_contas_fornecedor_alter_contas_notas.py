# Generated by Django 4.1.2 on 2022-10-06 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0003_alter_fornecedores_cnpj_alter_notas_numero_nota'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contas',
            name='fornecedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.fornecedores'),
        ),
        migrations.AlterField(
            model_name='contas',
            name='notas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='crud.notas'),
        ),
    ]
