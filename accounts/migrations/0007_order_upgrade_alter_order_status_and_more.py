# Generated by Django 4.1.3 on 2022-12-05 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20191213_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='upgrade',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('A+', 'A+'), ('A', 'A'), ('B', 'B')], max_length=200, null=True),
        ),
    ]
