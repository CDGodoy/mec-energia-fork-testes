# Generated by Django 4.1 on 2022-11-06 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('universities', '0004_merge_20221025_0920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distributor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('cnpj', models.CharField(help_text='14 números sem caracteres especiais', max_length=14, unique=True, verbose_name='CNPJ')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='universities.university')),
            ],
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('peak_tusd_in_reais_per_kw', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('peak_tusd_in_reais_per_mwh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('peak_te_in_reais_per_mwh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('off_peak_tusd_in_reais_per_kw', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('off_peak_tusd_in_reais_per_mwh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('off_peak_te_in_reais_per_mwh', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('na_tusd_in_reais_per_kw', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('distributor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tariffs.distributor')),
            ],
        ),
    ]