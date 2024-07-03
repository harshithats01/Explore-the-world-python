# Generated by Django 4.0.6 on 2022-11-11 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0004_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='services',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64, unique=True)),
                ('image', models.ImageField(upload_to='pics')),
                ('description', models.TextField(default='')),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
    ]
