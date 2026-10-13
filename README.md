# Product Display Application — FastAPI, Jinja2, MySQL, SQLAlchemy ORM

## Features
- Login form using FastAPI Form fields and a signed session cookie.
- After successful login, redirects directly to `/products`.
- Product records are fetched from MySQL using SQLAlchemy ORM.
- Product details are rendered dynamically with Jinja2.
- Logout clears the session.
- Simple HTML only; no CSS required.

## Project structure
```text
main.py
database.py
model.py
schema.sql
requirements.txt
.env.example
.gitignore
templates/
  home.html
  product.html
```

## Setup (Windows / VS Code)

1. Start MySQL Server.
2. Open MySQL Workbench and execute `schema.sql`. This creates the `product_store` database and sample products.
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\\Scripts\\activate
   ```
4. Install packages:
   ```bash
   pip install -r requirements.txt
   ```
5. Copy `.env.example` to `.env` and set your MySQL password. Change the login credentials and session secret as well.
6. Start the server from this folder:
   ```bash
   uvicorn main:app --reload
   ```
7. Open http://127.0.0.1:8000/

Example login credentials if you leave the values in `.env` unchanged:
- Username: `admin`
- Password: `change_this_password`

## How ORM works here
`model.py` defines `Product`, which maps to the `products` table. In `main.py`, `db.query(Product).order_by(Product.id).all()` uses SQLAlchemy ORM to return Product objects. Jinja2 displays those objects in `templates/product.html`.

## Important
- The database (`product_store`) must exist before the app starts. Run `schema.sql` first.
- Do not commit `.env` to GitHub.
- This is a learning/demo login. For public production use, add password hashing, CSRF protection, HTTPS, rate limiting, and a proper users table.
