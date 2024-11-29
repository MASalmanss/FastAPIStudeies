from fastapi import FastAPI

app = FastAPI()

books = [
    {"book1" : "heheh"},
    {"book2" : "heheh"},
    {"book3" : "heheh"},
    {"book4" : "heheh"},
    {"book5" : "heheh"},
]

@app.get("/books")
async def read_all_books():
    return books



@app.get("/books/{dynamic_param}")
def read_all_books_again(dynamic_param : str):
    return dynamic_param
