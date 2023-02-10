# Generated by Django 4.0.4 on 2022-04-28 06:23

import users.managers
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(help_text='Enter email address', max_length=254, unique=True, verbose_name='email address')),
                ('last_name', models.CharField(blank=True, max_length=40, verbose_name='last name')),
                ('first_name', models.CharField(blank=True, max_length=40, verbose_name='first name')),
                ('patronymic', models.CharField(blank=True, max_length=40, verbose_name='patronymic')),
                ('company', models.CharField(blank=True, help_text='Enter company name', max_length=40, verbose_name='company')),
                ('position', models.CharField(blank=True, help_text='Enter user position in company', max_length=40, verbose_name='position')),
                ('type', models.CharField(choices=[('shop', 'Shop'), ('buyer', 'Buyer')], default='buyer', max_length=10, verbose_name='user type')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_active', models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'List of users',
                'db_table': 'users',
                'ordering': ('email',),
            },
            managers=[
                ('objects', users.managers.UserManager()),
            ],
        ),
    ]
