# Divisão das pastas

___________

O arquivo Weights é o conjunto de pesos para o modelo LSTM. As pastas LSTM_Generated e RBM_Generated possuem os resultados dos modelos.

Para o LSTM_Generated foi se tentado gerar músicas usando sempre a nota de maior probabilidade, esses arquivos se encontram na pasta LSTM_ARGMAX.
As músicas geradas com base na probabilidade da distribuição se encontram na pasta LSTM_PROB.

Para o RBM_Generated foi se tentado gerar músicas usando 10 notas de conhecimento prévio, esses arquivos se encontram na pasta RBM_Sklearn_10.
As músicas geradas com 15 notas de conhecimento prévio se encontram na pasta RBM_Sklearn_15.
