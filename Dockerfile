# Use a imagem base
FROM continuumio/miniconda3:latest

# Crie e defina o diretório de trabalho
WORKDIR /opt/ml

# Instale as dependências necessárias usando conda
RUN conda install -y --quiet \
      pandas matplotlib plotly seaborn scikit-learn tensorflow

# Copie os arquivos do projeto para o contêiner
COPY setup_inicial.py ./
COPY data/raw /opt/ml/data/raw

# Defina o comando para iniciar o script
CMD ["python", "/opt/ml/setup_inicial.py"]
