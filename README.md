# Clase Duoc UC — GitHub Actions (CI)

Ejemplo educativo sin credenciales, infraestructura ni dependencias externas. Implementa **integración continua**, no un despliegue a producción.

## Prueba local

```bash
python3 -m unittest discover -s tests -v
```

## Demostración en GitHub

1. Crear repositorio **público** de demostración en tu cuenta personal y subir estos archivos, conservando `.github/workflows/ci.yml`.
2. Abrir **Actions** y observar la ejecución desencadenada por `push`.
3. Entrar al job `pruebas` y revisar steps y logs.
4. Descargar `reporte-pruebas` (artifact) del resumen de la ejecución.
5. Crear una rama, modificar una prueba para que falle (ej.: `3600` por `9999`) y abrir un pull request: debe aparecer una ejecución fallida.
6. Corregir la prueba y volver a observar el resultado verde.

**Nota docente:** no se necesita Docker ni Kubernetes. No ejecutar código arbitrario de terceros y no agregar secretos. Si no hay Internet, usar capturas preparadas.

## Preguntas para evaluar

- ¿Qué diferencia existe entre `push` y `pull_request`?
- ¿Quién ejecuta los `steps`?
- ¿Para qué sirve un `artifact`?
- ¿El pipeline realiza despliegue? No, valida código: es CI.
