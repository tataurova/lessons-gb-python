def hello_max():
    print('Hello', 'Max')


hello_max()


def hello(who):
    print('Hello', who)


hello('Leo')


def greeting(who, say='Hello'):
    print(say, who)


greeting('Leo', 'Hi')
greeting('Max', 'hello')
greeting(who='Max', say='hello')

greeting('Kate')

greeting('Ola', 'privet')


def greeting2(say, *args):
    print(say, args)


greeting2('Hello', 'Artem')

greeting2('Hello', 'Artem', 'Ola')


def get_person(**kwargs):
    for k, v in kwargs.items():
        print(k, v)


get_person(name='Leo', age=20, has_car=True)





