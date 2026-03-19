def question_2(df):
    candidats = df['candidat'].value_count()
    return(f"En 2022, il y avait {candidats} candidats à l'élection présidentielle.")