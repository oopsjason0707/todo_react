# Generated by Django 3.1.1 on 2020-09-24 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FavoriteLanguageGroup',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('reg_date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LanguageGroup',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('del_yn', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=10)),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('end_date', models.DateField(blank=True)),
                ('del_yn', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bucketList.languagegroup')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteLanguage',
            fields=[
                ('seq', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=100)),
                ('memo', models.TextField()),
                ('reg_date', models.DateField(auto_now_add=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bucketList.favoritelanguagegroup')),
            ],
        ),
    ]