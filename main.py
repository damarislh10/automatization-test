# Importaciones módulos Python
import sys
from FileMajority import FileMajority

class Main():
      def __init__(self):
    # Instanciar QApplication: Inicia app según configuración del escritorio del usuario y define su apariencia; maneja los eventos.
        FileMajority()

if __name__ == "__main__":
    app = Main()