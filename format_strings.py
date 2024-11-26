# Задание:
# Напишите код, который форматирует строки для следующих сценариев.
# Укажите переменные, которые должны быть вставлены в каждую строку:

# Использование %:
team1_num = 5               # Мастера кода
team2_num = 6               # Волшебники данных
print("В команде Мастера кода участников: %s!" % team1_num)
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))


# Использование format():
score_1 = 40    # количество задач решённых командой 1
score_2 = 42    # количество задач решённых командой 2
print("Команда Волшебники данных решила задач: {}!".format(score_2))

team1_time = 1552.512
team2_time = 2153.31451
team_time = team1_time + team2_time
print("Волшебники данных решили задачи за: {}c!".format(team1_time))


# Использование f-строк:

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных'
else:
    challenge_result = 'Ничья!'


tasks_total = score_1 + score_2             # общее количество задач
time_avg = team_time / tasks_total          # время на решение одной задачи
print(f'Результат битвы: {challenge_result}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg:.1f} секунды на задачу!')







