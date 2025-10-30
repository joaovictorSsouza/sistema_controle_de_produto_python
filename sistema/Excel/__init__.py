import pandas as pd
import os

def salvar_excel(lista_dados, nome_arquivo):
    if not lista_dados:
        print("Nenhum dado para salvar")
        return
    
    df = pd.DataFrame(lista_dados)

    if os.path.exists(nome_arquivo):
        df_existente = pd.read_excel(nome_arquivo)
        df = pd.concat([df_existente, df], ignore_index=True)

    df.to_excel(nome_arquivo, index=False)
    print(f"Dados salvos em {nome_arquivo} com sucesso!")

    