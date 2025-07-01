import csv
import random
from datetime import datetime, timedelta
import pandas as pd

def gerar_dados_sla(num_registros=1000):
    """Gera dados simulados de SLA"""
    
    # Listas de dados fictícios
    tipos_servico = ["Suporte Técnico", "Manutenção", "Atendimento ao Cliente", 
                    "Solicitação de Serviço", "Incidente Crítico"]
    categorias = ["Alta Prioridade", "Média Prioridade", "Baixa Prioridade"]
    status = ["Resolvido", "Pendente", "Em Andamento", "Cancelado"]
    departamentos = ["TI", "RH", "Financeiro", "Operações", "Comercial"]
    clientes = ["Cliente A", "Cliente B", "Cliente C", "Cliente D", "Cliente E"]
    
    # Gerar datas aleatórias nos últimos 6 meses
    data_atual = datetime.now()
    data_inicial = data_atual - timedelta(days=180)
    
    dados = []
    
    for _ in range(num_registros):
        # Datas aleatórias
        data_abertura = data_inicial + timedelta(days=random.randint(0, 180))
        tempo_resolucao = random.randint(1, 240)  # em horas
        sla_contratado = random.choice([24, 48, 72, 96])  # horas
        
        # Verificar se está dentro do SLA
        dentro_sla = tempo_resolucao <= sla_contratado
        
        # Adicionar alguns outliers
        if random.random() < 0.1:  # 10% de chance de ser outlier
            tempo_resolucao = sla_contratado + random.randint(1, 48)
            dentro_sla = False
        
        dados.append({
            "ID": random.randint(1000, 9999),
            "Tipo_Servico": random.choice(tipos_servico),
            "Categoria": random.choice(categorias),
            "Status": random.choice(status),
            "Departamento": random.choice(departamentos),
            "Cliente": random.choice(clientes),
            "Data_Abertura": data_abertura.strftime("%Y-%m-%d"),
            "Hora_Abertura": f"{random.randint(8, 18)}:{random.randint(0, 59):02d}",
            "Tempo_Resolucao_Horas": tempo_resolucao,
            "SLA_Contratado_Horas": sla_contratado,
            "Dentro_SLA": "Sim" if dentro_sla else "Não",
            "Satisfacao_Cliente": random.randint(1, 5),  # escala de 1-5
            "Complexidade": random.choice(["Baixa", "Média", "Alta"]),
            "Responsavel": f"Tecnico_{random.randint(1, 20)}"
        })
    
    return dados

def exportar_para_csv(dados, nome_arquivo="dados_sla_4.csv"):
    """Exporta os dados para um arquivo CSV"""
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=dados[0].keys())
        escritor.writeheader()
        escritor.writerows(dados)
    
    print(f"Dados exportados com sucesso para {nome_arquivo}")

def criar_dataset_para_powerbi():
    """Função principal para criar o dataset para Power BI"""
    print("Gerando dados de SLA...")
    dados_sla = gerar_dados_sla(1500000)  # Gera 1500 registros
    exportar_para_csv(dados_sla)
    
    # Opcional: Carregar os dados em um DataFrame para análise rápida
    df = pd.DataFrame(dados_sla)
    print("\nResumo dos dados gerados:")
    print(f"Total de registros: {len(df)}")
    print(f"Percentual dentro do SLA: {df[df['Dentro_SLA'] == 'Sim'].shape[0]/len(df)*100:.2f}%")
    
    return df

# Executar o programa
if __name__ == "__main__":
    df_sla = criar_dataset_para_powerbi()