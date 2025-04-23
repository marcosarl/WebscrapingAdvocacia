# Webscraping para extração de nomes e sites de escritórios de advocacia

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd
import os

# Configura o navegador (modo invisível)
options = Options()
options.add_argument("--headless=new")  # Novo modo headless do Chrome
driver = webdriver.Chrome(options=options)

# Inicializa variáveis
pagina = 21  # Continue de onde parou
arquivo_csv = "nomes_escritorios.csv"
nomes_total = set()

# Se já existir, carrega os nomes existentes
if os.path.exists(arquivo_csv):
    df_existente = pd.read_csv(arquivo_csv)
    nomes_total = set(df_existente["Nome"])

while True:
    url = f"https://analise.com/dna/busca?city=[71072,71072]&page={pagina}"
    print(f"\n🔎 Página {pagina}: {url}")

    driver.get(url)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'h3.text-xl'))
        )
        time.sleep(2)
    except:
        print("🚧 Nenhum escritório encontrado ou tempo excedido. Fim da coleta.")
        break

    cards = driver.find_elements(By.CSS_SELECTOR, 'h3.text-xl')
    nomes = [card.text.strip() for card in cards if card.text.strip()]

    if not nomes:
        print("🚧 Nenhum escritório encontrado. Fim da coleta.")
        break

    for nome in nomes:
        if nome not in nomes_total:
            nomes_total.add(nome)
            print(f"✔️ {nome}")

    df = pd.DataFrame(sorted(nomes_total), columns=["Nome"])
    df.to_csv(arquivo_csv, index=False, encoding="utf-8")

    pagina += 1
    time.sleep(1)

# Finaliza o navegador
driver.quit()
print(f"\n📄 Extração concluída! Total de escritórios: {len(nomes_total)}")
print(f"📂 Dados salvos em: {arquivo_csv}")