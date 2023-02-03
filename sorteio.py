import random

players = [
    ('teta', 'T4'),
    ('gui', 'T3'),
    ('henrique', 'T2'),
    ('ed', 'T1'),
    ('cabron', 'T4'),
    ('thalis', 'T3'),
    ('jeff', 'T2'),
    ('pastor', 'T4'),
    ('gabigol', 'T3'),
    ('leite', 'T2'),
    ('arthur', 'T4'),
    ('felipe', 'T3'),
    ('tutu', 'T2'),
    ('karly', 'T4'),
    ('will', 'T2'),
]

random.shuffle(players)

team1 = []
team2 = []
t1_team1 = 0
t2_team1 = 0
t1_team2 = 0
t2_team2 = 0

waiting_list = []

for player in players:
    if len(team1) == 5 and len(team2) == 5:
        waiting_list.append(player)
        continue
    elif len(team1) <= len(team2):
        if player[1] == 'T1' and t1_team1 >= 1:
            waiting_list.append(player)
            continue
        if player[1] == 'T1':
            t1_team1 += 1
            team1.append(player)
            if t1_team1 + t1_team2 == 2:
                for i in range(2):
                    team2.append(('jogadorT2', 'T2'))
        elif player[1] == 'T2' and t2_team1 >= 2:
            waiting_list.append(player)
            continue
        elif player[1] == 'T2':
            t2_team1 += 1
            team1.append(player)
        else:
            team1.append(player)
    elif len(team2) <= len(team1):
        if player[1] == 'T1' and t1_team2 >= 1:
            waiting_list.append(player)
            continue
        if player[1] == 'T1':
            t1_team2 += 1
            team2.append(player)
            if t1_team1 + t1_team2 == 2:
                for i in range(2):
                    team1.append(('jogadorT2', 'T2'))
        elif player[1] == 'T2' and t2_team2 >= 2:
            waiting_list.append(player)
            continue
        elif player[1] == 'T2':
            t2_team2 += 1
            team2.append(player)
        else:
            team2.append(player)

print('Time 1:')
for player in team1:
    print(player[0], '-', player[1])

print('\nTime 2:')
for player in team2:
    print(player[0], '-', player[1])

print('\nPra próxima:')
for player in waiting_list:
    print(player[0], '-', player[1])