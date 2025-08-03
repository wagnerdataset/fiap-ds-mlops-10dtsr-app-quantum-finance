# 💻 Predição de Score de Crédito com Streamlit

Este projeto implementa uma aplicação em Streamlit que consome uma API hospedada na AWS (Lambda + API Gateway), responsável por prever a **classificação de crédito** de um usuário com base em seus dados financeiros e históricos.

## 🧠 Modelo

O modelo de machine learning foi treinado para classificar a pontuação de crédito em três categorias:

| Score | Classificação |
|-------|----------------|
| 0     | Poor           |
| 1     | Standard       |
| 2     | Good           |

## 🚀 Tecnologias

- [Streamlit](https://streamlit.io/)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [API Gateway](https://aws.amazon.com/api-gateway/)
- [Scikit-learn](https://scikit-learn.org/)
- [XGBoost](https://xgboost.ai/)
- [Python 3.10+](https://www.python.org/)

