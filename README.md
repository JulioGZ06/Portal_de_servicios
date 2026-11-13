# Portal de servicios

## Propósito

Aplicación web desarrollada con Flask para consultar información de la empresa y sus servicios. Incluye herramientas para calcular el importe de una compra, calcular el salario semanal y convertir temperaturas de Celsius a Fahrenheit y Kelvin.

## Requisitos para la ejecución

- Python 3.9 o posterior.
- `pip` para instalar las dependencias.
- Un navegador web.
- Conexión a Internet para cargar los recursos CSS y JavaScript de Bootstrap desde su CDN.

## Crear y activar el entorno virtual

Desde la carpeta raíz del proyecto, abre PowerShell y ejecuta:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Si PowerShell impide activar el entorno por la política de ejecución, puedes usar el intérprete del entorno directamente, sin activarlo:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe server.py
```

## Instalar dependencias

Con el entorno virtual activado, instala los paquetes definidos en `requirements.txt`:

```powershell
python -m pip install -r requirements.txt
```

## Iniciar la aplicación

Desde la carpeta raíz del proyecto, con el entorno virtual activado, ejecuta:

```powershell
python server.py
```

Abre la aplicación en el navegador en:

```text
http://127.0.0.1:5000
http://128.0.227.128:5000
```