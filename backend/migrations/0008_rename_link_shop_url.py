# Generated by Django 4.0.4 on 2022-05-19 23:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_alter_orderitem_options_remove_shop_url_shop_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='link',
            new_name='url',
        ),
    ]
