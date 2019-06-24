from sqlalchemy import __version__, create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker
print("Версия SQLAlchemy:", __version__) # посмотреть версию SQLALchemy

######################Создание подключений к БД##############################
engine = create_engine('sqlite:///:memory:', echo=True)

# Создание подключения к локальной базе данных PostgreSQL
engine_1 = create_engine('postgresql+psycopg2://username:password@localhost:5432/mydb')

# Создание подключения к удаленной базе данных MySQL
#engine_2 = create_engine('mysql+pymysql://cookiemonster:chocolatechip@mysql01.monster.internal/cookies', pool_recycle=3600)

print(engine)
print(engine_1)

#########################Создание таблиц###########################
metadata = MetaData()
users_table = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('fullname', String),
    Column('password', String)
)

metadata.create_all(engine)

###############Определение класса Python для отображения в таблицу#############
class User:
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

#########################Настройка отображения##############################
mapper(User, users_table)                    # Создание отображения
user = User("Вася", "Василий", "qweasdzxc")
print(user)                                  # <User('Вася', 'Василий', 'qweasdzxc'>
print(user.id)                               # None

############################Создание сессии###############################
Session = sessionmaker(bind=engine)

session = Session()

#Session = sessionmaker()
#Session.configure(bind=engine)  # Как только у вас появится engine

#####################Добавление новых объектов########################
#vasiaUser = User("vasia", "Vasiliy Pypkin", "vasia2000")
session.add(user)
session.commit()
print(user.id)



