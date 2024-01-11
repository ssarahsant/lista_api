# Importação
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel  

app = FastAPI()

# Criação de Classe
# Através da Criação do Objeto será possivel otimizar as funções do Código
class Item(BaseModel):
    # Atributos
    text: str
    is_done: bool = False

# Criação de uma Lista
items = []

# Definição de caminho no FasAPI
# O get implica que o / for visitado a função abaixo será executada
@app.get("/")
def root():
    return {"Hello": "World"}
 
# Criação de um Endereço para a Aplicação (adiciona intens na lista)
# O usuário poderá acessar o endereço através de uma solicitação HTTP POST + um item de entrada
@app.post("/items")
def creat_item(item: Item):
    items.append(item)
    return items

# Criação de um Endereço para a Aplicação (retorna uma quantidade de itens conforme o número informado)
# O usuário poderá acessar o endereço através de uma solicitação GET que será retornado do primeiro item ate o que foi informado
# NESSE CASO, o valor ja está pré definido em 10, logo os 10 itens serão automaticamente retornados
@app.get("/items", response_model=list[Item])
def list_items(limit: int = 3):
    return items[0:limit]


# Criação de um Endereço para a Aplicação (retorna um item especifico da lista de acoro com o indice)
# O usuário poderá acessar o endereço através de uma solicitação GET ao informar o nome do item
@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    # Apresentação do item buscado
    if item_id < len(items):
        return items[item_id]
    # Tratamento de Erro (caso o item buscado não exista na lista)
    else:
        raise HTTPException(status_code=404, detail=f"Item {item_id} not found")

# Uvicorn (roda direto pelo programa python)
if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', host="127.0.0.1", port=8000, reload=True)