def question_2(df):
    # on exclut les votes nuls, blancs et l'abstention du décompte des candidats 
    candidats = df.loc[~df['candidat'].isin(['NR nuls', 'NR abstentions', 'NR blancs'])]['candidat'].nunique()
    return f"En 2022, il y avait {candidats} candidats à l'élection présidentielle."