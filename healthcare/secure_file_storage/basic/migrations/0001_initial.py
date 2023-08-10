# Generated by Django 3.2.8 on 2021-10-25 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=130)),
                ('password', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=230)),
                ('phone', models.CharField(max_length=15)),
                ('department', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=130)),
                ('password', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('age', models.CharField(default=None, max_length=100)),
                ('key', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PatientRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('file', models.CharField(max_length=200)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.doctor')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.patient')),
            ],
        ),
    ]
