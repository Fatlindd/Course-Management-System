# Generated by Django 4.0.10 on 2023-04-26 09:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher', to='courses.course')),
            ],
            options={
                'db_table': 'Teacher',
            },
        ),
    ]