# Generated by Django 3.0.6 on 2020-05-24 03:20

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Address', 'Address'), ('Email', 'Email'), ('Phone', 'Phone')], max_length=50, verbose_name='Contact type')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Contact_Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('subject', models.CharField(max_length=255, verbose_name='Subject')),
                ('message', models.TextField(verbose_name='Message')),
                ('sent_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Message sent date')),
                ('forwarded_to_email', models.BooleanField(default=False, verbose_name='Message has been forwarded to the email')),
            ],
            options={
                'verbose_name': 'Message sent by a visitor',
                'verbose_name_plural': 'Messages sent by visitors',
                'ordering': ('-sent_date',),
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('url', models.CharField(help_text='Example /about/ -page url', max_length=50, verbose_name='Url')),
                ('position', models.CharField(choices=[('1', 'Header'), ('2', 'Footer'), ('3', 'Both'), ('4', 'Useful Links')], help_text='1 => Header\n 2 => Footer \n 3 => Both \n 4 => Useful Links', max_length=50, verbose_name='Position')),
                ('ordering', models.PositiveIntegerField(default=1, verbose_name='Ordering')),
                ('target_blank', models.BooleanField(default=False, help_text='Opens the linked document / page in a new tab', verbose_name='Target blank function')),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
                'ordering': ('ordering',),
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('photo', models.ImageField(upload_to='', verbose_name='Photo')),
                ('photo_detail_page', models.ImageField(upload_to='', verbose_name='Photo on detail page')),
                ('url', models.URLField()),
                ('date', models.DateField(blank=True, verbose_name='Date')),
                ('ordering', models.PositiveIntegerField(default=1, verbose_name='Ordering')),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Portfolio',
                'verbose_name_plural': 'Portfolios',
                'ordering': ('ordering',),
            },
        ),
        migrations.CreateModel(
            name='Website_Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copyright_link', models.URLField(verbose_name='Link on copyright')),
                ('about_app_content', ckeditor.fields.RichTextField(blank=True, verbose_name='Content on About Application section')),
                ('about_me_content', ckeditor.fields.RichTextField(blank=True, verbose_name='Content on About me section')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='settings', verbose_name='Photo')),
                ('full_name', models.CharField(default='Bakir Yunusov', max_length=255, verbose_name='Full name')),
                ('position', models.CharField(default='Python Developer', max_length=255, verbose_name='Position')),
                ('notification_text', models.TextField(default='You have less 10 minutes left to finish your task.', verbose_name='Notification Text')),
                ('google_map_API_key', models.CharField(blank=True, max_length=255, verbose_name='Google Map API Key')),
                ('google_map_location_id', models.CharField(blank=True, max_length=255, verbose_name='Google Map Location ID')),
            ],
            options={
                'verbose_name': 'Website Settings',
                'verbose_name_plural': 'Website Settings',
            },
        ),
        migrations.CreateModel(
            name='Social_Accounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('ordering', models.PositiveIntegerField(default=1, verbose_name='Ordering')),
                ('a_tag_class', models.CharField(help_text='Example: facebook', max_length=255, verbose_name='A tag class name')),
                ('i_tag_class', models.CharField(help_text='Example: bx bxl-facebook', max_length=255, verbose_name='I tag class name')),
                ('i_tag_class_on_about_me', models.CharField(help_text='Example: icofont-facebook', max_length=255, verbose_name='I tag class name on About me section')),
                ('target_blank', models.BooleanField(default=False, help_text='Opens the linked document / page in a new tab', verbose_name='Target blank function')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Website_Settings')),
            ],
            options={
                'verbose_name': 'Social Account',
                'verbose_name_plural': 'Social Accounts',
                'ordering': ('ordering',),
            },
        ),
    ]
