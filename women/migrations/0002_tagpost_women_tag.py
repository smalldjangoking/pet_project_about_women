# Generated by Django 5.0 on 2023-12-19 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AddField(
            model_name='women',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tags', to='women.tagpost'),
        ),
    ]
