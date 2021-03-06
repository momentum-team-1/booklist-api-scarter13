# Generated by Django 3.0.7 on 2020-06-27 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_book_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='status',
            field=models.CharField(choices=[('NTRD', 'Not Yet Read'), ('RDNG', 'Currently Reading'), ('READ', 'Finished Reading')], default='NTRD', max_length=4),
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('book', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='api.Book')),
            ],
        ),
    ]
