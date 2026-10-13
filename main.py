from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from database import LocalSession, engine, Base
from model import Product
app = FastAPI()
templates = Jinja2Templates(directory="templates")
Base.metadata.create_all(bind=engine)
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="home.html",
        context={}
    )
@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    return RedirectResponse(
        url="/products",
        status_code=303
    )
@app.get("/products")
def products(request: Request):
    db = LocalSession()
    try:
        product_list = db.query(Product).all()

        return templates.TemplateResponse(
            request=request,
            name="product.html",
            context={"products": product_list}
        )
    finally:
        db.close()
@app.get("/logout")
def logout():
    return RedirectResponse(url="/", status_code=303)