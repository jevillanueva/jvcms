# Generated by Django 4.0.6 on 2022-07-08 04:40

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_blogpage_externalraws'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='externalRaws',
            field=wagtail.fields.StreamField([('external', wagtail.blocks.StructBlock([('rawHTML', wagtail.blocks.RawHTMLBlock(required=False)), ('rawImportScriptCSSAndMeta', wagtail.blocks.RawHTMLBlock(help_text='https://www.npmjs.com/package/react-helmet#reference-guide', required=False)), ('rawScripts', wagtail.blocks.RawHTMLBlock(required=False)), ('rawHTMLExtra', wagtail.blocks.RawHTMLBlock(required=False))]))], blank=True, use_json_field=None),
        ),
    ]
