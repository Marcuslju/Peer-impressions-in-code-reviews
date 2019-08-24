from fileHandler import *

import numpy as np
import pandas as pd

from scipy.interpolate import *

from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *

import datetime
from pandas.plotting import lag_plot

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

from datetime import date
from dateutil.relativedelta import relativedelta

codeReviews_accountMapping['Created'] = pd.to_datetime(codeReviews_accountMapping['Created'])


changesReviews['Created_y'] = pd.to_datetime(changesReviews['Created_y'])
changesReviews['Created_x'] = pd.to_datetime(changesReviews['Created_x'])

changesReviews['commit_between_review'] = (changesReviews['Created_y'] - changesReviews['Created_x'])





#################### Uncomment to get the Figure 1

"""
sumOfCommitsMonths = changesReviews['Created_x'].groupby(changesReviews.Created_x.dt.to_period("M")).agg('count')
sumOfCommitsMonths.to_csv("sumOfCommitsMonths.csv", sep=";")

col = ['Created_x', 'nrOfCommits']

sumOfCommitsMonths = pd.read_csv("sumOfCommitsMonths.csv",  names=col, delimiter=";")

changesReviews['Months'] = changesReviews.Created_x.dt.to_period("M")
changesReviews = changesReviews.loc[changesReviews.Review==-1]
changesReviews = changesReviews.sort_values("Author_ID")
changesReviews.to_csv("changeReviews.csv", sep=";")

sumOfCommitsMonths.plot(y="nrOfCommits", x="Created_x", kind='bar', legend=False)
plt.ylabel('Amount of commits')
plt.xlabel('Month commits been made')
"""

#################### Uncomment to get the Figure 1

#################### Uncomment to get the Figure 2

"""

changesReviews['commit_between_review'] = changesReviews['commit_between_review'].dt.days
changesReviews['commit_between_review'] = changesReviews['commit_between_review'].abs()

in_between = changesReviews['commit_between_review'].value_counts()

col = ['commit_between_review', 'nrOfCommits']
in_between.to_csv("in_between.csv", sep=";")
in_between = pd.read_csv("in_between.csv", names=col, sep=";", header=None)

in_between = in_between.sort_values("commit_between_review")

in_between.plot(y="nrOfCommits", x="commit_between_review", kind='bar', legend=False)
plt.ylabel('Amount of commits')
plt.xlabel('Time between commit and review')

"""

#################### Uncomment to get the Figure 2

##################### Uncomment for following Figures

"""
changesReviews['commit_between_review'] = changesReviews['commit_between_review'].dt.seconds
changesReviews['commit_between_review'] = changesReviews['commit_between_review'].abs()
changesReviews = changesReviews[changesReviews.commit_between_review < 864000] # 10 days between
changesReviews['commit_between_review'] = changesReviews['commit_between_review'].div(3600) # To hours
"""

##################### Uncomment for following Figures


##################### Uncomment for Figure 11

"""
for index, row in accountMapping.iterrows(): # yields both index and rows
    for j, inner_row in accountMapping.iterrows():
            current_author = changesReviews.loc[changesReviews.Author_ID == row['id'], :]
            current_author = current_author.loc[current_author.Reviewer_ID == inner_row['id'], :]
            current_author = current_author.sort_values('Created_x')
            if (current_author['Author_ID'].count() >= 4):

                df_x = mdates.date2num(current_author['Created_x'])
                df_y = current_author['commit_between_review']
                df2 = pd.DataFrame()
                df2['Created_x'] = current_author['Created_x']
                df2['commit_between_review'] = current_author['commit_between_review']
                df = df.append(df2)
                current_author.to_csv("current_author.csv", sep=";")

                same_cit_polyfit = np.polyfit(df_x, df_y, 1) #linear fit
                plt.plot(current_author["Created_x"], np.polyval(same_cit_polyfit, df_x), '-k') # evaluates the polynomial coefficient

df = df.sort_values('Created_x')
df_x = mdates.date2num(df['Created_x']).astype(float)
df_y = df['commit_between_review'].astype(float)

overall_polyfit = np.polyfit(df_x, df_y, 1) #linear fit
plt.plot(df["Created_x"], np.polyval(overall_polyfit, df_x), '--r', linewidth=6) # evaluates the polynomial coefficient
plt.ylabel('Hours between commit and review')
plt.xlabel('Date when the commit was created')

"""

##################### Uncomment for Figure 11

#################### Uncomment for Figure 12

"""
changesReviews = changesReviews.loc[changesReviews.Author_ID ==  169, :]
print("Most frequent reviewer:", changesReviews['Reviewer_ID'].value_counts().nlargest(27))
changesReviews = changesReviews.loc[changesReviews.Reviewer_ID == 2335, :]
changesReviews = changesReviews.sort_values('Created_x')
df_x = mdates.date2num(changesReviews['Created_x'])
df_y = changesReviews['commit_between_review']
diff_cit_polyfit = np.polyfit(df_x, df_y, 1) #linear fit
changesReviews.plot(x='Created_x', y='commit_between_review', style='o', legend=False)
plt.plot(changesReviews["Created_x"], np.polyval(diff_cit_polyfit, df_x), '--r') # evaluates the polynomial coefficient
plt.xlabel('Date when the commit was created')
plt.ylabel('Hours between commit and review')
"""

#################### Uncomment for Figure 12

#################### Uncomment for Figure 13

"""
changesReviews = changesReviews.loc[changesReviews.Author_ID ==  169, :]
print("Most frequent reviewer:", changesReviews['Reviewer_ID'].value_counts().nlargest(27))
changesReviews = changesReviews.loc[changesReviews.Reviewer_ID == 2335, :]
changesReviews = changesReviews.sort_values('Created_x')
changesReviews.plot(x='Created_x', y='Review', style='o', legend=False)
plt.xlabel('Date when the commit was created')
plt.ylabel('Review score')
"""

#################### Uncomment for Figure 13

####################### Uncomment for Figure 14

"""
df = pd.DataFrame(columns=['Created_x', 'commit_between_review'])
for index, row in surveyEmails.iterrows(): # yields both index and rows
    for j, inner_row in surveyEmails.iterrows():
            current_author = changesReviews.loc[changesReviews.Author_ID == row['id'], :]
            current_author = current_author.loc[current_author.Reviewer_ID == inner_row['id'], :]
            current_author = current_author.sort_values('Created_x')
            if not current_author.empty:

                df_x = mdates.date2num(current_author['Created_x'])
                df_y = current_author['commit_between_review']

                df2 = pd.DataFrame()
                df2['Created_x'] = current_author['Created_x']
                df2['commit_between_review'] = current_author['commit_between_review']


                df = df.append(df2)
                same_cit_polyfit = np.polyfit(df_x, df_y, 1) #linear fit
                plt.plot(current_author["Created_x"], np.polyval(same_cit_polyfit, df_x), '-k') # evaluates the polynomial coefficient


df = df.sort_values('Created_x')
df_x = mdates.date2num(df['Created_x']).astype(float)
df_y = df['commit_between_review'].astype(float)
same_cit_polyfit = np.polyfit(df_x, df_y, 1) #linear fit
plt.plot(df["Created_x"], np.polyval(same_cit_polyfit, df_x), '--r', linewidth=6)
plt.ylabel('Hours between commit and review')
plt.xlabel('Date when the commit was created')
"""

####################### Uncomment for Figure 14

###################### Uncomment for Figure 15

"""
df = pd.DataFrame(columns=['Created_x', 'Review'])
for index, row in surveyEmails.iterrows(): # yields both index and rows
    for j, inner_row in surveyEmails.iterrows():
            current_author = changesReviews.loc[changesReviews.Author_ID == row['id'], :]
            current_author = current_author.loc[current_author.Reviewer_ID == inner_row['id'], :]
            current_author = current_author.sort_values('Created_x')
            if not current_author.empty:

                df_x = mdates.date2num(current_author['Created_x'])

                df2 = pd.DataFrame()
                df2['Created_x'] = current_author['Created_x']

                df2['Review'] = current_author['Review']

                df = df.append(df2)

df = df.sort_values('Created_x')
print("Most frequent reviewer:", changesReviews['Reviewer_ID'].value_counts().nlargest(27))
changesReviews = changesReviews.sort_values('Created_x')
plt.scatter(df["Created_x"], df['Review'])
plt.ylabel('Review score')
plt.xlabel('Date when the commit was created')
"""

###################### Uncomment for Figure 15






plt.show()
