import pandas
dafr = pandas.read_csv('C:/Users/Tony/PycharmProjects/TeachMeSkills/titanic.csv')

# 1. Распечатайте колонки которые есть датафрейме.

print(dafr.columns)

# 2. Узнайте сколько людей было на борту

print(dafr.shape[0])

# 3. Узнайте сколько на борту было мужчин.

print(dafr[dafr['Sex'] == 'male'].shape[0])

# 4. Посчитайте процент выживших на борту.

print(dafr[dafr['Survived'] == 1].shape[0]/dafr.shape[0]*100)

# 5. Кого было больше на борту, мужчин или женщин ?

def mof():
    a = dafr[dafr['Sex'] == 'male'].shape[0]
    b = dafr[dafr['Sex'] == 'female'].shape[0]
    if a > b:
        return 'Male'
    else:
        return 'Female'

print(mof())

# 6. Посчитайте сколько процентов из выживших были мужчинами?

print(dafr[(dafr['Survived'] == 1) & (dafr['Sex'] == 'male')].shape[0]/
      dafr[dafr['Survived'] == 1].shape[0]*100)

# 7. Человек какого класса вероятнее всего не выжил ?

def dead():
    a = dafr[(dafr['Survived'] == 0) & (dafr['Pclass'] == 1)].shape[0]
    b = dafr[(dafr['Survived'] == 0) & (dafr['Pclass'] == 2)].shape[0]
    c = dafr[(dafr['Survived'] == 0) & (dafr['Pclass'] == 3)].shape[0]
    d = min(a, b, c)
    if d == a:
        return '1'
    elif d == b:
        return '2'
    else:
        return '3'

print(dead())