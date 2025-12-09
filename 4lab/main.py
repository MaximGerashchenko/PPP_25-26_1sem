
# вариант 5 

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} <{self.email}>"


def parse_csv(line):
    data = line[4:]
    parts = data.split(";")
    if len(parts) != 3:
        raise ValueError("csv формат: csv id;ФИО;email")
    name = parts[1].strip()
    email = parts[2].strip()
    return User(name, email)


def parse_raw(line):
    data = line[4:]
    parts = data.split()
    if len(parts) < 3:
        raise ValueError("raw формат: raw ФИО email")
    *name_parts, email = parts
    name = " ".join(name_parts)
    return User(name, email)


def is_valid_email(email):
    return "@" in email and "." in email


def read_users():
    users = []
    print("Введите строки (пустая строка — конец):")
    while True:
        line = input().strip()
        if line == "":
            break
        try:
            if line.startswith("csv "):
                u = parse_csv(line)
            elif line.startswith("raw "):
                u = parse_raw(line)
            else:
                print("Неизвестный формат, нужно csv или raw")
                continue
            users.append(u)
        except Exception as e:
            print("Ошибка:", e)
    return users


def main():
    users = read_users()
    print("Команда: emails или invalid")
    cmd = input().strip()

    if cmd == "emails":
        for u in users:
            print(u.email)
    elif cmd == "invalid":
        for u in users:
            if not is_valid_email(u.email):
                print(u)
    else:
        print("Неизвестная команда")


if __name__ == "__main__":
    main()
