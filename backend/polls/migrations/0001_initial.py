# Generated by Django 3.1.7 on 2021-04-29 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=20)),
                ('Desc_cat', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Gamme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=20)),
                ('Desc_gam', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=20)),
                ('Prix', models.IntegerField()),
                ('Desc_prod', models.CharField(max_length=100)),
                ('nbr_stock', models.IntegerField()),
                ('id_cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.categories')),
                ('id_ga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.gamme')),
            ],
        ),
    ]