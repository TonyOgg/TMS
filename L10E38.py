import pandas
idf = pandas.read_csv('C:/Users/Tony/PycharmProjects/TeachMeSkills/info.csv')
mdf = pandas.read_csv('C:/Users/Tony/PycharmProjects/TeachMeSkills/marks.csv')

# 1. Узнайте для скольких людей из датафрейма info неизвестны оценки.

alldf = idf.merge(mdf, left_on='id', right_on='id2')
print(idf.shape[0] - alldf.shape[0])

# 2. Узнайте для скольких людей из датафрейма marks неизвестны расса\пол\...

adf = mdf.merge(idf, left_on='id2', right_on='id', how='left')
rdf = adf[(adf['gender'] != 'female') & (adf['gender'] != 'male')]
print(rdf.shape[0])

# 3. Узнайте среднюю оценку по математике рассы "group A".

print(alldf['math'].mean())

#  4. Объедините датафреймы в один так чтобы в результирующем датафрейме были люди из обоих датафреймов info и marks.
# Для тех у кого нет оценок должны быть NaN на месте оценок. Для тех у кого нет информации о рассе\поле\образовании родителей на месте инфы должны быть NaN.

print(idf.merge(mdf, left_on='id', right_on='id2', how='outer'))

# 5. Объедините датафреймы в один так чтобы в результирующем датафрейме были все
# известные люди из датафрейма info. Для тех людей из info для которых нет оценок в
# marks, на месте оценок должны стоять NaN.

print(idf.merge(mdf, left_on='id', right_on='id2', how='left'))

# 6. Объедините датафреймы в один так чтобы в результирующем датафрейме были все
# известные люди из датафрейма marks. Для тех людей из marks для которых нет расс\пола\... в info, на месте расс\пола\... должны стоять NaN.

print(idf.merge(mdf, left_on='id', right_on='id2', how='right'))