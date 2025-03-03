# Aplicacion hecha en con FastAPI y Uvicorn en un entorno venv

## Base de datos mysql

### el script .sql lo encontramos en
[app/bd.sql](app/bd.sql)

### Crear y activar el entorno virtual  (windows)

## Iniciar Proyecto

#### Debemos previamente tener instalado el gesto pip

### Crear y activar el entorno virtual  (windows)
``` bash
python -m venv 4thewords
4thewords\Scripts\activate
```

### Instalamos las dependencias necesarias

``` bash
pip install -r requirements.txt
```


### Ejecutamos la aplicacion

``` bash
python -m app.main
```
### La aplicacion iniciara 
### [http://localhost:8080](http://localhost:8080)