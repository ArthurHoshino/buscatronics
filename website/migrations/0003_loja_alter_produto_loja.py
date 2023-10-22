# Generated by Django 4.2.6 on 2023-10-22 19:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_produto_loja'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='produto',
            name='loja',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.loja'),
        ),
    ]
