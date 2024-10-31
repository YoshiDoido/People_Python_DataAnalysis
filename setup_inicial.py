import pandas as pd

# Para criação de gráficos
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# Para preparação dos dados
from sklearn.model_selection import train_test_split #divisão dos dados para treinamento e teste
from sklearn.preprocessing import LabelEncoder   #para transformar Strings em números inteiros
from sklearn.preprocessing import StandardScaler #para a padronização dos dados

# Para criação de redes neurais
from sklearn.neural_network import MLPClassifier #rede neural
from sklearn.metrics import accuracy_score       #avaliação do modelo
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Para gravação de um modelo gerado por aprendizagem de máquina
from tensorflow.keras.models import load_model

base = pd.read_xlsx('data\raw\desenhar_arvore_binaria_mountains_beach.xlsx')