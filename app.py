from flask import Flask, render_template, request
import numpy as np
import pandas as pd
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
import seaborn as sns
import matplotlib.pyplot as plt
from io import BytesIO
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Receber valores de entrada do usuário
            expected_results = list(map(int, request.form['expected_results'].split(',')))
            predicted_results = list(map(int, request.form['predicted_results'].split(',')))

            # Verificar se as listas têm o mesmo tamanho
            if len(expected_results) != len(predicted_results):
                return render_template('index.html', error="O número de resultados esperados e previstos deve ser igual.")

            # Cálculo de métricas
            accuracy = accuracy_score(expected_results, predicted_results)
            precision = precision_score(expected_results, predicted_results, average='binary')
            recall = recall_score(expected_results, predicted_results, average='binary')
            f1 = f1_score(expected_results, predicted_results, average='binary')

            # Geração de matriz de confusão
            conf_matrix = confusion_matrix(expected_results, predicted_results)
            fig, ax = plt.subplots()
            sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", ax=ax)
            ax.set_xlabel("Predicted")
            ax.set_ylabel("Expected")

            # Converter gráfico em imagem base64 para exibir no HTML
            img = BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            plot_url = base64.b64encode(img.getvalue()).decode()

            return render_template('index.html', accuracy=accuracy, precision=precision,
                                   recall=recall, f1=f1, plot_url=plot_url)

        except ValueError:
            return render_template('index.html', error="Por favor, insira apenas números separados por vírgula.")
    
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
