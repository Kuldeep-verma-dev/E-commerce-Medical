# Generated by Django 3.2.4 on 2023-05-31 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_healthnote'),
    ]

    operations = [
        migrations.AddField(
            model_name='healthnote',
            name='note',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='healthnote',
            name='name',
            field=models.CharField(max_length=70),
        ),
    ]