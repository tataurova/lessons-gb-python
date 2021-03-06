date = str(input('Введите дату в формате dd.mm.yyyy: '))

date_list = date.split('.')

months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
          'июля',
          'августа', 'сентября', 'октября', 'ноября', 'декабря']

days_units = ['первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое',
              'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое',
              'семнадцатое',
              'восемнадцатое', 'девятнадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе', 'двадцать третье',
              'двадцать четвертое', 'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое',
              'двадцать девятое', 'тридцатое', 'тридцать первое']

day_new_format = days_units[int(date_list[0]) - 1]
month_new_format = months[int(date_list[1]) - 1]
year_new_format = date_list[2]

print('{} {} {} года'.format(day_new_format, month_new_format, year_new_format))
