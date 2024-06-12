# Generated by Django 4.2.13 on 2024-06-08 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.CharField(choices=[('abap', 'ABAP'), ('abnf', 'ABNF'), ('ada', 'Ada'), ('adl', 'ADL'), ('agda', 'Agda'), ('python', 'Python')], default='python', max_length=100),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='style',
            field=models.CharField(choices=[('algol', 'algol'), ('algol_nu', 'algol_nu'), ('friendly', 'friendly')], default='friendly', max_length=100),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='title',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
