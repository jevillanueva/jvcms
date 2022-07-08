# Generated by Django 4.0.6 on 2022-07-08 06:32

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_alter_blogpage_externalraws'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='particle_param',
            field=wagtail.fields.StreamField([('param', wagtail.blocks.RawHTMLBlock(required=False))], blank=True, use_json_field=None),
        ),
    ]
