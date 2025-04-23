# Web Scraping de Escritórios de Advocacia

Este projeto utiliza **Web Scraping** para coletar dados de escritórios de advocacia, como nomes e sites, de uma página específica da plataforma [Análise](https://analise.com/dna/).

## 🛠️ Funcionalidade

O código foi desenvolvido para automatizar a coleta de dados de forma rápida e eficiente. Ele percorre várias páginas da plataforma, extraindo as informações dos escritórios, e armazena esses dados em um arquivo CSV.

## 🚀 Como Usar

1. **Pré-requisitos:**
   - Python 3.x
   - Bibliotecas: `selenium`, `pandas`, `chromedriver` (versão compatível com seu navegador)

2. **Instalar as dependências:**
   - Execute o comando no terminal:
     ```bash
     pip install selenium pandas
     ```

3. **Configurar o ChromeDriver:**
   - Baixe o **ChromeDriver** adequado para sua versão do Google Chrome [aqui](https://sites.google.com/chromium.org/driver/).
   - Coloque o **ChromeDriver** no mesmo diretório do script ou no PATH.

4. **Executar o script:**
   - Após configurar o ambiente, basta executar o script Python:
     ```bash
     python nome_do_arquivo.py
     ```

## ⚠️ Cuidados

- **Respeite as regras do site**: Sempre verifique se o scraping está de acordo com os termos de serviço do site.
- **Evite sobrecarga no servidor**: Defina intervalos de tempo entre as requisições para não sobrecarregar os servidores do site.

## 📝 Licença

Este projeto está licenciado sob os termos da licença **MIT**.  
Você pode usar, copiar, modificar, mesclar, publicar, distribuir e vender cópias do código, desde que mantenha o aviso de copyright original.

## 📧 Autor

Marcos Antonio
