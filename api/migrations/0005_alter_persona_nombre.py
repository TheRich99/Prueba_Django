# Generated by Django 4.2.1 on 2023-06-02 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_persona_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]