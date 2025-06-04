import pandas as pd
from pymongo import MongoClient
import unicodedata
import warnings

# Suprimir avisos
warnings.filterwarnings("ignore")

# Conexão com o MongoDB (CosmosDB)
connection_string = "mongodb+srv://infra321:admin#333@infra-t3-mongo.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000"
client = MongoClient(connection_string, serverSelectionTimeoutMS=5000)

try:
    # Nome do arquivo CSV
    csv_file = "C:\\Users\\Home\\Downloads\\dee-1111.csv"

    # Definir o cabeçalho manualmente
    colunas_base = ["Município", "ibge", "latitude", "longitude"]
    anos = range(1974, 2024)
    colunas_anos = [f"Agricultura/Culturas Temporárias/Soja/Área Colhida {ano} (ha)" for ano in anos]
    colunas = colunas_base + colunas_anos

    # Ler o CSV
    df = pd.read_csv(
        csv_file,
        sep=",",  # Alterado para vírgula
        encoding="ISO-8859-1",
        quotechar='"',
        skiprows=1,  # Ignorar a primeira linha problemática
        names=colunas,
        skipinitialspace=True
    )

    # Diagnosticar o DataFrame
    print("Cabeçalho do DataFrame:")
    print(df.head())
    print("Dimensões do DataFrame:", df.shape)

    # Filtrar linhas válidas
    df = df.dropna(subset=["ibge", "latitude", "longitude"])

    # Converter colunas específicas para os tipos corretos
    df["ibge"] = pd.to_numeric(df["ibge"], errors="coerce")
    df["latitude"] = pd.to_numeric(df["latitude"], errors="coerce")
    df["longitude"] = pd.to_numeric(df["longitude"], errors="coerce")

    # Tratar valores ausentes
    df = df.dropna()

    # Conectar ao MongoDB e preparar a coleção
    db = client["meu_banco"]
    collection = db["AreaProduzida"]

    # Converter os dados do DataFrame para uma lista de dicionários
    data = []
    for idx, row in df.iterrows():
        try:
            document = {
                "id": idx + 1,
                "Municipio": str(row["Município"]),
                "IBGE": int(row["ibge"]),
                "Latitude": float(row["latitude"]),
                "Longitude": float(row["longitude"]),
                "AreasColhidas": {
                    str(ano): row[f"Agricultura/Culturas Temporárias/Soja/Área Colhida {ano} (ha)"]
                    for ano in anos
                }
            }
            data.append(document)
        except Exception as e:
            print(f"Erro ao processar a linha {idx}: {e}")
            print(row)

    # Inserir no MongoDB
    if not data:
        raise ValueError("A lista 'data' está vazia. Não há documentos para inserir no MongoDB.")
    else:
        result = collection.insert_many(data)
        print(f"{len(result.inserted_ids)} documentos inseridos com sucesso!")

except Exception as e:
    print(f"Erro ao inserir os dados: {e}")

finally:
    client.close()
    print("Conexão com MongoDB encerrada.")