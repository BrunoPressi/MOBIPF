import pandas as pd
import random
from datetime import datetime, timedelta

N = 5000

regioes = {
    "Norte":  {"lat": (-25.41, -25.38), "lon": (-49.29, -49.24)},
    "Sul":    {"lat": (-25.48, -25.44), "lon": (-49.32, -49.28)},
    "Leste":  {"lat": (-25.44, -25.41), "lon": (-49.25, -49.20)},
    "Oeste":  {"lat": (-25.44, -25.41), "lon": (-49.34, -49.30)},
    "Centro": {"lat": (-25.44, -25.41), "lon": (-49.29, -49.26)}
}


ruas = [
    "Av. Brasil", "Rua de algum lugar", "Av. Presidente Vargas",
    "Av. Dr Álvaro Severo de Miranda", "Av. Scarpelini Ghezi"
]

tipos_acidente = ["Colisão", "Atropelamento", "Capotamento", "Queda de moto"]
tipos_veiculo = ["Carro", "Moto", "Ônibus", "Caminhão", "Bicicleta"]

climas = ["Seco", "Chuva", "Neblina"]
superficie = ["Seca", "Molhada", "Escorregadia"]

dados = []

data_inicio = datetime(2005, 1, 1)
data_fim = datetime(2025, 12, 31)

for i in range(1, N + 1):
    regiao = random.choice(list(regioes.keys()))
    lat = random.uniform(*regioes[regiao]["lat"])
    lon = random.uniform(*regioes[regiao]["lon"])


    data = data_inicio + timedelta(
        days=random.randint(0, (data_fim - data_inicio).days)
    )

    hora = random.randint(0, 23)
    minuto = random.choice([0, 15, 30, 45])

    tipo = random.choices(
        tipos_acidente,
        weights=[0.55, 0.20, 0.10, 0.15]
    )[0]

    houve_outros_veiculos = random.choice(["Sim", "Não"])
    qtd_veiculos = random.randint(2, 4) if houve_outros_veiculos == "Sim" else 1

    havia_ocupantes = random.choice(["Sim", "Não"])
    qtd_ocupantes = random.randint(2, 5) if havia_ocupantes == "Sim" else 1

    teste_bafometro = random.choices(
        ["Sim", "Não"], weights=[0.35, 0.65]
    )[0]

    resultado_bafometro = (
        random.choice(["Negativo", "Positivo"])
        if teste_bafometro == "Sim"
        else "Não realizado"
    )

    possui_habilitacao = random.choices(
        ["Sim", "Não"], weights=[0.9, 0.1]
    )[0]

    clima = random.choices(
        climas, weights=[0.65, 0.30, 0.05]
    )[0]

    iluminacao = "Noite" if hora < 6 or hora > 18 else "Dia"
    clima_luminosidade = f"{clima} / {iluminacao}"

    # ===============================
    # ENVOLVIDOS / FERIDOS / ÓBITOS
    # ===============================

    # ENVOLVIDOS (inclui condutor)
    if tipo == "Atropelamento":
        envolvidos = random.randint(2, 5)
    else:
        envolvidos = random.choices(
            [1, 2, 3, 4, 5],
            weights=[0.40, 0.30, 0.18, 0.08, 0.04]
        )[0]

    # FERIDOS
    feridos = random.choices(
        list(range(envolvidos + 1)),
        weights=[0.35] + [0.65 / envolvidos] * envolvidos
    )[0]

    # ÓBITOS (evento raro)
    if feridos > 0:
        obitos = random.choices(
            list(range(feridos + 1)),
            weights=[0.97] + [0.03 / feridos] * feridos
        )[0]
    else:
        obitos = 0

    dados.append({
        "TIPO DE ACIDENTE": tipo,
        "DATA": data.date(),
        "HORA": f"{hora:02d}:{minuto:02d}",
        "REGIÃO": regiao,
        "COORDENADA GEOGRÁFICA": f"{lat:.6f}, {lon:.6f}",
        "SITUAÇÃO CLIMÁTICA/LUMINOSIDADE": clima_luminosidade,
        "CONDIÇÕES DA SUPERFÍCIE DE ROLAMENTO": random.choice(superficie),
        "POSSUI SINALIZAÇÃO HORIZONTAL": random.choice(["Sim", "Não"]),
        "POSSUI SINALIZAÇÃO VERTICAL": random.choice(["Sim", "Não"]),
        "PRÓXIMO A EQUIPO ELETRÔNICO": random.choice(["Sim", "Não"]),
        "HOUVE OUTROS VEÍCULOS ENVOLVIDOS": houve_outros_veiculos,
        "QUANTOS VEÍCULOS": qtd_veiculos,
        "HAVIA OUTROS OCUPANTES NO VEÍCULO": havia_ocupantes,
        "QUANTOS OCUPANTES": qtd_ocupantes,

        "ENVOLVIDOS": envolvidos,
        "FERIDOS": feridos,
        "ÓBITOS": obitos,

        "FOI REALIZADO O TESTE DE BAFÔMETRO": teste_bafometro,
        "QUAL O RESULTADO": resultado_bafometro,
        "POSSUI HABILITAÇÃO": possui_habilitacao,
        "VEÍCULO TIPO": random.choice(tipos_veiculo),
        "HOUVE DANOS AO PATRIMÔNIO PÚBLICO?": random.choice(["Sim", "Não"]),
        "HOUVE DANOS AO MEIO AMBIENTE?": random.choices(
            ["Sim", "Não"], weights=[0.05, 0.95]
        )[0]
    })

df = pd.DataFrame(dados)
df.to_csv("sinistros_ficticios.csv", index=False, encoding="utf-8-sig")

print("Arquivo 'sinistros_ficticios.csv' gerado com sucesso!")
