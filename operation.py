from pandas import DataFrame, read_csv
import pandas as pd
from passenge import Passenger
from collections import Counter


def calculation(input_age=0, input_class=0, input_gender=""):
    location = r'titanic.csv'
    df = pd.read_csv(location)
    passengers = []
    for i in range(len(df.PassengerId)):
        p = Passenger(df['PassengerId'][i], df['Survived'][i], df['Pclass'][i], df['Name'][i], df['Sex'][i],
                      df['Age'][i], df['SibSp'][i], df['Parch'][i], df['Ticket'][i], df['Fare'][i], df['Cabin'][i],
                      df['Embarked'][i])
        passengers.append(p)
    result_calculation = {
        'Count male': sum_male(passengers),
        'Count female': sum_female(passengers),
        'Percent of survived': percent_of_survived(passengers),
        'Percent of first class': percent_of_first_class(passengers),
        'Age median': age_median(passengers),
        'Age mean': age_mean(df['Age']),
        'Most popular female name': most_popular_female(passengers),
        'Probability of surviving': probability_of_surviving(passengers, input_age, input_class, input_gender),
    }
    for i, j in result_calculation.items():
        print(i, ':', j)
    return result_calculation


def sum_male(passengers):
    return len([i for i in range(len(passengers)) if passengers[i].sex == 'male'])


def sum_female(passengers):
    return len([i for i in range(len(passengers)) if passengers[i].sex == 'female'])


def percent_of_survived(passengers):
    if len(passengers) == 0 :
        return 0
    sum_survived = len([i for i in range(len(passengers)) if passengers[i].survived == 1])
    return float(format(sum_survived / len(passengers) * 100, '.2f'))


def percent_of_first_class(passengers):
    sum_first_class = len([i for i in range(len(passengers)) if passengers[i].pclass == 1])
    return format(sum_first_class / len(passengers) * 100, '.2f')


def age_median(passengers):
    sum_age = 0
    for i in range(len(passengers)):
        if str(passengers[i].age) != 'nan':
            sum_age += passengers[i].age
    return format(sum_age / len(passengers), '.2f')


def age_mean(passengers):
    age_counts = Counter(passengers)
    top_count = age_counts.most_common(1)
    return top_count[0][0]


def most_popular_female(passengers):
    females_name = []
    for i in range(len(passengers)):
        if passengers[i].sex == 'female':
            s = passengers[i].name
            females_name.append(s.split('. ')[-1])
    name_counts = Counter(females_name)
    top_count = name_counts.most_common(1)
    return top_count[0][0]


def probability_of_surviving(passengers, input_age, input_class, input_gender):
    age_survived = []
    class_survived = []
    gender_survived = []
    for i in range(len(passengers)):
        if passengers[i].age == input_age:
            age_survived.append(passengers[i])
        if passengers[i].pclass == input_class:
            class_survived.append(passengers[i])
        if passengers[i].sex == input_gender:
            gender_survived.append(passengers[i])
    count = 0
    sum_ = 0
    if len(age_survived) != 0:
        sum_ += percent_of_survived(age_survived)
        count += 1
    if len(class_survived) != 0:
        sum_ += percent_of_survived(class_survived)
        count += 1
    if len(gender_survived) != 0:
        sum_ += percent_of_survived(gender_survived)
        count += 1
    return float(format(sum_/count,'.2f'))


calculation(0,2,'female')
