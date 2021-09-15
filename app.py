import streamlit as st
import pandas as pd
from utils.functions import clean_location
from utils.constants import LOCATION_REPLACE


@st.cache
def load_data():
    return pd.read_csv('data/output.csv')


def main():
    st.title('Analise de tweets sobre #blockchain e #crypto')
    df_tweets = load_data()

    st.markdown("""
    [![Github](https://img.shields.io/badge/-Github-181717?style=for-the-badge&logo=Github&logoColor=white)](#)
    [![Medium](https://img.shields.io/badge/-Medium-03a57a?style=for-the-badge&labelColor=000000&logo=Medium&logoColor=white)](#)

    Esse trabalho tem como objetivo analisar os tweets sobre #cripto e #blockchain.

    Esse trabalho foi desenvolvido para a disciplina de Analise de Redes (IMD1155)
    do curso de Bacharelado em Tecnologia da Informação (BTI)
    da Universidade Federal do Rio Grande do Norte (UFRN),
    possuindo [Ivanovitch Medeiros Dantas da Silva](https://github.com/ivanovitchm) como professor.

    Grupo: [Álvaro Ferreira Pires de Paiva](https://github.com/alvarofpp) e
    [Marcos Vinícius Rêgo Freire](https://github.com/mvinnicius22).

    ----------

    ## Dataset

    O dataset usado nos experimentos possui um total de {} linhas e {} colunas.
    Não ocorreu de um mesmo usuário ter mais de um tweet no nosso dataset.

    ----------

    ## Análises
    Aqui será apresentado algumas análise referentes aos tweets.

    ### Top tweets com mais retweets
    """.format(df_tweets.shape[0], df_tweets.shape[1]))

    top_retweets = df_tweets.sort_values(by=['retweet_count'], ascending=False)[:10] \
        .reset_index() \
        .drop(labels=['index', 'id', 'followers_count', 'favorite_count', ], axis=1)
    top_retweets.index = top_retweets.index + 1
    st.table(top_retweets)

    st.markdown("""
    Como dar para perceber, muitos tweets são de possíveis bots.

    ### Top tweets com mais curtidas
    """)

    top_retweets = df_tweets.sort_values(by=['favorite_count'], ascending=False)[:10] \
        .reset_index() \
        .drop(labels=['index', 'id', 'followers_count', 'retweet_count'], axis=1)
    top_retweets.index = top_retweets.index + 1
    st.table(top_retweets)

    st.markdown("""
    Nos tweets com mais curtidas, já encontramos um conteúdo mais diversificado, com perfis influenciadores sobre o
    tema e não apenas bots.

    ### Top localizações dos usuários
    """)

    series_location = df_tweets['location'].dropna() \
        .apply(clean_location) \
        .replace(LOCATION_REPLACE) \
        .value_counts() \
        .drop(labels=['she/her']) \
        .rename_axis('location') \
        .reset_index(name='counts')
    series_location.index = series_location.index + 1

    st.table(series_location[:10])

    st.markdown("""
    Ocorre uma predominância em países da Ásia.

    ### Top línguas dos tweets
    """)

    df_language = df_tweets['lang'].value_counts() \
        .rename_axis('language') \
        .reset_index(name='counts')
    df_language.index = df_language.index + 1

    st.table(df_language[:10])

    st.markdown("""
    Como já era de se esperar, tem uma predominância do inglês.
    
    ### Quais as hastags mais usadas em conjunto com #blockchain e #crypto?
    """)
    hastags_rows = df_tweets['text'].drop_duplicates() \
        .str \
        .findall(r'(?:(?<=\s)|(?<=^))#.*?(?=\W|$)')

    hastags = pd.Series([
        hastag.lower()
        for hastags_row in hastags_rows
        if len(hastags_row) > 0
        for hastag in hastags_row
        if hastag.lower() not in ['#blockchain', '#crypto']
    ]).value_counts() \
        .rename_axis('hastag') \
        .reset_index(name='counts')
    hastags.index = hastags.index + 1

    st.table(hastags[:10])

    st.markdown("""
    Podemos ver uma grande associação com termos presentes no mercado financeiro, como bitcoin e NFT.

    ### Quais os usuários mais citados nos tweets?
    """)
    citations_rows = df_tweets['text'].drop_duplicates() \
        .str \
        .findall(r'(?:(?<=\s)|(?<=^))@.*?(?=\W|$)')

    citations = pd.Series([
        at.lower()
        for citation_row in citations_rows
        if len(citation_row) > 0
        for at in citation_row
    ]).value_counts() \
        .rename_axis('citation') \
        .reset_index(name='counts')
    citations.index = citations.index + 1

    st.table(citations[:10])

    st.markdown("""
    A maioria das citações ocorre para perfis de organizações que promovem o blockchain ou criptomoedas.
    """)


if __name__ == "__main__":
    main()
