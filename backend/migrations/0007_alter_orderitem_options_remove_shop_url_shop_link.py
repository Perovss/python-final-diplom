# Generated by Django 4.0.4 on 2022-05-19 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_order_alter_category_options_alter_parameter_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Order position', 'verbose_name_plural': 'Order positions'},
        ),
        migrations.RemoveField(
            model_name='shop',
            name='url',
        ),
        migrations.AddField(
            model_name='shop',
            name='link',
            field=models.URLField(blank=True, null=True, verbose_name='link'),
        ),
    ]
