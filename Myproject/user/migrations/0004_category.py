# Generated by Django 3.2.4 on 2022-09-02 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_contectus_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('CPic', models.ImageField(default='', upload_to='static/category/')),
            ],
        ),
    ]
