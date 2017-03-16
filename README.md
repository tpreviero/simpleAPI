# simpleAPI

## Procedimentos
### Clone o repositório

```console
git clone git@github.com:tpreviero/simpleAPI.git simpleAPI
cd simpleAPI
```

### Crie um virtualenv com Python 3.6 e ative
```console
virtualenv .env -p python3
source .env/bin/activate
```
### Dependencias
```console
pip install -r requirements.txt
```

### Subindo banco
```console
./manage.py migrate
```
## Rodar o servidor
```console
 ./manage.py runserver
 ```
Abrir a url: http://127.0.0.1:8000/employee/

## CURL 

### GET
 ```console
 curl -H "Content-Type: application/javascript" http://localhost:8000/employee/
  ```
