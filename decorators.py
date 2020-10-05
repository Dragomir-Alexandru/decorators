import datetime
import time

def time_informations(function):
    def wrapper():
        start =str(datetime.datetime.now())
        start_timer = time.perf_counter()
        function()
        end_timer = time.perf_counter()
        durata = (end_timer - start_timer)
        end = str(datetime.datetime.now())
        return print(f'Start={start[11:16]}\nEnd={end[11:16]}\nDuration={durata} seconds')
    return wrapper



def jurnal_activitate(function):
    def wrapper():
        try:
            log = open(f'Activity_log_{function.__name__}.txt', 'x')
            log.close()
        except:
            pass
        start = str(datetime.datetime.now())
        function()
        end = str(datetime.datetime.now())
        log = open(f'Activity_log_{function.__name__}.txt', 'a')
        log.write(f'\nStart={start[11:16]}\nNume Functie={function.__name__}\nEnd={end[11:16]}\n')
        log.close()
        return print('Activity logged')
    return wrapper


@time_informations
def milion():
    for i in range(1,1000001):
        print(i)
    return 'Sa printat pana la 1.000.000'

@time_informations
def fisiere():
    for i in range(1,11):
        file = open(f'Fisier_{i}', 'w')
        for j in range(1,1000001):
            file.write(f'{j}\n')
        file.close()

@time_informations
def cinci_cuvinte():
    cuvinte = ['Alex', 'Alexandra', 'Bogdan', 'Sergiu', 'Abecedar']
    for i in cuvinte:
        time.sleep(5)
        print(i)

print(milion())
print(fisiere())
cinci_cuvinte()




@jurnal_activitate
def milion():
    for i in range(1,1000001):
        print(i)
    return 'Sa printat pana la 1.000.000'

@jurnal_activitate
def fisiere():
    for i in range(1,11):
        file = open(f'Fisier_{i}', 'w')
        for j in range(1,1000001):
            file.write(f'{j}\n')
        file.close()

@jurnal_activitate
def cinci_cuvinte():
    cuvinte = ['Alex', 'Alexandra', 'Bogdan', 'Sergiu', 'Abecedar']
    for i in cuvinte:
        time.sleep(5)
        print(i)

print(milion())
print(fisiere())
cinci_cuvinte()





