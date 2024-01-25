import psycopg2

conn = psycopg2.connect(
    dbname="multiShop_db",
    user="postgres",
    password="123",
    host="127.0.0.1"
)

cur = conn.cursor()

registrationEL = input("Вы хотите зарегестрироваться, да \ нет?: ")

if registrationEL == "да":
    new_username = input("Заполните username: ")
    new_password_hash = input("Заполните password_hash: ")

    cur.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s);", (new_username, new_password_hash))
    print("Успешно зарегстрирован")
    conn.commit()

print("Авторизация пользователя, введите username и пароль.")
username = input("Введите username: ")
password_hash = input("Введите password_hash: ")

cur.execute("SELECT * FROM users WHERE username = %s AND password_hash = %s;", (username, password_hash))

rows = cur.fetchall()

if rows:
    print("Успешная аутентификация")
else:
    print("Неверные учетные данные")

cur.close()
conn.close()