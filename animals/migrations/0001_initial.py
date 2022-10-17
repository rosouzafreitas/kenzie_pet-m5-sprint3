# Generated by Django 4.1.1 on 2022-10-17 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('traits', '0001_initial'),
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('weight', models.FloatField()),
                ('sex', models.CharField(choices=[('Macho', 'Male'), ('Fêmea', 'Female'), ('Não informado', 'Uninformed')], default='Não informado', max_length=15)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='animals', to='groups.group')),
                ('traits', models.ManyToManyField(related_name='traits', to='traits.trait')),
            ],
        ),
    ]