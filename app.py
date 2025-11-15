import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv("student.csv")

st.set_page_config(
  page_title="Dashboard com Streamlit",
  page_icon="📊",
)

st.sidebar.title("Navegação")
pagina = st.sidebar.selectbox("Escolha a página", 
                              ["Introdução", "Horas estudadas X Nota", "Escolaridade dos pais X Nota", "Motivação X Nota", "Análise 4", "Análise 5", "Análise 6"])

if pagina == "Introdução":
    st.title("Bem-vindo ao Dashboard de Desempenho Estudantil")

    st.subheader("📘 Objetivo do Dashboard")
    st.write(
        "Este dashboard analisa fatores que influenciam o desempenho acadêmico dos estudantes, "
        "permitindo visualizar relações entre hábitos de estudo, condições familiares, motivação, "
        "ambiente escolar e outros aspectos presentes no conjunto de dados *Student Performance Factors*."
    )

    st.subheader("🧭 Navegação entre as Seções")
    st.write(
        "Use a barra lateral para acessar cada análise. Cada página apresenta um tipo específico de "
        "visualização, facilitando a exploração dos dados. As seções incluem relações entre horas de estudo, "
        "escolaridade dos pais, motivação e outros fatores relevantes para o desempenho."
    )

    st.subheader("📈 Como os Filtros Influenciam os Dados")
    st.write(
        "Alguns gráficos permitem interação através de filtros, como seleção de níveis de motivação ou "
        "exibição de valores. Ao alterar os filtros, os gráficos são atualizados automaticamente, "
        "permitindo observar padrões e comparar cenários específicos."
    )

    st.subheader("🔍 Pré-visualização dos Dados")
    st.write("Abaixo você pode ver as primeiras linhas do dataset utilizado:")
    st.write(df.head())

elif pagina == "Horas estudadas X Nota":
    st.title("Horas estudadas X Nota")
    st.subheader("Relação entre horas de estudo e nota")
    st.write("Este gráfico mostra como as horas de estudo se relacionam com a nota final do exame. Cada ponto representa um estudante, dividido por gênero. O tamanho do ponto indica as horas de sono, permitindo observar se estudantes mais descansados têm desempenho diferente. O objetivo é identificar padrões de estudo e desempenho.")

    fig = px.scatter(
    df,
    x="Hours_Studied",
    y="Exam_Score",
    color="Gender",
    size="Sleep_Hours",
    hover_data=["Extracurricular_Activities", "Internet_Access"],
    title="Horas de estudo X Nota do exame"
    )

    fig.update_layout(
        xaxis_title="Horas de estudo",
        yaxis_title="Nota do exame"
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
elif pagina == "Escolaridade dos pais X Nota":
    st.title("Escolaridade dos pais X Nota")
    st.subheader("Distribuição das notas por escolaridade dos pais")
    st.write("Este boxplot compara as notas dos alunos conforme o nível de escolaridade dos pais. A visualização mostra como a formação familiar pode influenciar o desempenho acadêmico, permitindo identificar se níveis mais altos de educação dos pais estão associados a melhores resultados dos filhos.")

    fig = px.box(
        df,
        x="Parental_Education_Level",
        y="Exam_Score",
        color="Parental_Education_Level",
        title="Nota do exame por escolaridade dos pais"
    )

    fig.update_layout(
        xaxis_title="Escolaridade dos pais",
        yaxis_title="Nota do exame"
    )

    st.plotly_chart(fig, use_container_width=True)

elif pagina == "Motivação X Nota":
    st.title("Motivação X Nota")
    st.subheader("Impacto dos níveis de motivação no desempenho")
    st.write("Este gráfico apresenta a média das notas conforme o nível de motivação dos estudantes. Os filtros permitem selecionar quais níveis exibir. A análise busca demonstrar o impacto da motivação no desempenho acadêmico, observando se alunos mais motivados tendem a ter notas superiores.")

    st.write("Use o filtro abaixo para selecionar os níveis de motivação incluídos no gráfico.")

    niveis = sorted(df["Motivation_Level"].unique())

    niveis_escolhidos = st.multiselect(
        "Selecione os níveis de motivação:",
        options=niveis,
        default=niveis
    )

    df_filtrado = df[df["Motivation_Level"].isin(niveis_escolhidos)]
    media_motivacao = (
        df_filtrado.groupby("Motivation_Level")["Exam_Score"]
        .mean()
        .reset_index()
        .sort_values(by="Motivation_Level")
    )

    fig = px.bar(
        media_motivacao,
        x="Motivation_Level",
        y="Exam_Score",
        color="Motivation_Level",
        title="Desempenho Médio por Nível de Motivação",
    )
    
    fig.update_layout(
        xaxis_title="Nível de Motivação",
        yaxis_title="Média da Nota"
    )

    mostrar = st.checkbox("Mostrar valores nas barras")
    if mostrar:
        fig.update_traces(texttemplate="%{y:.1f}", textposition="outside")


    st.plotly_chart(fig, use_container_width=True)

elif pagina == "Análise 4":
    st.title("Página de Análise 4")
    # gráfico 4

elif pagina == "Análise 5":
    st.title("Página de Análise 5")
    # gráfico 5

elif pagina == "Análise 6":
    st.title("Página de Análise 6")
    # gráfico 6