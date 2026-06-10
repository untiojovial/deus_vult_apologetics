# Prototipo Hugo: Defendiendo la Fe

Prototipo minimo de blog de apologetica con un articulo de bienvenida.

## Ejecutar en local

1. Instala Hugo Extended.
2. Inicializa el submodulo del tema (si clonas el repo en otra maquina):

   ```bash
   git submodule update --init --recursive
   ```

3. Desde esta carpeta, ejecuta:

   ```bash
   hugo server -D
   ```

4. Abre http://localhost:1313

## Crear otro articulo

```bash
hugo new content posts/mi-siguiente-articulo.md
```

Luego cambia `draft: false` cuando este listo.
