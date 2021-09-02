# Generated by Django 3.2.5 on 2021-09-01 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0005_alter_question_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='company',
            field=models.CharField(choices=[('HUP', 'HUP TELECOM'), ('VNT', 'VOANET TELECOM'), ('DGT', 'DIGITAL TELECOM')], max_length=255, null=True, verbose_name='Empresa'),
        ),
    ]
