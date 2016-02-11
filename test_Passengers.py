from unittest.case import TestCase
from passengers import Passengers
from pandas import DataFrame, read_csv
import pandas as pd


class TestPassengers(TestCase):
    def test_passengers(self):
        df = pd.DataFrame(
            {
                'PassengerId' : [1, 2, 3, 4, 5, 6],
                'Sex': ["male", "female", "female", "female", "female", ""],
                'Survived': [0, 1, 1, 0, 1, 0],
                'Age': [2, 8, 0, 4, 2, 2],
                'Pclass': [1, 2, 3, 1, 1, 3],
                'Name': ["Navratil, Master. Edmond Roger",
                         "Davison, Mrs. Thomas Henry (Mary E Finck)",
                         "Brown, Miss. Mary ""Mildred""",
                         "Moussa, Mrs. (Anna Boulos)",
                         "Pain Olala, Dr. Mary",
                         "Emanuel Shannel, Miss. Virginia Ethel"
                         ]
            })
        pas = Passengers(df)
        test_data = [
            (pas.sum_male(), 1),
            (pas.sum_female(), 4),
            (pas.persent_of_survavivng(), 50),
            (pas.mean_age_of_passenger(), 3),
            (pas.median_age_of_passenger(), 2),
            (pas.persent_of_first_class(), 50),
            (pas.most_popular_female_name(), ('Mary', 3)),
            (pas.probability_of_survaving(2,1,'female'), 47.222222222222214)
        ]

        for input_data, expected_result in test_data:
            self.assertEquals(input_data,expected_result)
