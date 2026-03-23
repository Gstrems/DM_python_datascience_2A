def principales_surrepresentations(score_departements, candidat):
    diag = score_departements[
        score_departements['candidat'] == candidat
    ].sort_values(by='surrepresentation', ascending=False, key=abs).head(5)[::-1].plot.barh(
        x = 'code_departement',
        y = 'surrepresentation',
        title = "Top 5 des surreprésentations de " + candidat,
        legend=False,
        xlabel="Surreprésentation",
        ylabel="Département",
        grid=True
    )

    diag.yaxis.grid(False)