
import numpy as np
import pandas as pd

##################################### Reads the files
survey = pd.read_csv("Code_review_perception.csv", delimiter=",")
survey.columns = ['id', 'start_time', 'completion_time', 'none', 'name', 'email', 'years_in_pos', 'city', 'average_contributing_month', 'percent_code_review', 'rewards', 'code_reviews_beneficial', 'hours_reviewing_others_Inweek', 'week_reviewing_others_total', 'balance_spent_between_reviewing_and_commit', 'face_to_face_amount', 'perception_of_author_neg', 'perception_of_author_pos']

surveyEmails = pd.read_csv("surveyEmails.csv", delimiter=";")

accountMapping= pd.read_csv("account_mapping.csv", delimiter=",")
df_code_changes = pd.read_csv("gerrit_changes.csv", delimiter=";")
df_code_reviews = pd.read_csv("gerrit_reviews.csv", delimiter=";")
##################################### Reads the files

changesReviews = pd.merge(df_code_changes, df_code_reviews, left_on='ID', right_on='Change_ID')
changesReviews = changesReviews.drop(['ID'], axis=1)
changesReviews.to_csv("changesReviews.csv", sep=";")

codeChange_accountMapping = pd.merge(accountMapping, df_code_changes, left_on='id', right_on='Author_ID')
codeChange_accountMapping.to_csv("codeChange_accountMapping.csv", sep=";")

authorEmails = codeChange_accountMapping.groupby('email').nunique()
authorEmails.to_csv("emailauthor.csv", sep=";")
print("The emails: ", codeChange_accountMapping.groupby('email').nunique())

codeChange_accountMapping['Created'] = pd.to_datetime(codeChange_accountMapping['Created'])


codeReviews_accountMapping = pd.merge(df_code_reviews, accountMapping, left_on='Reviewer_ID', right_on='id')
codeReviews_accountMapping.to_csv("codeReviews_accountMapping.csv", sep=";")

reviewerEmails = codeReviews_accountMapping.groupby('email').nunique()
reviewerEmails.to_csv("emailreviewer.csv", sep=";")
print(codeReviews_accountMapping)
