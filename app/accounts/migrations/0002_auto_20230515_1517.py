# Generated by Django 3.2 on 2023-05-15 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='fullname',
            new_name='name',
        ),
        migrations.AddField(
            model_name='myuser',
            name='surname',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
