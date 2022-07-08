# Generated by Django 4.0.6 on 2022-07-08 02:29

from django.db import migrations
import wagtail.blocks
import wagtail.documents.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20220218_0034'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='externalRaws',
            field=wagtail.fields.StreamField([('external', wagtail.blocks.StructBlock([('document', wagtail.documents.blocks.DocumentChooserBlock(required=False)), ('rawHTML', wagtail.blocks.RawHTMLBlock(required=False)), ('rawImportScriptCSSAndMeta', wagtail.blocks.RawHTMLBlock(help_text='https://www.npmjs.com/package/react-helmet#reference-guide', required=False))]))], blank=True, use_json_field=None),
        ),
    ]
