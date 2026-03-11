from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("health", "0005_remove_contact_surname"),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                CREATE TABLE IF NOT EXISTS health_contact (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    name VARCHAR(100) NOT NULL,
                    email VARCHAR(100) NOT NULL,
                    subject VARCHAR(200) NOT NULL,
                    message TEXT NOT NULL
                );
            """,
            reverse_sql="DROP TABLE IF EXISTS health_contact;",
        ),
    ]
