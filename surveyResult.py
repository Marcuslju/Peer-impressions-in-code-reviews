from fileHandler import *
import numpy as np
import pandas as pd

from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *

import datetime
from pandas.plotting import lag_plot


import matplotlib.pyplot as plt

from datetime import date
from dateutil.relativedelta import relativedelta




survey['percent_code_review'] = survey['percent_code_review'].multiply(10)
print(survey['email'])

##################### Uncomment for Figure 3

"""
total_reviews_percent = survey['percent_code_review'].value_counts()
col = ['percent', 'nrOfReviews']
total_reviews_percent.to_csv("total_reviews_percent.csv", sep=";")
total_reviews_percent = pd.read_csv("total_reviews_percent.csv", names=col, sep=";", header=None)
total_reviews_percent = total_reviews_percent.sort_values('percent')
total_reviews_percent.plot(y="nrOfReviews", x="percent", kind='bar', legend=False)
plt.title('Commits in projects that utilize peer code reviews')
plt.ylabel('Frequency of participants')
plt.xlabel('Percent of participants projects that utilize peer code reviews')
plt.show()
"""

##################### Uncomment for Figure 3

##################### Uncomment for Figure 4

"""
survey['hours_reviewing_others_Inweek'] = survey['hours_reviewing_others_Inweek'].str.extract('(\d+)')
total_hours_freq_week = survey['hours_reviewing_others_Inweek'].value_counts()
col = ['hours_reviewing_others_Inweek', 'freqParticipants']
total_hours_freq_week.to_csv("total_hours_freq_week.csv", sep=";")
total_hours_freq_week = pd.read_csv("total_hours_freq_week.csv", names=col, sep=";", header=None)
total_hours_freq_week = total_hours_freq_week.sort_values('hours_reviewing_others_Inweek')
total_hours_freq_week.plot(y="freqParticipants", x="hours_reviewing_others_Inweek", kind='bar', legend=False)
plt.title('Time in hours participants spent reviewing others code in a week')
plt.ylabel('Frequency of participants')
plt.xlabel('Hours reviewing other author code')
plt.show()
"""

##################### Uncomment for Figure 4

##################### Uncomment for Figure 5

"""
total_diff_others = survey['week_reviewing_others_total'].value_counts()
col = ['week_reviewing_others_total', 'freqParticipants']
total_diff_others.to_csv("total_diff_others.csv", sep=";")
total_diff_others = pd.read_csv("total_diff_others.csv", names=col, sep=";", header=None)
total_diff_others = total_diff_others.sort_values('freqParticipants')
total_diff_others.plot(y="freqParticipants", x="week_reviewing_others_total", kind='bar', legend=False)
plt.title('Total of different code authors participants reviews code for in a week')
plt.ylabel('Frequency of participants')
plt.xlabel('Amount of different code authors')
plt.show()
"""

##################### Uncomment for Figure 5


##################### Uncomment for Figure 10

"""
total_people_contributing = survey['average_contributing_month'].value_counts()
col = ['average_contributing_month', 'freqParticipants']
total_people_contributing.to_csv("total_people_contributing.csv", sep=";")
total_people_contributing = pd.read_csv("total_people_contributing.csv", names=col, sep=";", header=None)
total_people_contributing = total_people_contributing.sort_values('freqParticipants')
total_people_contributing.plot(y="freqParticipants", x="average_contributing_month", kind='bar', legend=False)
plt.ylabel('Frequency of participants')
plt.xlabel('Amount of people contributing to code reviews or code commits in projects')
plt.show()
"""

##################### Uncomment for Figure 10
