def all_players_plus(data):
    for d in data:
        print(
            f"ФИО: {d['bio']['name']} {d['bio']['surname']}, дата рождения: {d['bio']['birthdate']}, номер игрока: {d['num']},\
            количество матчей: {d['match']}, количество голов: {d['goal']}, количество передач: {d['assist']},\
            количество жёлтых карточек: {d['yellow_card']}, количество красных карточек: {d['red_card']}, общий счёт: {d['score']} ")
    print(c)
