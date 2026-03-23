def question_4(df):
    table_filtree = df[~df['candidat'].isin(['NR nuls', 'NR abstentions', 'NR blancs'])]

    score_departements = table_filtree.groupby(
            ['code_departement', 'candidat']
            ).agg(
                votes=('voix', 'sum'),
                ).reset_index()

    total = table_filtree.groupby(
            ['code_departement']
        ).agg({'voix': 'sum'}).merge(
        score_departements,
        left_on='code_departement',
        right_on='code_departement',
        how='right'
    ).reset_index()

    score_departements['score'] = score_departements['votes'] / total['voix']
    return score_departements
