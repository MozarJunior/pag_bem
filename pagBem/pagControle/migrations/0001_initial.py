# Generated by Django 4.2.5 on 2023-11-12 20:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('login', models.CharField(max_length=100, unique=True)),
                ('senha', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('login', models.CharField(max_length=20)),
                ('senha', models.CharField(max_length=20)),
                ('ativo', models.BooleanField()),
                ('criadoEm', models.DateTimeField(auto_now_add=True)),
                ('atualizadoEm', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estabelecimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Plano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('valor', models.FloatField()),
                ('duracaoDias', models.IntegerField()),
                ('frequencia', models.IntegerField()),
                ('estabelecimento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pagControle.estabelecimento')),
            ],
        ),
        migrations.CreateModel(
            name='PlanoControle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingresso', models.DateTimeField(auto_now_add=True)),
                ('vencimento', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pagControle.cliente')),
                ('plano', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pagControle.plano')),
            ],
        ),
        migrations.CreateModel(
            name='EstabelecimentoCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingresso', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pagControle.cliente')),
                ('estabelecimento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pagControle.estabelecimento')),
            ],
        ),
    ]
