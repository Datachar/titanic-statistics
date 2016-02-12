from unittest.case import TestCase
from passengers import Passengers
import pandas as pd


class TestPassengers(TestCase):
    def setUp(self):
        self.pas = Passengers('test_passengers_data.csv')

    def test_sum_male(self):
        self.assertEquals(self.pas.sum_male(), 1)

    def test_sum_female(self):
        self.assertEquals(self.pas.sum_female(), 4)

    def test_percent_of_surviving(self):
        self.assertEquals(self.pas.percent_of_surviving(), 50)

    def test_mean_age_of_passenger(self):
        self.assertEquals(self.pas.mean_age_of_passenger(), 3)

    def test_median_age_of_passenger(self):
        self.assertEquals(self.pas.median_age_of_passenger(), 2)

    def test_percent_of_first_class(self):
        self.assertEquals(self.pas.percent_of_first_class(), 50)

    def test_most_popular_female_name(self):
        self.assertEquals(self.pas.most_popular_female_name(), 'Mary')

    def test_probability_of_surviving(self):
        self.assertEquals(self.pas.probability_of_surviving(2, 1, 'female'), 47.222222222222214)
