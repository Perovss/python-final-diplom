# Generated by Django 4.0.4 on 2022-05-18 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_contact'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('email',), 'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
