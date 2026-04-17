# 📊 Projeto de Machine Learning - Previsão de CO(GT)

## 📌 Descrição

Este projeto tem como objetivo desenvolver um pipeline completo de Machine Learning para prever a concentração de Monóxido de Carbono (CO(GT)) com base no dataset **AirQualityUCI**.

O projeto contempla desde a análise exploratória dos dados até a disponibilização do modelo treinado por meio de uma API utilizando Flask.

---

## 🧠 Tecnologias Utilizadas

* Python 3.10
* Pandas
* NumPy
* Scikit-learn
* Flask
* Docker (opcional)

---

## 📁 Estrutura do Projeto

```
📦 projeto/
 ├── air_quality_ml.ipynb   # Notebook com análise e treinamento
 ├── modelo.pkl            # Modelo treinado (Random Forest)
 ├── app.py                # API Flask
 ├── requirements.txt      # Dependências
 ├── Dockerfile            # Configuração Docker
 ├── docker-compose.yml    # Orquestração Docker
 └── README.md             # Documentação
```

---

## 🔍 Etapas do Projeto

### 1. Análise Exploratória

* Estrutura dos dados
* Estatísticas descritivas
* Identificação de valores ausentes
* Correlação entre variáveis

### 2. Tratamento de Dados

* Remoção de colunas irrelevantes
* Substituição de valores inválidos (-200)
* Tratamento de dados ausentes

### 3. Modelagem

Foram utilizados dois modelos:

* Regressão Linear
* Random Forest Regressor

### 4. Avaliação

Métricas utilizadas:

* MAE (Erro Absoluto Médio)
* MSE (Erro Quadrático Médio)
* RMSE
* R²

📌 O modelo **Random Forest** apresentou melhor desempenho e foi escolhido como modelo final.

---

## 🤖 API de Previsão

A API foi desenvolvida utilizando Flask e permite realizar previsões da concentração de CO(GT).

### ▶️ Como executar (forma recomendada)

```bash
pip install -r requirements.txt
python app.py
```

A API estará disponível em:

```
http://127.0.0.1:5000
```

---

## 🔗 Endpoint

### POST `/predict`

Recebe um JSON com os dados de entrada e retorna a previsão.

### 📥 Exemplo de requisição:

```json
{
  "PT08.S1(CO)": 1360,
  "NMHC(GT)": 150,
  "C6H6(GT)": 11.9,
  "PT08.S2(NMHC)": 1046,
  "NOx(GT)": 166,
  "PT08.S3(NOx)": 1056,
  "NO2(GT)": 113,
  "PT08.S4(NO2)": 1692,
  "PT08.S5(O3)": 1268,
  "T": 13.6,
  "RH": 48.9,
  "AH": 0.7578
}
```

### 📤 Exemplo de resposta:

```json
{
  "predicted_CO": 2.5,
  "classificacao": "bom"
}
```

---

## 📊 Classificação da Qualidade do Ar

A classificação é feita com base no valor previsto de CO(GT):

* **Bom**: ≤ 4
* **Médio**: > 4 e ≤ 9
* **Ruim**: > 9

---

## 🐳 Execução com Docker (Opcional)

```bash
docker-compose up --build
```

⚠️ Observação: Dependendo da versão do Docker, pode haver incompatibilidade com `docker-compose`.

---

## 📌 Considerações Finais

Este projeto demonstra a aplicação prática de técnicas de Machine Learning em um problema real de previsão ambiental, integrando análise de dados, modelagem preditiva e desenvolvimento de APIs.

---

## 👨‍💻 Autor

Thiago Dellano Machado de Oliveira | 24101272
