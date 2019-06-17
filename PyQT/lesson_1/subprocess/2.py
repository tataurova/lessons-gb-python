from subprocess import call, Popen, PIPE

# stdout=PIPE - стандартный поток вывода
# Popen поддерживает менеджеры контекста
with Popen("dir", shell=True, stdout=PIPE) as p:
    out = p.stdout.read().decode('cp866')
    print(out)

# запускаем приложение
# и ждем, пока оно не будет закрыто
# (а Popen не ждет)
# проверяем код возврата
returncode = call("regedit.exe")
if returncode == 0:
    print("Все хорошо!")
else:
    print("Ошибка!")

