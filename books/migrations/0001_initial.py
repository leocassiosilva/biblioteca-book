# Generated by Django 4.0.5 on 2022-06-03 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(db_column='id_books', primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=100)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('data_cadastro', models.DateField(auto_now_add=True, verbose_name='Data de cadastro')),
            ],
            options={
                'db_table': 'book',
                'managed': True,
            },
        ),
    ]
