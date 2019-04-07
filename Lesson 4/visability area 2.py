m = 'меня видно везде'


def a():
    ma = 'меня видно в b() и в a()'

    def b():
        print(m)
        print(ma)
        mb = 'меня видно в c() и b(), но не видно в a()'

        def c():
            print(a)
            print(ma)
            print(mb)
            mc = 'меня видно только в c()'
            print(mc)

        c()
    b()

a()
