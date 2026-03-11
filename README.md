# 🌾 Análise de Impacto Econômico da Produção de Soja no RS (infrabdT3)

## 🎯 O Problema e o Contexto

O agronegócio é um dos pilares da economia brasileira, mas como medir o impacto real e direto de uma cultura específica no desenvolvimento local?

Este projeto de análise de dados busca responder a essa pergunta investigando a correlação entre a produção agrícola de soja e o Produto Interno Bruto (PIB) dos municípios do Rio Grande do Sul. Através do cruzamento de dados públicos do IBGE e do Governo do Estado, a aplicação extrai, armazena e consulta grandes volumes de informações para identificar se o sucesso da safra se traduz diretamente em crescimento econômico para as cidades produtoras.

---

## 🏗️ Arquitetura e Tecnologias

Para suportar a ingestão e a análise dos dados, o projeto utiliza um ecossistema misto de bancos de dados relacionais e não-relacionais, orquestrados via código:

- **Python**: Utilizado para a arquitetura base, processamento e manipulação dos dados.

- **MongoDB**: Banco de dados NoSQL para armazenamento flexível das estruturas de dados.

- **Microsoft Azure / SQL**: Utilizado para a realização das consultas analíticas (queries) e cruzamento dos indicadores.

---

## 📊 Fontes de Dados

Os dados utilizados neste projeto são de domínio público e foram extraídos das seguintes fontes oficiais:

### Produto Interno Bruto (PIB)

Dados oficiais do IBGE, disponibilizados pelo Departamento de Economia e Estatística do RS.

🔗 **Acessar Dataset do PIB**  
https://dados.rs.gov.br/dataset/dee-4571/resource/0c1799a1-6d61-40db-9f45-0e8bbd3873d6

### Produção Agrícola

Dados oficiais do Governo do Estado do RS sobre a colheita e plantio.

🔗 **Acessar Dataset da Produção Agrícola**  
https://dados.rs.gov.br/dataset/dee-1110

---

## 📈 Resultados da Análise

O cruzamento de dados utilizando consultas SQL revelou insights valiosos sobre a economia gaúcha:

### 📍 O Caso de Dom Pedrito

O município, consolidado como o maior produtor de soja do estado, demonstrou uma relação direta e proporcional entre as safras recordes de soja e o crescimento expressivo do seu PIB municipal.

### 🔄 Padrão Econômico Regional

Ao expandir as consultas para outros municípios com forte presença do agronegócio, os gráficos indicaram que a correlação positiva se mantém. Cidades que aumentam sua produção de soja invariavelmente apresentam saltos em seus indicadores de riqueza.

### 🚀 Conclusão

Os dados comprovam o papel estratégico da soja não apenas como commodity de exportação, mas como um motor primário de desenvolvimento econômico e social nas regiões onde sua produção é expressiva.

---

## 👨🏻‍💻 Autoria

Desenvolvido por **Lucas Volkweis** como **Trabalho 3 (T3)** para a disciplina de **Infraestrutura de Dados (PUCRS)**.
