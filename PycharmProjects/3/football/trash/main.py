import json
with open("player.json", "r") as wf:
    data = json.load(wf)

#print(data)

def red_card():
    i = 1
    for params in data["goal"]:
        #print(params["red_card"])
        if params["red_card"] != 0:
            print(f"[{i}]. Имя: {params['name']}, фамилия: {params['surname']}, дата рождения: {params['birthdate']}")
            i += 1


def best_score():
    sorted_obj = dict(wf)
    sorted_obj['predictions'] = sorted(wf['predictions'], key=lambda x: x['percentage'], reverse=True)




red_card()