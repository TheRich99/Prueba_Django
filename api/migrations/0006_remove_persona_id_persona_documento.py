# Generated by Django 4.2.1 on 2023-06-02 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_persona_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='id',
        ),
        migrations.AddField(
            model_name='persona',
            name='documento',
            field=models.CharField(default='', max_length=20, primary_key=True, serialize=False),
        ),
    ]