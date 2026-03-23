def question_3(df):
    table_filtree = df[~df['candidat'].isin(['NR nuls', 'NR abstentions', 'NR blancs'])]
    voix_exprim = table_filtree['voix'].sum()
    table_voix = table_filtree.groupby('candidat', as_index=False)['voix'].sum().rename(columns={'voix': 'Nombre de vote (total)'})
    table_voix['Score(% exprimé)'] = table_voix['Nombre de vote (total)']/voix_exprim
    table_voix = table_voix.sort_values(by='Nombre de vote (total)', ascending=False)
    return table_voix


    