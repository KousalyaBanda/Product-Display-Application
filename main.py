import os
from contextlib import contextmanager

import mysql.connector
from mysql.connector import Error
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Product Display Application")
templates = Jinja2Templates(directory="templates")


def get_db_connection():
    """Create and return a MySQL connection using environment settings."""
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "test"),
        password=os.getenv("DB_PASSWORD", "Kousalya@1125"),
        database=os.getenv("DB_NAME", "product_store"),
    )


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={"title": "Product Display App"},
    )


@app.get("/products", response_class=HTMLResponse)
def products(request: Request):
    """Fetch products from MySQL and render them with Jinja2."""
    connection = None
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, name, price, description FROM products ORDER BY id"
        )
        product_rows = cursor.fetchall()
        cursor.close()

        product_list = [
            {
                "id": row[0],
                "name": row[1],
                "price": float(row[2]),
                "description": row[3] or "",
            }
            for row in product_rows
        ]

        return templates.TemplateResponse(
            request=request,
            name="product.html",
            context={
                "title": "Products",
                "products": product_list,
                "error": None,
            },
        )
    except Error as exc:
        # Do not expose database credentials or internal details to the browser.
        print(f"MySQL error while fetching products: {exc}")
        return templates.TemplateResponse(
            request=request,
            name="product.html",
            context={
                "title": "Products",
                "products": [],
                "error": (
                    "Could not load products. Check that MySQL is running, "
                    "the database is created, and your .env settings are correct."
                ),
            },
            status_code=503,
        )
    finally:
        if connection is not None and connection.is_connected():
            connection.close()


@app.get("/health")
def health():
    """Small endpoint useful for checking whether the app is running."""
    return {"status": "ok"}
