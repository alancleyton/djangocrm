# Generated by Django 5.0.6 on 2024-06-20 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_customer_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]