def question_3(df):
    voix_exprim = df[~df['candidat'].isin(['NR nuls', 'NR abstentions', 'NR blancs'])]['voix'].sum()
    