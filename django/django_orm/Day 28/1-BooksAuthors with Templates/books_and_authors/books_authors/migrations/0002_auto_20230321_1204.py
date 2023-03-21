# Generated by Django 3.2.18 on 2023-03-21 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('books', models.ManyToManyField(related_name='authors', to='books_authors.Book')),
            ],
        ),
        migrations.DeleteModel(
            name='Auther',
        ),
    ]