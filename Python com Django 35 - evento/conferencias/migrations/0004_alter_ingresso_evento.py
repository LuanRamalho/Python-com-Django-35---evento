# Generated by Django 5.1.2 on 2025-02-24 19:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferencias', '0003_participante_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingresso',
            name='evento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingressos', to='conferencias.evento'),
        ),
    ]
