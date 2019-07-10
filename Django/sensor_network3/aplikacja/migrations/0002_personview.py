# Generated by Django 2.2.1 on 2019-07-10 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplikacja', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonView',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
            ],
            options={
                'db_table': 'aplikacja_person_view',
                'managed': False,
            },
        ),
        migrations.RunSQL(
            """
CREATE VIEW aplikacja_person_view AS
SELECT
row_number() OVER () AS id,
p.first_name,
p.last_name,
date("now") - date(p.birth_date) AS age
FROM aplikacja_person AS p;
            """
        )
    ]
