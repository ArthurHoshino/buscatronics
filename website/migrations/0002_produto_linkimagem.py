# Generated by Django 4.2.6 on 2023-11-02 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='linkImagem',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
