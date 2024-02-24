import psycopg2
from config_data import config

dbname = config.DB_NAME
user = config.DB_USER
password = config.DB_PASSWORD
host = config.DB_HOST


def connect_to_db():
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)
    cursor = conn.cursor()
    conn.autocommit = True
    return conn, cursor

def close_db_connection(conn, cursor):
    cursor.close()
    conn.close()


def add_author(name, nickname, name_in_db, about='', phone=''):
    conn, cursor = connect_to_db()

    sql = f"INSERT INTO public.authors (name, nickname, name_in_db, about, phone) " \
          f"VALUES ('{name}', '{nickname}', '{name_in_db}', '{about}', '{phone}')"

    cursor.execute(sql)
    print(f"{nickname} добавлен")

    close_db_connection(conn, cursor)

def all_authors():
    conn, cursor = connect_to_db()

    sql = "SELECT name, nickname, name_in_db FROM public.authors"

    cursor.execute(sql)
    authors = cursor.fetchall()

    close_db_connection(conn, cursor)
    return authors

def create_db():
    conn, cursor = connect_to_db()

    sql = 'CREATE TABLE IF NOT EXISTS public.authors (name VARCHAR, nickname VARCHAR, name_in_db VARCHAR, phone VARCHAR, about VARCHAR);'
    cursor.execute(sql)
    close_db_connection(conn, cursor)

def refresh_db():
    conn, cursor = connect_to_db()

    try:
        cursor.execute("DROP TABLE public.authors;")
    except:
        pass

    create_db()

    insert_data_sql = """
        INSERT INTO public.authors (name, nickname, name_in_db)
        VALUES (%s, %s, %s)
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
        ('Дмитрий Корниенко', '@dimkor42', 'Дима'),
        ('Дарья', '@drrmmn', 'Дарья'),
    ]

    cursor.executemany(insert_data_sql, authors_data)
    close_db_connection(conn, cursor)
