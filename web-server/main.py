import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return ["Product 1", "Product 2", "Product 3"]

@app.get("/contact", response_class=HTMLResponse)
def get_contact():
    return "<h1>Esto es una pagina de contacto</h1>"

def run():
    store.get_data()

if __name__ == "__main__":
    run()
