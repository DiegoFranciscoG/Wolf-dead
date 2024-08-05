
```markdown
# DueloInmortal: Deadpool vs. Wolverine

**DueloInmortal** es un proyecto que simula una batalla por turnos entre los icónicos personajes de cómic Deadpool y Wolverine. Cada personaje tiene puntos de vida iniciales definidos por el usuario y posee características únicas de ataque y evasión. El objetivo del programa es simular el combate y determinar un ganador.

## Requisitos del Sistema

- Python 3.x

## Uso

Ejecuta el programa en la línea de comandos y sigue las instrucciones para ingresar la vida inicial de cada personaje:

```bash
python batalla.py
```

## Detalles del Combate

- **Ataque de Deadpool**: Daño entre 10 y 100 puntos.
- **Ataque de Wolverine**: Daño entre 10 y 120 puntos.
- **Evasión de Deadpool**: 25% de probabilidades de evitar un ataque.
- **Evasión de Wolverine**: 20% de probabilidades de evitar un ataque.
- Si un personaje realiza un ataque con el daño máximo, el otro no puede atacar en el siguiente turno.

## Resultado

El combate continúa hasta que uno de los personajes tenga 0 o menos puntos de vida. El programa muestra el ganador al finalizar.
