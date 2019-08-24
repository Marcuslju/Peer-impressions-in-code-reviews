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

##################################### Connects the changes och reviews to get common emails
emails = pd.concat([codeChange_accountMapping, codeReviews_accountMapping], axis=0, ignore_index=True)
## From ericsson
#emails = emails[emails['email'].str.contains("@ericsson")]
emails = emails.groupby('email').nunique()
emails.to_csv("emails.csv", sep=";")
##################################### Connects the changes och reviews to get common emails

print("Total code review contributors: ", emails.count())
# total number of distinct reviewers and committers ---------------------------
total_reviewers = changesReviews.groupby('Reviewer_ID').first().reset_index()
total_distinct_reviews = total_reviewers
reviewers_changesReviews = changesReviews

for index, row in total_reviewers.iterrows(): # yields both index and rows
    for j, inner_row in changesReviews.iterrows():
        if row.Reviewer_ID == inner_row.Author_ID:
            reviewers_changesReviews = reviewers_changesReviews[reviewers_changesReviews.Reviewer_ID == row.Reviewer_ID]
            total_distinct_reviews = total_distinct_reviews[total_distinct_reviews.Reviewer_ID!=row.Reviewer_ID]

print("Distinct reviewers: ",total_distinct_reviews.count())
total_distinct_reviews.to_csv("total_distinct_reviews.csv")






total_authors = changesReviews.groupby('Author_ID').first().reset_index()
total_distinct_committer = total_authors
authors_changesReviews = changesReviews

for index, row in total_authors.iterrows(): # yields both index and rows
    for j, inner_row in changesReviews.iterrows():
        if row.Author_ID == inner_row.Reviewer_ID:
            authors_changesReviews = authors_changesReviews[authors_changesReviews.Author_ID == row.Author_ID]
            total_distinct_committer = total_distinct_committer[total_distinct_committer.Author_ID!=row.Author_ID]

print("Distinct committers: ", total_distinct_committer.count())
total_distinct_committer.to_csv("total_distinct_committer.csv")

# total number of distinct reviewers and committers ---------------------------

# total number of commits and reviews -----------------------------------------
total_commits = codeChange_accountMapping['Author_ID'].count()
print("Amount commits: ", total_commits)
total_reviews = codeReviews_accountMapping['Reviewer_ID'].count()
print("Amount reviews: ", total_reviews)
# total number of commits and reviews -----------------------------------------

# min, max, average reviewers per commit --------------------------------------

########################### commits

per_commit = changesReviews.groupby(['Author_ID']).size()

print("Min commits: ", per_commit.min())

print("Max commits: ", per_commit.max())

print("Average commits: ", per_commit.mean())

########################### commits

########################### reviews

per_review = changesReviews.groupby(['Reviewer_ID']).size()

print("Min reviews: ", per_review.min())

print("Max reviews: ", per_review.max())

print("Average reviews: ", per_review.mean())

########################### reviews

# min, max, average reviewers per commit --------------------------------------

# min, max, average time between commit and review ---------------------------
changesReviews['Created_y'] = pd.to_datetime(changesReviews['Created_y'])
changesReviews['Created_x'] = pd.to_datetime(changesReviews['Created_x'])

changesReviews['commit_between_review'] = (changesReviews['Created_y'] - changesReviews['Created_x'])
print("Total in between the largest to smallest chunks of time: ", changesReviews['commit_between_review'].sort_values(ascending=False)) # ordered in a descending order

min_time_commit_between_review = changesReviews['commit_between_review'].nsmallest(1)
print("Min time between commit and review: ", min_time_commit_between_review)

max_time_commit_between_review = changesReviews['commit_between_review'].nlargest(1)
print("Max time between commit and review: ", max_time_commit_between_review)

average_time_commit_between_review = changesReviews['commit_between_review'].mean()
print("Average between commit and review: ", average_time_commit_between_review)
# min, max, average time between commit and review ---------------------------
