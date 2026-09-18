## Paquetes

Los paquetes son una forma de estructurar el [namespace](https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces) de módulos de Python mediante el uso de "nombres de módulos con puntos". Por ejemplo, el nombre del módulo `A.B` designa un submódulo llamado `B` en un paquete llamado `A`. Al igual que el uso de módulos ahorra a los autores de diferentes módulos tener que preocuparse por los nombres de las variables globales de los demás, el uso de nombres de módulos con puntos ahorra a los autores de paquetes de varios módulos como [NumPy](https://numpy.org/) o [Pillow](https://pypi.org/project/Pillow/) tener que preocuparse por los nombres de los módulos de los demás.

<div class="hint">Los archivos <code>__init__.py</code> son necesarios para hacer que Python trate los directorios que contienen el archivo como paquetes. Esto evita que los directorios con un nombre común, como <code>string</code>, oculten accidentalmente módulos válidos que ocurren más adelante en la ruta de búsqueda del módulo. En el caso más simple, <code>__init__.py</code> puede ser solo un archivo vacío.</div>

Echa un vistazo a los paquetes `functions` y `classes` que hemos creado. Los usuarios de los paquetes pueden importar módulos individuales del paquete, por ejemplo:

```python
import functions.greeting.hello
```

Esto carga el submódulo `functions.greeting.hello`. Debe hacerse referencia a él con su nombre completo:

```python
functions.greeting.hello.hello('Susan')
```
Una forma alternativa de importar el submódulo es:

```python
from functions.greeting import hello
```

Esto también carga el submódulo `hello`, y lo hace disponible sin su prefijo de paquete, por lo que se puede utilizar de la siguiente manera:

```python
hello.hello('Susan')
```

Puedes aprender más sobre los paquetes leyendo <a href="https://docs.python.org/3/tutorial/modules.html#packages">esta página</a> de la Documentación de Python.

Para obtener información más estructurada y detallada, también puedes referirte a [esta página de la base de conocimientos de Hyperskill](https://hyperskill.org/learn/step/6384?utm_source=jba&utm_medium=jba_courses_links).

### Tarea
Observa la estructura de archivos en los directorios `classes` y `functions` y sus subdirectorios.

En el editor de código, importa el módulo `official` correctamente para hacer que la última instrucción `print` funcione.

En la segunda instrucción de impresión, agrega una llamada a la función (encuentra la función correcta) para que imprima un adiós a `'Alex'`.

<div class="hint">Accede al módulo utilizando una sintaxis como <code>paquete.subpaquete.módulo</code>.</div>
<div class="hint">Usa una sintaxis como <code>import module as something</code>.</div>
<div class="hint">Revisa las importaciones: hay una que podría tener la función correcta para la segunda tarea.
Ten cuidado al usarla: el módulo ya está importado con un nombre específico.</div>