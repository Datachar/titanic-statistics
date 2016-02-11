import sys

from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QTextBrowser, QLineEdit, QGridLayout, QPushButton, QLayout
from PyQt5.QtGui import QTextLayout

from passenger import Passenger
#from utils import create_analysis_widget


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

    def run(self):
        app = QApplication(sys.argv)

        self.main_windows = QWidget()

        self.main_windows.setWindowTitle('title')
        self.main_windows.resize(400, 400)
        # self.main_layout = QTextLayout()

        self.sum_male = QLabel(get_sum_male('Amount male'), self.main_windows)
        self.sum_male.move(20, 20)

        self.sum_female = QLabel(get_sum_female('Amount female'), self.main_windows)
        self.sum_female.move(20, 40)

        self.percent_of_surviving = QLabel(get_percent_of_survived('Percent of first class passengers'), self.main_windows)
        self.percent_of_surviving.move(20, 60)

        self.age_mean = QLabel(get_age_mean('Mean age of passengers'), self.main_windows)
        self.age_mean.move(20, 80)

        self.age_median = QLabel(get_age_median('Median age of passengers'), self.main_windows)
        self.age_median.move(20, 100)

        self.most_popular_female_name = None

        self.form_layout = self.prob_of_surv()
      #  self.form_layout.setDefaultPositioning()
        self.main_windows.setLayout(self.form_layout)
       # self.main_windows.unsetLayoutDirection()
       # self.main_windows.
        self.main_windows.show()
        sys.exit(app.exec_())

    '''
    def btn_action(self):
        btn = QPushButton('ok')
        btn.clicked.connect()
    '''

    def prob_of_surv(self):
        age = QLabel('Age')
        klass = QLabel('Class')
        gender = QLabel('Gender')

        ageEdit = QLineEdit()
        klassEdit = QLineEdit()
        genderEdit = QLineEdit()

        grid = QGridLayout()
        grid.activate()
        grid.setSpacing(10)

        grid.addWidget(klass, 1, 0)
        grid.addWidget(klassEdit, 1, 1)

        grid.addWidget(age, 2, 0)
        grid.addWidget(ageEdit, 2, 1)

        grid.addWidget(gender, 3, 0)
        grid.addWidget(genderEdit, 3, 1)

        return grid


def get_sum_male(text):
    res = text + ': ' + str(Passenger.sum_male())
    return res


def get_sum_female(text):
    res = text + ': ' + str(Passenger.sum_female())
    return res


def get_percent_of_survived(text):
    res = text + ': ' + str(Passenger.per_of_survived())
    return res


def get_age_mean(text):
    res = text + ': ' + str(Passenger.age_mean())
    return res


def get_age_median(text):
    res = text + ': ' + str(Passenger.age_median())
    return res

# def get_probability_of_surviving(text, )


