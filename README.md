# Procesador Correos

Procesador de correo para COVISA

## Características

  - Validar Correos
  - Concatenar archivos Excel
  - Concatenar archivos CSV
  - Tranformar Exce a CSV
  - Borrar correos duplicados

### Instalar dependencias

Para generar un archivo ejecutable se requiere 'pyinstaller'

```sh
$ pip install pyinstaller
```

Para instalar las dependencias del código

```sh
$ pip install validate_email
$ pip install parseaddr
$ pip install pandas
```

### Generar .exe

En la raíz del proyecto

```sh
$ pyinstaller --clean --onefile --noconsole --icon=app.ico --add-data "app.ico;." main.py
```

Esto generará el archivo 'main.exe' que puede ser ejecutado standalone
