# ☀️ Weather App ⛅

Bem-vindo ao **Weather App**! 🌦️ Este é um simples aplicativo para consultar a previsão do tempo em qualquer cidade do mundo, utilizando a API do [WeatherAPI](https://www.weatherapi.com/). 🔮

## 🚀 Funcionalidades
- 🔍 Busca por cidade para obter a previsão atual.
- 🌡️ Exibe a temperatura atual em Celsius.
- ☁️ Mostra a condição climática (ensolarado, nublado, chuvoso, etc.).
- 📝 Histórico das consultas recentes.

## 🛠️ Tecnologias Utilizadas
- 🐍 **Python**: Linguagem principal do projeto.
- 🖼️ **Flet**: Framework para construção da interface gráfica.
- 🌐 **Requests**: Biblioteca para fazer requisições HTTP à API.
- 🔑 **Decouple**: Para carregar as variáveis de ambiente com segurança.

## 📦 Instalação

Siga os passos abaixo para rodar o projeto localmente:

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/weather_app.git
   ```

2. Acesse o diretório do projeto:
   ```bash
   cd weather_app
   ```

3. Crie um ambiente virtual e ative-o (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

5. Crie um arquivo `.env` na raiz do projeto com a sua chave da API:
   ```env
   API_KEY=your_api_key_here
   ```

6. Rode o projeto:
   ```bash
   python weather_app.py
   ```

## 🧑‍💻 Como Usar

1. Ao iniciar o app, você verá um campo para digitar o nome de uma cidade. 🏙️
2. Insira o nome da cidade e clique no botão **Buscar** 🔍.
3. A previsão do tempo será exibida com informações como:
   - Cidade 🏙️
   - Temperatura 🌡️
   - Condição climática ☁️

## 🎨 Interface

A interface é simples e direta:

- Um campo para inserir o nome da cidade 🏙️.
- Um botão **Buscar** para solicitar a previsão do tempo 🔍.
- Uma lista que exibe as previsões anteriores 🌦️.

## 📄 Licença

Este projeto está sob a licença MIT. 📜

## 🤝 Contribuições

Contribuições são sempre bem-vindas! 💡 Abra uma **issue** ou envie um **pull request** para sugerir melhorias.
