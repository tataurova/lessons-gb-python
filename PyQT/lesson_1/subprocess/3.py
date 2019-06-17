from subprocess import call, Popen, PIPE

'''
Здесь мы создали переменную под названием program и назначили ей значение notepad.exe. 
После этого мы передали её классу Popen. После запуска этого кода, вы увидите, 
что он мгновенно вернет объект subprocess.Popen, а вызванное приложение будет выполняться. 
'''

# сравните это
#program = "regedit.exe"
#process = Popen(program)
#code = process.wait()

#print(process)
#print(code)

# и это
program = "regedit.exe"
process = Popen(program)

print(process)
print(code)


