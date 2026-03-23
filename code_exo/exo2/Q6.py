def question_6(score_departements):
    score_departements['surrepresentation'] = 100*(
        score_departements['score_departement'] - score_departements['score_national']
    ) / score_departements['score_national']
