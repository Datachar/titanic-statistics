from pandas import DataFrame, read_csv
import pandas as pd
from collections import Counter


class Passengers:
    def __init__(self, df):
        self.df = df

    def sum_male(self):
        sum_ = self.df.Sex.where(self.df.Sex == 'male').count()
        return sum_

    def sum_female(self):
        sum_ = self.df.Sex.where(self.df.Sex == 'female').count()
        return sum_

    def persent_of_survavivng(self):
        sum_ = self.df.Survived.where(self.df.Survived == 1).count()
        return sum_/len(self.df)*100

    def persent_of_first_class(self):
        sum_ = self.df.Pclass.where(self.df.Pclass == 1).count()
        return sum_/len(self.df)*100

    def mean_age_of_passenger(self):
        return self.df.Age.mean()

    def median_age_of_passenger(self):
        return self.df.Age.median()

    def correlation(self):
        return self.df[['SibSp', 'Parch']].corr()

    def most_popular_female_name(self):
        all_name = list(self.df.Name.where(self.df.Sex == 'female'))
        name = []
        for i in all_name:
            if str(i) != 'nan' :
                name_split = str(i).split(', ')
                name_split = name_split[1].split(' ')
                if name_split[0] == 'Miss.' or name_split[0] == 'Mlle.' or\
                                name_split[0] == 'Dr.' or name_split[0] == 'Mme.' or\
                                name_split[0] == 'Ms.':
                    name.append(name_split[1])
                elif name_split[0] == 'Mrs.' or name_split[0] == 'Lady.':
                    start = i.find('(')
                    end = i.find(' ', start)
                    name.append(i[start+1:end])
                else:
                    name.append(i)
        word_counts = Counter(name)
        top_three = word_counts.most_common(1)
        return top_three[0]

    def probability_of_survaving(self, input_age, input_class, input_gender):
        count_survaving_age = self.df.PassengerId.where(self.df.Age == input_age).where(self.df.Survived == 1).count()
        count_survaving_class = self.df.PassengerId.where(self.df.Pclass == input_class).where(self.df.Survived == 1).count()
        count_survaving_gender = self.df.PassengerId.where(self.df.Sex == input_gender).where(self.df.Survived == 1).count()
        count_all_age = self.df.PassengerId.where(self.df.Age == input_age).count()
        count_all_class = self.df.PassengerId.where(self.df.Pclass == input_class).count()
        count_all_gender = self.df.PassengerId.where(self.df.Sex == input_gender).count()
        if count_all_age == 0 or count_all_class == 0 or count_survaving_gender == 0:
            return 0
        result = (count_survaving_age/count_all_age +
                  count_survaving_class/count_all_class +
                  count_survaving_gender/count_all_gender)/3 * 100
        return result
