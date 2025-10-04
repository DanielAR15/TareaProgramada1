# -*- coding: utf-8 -*-
"""
Menú principal para manejar el modelo Diccionario.
"""

from __future__ import annotations
import sys
from rich import box
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from tarea1.diccionario import Diccionario
from tarea1.listaordenadadinamica import ListaOrdenadaDinámica
from tarea1.listaordenadaestatica import ListaOrdenadaEstática
from tarea1.tablahash import TablaHash
console = Console()

# =====================
# Utilidades de pantalla
# =====================

def panel_contenido(texto: str, *, titulo: str = "Diccionario", width: int | None = None) -> None:
    console.clear()
    if width is None:
        width = min(80, max(40, console.size.width - 4))
    panel = Panel(
        Align.left(texto),
        title=titulo,
        title_align="center",
        padding=(1, 4),
        box=box.DOUBLE,
        width=width,
        style="white on blue",
    )
    console.print(panel, justify="left")


def pausa(msg: str = "Pulse [bold]Enter[/] para continuar") -> None:
    Prompt.ask(msg, default="", show_default=False)


def leer_hilera(pregunta: str) -> str:
    """
    Lee una hilera (máx. 20 caracteres).
    """
    s = Prompt.ask(pregunta).strip()
    return s[:20]


# =====================
# Lectura de una tecla
# =====================

def leer_tecla(validos: str) -> str:
    """
    Lee una tecla y asegura que sea una de las válidas.
    """
    try:
        import msvcrt
    except Exception:
        msvcrt = None

    if msvcrt is not None:
        while True:
            ch = msvcrt.getwch()
            if ch in ("\x00", "\xe0"):
                _ = msvcrt.getwch()
                continue
            if ch in validos:
                console.print(ch, end="")
                return ch
    else:
        import termios, tty
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            while True:
                ch = sys.stdin.read(1)
                if ch in validos:
                    console.print(ch, end="")
                    return ch
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)


# =====================
# Operaciones de menú
# =====================

def agregar(diccionario: Diccionario) -> None:
    """
    Agrega un elemento al diccionario.
    """
    texto = "Digite la hilera que desea agregar:"
    panel_contenido(texto)
    h = leer_hilera("")
    diccionario.inserte(h)
    console.print("[green]Elemento insertado.[/]")
    pausa()


def borrar(diccionario: Diccionario) -> None:
    """
    Borra un elemento del diccionario.
    """
    texto = "Digite la hilera que desea borrar:"
    panel_contenido(texto)
    h = leer_hilera("")
    if diccionario.borre(h):
        console.print("[green]Elemento borrado.[/]")
    else:
        console.print("[red]El elemento NO existe.[/]")
    pausa()


def existencia(diccionario: Diccionario) -> None:
    """
    Verifica si un elemento existe en el diccionario.
    """
    texto = "Digite la hilera que desea verificar:"
    panel_contenido(texto)
    h = leer_hilera("")
    if diccionario.miembro(h):
        console.print("[green]El elemento existe.[/]")
    else:
        console.print("[red]El elemento no existe.[/]")
    pausa()


def imprimir(diccionario: Diccionario) -> None:
    """
    Imprime todos los elementos del diccionario.
    """
    panel_contenido("Imprimir el diccionario")
    diccionario.imprima()
    pausa()


def limpiar(diccionario: Diccionario) -> None:
    """
    Limpia todo el contenido del diccionario.
    """
    diccionario.limpie()
    panel_contenido("Diccionario limpio.")
    pausa()


# =====================
# Menús
# =====================

def render_menu_etapa() -> None:
    """
    Muestra el menú principal.
    """
    cuerpo = (
        "\n"
        "            Etapa\n\n"
        "[1] Menú diccionarios \n"
        "[2] Pruebas de rendimiento ([italic]benchmarking[/])\n\n"
        "Digite una opción: "
    )
    panel_contenido(cuerpo)


def render_menu_clase() -> None:
    """
    Muestra el menú de elección de tipo de diccionario.
    """
    cuerpo = (
        "\n"
        "            Clase Diccionario\n\n"
        "[1] ListaOrdenadaDinámica\n"
        "[2] ListaOrdenadaEstática\n"
        "[3] TablaHashAbierta\n"
        "[4] ABBPunteros\n"
        "[5] ABBVectorHeap\n"
        "[6] TriePunteros\n"
        "[7] TrieArreglos\n\n"
        "Digite una opción [_]"
    )
    panel_contenido(cuerpo)


def render_menu_diccionario() -> None:
    """
    Muestra el menú de operaciones del diccionario.
    """
    cuerpo = (
        "\n"
        "            Diccionario\n\n"
        "[1] Agregar un elemento\n"
        "[2] Borrar un elemento\n"
        "[3] Verificar existencia\n"
        "[4] Imprimir el diccionario\n"
        "[5] Limpiar el diccionario\n"
        "[6] Salir\n\n"
        "Digite una opción [_]"
    )
    panel_contenido(cuerpo)


def menu_etapa() -> str:
    """
    Devuelve la opción elegida en el menú de etapa.
    """
    render_menu_etapa()
    return leer_tecla("12")


def menu_clase() -> Diccionario:
    """
    Devuelve un objeto del tipo de diccionario elegido.
    """
    while True:
        render_menu_clase()
        opcion = leer_tecla("1234567")
        match opcion:
            case "1":
                return ListaOrdenadaDinámica()
            case "2":
                return ListaOrdenadaEstática(100)
            case "3":
                return TablaHash()
            case "4":
                from tarea1.abbpunteros import ABBPunteros
                return ABBPunteros()
            case "5":
                from tarea1.abbvectorheap import ABBVectorHeap
                return ABBVectorHeap()
            case "6":
                from tarea1.triepunteros import TriePunteros
                return TriePunteros()
            case "7":
                from tarea1.triearreglos import TrieArreglos
                return TrieArreglos()


def menu_diccionario(diccionario: Diccionario) -> None:
    """
    Muestra el menú de operaciones y ejecuta acciones según la elección.
    """
    while True:
        render_menu_diccionario()
        opcion = leer_tecla("123456")
        match opcion:
            case "1":
                agregar(diccionario)
            case "2":
                borrar(diccionario)
            case "3":
                existencia(diccionario)
            case "4":
                imprimir(diccionario)
            case "5":
                limpiar(diccionario)
            case "6":
                console.clear()
                break


def main() -> None:
    """
    Función principal que inicia el programa.
    """
    opcion = menu_etapa()
    match opcion:
        case "1":
            diccionario = menu_clase()
            menu_diccionario(diccionario)
        case "2":
            console.print("Pruebas de rendimiento - No implementado aún")
            pausa()
