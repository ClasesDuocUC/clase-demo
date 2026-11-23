# Clase Duoc UC — CI con GitHub Actions

Calculadora en **Python 3.12** con cuatro operaciones y argumentos por línea de comandos. Ejemplo para la clase simulada *Introducción a Herramientas DevOps (ISY1101)*. No necesita dependencias externas ni secretos.

## Ejecutar la calculadora

Desde la raíz del repositorio:

```bash
python3 app.py sumar 10 5           # Resultado: 15
python3 app.py restar 10 5          # Resultado: 5
python3 app.py multiplicar 10 5     # Resultado: 50
python3 app.py dividir 10 5         # Resultado: 2
python3 app.py dividir 10 0         # Error controlado: no se puede dividir por cero
python3 app.py --help
```

Admite decimales y números negativos. El orden es **operación primer_número segundo_número**. Los nombres de operaciones válidos son `sumar`, `restar`, `multiplicar` y `dividir`.

## Ejecutar pruebas localmente

```bash
python3 -m unittest discover -s tests -v
```

## Pipeline de integración continua

En [`.github/workflows/ci.yml`](.github/workflows/ci.yml) se encuentra un workflow que:

1. Se activa ante `push`, `pull_request` o manualmente (`workflow_dispatch`).
2. Ejecuta un **job** `pruebas` en un **runner** Ubuntu.
3. Utiliza las acciones reutilizables `actions/checkout` y `actions/setup-python`.
4. Valida sintaxis y ejecuta las pruebas automatizadas.
5. Publica un **artifact** llamado `reporte-pruebas` con el log de tests, incluso si hay fallos (si el reporte se generó).

Este ejemplo implementa **CI**. No realiza despliegue continuo.

## Demostración didáctica: rojo → verde

1. Publica estos archivos en `https://github.com/ClasesDuocUC/clase-demo`.
2. Abre la pestaña **Actions** y revisa una ejecución exitosa, sus pasos y el artefacto descargable.
3. Crea una rama `demo-fallo` y modifica **solo la prueba** `test_multiplicar`, cambiando el resultado esperado de `50` a `9999`.
4. Abre un pull request y observa el fallo, identificando la aserción que no coincide.
5. Corrige el resultado esperado a `50`; la siguiente ejecución debe quedar verde.

**Respaldo para clase:** guarda capturas de una ejecución exitosa, otra fallida y del artefacto, por si no funciona Internet. Evita modificar `main` para simular errores.

## Preguntas para los estudiantes

- ¿Qué diferencia existe entre `push` y `pull_request`?
- ¿Qué función tienen un workflow, un job, un step y un runner?
- ¿Por qué falla el pipeline cuando una prueba espera un valor incorrecto?
- ¿Dónde se consulta el artefacto de reporte?
- ¿En qué se diferencia CI de Continuous Delivery y Continuous Deployment?
