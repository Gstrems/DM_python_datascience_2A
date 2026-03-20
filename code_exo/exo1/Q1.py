def question_1(df):
    import pandas as pd
    df['prenom'] = df['prenom'].replace(['NaN', 'nan', ''], pd.NA) # on s'assure que les nan deviennent bien des NA
    df['prenom'] = df['prenom'].fillna('NR') # on les remplace par une modalité en soi, pour ne pas perdre l'info de 'nom' quand on créera 'candidat'
    df['code_commune'] = df['code_commune'].astype(str).str.zfill(3)
    df['code_departement'] = df['code_departement'].astype(str)
    df['code_departement'] = df['code_departement'] + df['code_commune']
    df['candidat'] = df['prenom'].astype(str) + ' ' + df['nom'].astype('str')
    return df
