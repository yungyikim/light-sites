# Generated by Django 2.2.6 on 2019-11-08 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('subject', models.CharField(help_text='게시물 제목', max_length=128)),
                ('content', models.TextField(help_text='HTML형태의 게시물 내용', null=True)),
                ('create_date', models.DateTimeField(db_index=True)),
                ('modified_date', models.DateTimeField()),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
