import sys
import pandas as pd

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QLineEdit, QGridLayout, QPushButton
from passenger import Passengers


df = pd.read_csv(r'titanic.csv')
pas = Passengers(df)


class TitanicStatApp:
    def __init__(self):
        self.main_windows = None
        self.main_layout = None
        self.form_layout = None
        self.main_layout = None
        self.analysis_layout = None
        self.result_layout = None

    def run(self):
        app = QApplication(sys.argv)

        self.main_windows = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_windows.setWindowTitle('title')
        self.main_windows.resize(370, 300)

        self.form_layout = self.probably_of_static()
        self.analysis_layout = visual_analysis_data()

        self.main_layout.addLayout(self.analysis_layout)
        self.main_layout.addLayout(self.form_layout)

        self.main_windows.setLayout(self.main_layout)
        self.main_windows.show()
        sys.exit(app.exec_())

    def probably_of_static(self):
        pas_age = QLabel('Age')
        pas_class = QLabel('Class')
        pas_gender = QLabel('Gender')

        input_age = QLineEdit()
        input_class = QLineEdit()
        input_gender = QLineEdit()

        grid = QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(pas_age, 1, 0)
        grid.addWidget(input_age, 1, 1)

        grid.addWidget(pas_class, 2, 0)
        grid.addWidget(input_class, 2, 1)

        grid.addWidget(pas_gender, 3, 0)
        grid.addWidget(input_gender, 3, 1)

        def save_form_result():
            tmp_age = input_age.text()
            tmp_class = input_class.text()
            tmp_gender = input_gender.text()
            self.probability_of_surviving(input_age=tmp_age, input_class=tmp_class, input_gender=tmp_gender)

        btn = QPushButton('ok')
        btn.clicked.connect(save_form_result)

        grid.addWidget(btn, 7, 0)
        return grid

    def probability_of_surviving(self, input_age, input_class, input_gender):
        input_age = int(input_age)
        input_class = int(input_class)
        input_gender = str(input_gender)

        res = QLabel('Probability of surviving: %0.5s' % str(pas.probability_of_surviving(
                input_age=input_age, input_class=input_class, input_gender=input_gender)))
        grid = QGridLayout()
        grid.setSpacing(5)

        grid.addWidget(res, 1, 1)
        self.result_layout = grid
        self.main_layout.addLayout(self.result_layout)


def visual_analysis_data():
    grid = QGridLayout()
    grid.setSpacing(5)

    sum_male = QLabel(get_sum_male('Amount male'))
    grid.addWidget(sum_male, 1, 0)

    sum_female = QLabel(get_sum_female('Amount female'))
    grid.addWidget(sum_female, 2, 0)

    percent_of_surviving = QLabel(get_percent_of_surviving('Percent of first class passengers'))
    grid.addWidget(percent_of_surviving, 3, 0)

    age_mean = QLabel(get_age_mean('Mean age of passengers'))
    grid.addWidget(age_mean, 4, 0)

    age_median = QLabel(get_age_median('Median age of passengers'))
    grid.addWidget(age_median, 5, 0)

    most_popular_female_name = QLabel(get_most_popular_female_name('Most popular female name'))
    grid.addWidget(most_popular_female_name, 6, 0)

    return grid


def get_sum_male(text):
    res = text + ': ' + str(pas.sum_male())
    return str(res)


def get_sum_female(text):
    res = text + ': ' + str(pas.sum_female())
    return str(res)


def get_percent_of_surviving(text):
    res = text + ': %0.5s' % str(pas.percent_of_surviving())
    return str(res)


def get_age_mean(text):
    res = text + ': %0.5s' % str(pas.mean_age_of_passenger())
    return str(res)


def get_age_median(text):
    res = text + ': ' + str(pas.median_age_of_passenger())
    return str(res)


def get_most_popular_female_name(text):
    res = text + ': ' + str(pas.most_popular_female_name()[0])
    return str(res)
