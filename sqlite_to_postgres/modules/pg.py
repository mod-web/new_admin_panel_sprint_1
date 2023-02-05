from psycopg2.extras import execute_batch
from datetime import datetime


class PostgresSaver:
    def __init__(self, pg_conn):
        self.pg_conn = pg_conn

    def save_data(self, data: list, table: str, batch_size: int = 25):
        if table == 'film_work':
            with self.pg_conn.cursor() as cursor:
                cmd = 'INSERT INTO content.film_work ' \
                      '(id, title, created, modified, description, creation_date, rating, type) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING; '
                imp = [(d.id, d.title, d.created_at, datetime.now(), d.description,
                        d.creation_date, d.rating, d.type) for d in data]
                execute_batch(cursor, cmd, imp, page_size=batch_size)
                self.pg_conn.commit()
                self.pg_conn.close()

        if table == 'person':
            with self.pg_conn.cursor() as cursor:
                cmd = 'INSERT INTO content.person (id, full_name, created, modified) \
                       VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO NOTHING; '
                imp = [(d.id, d.full_name, d.created_at, datetime.now()) for d in data]
                execute_batch(cursor, cmd, imp, page_size=batch_size)
                self.pg_conn.commit()
                self.pg_conn.close()

        if table == 'genre':
            with self.pg_conn.cursor() as cursor:
                cmd = 'INSERT INTO content.genre (id, name, description, created, modified) \
                       VALUES (%s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING; '
                imp = [(d.id, d.name, d.description, d.created_at, datetime.now()) for d in data]
                execute_batch(cursor, cmd, imp, page_size=batch_size)
                self.pg_conn.commit()
                self.pg_conn.close()

        if table == 'genre_film_work':
            with self.pg_conn.cursor() as cursor:
                cmd = 'INSERT INTO content.genre_film_work (id, genre_id, film_work_id, created) \
                       VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO NOTHING; '
                imp = [(d.id, d.genre_id, d.film_work_id, datetime.now())
                       for d in data]
                execute_batch(cursor, cmd, imp, page_size=batch_size)
                self.pg_conn.commit()
                self.pg_conn.close()

        if table == 'person_film_work':
            with self.pg_conn.cursor() as cursor:
                cmd = 'INSERT INTO content.person_film_work (id, person_id, film_work_id, role, created) \
                       VALUES (%s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING; '
                imp = [(d.id, d.person_id, d.film_work_id, d.role, datetime.now()) for d in data]
                execute_batch(cursor, cmd, imp, page_size=batch_size)
                self.pg_conn.commit()
                self.pg_conn.close()
