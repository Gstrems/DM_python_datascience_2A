def question_1(df):
    df['code_commune'] = df['code_commune'].astype(str).str.zfill(3)
    df['code_departement'] = df['code_departement'].astype(str)
    df['code_departement'] = df['code_departement'] + df['code_commune']
    df['candidat'] = df['prenom'].astype(str) + ' ' + df['nom'].astype(str)
    return df
