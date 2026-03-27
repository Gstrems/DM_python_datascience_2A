#pip install py7zr geopandas openpyxl tqdm s3fs
#pip install PyYAML
#pip install cartiflette
import matplotlib.pyplot as plt


# sq: surrepresentation('Nom candidat') -> float % (= 100 pour 100%)
# sq: scores_departements = 'dep' 'votes' 'score'
def chargement_question_8(departement_borders):
    if departement_borders.crs != 'EPSG:2154':
        departement_borders = departement_borders.to_crs(2154)
    bdd_quest_8 = departement_borders.copy()
    return bdd_quest_8

def question_8(score_departements, departement_borders, nom_candidat):
    departement_borders_copy = chargement_question_8(departement_borders)
    score_geopandas = departement_borders_copy.merge(score_departements,
                                                     left_on='INSEE_DEP',
                                                     right_on='code_departement',
                                                     how='left')

    if score_geopandas is None or nom_candidat not in score_geopandas['candidat'].values:
        print(f"Erreur: données non disponibles ou candidat '{nom_candidat}' non trouvé")
        return
    score_geopandas = score_geopandas.loc[score_geopandas['candidat'] == nom_candidat]
    if score_geopandas.empty:
        print(f"Aucune donnée pour le candidat {nom_candidat}")
        return

    fig, ax = plt.subplots(figsize=(20, 10))
    departement_borders_copy.boundary.plot(ax=ax, color='black', linewidth=0.5)
    score_geopandas.plot(
        column="surrepresentation",
        ax=ax,
        legend=True,
        cmap="coolwarm",
        legend_kwds={"label": f"Surreprésentation de {nom_candidat} (%)"}
    )
    ax.set_axis_off()
    ax.set_title(f"Surreprésentation de {nom_candidat} par département", fontsize=16)
