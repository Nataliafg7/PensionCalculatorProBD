
import sys 
sys.path.append("src")
from vista.pension_vista import PensionVista

def main():
    vista = PensionVista()
    vista.ejecutar()

if __name__ == "__main__":
    main()
