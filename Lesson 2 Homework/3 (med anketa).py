weight_too_low_msg = '{} {}, возраст {}, вес {}: Недостаточная масса тела. Следует записаться на прием'
weight_too_high_msg = '{} {}, возраст {}, вес {}: Ожирение. Следует записаться на прием'
weight_normal_msg = '{} {}, возраст {}, вес {}: Вес в норме'

print('Здравствуйте. Пройдите опрос:')
age = int(input('Возраст '))

if age < 18:
    print('Запишитесь в детское отделение')
else:
    name = str(input('Имя '))
    surname = str(input('Фамилия '))
    weight = int(input('Вес '))
    height = int(input('Рост в сантиметрах '))

# расчет состояния здоровья исходя из ИМТ (индекса массы тела):

    IMT = weight / ((height * 0.01) ** 2)
    if IMT < 18.5:
        print(weight_too_low_msg.format(name, surname, age, weight))
    if 18.5 <= IMT <= 25:
        print(weight_normal_msg.format(name, surname, age, weight))
    if IMT > 25:
        print(weight_too_high_msg.format(name, surname, age, weight))

# расчет состояния здоровья из задания:

    if age >= 30:
        if weight < 50 or weight > 120:
            print('Пациенту требуется заняться собой')
        else:
            print('Пациент в хорошем состоянии')
    if age < 30:
        if weight < 50 or weight > 120:
            print('Пациенту требуется заняться собой')
        else:
            print('Пациент в хорошем состоянии')

# на экран выводится 2 заключения о состоянии здоровья.
