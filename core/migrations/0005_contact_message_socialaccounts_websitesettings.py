# Generated by Django 3.0.6 on 2020-05-20 02:39

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200520_0603'),
    ]

    operations = [
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
            name='WebsiteSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('copyright_link', models.URLField(verbose_name='Link on copyright')),
                ('about_me_content', ckeditor.fields.RichTextField(verbose_name='Content on About me section')),
                ('google_map_API_key', models.CharField(blank=True, max_length=255, verbose_name='Google Map API Key')),
                ('google_map_location_id', models.CharField(blank=True, max_length=255, verbose_name='Google Map Location ID')),
            ],
        ),
        migrations.CreateModel(
            name='SocialAccounts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('ordering', models.PositiveIntegerField(default=1, verbose_name='Ordering')),
                ('a_tag_class', models.CharField(help_text='Example: facebook', max_length=255, verbose_name='A tag class name')),
                ('i_tag_class', models.CharField(help_text='Example: bx bxl-facebook', max_length=255, verbose_name='I tag class name')),
                ('target_blank', models.BooleanField(default=False, help_text='Opens the linked document / page in a new tab', verbose_name='Target blank function')),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.WebsiteSettings')),
            ],
            options={
                'verbose_name': 'Social Account',
                'verbose_name_plural': 'Social Accounts',
                'ordering': ('ordering',),
            },
        ),
    ]