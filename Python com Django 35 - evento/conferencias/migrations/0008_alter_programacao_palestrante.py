# Generated by Django 5.1.2 on 2025-02-24 19:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferencias', '0007_alter_programacao_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programacao',
            name='palestrante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='programacoes', to='conferencias.palestrante'),
        ),
    ]
