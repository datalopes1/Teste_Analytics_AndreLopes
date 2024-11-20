import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime
import random
from tqdm import tqdm
import sqlite3

fake = Faker('pt_BR')
Faker.seed(42)
random.seed(42)

cat_produtos = {
    'Periféricos': [
        ('Mouse', (10, 200)),
        ('Teclado', (25, 800)),
        ('Headset', (50, 500)),
        ('Webcam', (50, 280)),
        ('Joystick', (120, 500)),
        ('Adaptador Wi-Fi', (80, 100))
    ],
    'Desktop': [
        ('MOBA Setup', (2000, 10000)),
        ('HOME OFFICE Setup', (1500, 3000)),
        ('GAMER Setup', (4000, 30000))
    ],
    'Laptop': [
        ('BASIC Notebook', (1800, 2500)),
        ('PRO Notebook', (2500, 4000)),
        ('GAMER Notebook', (4000, 12000))
    ]
}

def generate_dataset(n_entries: int, start_date: str, end_date: str) -> pd.DataFrame:
    
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    dados = []

    for id in tqdm(range(1, n_entries + 1), desc = "Gerando o dataset", unit = "registro"):
        data = fake.date_between(start_date, end_date)

        categoria = random.choice(list(cat_produtos.keys()))
        produto, faixa_preco = random.choice(cat_produtos[categoria])

        if categoria in ['Desktop', 'Laptop']:
            quantidade = np.random.choice([1, 1, 1, 2, 3], p = [0.9, 0.025, 0.025, 0.025, 0.025])
        else:
            quantidade = np.random.choice([1, 2, 3, 4, 5], p = [0.7, 0.075, 0.075, 0.075, 0.075])

        preco = round(random.uniform(faixa_preco[0], faixa_preco[1]), 2)

        dados.append({
            'Id': id,
            'Data': data,
            'Produto': produto,
            'Categoria': categoria,
            'Quantidade': quantidade,
            'Preço': preco
        })

    df = pd.DataFrame(dados)
    return df

if __name__ == "__main__":
    n_entries = int(input((f"Insira o número de registros: ")))
    start_date = str(input((f"Insira a data inicial no formato YYYY-MM-DD: ")))
    end_date = str(input((f"Insira a data inicial no formato YYYY-MM-DD: ")))
    db_file = 'data/database.db'

    df = generate_dataset(n_entries, start_date, end_date)

    with sqlite3.connect(db_file) as conn:
        df.to_sql("vendas", conn, if_exists="replace", index = False)
        print(f"Arquivo .db com {n_entries} registros salvo na pasta 'data/'")
