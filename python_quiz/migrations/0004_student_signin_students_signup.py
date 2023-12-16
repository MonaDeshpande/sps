# Generated by Django 4.1.4 on 2023-12-15 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('python_quiz', '0003_alter_administrator_questions_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='student_signin',
            fields=[
                ('email_id', models.EmailField(blank=True, max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='students_signup',
            fields=[
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('student_id', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='administrator_login/')),
                ('email_id', models.EmailField(blank=True, max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('reenter_password', models.CharField(max_length=100)),
            ],
        ),
    ]