from faker import Faker
def names():
    faker = Faker()
    nombres = []
    apellidos = []
# Generar un nombre aleatorio
    for i in range(600):
        name = faker.name()
        nombres.append(name)
    
    
# Generar un apellido aleatorio
    for i in range (600):
        last_name = faker.last_name()
        apellidos.append(last_name)

    return nombres, apellidos


names()



