import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QTextBrowser, QLineEdit, QGridLayout, QPushButton, QLayout
from PyQt5.QtGui import QTextLayout

from passenger import Passengers
#from utils import create_analysis_widget
from pandas import DataFrame, read_csv
import pandas as pd

df = pd.read_csv(r'titanic.csv')
pas = Passengers(df)

class TitanicStatApp:
    def __init__(self):
        # self.analysis_data = {}
        self.main_windows = None
        self.main_layout = None

        self.sum_male = None
        self.sum_female = None
        self.percent_of_surviving = None
        self.age_mean = None
        self.age_median = None
        self.most_popular_female_name = None
        self.prob_of_surviving = None
        self.form_layout = None
        self.main_layout = None
        self.analysis_layout = None

    def run(self):
        app = QApplication(sys.argv)

        self.main_windows = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_windows.setWindowTitle('title')
        self.main_windows.resize(400, 400)

        self.most_popular_female_name = None

        self.form_layout = self.probably_of_static()
        self.analysis_layout = self.analysis_data_show()

        self.main_layout.addLayout(self.analysis_layout)
        self.main_layout.addLayout(self.form_layout)



        self.main_windows.setLayout(self.main_layout)
        self.main_windows.show()
        sys.exit(app.exec_())

    def probably_of_static(self):
        age = QLabel('Age')
        klass = QLabel('Class')
        gender = QLabel('Gender')

        ageEdit = QLineEdit()
        klassEdit = QLineEdit()
        genderEdit = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(klass, 1, 0)
        grid.addWidget(klassEdit, 1, 1)

        grid.addWidget(age, 2, 0)
        grid.addWidget(ageEdit, 2, 1)

        grid.addWidget(gender, 3, 0)
        grid.addWidget(genderEdit, 3, 1)

        return grid

    def analysis_data_show(self):
        grid = QGridLayout()
        grid.setSpacing(5)

        sum_male = QLabel(get_sum_male('Amount male'))
        grid.addWidget(sum_male, 1,0)

        sum_female = QLabel(get_sum_female('Amount female'))
        grid.addWidget(sum_female, 2,0)

        percent_of_surviving = QLabel(get_percent_of_surviving('Percent of first class passengers'))
        grid.addWidget(percent_of_surviving, 3,0)

        age_mean = QLabel(get_age_mean('Mean age of passengers'))
        grid.addWidget(age_mean)

        age_median = QLabel(get_age_median('Median age of passengers'))
        grid.addWidget(age_median)

        return grid


def get_sum_male(text):
    res = text + ': ' + str(pas.sum_male())
    return str(res)


def get_sum_female(text):
    res = text + ': ' + str(pas.sum_female())
    return str(res)


def get_percent_of_surviving(text):
    res = text + ': ' + str(pas.percent_of_surviving())
    return str(res)


def get_age_mean(text):
    res = text + ': ' + str(pas.mean_age_of_passenger())
    return str(res)


def get_age_median(text):
    res = text + ': ' + str(pas.median_age_of_passenger())
    return str(res)

# def get_probability_of_surviving(text, )


