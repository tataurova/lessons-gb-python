import pickle

# открываем фалй

with open('person.dat', 'rb') as f:
    # читаем объект
    person = pickle.load(f)

print(person)