import psycopg2


def add_author(name, nickname, name_in_db, about='', phone=''):
    create_db()

    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="postgres")
    cursor = conn.cursor()
    conn.autocommit = True

    sql = f"INSERT INTO authors (name, nickname, name_in_db, about, phone) " \
          f"VALUES ('{name}', '{nickname}', '{name_in_db}', '{about}', '{phone}')"

    cursor.execute(sql)
    print(f"{nickname} добавлен")
    cursor.close()
    conn.close()

def all_authors():
    create_db()
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="postgres")
    cursor = conn.cursor()
    conn.autocommit = True

    sql = "SELECT name, nickname, name_in_db FROM authors"

    cursor.execute(sql)
    authors = cursor.fetchall()
    cursor.close()
    conn.close()
    return authors


def create_db():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="postgres")
    cursor = conn.cursor()
    conn.autocommit = True

    sql = 'CREATE TABLE IF NOT EXISTS authors (name VARCHAR, nickname VARCHAR, name_in_db VARCHAR, phone VARCHAR, about VARCHAR);'
    cursor.execute(sql)
    cursor.close()
    conn.close()


def check_db():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="postgres")
    cursor = conn.cursor()
    conn.autocommit = True

    cursor.execute("DROP TABLE authors;")

    create_db()
    refresh_db()

        cursor.close()
        conn.close()


def refresh_db():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="postgres", host="postgres")
    cursor = conn.cursor()
    conn.autocommit = True

    insert_data_sql = """
        INSERT INTO authors (name, nickname, name_in_db)
        VALUES (?, ?, ?)
    """

    authors_data = [
        ('Кирилл Мироненко', '@quir1ll', 'Кирилл'),
        ('Кирилл Моралес', '@kirill_morales', 'Моралес'),
        ('Саша Никитенко', '@isaywheee', 'Саша'),
        ('Артем Вайс', '@Vice_Mallow', 'Артем'),
        ('Екатерина Генералова', '@Catygen', 'Генералова'),
        ('Дина Скворцова', '@interneuronic', 'Дина'),
        ('Егор Бабин', '@baego', 'Егор'),
        ('Арсений Мирный', '@ArseniyMirniy', 'Арсений'),
        ('Вадим Макаренко', '@Mkarow', 'Вадим'),
        ('Ирина Гродзинская', '@Irina_Grodzinskaya', 'Ира'),
        ('Анна Османова', '@annacalico', 'Анна'),
        ('Шамиль Алиуллов', '@aliullov_sh', 'Шамиль'),
        ('Ана Бартенева', '@the_barteneva', 'Ана'),
        ('Борис Стародубцев', '@johnyscreams', 'Бо'),
        ('Вика Баранова', '@barvikki', 'Вика'),
        ('Сергей Рыбалко', '@pescadotravel', 'Сергей'),
        ('Алина Орлова', '@suspicious_fox', 'Алина'),
        ('Полина Нестерова', '@Rbhgb', 'Полина'),
        ('Ксения Седна', '@Sedn04ka', 'Седна'),
        ('Никита Баранов', '@Hurtson', 'Никита'),
        ('Дмитрий Корниенко', '@dimkor42', 'Дима')
    ]
    # insert_data_sql = '''
    #     INSERT INTO authors (name, nickname, name_in_db)
    #     VALUES
    #       ('Кирилл Мироненко', '@quir1ll', 'Кирилл'),
    #       ('Кирилл Моралес', '@kirill_morales', 'Моралес'),
    #       ('Саша Никитенко', '@isaywheee', 'Саша'),
    #       ('Артем Вайс', '@Vice_Mallow', 'Артем'),
    #       ('Екатерина Генералова', '@Catygen', 'Генералова'),
    #       ('Дина Скворцова', '@interneuronic', 'Дина'),
    #       ('Егор Бабин', '@baego', 'Егор'),
    #       ('Арсений Мирный', '@ArseniyMirniy', 'Арсений'),
    #       ('Вадим Макаренко', '@Mkarow', 'Вадим'),
    #       ('Ирина Гродзинская', '@Irina_Grodzinskaya', 'Ира'),
    #       ('Анна Османова', '@annacalico', 'Анна'),
    #       ('Шамиль Алиуллов', '@aliullov_sh', 'Шамиль'),
    #       ('Ана Бартенева', '@the_barteneva', 'Ана'),
    #       ('Борис Стародубцев', '@johnyscreams', 'Бо'),
    #       ('Вика Баранова', '@barvikki', 'Вика'),
    #       ('Сергей Рыбалко', '@pescadotravel', 'Сергей'),
    #       ('Алина Орлова', '@suspicious_fox', 'Алина'),
    #       ('Полина Нестерова', '@Rbhgb', 'Полина'),
    #       ('Ксения Седна', '@Sedn04ka', 'Седна'),
    #       ('Никита Баранов', '@Hurtson', 'Никита'),
    #       ('Дмитрий Корниенко', '@dimkor42', 'Дима');
    # '''

    cursor.executemany(insert_data_sql, authors_data)
    # cursor.execute(insert_data_sql)
    cursor.close()
    conn.close()

