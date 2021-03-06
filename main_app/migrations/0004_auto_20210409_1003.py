# Generated by Django 3.1.6 on 2021-04-09 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_driven'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='driven',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='driven',
            name='date',
            field=models.DateField(verbose_name='driven date'),
        ),
        migrations.AddField(
            model_name='car',
            name='mods',
            field=models.ManyToManyField(to='main_app.Mod'),
        ),
    ]
