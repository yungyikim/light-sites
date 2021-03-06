# Generated by Django 2.2.7 on 2019-11-10 16:12

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
                ('subject', models.CharField(help_text='게시물 제목', max_length=70)),
                ('description', models.TextField(null=True)),
                ('content', models.TextField(help_text='HTML형태의 게시물 내용', null=True)),
                ('create_date', models.DateTimeField(db_index=True)),
                ('modified_date', models.DateTimeField()),
            ],
            options={
                'ordering': ('id',),
            },
        ),
    ]
