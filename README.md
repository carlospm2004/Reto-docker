# Informe de notas con Python y Docker

## Integrantes

- MANOLO_TORTAJADA (MDIA)
- ANGEL_CARLOS_PEREZ (MDIA)
- ANTONIO_NAVARRO (MDES)

## Pull request

[Pull request de `develop` a `main`](https://github.com/carlospm2004/Reto-docker/pull/1)

## Construcción y ejecución

Desde la carpeta raíz del proyecto, construye la imagen Docker:

```bash
docker build -t informe-notas .
```

Después, ejecuta el contenedor para mostrar el informe de notas:

```bash
docker run --rm informe-notas
```

El programa mostrará el informe completo por consola y el contenedor terminará automáticamente al finalizar.
