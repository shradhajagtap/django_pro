# Generated by Django 5.0.3 on 2024-03-14 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20)),
                ('company_owner', models.CharField(max_length=20)),
                ('company_total_emp', models.IntegerField()),
                ('company_state', models.CharField(max_length=10)),
                ('city_pincode', models.IntegerField()),
                ('payment_mode', models.CharField(choices=[('OL', 'Online'), ('OFF', 'Offline')], max_length=20)),
                ('city_mode', models.CharField(choices=[('MUMBAI', 'Mumbai'), ('PUNE', 'Pune'), ('NASHIK', 'Nashik'), ('OBAD', 'Obad')], default='Pune', max_length=20)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
