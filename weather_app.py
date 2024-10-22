

import flet as ft
import requests
from decouple import config

API_KEY = config("API_KEY")

def main(page):
    page.title = "Previsão do Tempo"
    saved_forecasts = []

    def get_weather(e):
        city = city_input.value
        response = requests.get(
            url=f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"
        )
        if response.status_code == 200:
            weather_data = response.json()
            city_name = f"Cidade: {weather_data['location']['name']}"
            temperature = f"Temperatura: {weather_data['current']['temp_c']}°C"
            condition = f"Condição: {weather_data['current']['condition']['text']}"
            saved_forecasts.append(f"{city_name} - {temperature} - {condition}")
        else:
            forecast_list.controls.append(ft.Text("Erro ao buscar a previsão do tempo."))
        page.update()

    city_input = ft.TextField(
        label="Digite o nome da cidade:"
        )
    search_button = ft.TextButton(
        text="Buscar",
        on_click=get_weather
    )
    forecast_list = ft.ListView(expand=True)

    page.add(ft.Column([
        city_input,
        search_button,
        forecast_list
    ]))

#  Rodar aplicação Desktop
ft.app(target=main)

# Rodar aplicação Web
# ft.app(target=main, view=ft.AppView.WEB_BROWSER)
