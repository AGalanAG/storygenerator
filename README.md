# Generador de Cuentos de Fantasía

Un generador automático de cuentos de fantasía que utiliza cadenas de Markov para crear historias únicas con elementos de fantasía clásica. Disponible como aplicación web con Flask y como script independiente.

## Características

- Genera cuentos de fantasía en español con estructura narrativa clásica
- Utiliza cadenas de Markov entrenadas con textos existentes para generar contenido original
- Combina elementos aleatorios (héroes, villanos, ubicaciones, objetos mágicos)
- Disponible como aplicación web con interfaz sencilla
- Sistema de logging para seguimiento del proceso de generación

## Requisitos

- Python 3.6 o superior
- Flask
- Directorio con archivos .txt para entrenamiento

## Instalación

1. Clona este repositorio
   ```
   git clone https://github.com/tuusuario/generador-cuentos-fantasia.git
   cd generador-cuentos-fantasia
   ```

2. Instala las dependencias
   ```
   pip install flask
   ```

3. Configura el directorio de textos de entrenamiento
   - Crea un directorio para almacenar tus textos de entrenamiento
   - Añade archivos .txt con historias de fantasía para entrenar el modelo
   - Actualiza la ruta en `app.py` o en `fantasy_story_generator.py` según corresponda

## Uso

### Como aplicación web

1. Ejecuta la aplicación Flask:
   ```
   python app.py
   ```

2. Abre tu navegador en `http://localhost:5000`

3. Haz clic en el botón para generar una nueva historia

### Como script independiente

1. Ejecuta el script principal:
   ```
   python fantasy_story_generator.py
   ```

2. La historia generada se mostrará en la consola

## Estructura del proyecto

- `app.py`: Aplicación web Flask que sirve como interfaz
- `fantasy_story_generator.py`: Clase principal que implementa la generación de historias
- `templates/index.html`: Plantilla HTML para la interfaz web (necesaria para ejecutar la aplicación)

## Funcionamiento interno

El generador utiliza cadenas de Markov para crear texto basado en patrones aprendidos de los textos de entrenamiento. La historia sigue una estructura de cinco partes:

1. **Introducción**: Presenta al héroe, villano y ubicación
2. **Conflicto**: Establece el problema principal y los objetos mágicos
3. **Desarrollo**: Expande la historia utilizando cadenas de Markov
4. **Clímax**: Describe el enfrentamiento decisivo
5. **Resolución**: Proporciona un final satisfactorio

## Personalización

Puedes personalizar los elementos de la historia modificando los diccionarios en la clase `FantasyStoryGenerator`:

```python
self.story_elements = {
    'heroes': ['el joven mago', 'la valiente guerrera', 'el sabio druida'],
    'villains': ['el dragón oscuro', 'el hechicero maligno', 'la reina de las sombras'],
    'locations': ['el bosque encantado', 'la montaña maldita', 'el castillo antiguo'],
    'objects': ['la espada mágica', 'el cristal del poder', 'el grimorio ancestral'],
    'conflicts': ['buscar el objeto perdido', 'derrotar al villano', 'romper la maldición']
}
```

## Detalles técnicos

- La generación se basa en cadenas de Markov de orden 3 (utiliza grupos de 3 palabras para predecir la siguiente)
- El sistema carga textos de entrenamiento desde archivos .txt
- Implementa manejo de errores para archivos inexistentes o corruptos
- El logging guarda información sobre el proceso de carga y entrenamiento

## Ejemplos de resultado

El generador produce historias como:

```
En un reino lejano, el sabio druida vivía tranquilamente hasta que la reina de las sombras apareció en el castillo antiguo.

Para enfrentarlo, decidió derrotar al villano usando el grimorio ancestral.

El viaje se volvió más peligroso de lo que imaginaban cuando descubrieron que antiguos secretos habían sido desenterrados por los seguidores de la oscuridad.

En una épica batalla final, el sabio druida se enfrentó a la reina de las sombras.

Finalmente, la paz retornó al reino, y el sabio druida fue recordado como un héroe legendario.
```

## Contribuir

Si deseas contribuir a este proyecto, puedes:

1. Añadir más textos de entrenamiento
2. Mejorar el algoritmo de generación de Markov
3. Expandir los elementos de fantasía
4. Mejorar la interfaz web
