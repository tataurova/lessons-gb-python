from subprocess import Popen, PIPE

args = ["ping", "www.google.ru"]
process = Popen(args, stdout=PIPE)

# communicate - связь с созданным процессом
# None – это результат stderr, а это значит, что ошибок не найдено
data = process.communicate()
for line in data:
    print(line.decode("cp866"))

