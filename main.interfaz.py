from kivy.app import App

import sys 
sys.path.append("src")
# Importa la clase PensionCalculatorApp desde el archivo pension_interface.py
from vista.pension_interface import *
if __name__ == '__main__':
    PensionCalculatorApp().run()
