import httpx
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from src.settings import settings

app = FastAPI(title="{{ cookiecutter.project_name }}")

app.mount("/static", StaticFiles(directory="src/static"), name="static")
templates = Jinja2Templates(directory="src/templates")

# WMO weather code -> (description, emoji)
WEATHER_CODES: dict[int, tuple[str, str]] = {
    0: ("Clear sky", "☀️"),
    1: ("Mainly clear", "🌤️"),
    2: ("Partly cloudy", "⛅"),
    3: ("Overcast", "☁️"),
    45: ("Fog", "🌫️"),
    48: ("Icy fog", "🌫️"),
    51: ("Light drizzle", "🌦️"),
    53: ("Drizzle", "🌦️"),
    55: ("Heavy drizzle", "🌧️"),
    61: ("Light rain", "🌧️"),
    63: ("Rain", "🌧️"),
    65: ("Heavy rain", "🌧️"),
    71: ("Light snow", "🌨️"),
    73: ("Snow", "❄️"),
    75: ("Heavy snow", "❄️"),
    80: ("Rain showers", "🌦️"),
    81: ("Heavy showers", "🌧️"),
    82: ("Violent showers", "⛈️"),
    95: ("Thunderstorm", "⛈️"),
    96: ("Thunderstorm with hail", "⛈️"),
    99: ("Thunderstorm with heavy hail", "⛈️"),
}


@app.get("/", response_class=HTMLResponse)
async def index(request: Request) -> HTMLResponse:
    return templates.TemplateResponse(request, "index.html")


@app.get("/weather", response_class=HTMLResponse)
async def weather(request: Request) -> HTMLResponse:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://api.open-meteo.com/v1/forecast",
            params={
                "latitude": 51.5,
                "longitude": -0.12,
                "current_weather": True,
            },
        )
        response.raise_for_status()
        data = response.json()

    current = data["current_weather"]
    code = int(current["weathercode"])
    description, emoji = WEATHER_CODES.get(code, ("Unknown", "🌡️"))

    return templates.TemplateResponse(
        request,
        "weather_card.html",
        {
            "temperature": current["temperature"],
            "windspeed": current["windspeed"],
            "winddirection": current["winddirection"],
            "description": description,
            "emoji": emoji,
            "time": current["time"],
        },
    )
