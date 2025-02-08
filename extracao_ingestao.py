import pandas as pd
from pyspark.sql import SparkSession

# Caminho para o arquivo CSV
file_path = 'dados_saude_publica.csv'

# Ler o arquivo CSV com Pandas
data = pd.read_csv(file_path)

# Criar sessão Spark
spark = SparkSession.builder.appName('EngenhariaDados').getOrCreate()

# Carregar dados no Spark DataFrame
df = spark.read.csv(file_path, header=True, inferSchema=True)