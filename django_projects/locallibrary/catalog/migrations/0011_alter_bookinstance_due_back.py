# Generated by Django 3.2.1 on 2023-02-19 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_bookinstance_due_back'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='due_back',
            field=models.DateField(blank=True, null=True),
        ),
    ]