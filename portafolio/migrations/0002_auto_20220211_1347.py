# Generated by Django 3.2.12 on 2022-02-11 17:47

from django.db import migrations, models
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portafolioindex',
            name='employmentHistory',
            field=wagtail.core.fields.StreamField([('jobTitle', wagtail.core.blocks.RichTextBlock(blank=True)), ('employer', wagtail.core.blocks.RichTextBlock(blank=True)), ('city', wagtail.core.blocks.RichTextBlock(blank=True)), ('description', wagtail.core.blocks.RichTextBlock(blank=True)), ('initDate', wagtail.core.blocks.RichTextBlock(blank=True)), ('endDate', wagtail.core.blocks.RichTextBlock(blank=True))], blank=True),
        ),
        migrations.AlterField(
            model_name='portafolioindex',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='portafolioindex',
            name='phone',
            field=models.TextField(blank=True),
        ),
    ]
