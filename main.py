import streamlit as st
# importing numpy and pandas for to work with sample data.
import numpy as np
import pandas as pd
import plotly.express as px


def importingDataset(nr=1000000):
    return pd.read_csv("../effectifs.csv", delimiter=";", low_memory=False, nrows=nr)


def correctDataSet(df):
    df['age_m'] = df['cla_age_5'].str.extract(r'(\d+)').astype(float)
    df['prop_pec'] = df['ntop']/df['npop']

    df = df.drop(df[df['dept'] == '973'].index)
    df = df.drop(df[df['dept'] == '976'].index)
    df = df.drop(df[df['dept'] == '974'].index)
    df = df.drop(df[df['dept'] == '2A'].index)
    df = df.drop(df[df['dept'] == '999'].index)
    df = df.drop(df[df['dept'] == '971'].index)
    df = df.drop(df[df['dept'] == '972'].index)
    return df


def home():
    url = "https://www.linkedin.com/in/luis-alexandre-alba-sanchez?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BMb6wDE4gQWKN7%2Bmz1SkjCg%3D%3D"
    st.write("Check out [my linkedIn page !](%s)" % url)
    url2 = "https://github.com/Luis-alba-sanchez"
    st.write("And do not forget to heck out [my GitHub page !](%s) too" % url2)

    st.title('Patient numbers by pathology, gender, age group and territory in France')
    expander = st.expander('''Description (in french)''')
    expander.write('''
            Ce jeu de données est une des sources de datavisualisations disponibles sur le site Data pathologies.
            
            Mise à jour du 10/07/2023 : actualisation des données de 2015 à 2021
            L’historique des données a été mis à jour :
            
            les données de 2015 à 2020 ont été actualisées
            les données de 2021 sont maintenant disponibles
            Cette nouvelle version des données (juillet 2023) remplace ainsi la précédente (datant de juin 2022).
            
            Informations générales :
            Les données présentent des informations sur les effectifs de patients pris en charge par l'ensemble des régimes d'assurance maladie. Elles sont disponibles par pathologie, traitement chronique ou épisode de soins, sexe, classe d’âge, région et département.
            
            Les pathologies, traitements chroniques et épisodes de soins sont regroupés dans les catégories suivantes :
            
            maladies cardio-neurovasculaires ;
            traitements du risque vasculaire (hors pathologies cardio-vasculaires) ;
            diabète ;
            cancers ;
            pathologies psychiatriques ;
            traitements psychotropes (hors pathologies psychiatriques) ;
            maladies neurologiques et dégénératives ;
            maladies respiratoires chroniques ;
            maladies inflammatoires ou rares ou virus de l’immunodéficience humaine (VIH) ou sida ;
            insuffisance rénale chronique terminale (IRCT) ;
            maladies du foie ou du pancréas ;
            autres affections de longue durée (ALD dont 31 et 32) ;
            séjours en hospitalisation complète pour prise en charge de la Covid-19 (à partir de 2020) ;
            maternité ;
            traitements chroniques par antalgiques, anti-inflammatoires non stéroïdiens (AINS) et corticoïdes ;
            séjours hospitaliers ponctuels.
            L'effectif de personnes qui ne présentent aucune des pathologies, traitements chroniques ou épisodes de soins mentionnés ci-dessus est également présenté.
            
            La prévalence correspondante est également présentée dans les données. Elle correspond à la proportion de patients pris en charge, à un moment donné, pour une pathologie (ou traitement chronique ou épisode de soins) dans une population (en %). La population utilisée ici est celle de la cartographie des pathologies et des dépenses de l'Assurance Maladie.
            
            Qu’est-ce que la population de la cartographie des pathologies et des dépenses de l’Assurance Maladie ?
            La population de la cartographie recense l’ensemble des bénéficiaires de l’assurance maladie obligatoire, quel que soit leur régime d’affiliation :
            
            ayant bénéficié d'au moins une prestation dans l’année (soins de médecins, soins infirmiers ou de kinésithérapie, médicament, biologie, transports etc.) ;
            et/ou ayant séjourné au moins une fois dans un établissement de santé public ou privé dans l’année (séjours en médecine, chirurgie, obstétrique, psychiatrie, soins de suite et de réadaptation, actes et consultations externes ou hospitalisation à domicile).
            Elle rassemble en 2021, 68,7 millions de bénéficiaires de l'ensemble des régimes d'assurance maladie, ayant eu recours à des soins remboursés. Cette population est utilisée par la Caisse nationale de l’assurance Maladie (Cnam) pour réaliser de nombreuses études et produire des données sur les pathologies et les dépenses de l’Assurance Maladie.
            
            Pour plus d'informations, consulter la page Méthode de ce site.''')


def describePage(df):
    expander = st.expander('''column's meaning (in french)''')
    # st.header('''column's meaning (in french)''')
    expander.write('''Description du fichier\n
                annee: annee[date] année\n
                patho_niv1: patho_niv1[text] groupe de pathologies (ou traitements chroniques ou épisodes de soins)\n
                patho_niv2: patho_niv2[text] sous-groupe de pathologies (ou traitements chroniques ou épisodes de 
                soins)\n
                patho_niv3: patho_niv3[text] sous-groupe détaillé de pathologies (ou traitements chroniques ou 
                épisodes de soins)\n
                top: top[text] libellé technique de la pathologie (ou traitement chronique ou épisode de soins)\n
                cla_age_5: cla_age_5[text] classe d’âge (5 ans)\n
                sexe: sexe[text] sexe\n
                region: region[text] région\n
                dept: dept[text] département\n
                Ntop: ntop[int] effectif de patients pris en charge pour la pathologie (ou traitement chronique ou 
                épisode de soins) dont il est question\n
                Npop: npop[int] population de référence qui est celle de la cartographie des pathologies et des 
                dépenses de l’Assurance Maladie\n
                prev: prev[double] prévalence de patients pris en charge pour la pathologie (ou traitement chronique 
                ou épisode de soins) dont il est question\n
                Niveau prioritaire: niveau_prioritaire[text]\n
                libelle_classe_age: libelle_classe_age[text] libellé de la classe d’âge\n
                libelle_sexe: libelle_sexe[text] libellé du sexe\n
                tri: tri[double]''')

    st.header('Data Statistics')
    st.write(df.describe())

    st.header('Data Header')
    st.write(df.head())


def role(df):
    p2_list = ['Accident vasculaire cérébral',
        'Artériopathie oblitérante du membre inférieur',
        'Autres affections cardiovasculaires', 'Insuffisance cardiaque',
        'Maladie coronaire', 'Maladie valvulaire',
        'Embolie pulmonaire aiguë',
        'Troubles du rythme ou de la conduction cardiaque']

    dept = st.selectbox('Select the department', options=df['dept'].unique())

    alist=[]

    for i in range(0, len(p2_list)):
        alist.append(df.loc[(df['patho_niv1'] == 'Maladies cardio-neurovasculaires')
                    & (df['dept'] == dept)
                    & (df['patho_niv2'] == p2_list[i])])

    plotlist=[]
    for i in range(0, len(p2_list)):
        plotlist.append(px.area(alist[i],
                       x='annee',
                       y='prev',
                       color='sexe'
                       ))

    for i in range(0, len(p2_list)):
        st.write(f'{p2_list[i]} evolution over time per attribute and department')
        st.plotly_chart(plotlist[i], use_container_width=True)





def evolutionTime(df):
    col1, col2 = st.columns(2)
    p1 = col1.selectbox('Select the class 1 pathology', options=df['patho_niv1'].unique())
    dept = col2.selectbox('Select the department', options=df['dept'].unique())
    #sexe = col1.selectbox('Select the sex', options=df['sexe'].unique())
    niveau_prioritaire = col1.selectbox('Select the priority level', options=df['niveau_prioritaire'].unique())
    ca5 = col2.selectbox('Select the class age', options=df['cla_age_5'].unique())

    l=df.loc[(df['patho_niv1']==p1)
                         & (df['dept']==dept)
                         # & (df['sexe']==sexe)
                         & (df['cla_age_5']==ca5)
                          & (df['niveau_prioritaire'] == niveau_prioritaire)]

    plot = px.area(l,
                  x='annee',
                  y='prev',
                  color='sexe'
                   )
    st.plotly_chart(plot, use_container_width=True)

    st.write(df.loc[(df['patho_niv1']==p1)])


def evolutionDept(df):
    col1, col2 = st.columns(2)
    p1 = col1.selectbox('Select the class 1 pathology', options=df['patho_niv1'].unique())
    year = col2.selectbox('Select the year', options=df['annee'].unique())
    sexe = col1.selectbox('Select the sex', options=df['sexe'].unique())
    ca5 = col2.selectbox('Select the class age', options=df['cla_age_5'].unique())

    l=df.loc[(df['patho_niv1']==p1)&(df['annee']==year)&(df['sexe'] == sexe)& (df['cla_age_5'] == ca5)]

    # dict = {'annee': [], 'patho_niv1': [], 'cla_age_5': [], 'sexe': [], 'dept': [], 'prev': [], 'prop_pec': []}
    # for i in range(0, l.shape[0]):
    #     dict['annee'].append(year)
    #     dict['patho_niv1'].append(p1)
    #     dict['cla_age_5'].append(ca5)
    #     dict['sexe'].append(sexe)
    #     dict['dept'].append(l[i:i + 1]['dept'].item())
    #     npop_tot = l[l['dept'] == l[i:i + 1]['dept'].item()]['npop'].sum()
    #     dict['prev'].append(l[i:i + 1]['npop'].item() * l[i:i + 1]['prev'].item() / npop_tot)
    #     prop_pec_tot = l[l['dept'] == l[i:i + 1]['dept'].item()]['prop_pec'].sum()
    #     dict['prop_pec'].append(l[i:i + 1]['npop'].item() * l[i:i + 1]['prop_pec'].item() / prop_pec_tot)
    #
    # good_df = pd.DataFrame(dict)

    plot = px.bar(l,
                  x='dept',
                  y='prev',
                  color='prop_pec')
    st.plotly_chart(plot, use_container_width=True)


def heatmap(df):
    col1, col2 = st.columns(2)
    p1 = col1.selectbox('Select the class 1 pathology', options=df['patho_niv1'].unique())
    ca5 = col2.selectbox('Select the class age', options=df['cla_age_5'].unique())

    l=df.loc[(df['patho_niv1']==p1) & (df['cla_age_5'] == ca5)]

    plot = px.density_heatmap(l, x="dept", y="annee", z="prev", histfunc="avg", nbinsx=96, text_auto=True)
    st.plotly_chart(plot, use_container_width=True)


def page():
    val=1000000
    df = correctDataSet(importingDataset(val))

    # sidebar
    st.sidebar.title('Navigation')
    options = st.sidebar.radio('Pages', options=['Home',
                                                 'Describe',
                                                 'Evolution over the years',
                                                 'Evolution per Department',
                                                 'Heatmap',
                                                 'Role'])

    if options == 'Home':
        home()
    if options == 'Describe':
        describePage(df)
    if options == 'Evolution over the years':
        evolutionTime(df)
    if options == 'Evolution per Department':
        evolutionDept(df)
    if options == 'Heatmap':
        heatmap(df)
    if options == 'Role':
        role(df)











page()
