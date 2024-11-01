# Programa de Otimização de Ofertas Comerciais para Passagens Aéreas
**English en-us VERSION BELOW**

## Contexto e Motivação
Uma companhia aérea busca expandir o número de passageiros em seu programa de fidelidade, que inclui três níveis de cartões: **Ametista**, **Ônix** e **Rubi**, sendo o Rubi o de maior benefício. Com uma base de novos clientes fornecida pelo time de marketing, o time comercial, devido a recursos limitados, precisa otimizar as abordagens focando nos clientes com maior probabilidade de adesão ao programa.

### Objetivo
Identificar a probabilidade de adesão de cada cliente aos níveis Ametista, Ônix e Rubi, ajudando o time comercial a realizar ofertas personalizadas, aumentando as taxas de conversão e otimizando os recursos de vendas.

## Estrutura do Projeto

### Coleta e Limpeza de Dados
- **Padronização** de variáveis e formatação dos dados.
- **Tratamento de dados ausentes** (NA) e **remoção de outliers** para melhorar a qualidade dos dados.
- **Limpeza** dos dados para assegurar a consistência nas análises subsequentes.

### Análise Descritiva e Visual
- Estatísticas descritivas para explorar o perfil dos clientes.
- Visualizações para insights iniciais, como segmentações e frequências de variáveis.

### Feature Engineering
- Criação de novas variáveis, como frequência de voos com acompanhantes, total de pontos resgatados, entre outras.
- Extração de insights para enriquecer o modelo preditivo.

### Modelagem Preditiva e Avaliação
- Desenvolvimento de um modelo de **classificação** para prever a probabilidade de adesão a cada nível do programa.
- Avaliação e experimentação com diferentes técnicas (Decision Trees, Random Forest, Gradient Boosting).
- **AUC e Precision-Recall** como métricas de performance do modelo.
- Seleção do modelo final baseado na **interpretabilidade** e na **precisão preditiva**.

### Implementação e Deploy
- Deploy do modelo em um dashboard interativo utilizando **Streamlit Cloud**.
- Dashboards para visualizar a probabilidade de adesão por perfil de cliente e insights em tempo real.

## Planejamento da Solução

### Problema de Negócio
A companhia aérea deseja aumentar o número de adesões ao programa de fidelidade através de abordagens otimizadas. A solução envolve a previsão da probabilidade de cada cliente assinar um dos três níveis de cartão (Ametista, Ônix, Rubi) e seleção de perfis-alvo para cada oferta.

### Relatório Final
1. Identificação dos clientes com maior probabilidade de adesão aos níveis Ametista, Ônix e Rubi.
2. Distribuição percentual da probabilidade de assinatura para os três níveis.
3. Características mais relevantes para a adesão ao programa.
4. Estimativa de receita com a conversão dos clientes para os diferentes níveis de fidelidade.
5. Estratégias de marketing recomendadas para melhorar a taxa de conversão.

### Variáveis Utilizadas
1. **loyalty_number** - Identificador único do cliente.
2. **year** e **month** - Data de registro da atividade.
3. **flights_booked** - Número de voos reservados.
4. **flights_with_companions** - Voos reservados com acompanhantes.
5. **total_flights** - Total de voos realizados.
6. **distance** - Distância total voada.
7. **points_accumulated** e **points_redeemed** - Pontos acumulados e resgatados.
8. **dollar_cost_points_redeemed** - Valor monetário dos pontos resgatados.
9. **country, province, city, postal_code** - Localização do cliente.
10. **gender, education, salary, marital_status** - Dados demográficos.
11. **loyalty_card, clv, enrollment_type** - Tipo de cartão, valor de vida do cliente e tipo de inscrição.
12. **enrollment_year e enrollment_month** - Data de inscrição no programa.

### Ferramentas Utilizadas
- **Python v3.12** e **VS Code** para desenvolvimento.
- **Pandas, Numpy** para manipulação de dados.
- **Scikit-Learn, Matplotlib e Seaborn** para modelagem e visualização.
- **Streamlit** para deploy da aplicação.
- **Pickle** para serialização do modelo.

### Insights e Resultados de Negócio
- A taxa de conversão para clientes "Rubi" é superior em 34,64%.
- Receita total estimada de R$12.168.750,00 e lucro de R$9.735.000,00 com conversões para os três tipos de cartões.
- O cartão "Rubi" representa o maior potencial de lucro marginal, com uma receita média estimada de R$51,96 por cliente.

### Estratégias de Engajamento e Retenção
- **Benefícios Personalizados:** Ofertas específicas para cada nível de cartão, como descontos e upgrades de classe.
- **Parcerias Estratégicas:** Alianças com empresas complementares para proporcionar descontos e experiências exclusivas.
- **Ofertas Sazonais:** Promoções durante datas estratégicas para atrair novos clientes ao programa.
- **Feedback e Melhoria Contínua:** Coleta de feedback para ajustes nos benefícios de cada nível.
- **Campanhas de Referência:** Incentivos para clientes que indicam amigos ao programa de fidelidade.

### Conclusão
O projeto fornece uma solução eficaz para o time comercial da companhia aérea otimizar as abordagens com clientes, aumentar as taxas de adesão ao programa de fidelidade e maximizar a receita esperada. Com os insights obtidos, o time de marketing pode agora personalizar as campanhas e maximizar o impacto dos esforços comerciais. Deploy do projeto disponivel no [Link](https://flight-project.streamlit.app/)

---

## Optimization of Commercial Offers for Airline Tickets

### Business Problem
An airline seeks to expand its loyalty program, which includes three membership levels: **Amethyst**, **Onyx**, and **Ruby**. Given limited resources, the sales team needs to focus on customers most likely to join the program.

### Objective
Identify the probability of each customer subscribing to a specific loyalty tier, enabling targeted offers, increasing conversion rates, and optimizing sales efforts.

### Project Phases
- **Data Collection & Cleaning**
- **Descriptive Analysis & Feature Engineering**
- **Predictive Modeling & Evaluation**
- **Implementation and Dashboard Deployment**

### Solution Planning
#### Key Business Insights
- Identify customers most likely to join each card level.
- Analyze distribution and key characteristics influencing loyalty.
- Estimate revenue impact with targeted conversion strategies.

#### Tools and Technologies
- **Python, Streamlit, Scikit-Learn, Pickle** for data processing, model deployment, and visualization.

#### Engagement & Retention Strategies
- **Personalized Benefits:** Tailored offers for each membership level.
- **Seasonal Offers:** Promotions during specific periods to increase membership sign-ups.

This project equips the sales and marketing teams with precise insights to improve loyalty program conversion rates and revenue, paving the way for more efficient customer engagement and retention. Project deployment available on [Link](https://flight-project.streamlit.app/)
