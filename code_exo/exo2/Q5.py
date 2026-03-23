def question_5(score_departements, table_voix):
    score_departements = score_departements.merge(
        table_voix,
        left_on=['candidat'],
        right_on=['candidat'],
        how='right'
    )

    score_departements = score_departements.rename(
        columns={
            'votes': 'votes_departement',
            'score': 'score_departement',
            'Nombre de vote (total)': 'votes_national',
            'Score(% exprimé)': 'score_national'
            }
            )
    
    return score_departements
