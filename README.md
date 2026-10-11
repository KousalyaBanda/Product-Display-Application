# Product Display Application

A beginner-friendly Product Display App built with **FastAPI, Jinja2, and MySQL**. Product records are fetched from MySQL using the Python MySQL Connector (DB-API) and rendered dynamically in a Jinja2 template.

## 1. Project structure

```text
product_display_app/
├── main.py
├── schema.sql
├── requirements.txt
├── .env.example
├── .gitignore
├── templates/
│   ├── home.html
│   └── product.html
└── static/
    └── style.css
```

## 2. Requirements

- Python 3.10+
- MySQL Server
- VS Code (recommended)

## 3. Create and activate a virtual environment

Windows:

```bash
python -m venv .venv
.venv\\Scripts\\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 4. Set up MySQL

1. Start your MySQL server.
2. Open MySQL Workbench or the MySQL command line.
3. Run the SQL in `schema.sql`. This creates `product_store`, creates the `products` table, and inserts sample products.

Command-line alternative:

```bash
mysql -u root -p < schema.sql
```

## 5. Configure database credentials

Copy `.env.example` to a new file named `.env` and edit the password to match your MySQL installation:

```env
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=your_actual_password
DB_NAME=product_store
```

Do not upload `.env` to GitHub. It is included in `.gitignore`.

## 6. Run the application

From the project root, run:

```bash
uvicorn main:app --reload
```

Open these URLs:

- Home page: http://127.0.0.1:8000/
- Product display: http://127.0.0.1:8000/products
- Health check: http://127.0.0.1:8000/health

## 7. How it works

1. FastAPI receives a request to `/products`.
2. `get_db_connection()` connects to MySQL using the `.env` settings.
3. `cursor.execute()` runs a `SELECT` query against the `products` table.
4. `fetchall()` retrieves the product rows.
5. The route passes the records to `product.html` in the template context.
6. Jinja2 loops through `products` and renders a card for each product.
7. The database connection is closed after the request.

## 8. Add a product

Run a query in MySQL Workbench:

```sql
USE product_store;

INSERT INTO products (name, price, description)
VALUES ('Keyboard', 1499.00, 'A compact keyboard for everyday typing.');
```

Refresh `/products` to see the new product.

## Troubleshooting

- **Access denied:** verify `DB_USER` and `DB_PASSWORD` in `.env`.
- **Unknown database:** run `schema.sql`.
- **Can't connect to MySQL:** make sure MySQL Server is running and `DB_PORT` is correct.
- **No products found:** check the rows in `product_store.products`.
- **Template/static errors:** run Uvicorn from the project root folder.

## Optional next step: SQLAlchemy ORM

This starter uses a direct database driver (Python DB-API) to match the assignment's PDBC/driver approach. To move to SQLAlchemy later, replace the direct connection and cursor query with an SQLAlchemy engine, `Session`, and a `Product` model. The Jinja2 templates can remain largely unchanged.
