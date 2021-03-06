from subprocess import call, Popen, PIPE

# выполнение простой системной команды
# эта функция позволяет вызвать другую программу,
# дождаться завершения команды и вернуть код возврата
# код 0 - все в порядке
# shell=True - выполнение кода через оболочку
ret = call("dir", shell=True)
print(ret)

# выполнение системной команды с сохранением вывода
# в отличие от метода call, Popen не дожидается конца
# выполнения вызванного процесса (он завершается, а запущенное приложение 'висит'),
# если вы не укажете это в методе wait.
p = Popen("dir", shell=True, stdout=PIPE)
# вывод результатов выполнения команды с декодированием
out = p.stdout.read().decode('cp866')
print(out)



