# Generated by Django 3.2.4 on 2021-10-14 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('website', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=50)),
                ('message', models.TextField(max_length=100)),
            ],
        ),
    ]