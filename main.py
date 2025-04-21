from fastapi import FastAPI

from string_calculator.app.routers import calculator

app = FastAPI(
    title="String Calculator",
    description="A FastAPI-based service that adds numbers from a string using various delimiters. Built with TDD practices.",
    version="1.0.0",
    servers=[{"url": "http://127.0.0.1:8000", "description": "Local development server"},],
)

app.include_router(calculator.router, prefix="/calculator", tags=["Calculator"])
