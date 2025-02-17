# Generated by Django 4.2.16 on 2024-11-18 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoanProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField()),
                ('loan_inci_expn', models.TextField()),
                ('erly_rpay_fee', models.TextField()),
                ('dly_rate', models.TextField()),
                ('loan_lmt', models.TextField()),
                ('dcls_strt_day', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='LoanOptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('mrtg_type_nm', models.TextField()),
                ('rpay_type_nm', models.TextField()),
                ('lend_rate_type_nm', models.TextField()),
                ('lend_rate_min', models.FloatField(null=True)),
                ('lend_rate_max', models.FloatField(null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.loanproducts')),
            ],
        ),
    ]
