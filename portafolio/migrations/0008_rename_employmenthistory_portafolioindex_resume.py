# Generated by Django 3.2.12 on 2022-02-11 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0007_alter_portafolioindex_employmenthistory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='portafolioindex',
            old_name='employmentHistory',
            new_name='resume',
        ),
    ]
