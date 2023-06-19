# ./app/main.py
from blacksheep import Application

app = Application()


@app.router.get('/')
def home_route():
    return 'asdb'
