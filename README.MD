# PensionCalculatorPro

## Por:
Juliana Casas Ramírez
Natalia Florez Guzmán

## ¿Qué es?

La calculadora de pensiones es una herramienta digital que ayuda a las personas a estimar el monto de sus pensiones futuras. Utilizando información como la edad actual, el género, el salario actual, las semanas laboradas, el ahorro acumulado, la rentabilidad del fondo de pensiones y la tasa de administración del mismo, esta herramienta proporciona una proyección del ingreso que recibirán durante su jubilación.

## Propósito
El propósito de la calculadora de pensiones es permitir a los usuarios planificar su futuro financiero durante la jubilación. Al proporcionar una estimación del ingreso futuro, los individuos pueden tomar decisiones informadas sobre ahorros y contribuciones al fondo de pensiones, así como ajustar su planificación financiera para asegurar un retiro cómodo y sin preocupaciones.

## ¿Cómo lo haces funcionar?

### Prerrequisitos para Abrir la Calculadora Pensional

Antes de comenzar, asegúrate de tener lo siguiente:

1. **Computadora:** Necesitarás una computadora (Windows, macOS o Linux) para abrir la Calculadora Pensional.

2. **Conexión a Internet:** Asegúrate de tener una conexión a Internet estable para descargar la carpeta "PensionCalculatorProBD-main".

3. **Programa de Extracción de Archivos:** Deberás tener instalado un programa que te permita extraer archivos comprimidos, como WinRAR, 7-Zip o el descompresor integrado en tu sistema operativo.

4. **Espacio en Disco:** Asegúrate de tener suficiente espacio en disco para almacenar y ejecutar la Calculadora Pensional.

5. **Permisos de Ejecución:** Es posible que necesites tener permisos de ejecución para ejecutar el archivo ejecutable "Ejecutable_Calculadora". Si estás utilizando un sistema operativo que requiere permisos de administrador, asegúrate de tenerlos.

Con estos prerrequisitos, estarás listo/a para abrir y utilizar la Calculadora Pensional en tu computadora. Si tienes alguna pregunta o necesitas ayuda adicional, no dudes en contactarnos. ¡Disfruta utilizando la Calculadora Pensional!

### Ejecución:
### Paso a Paso para Abrir la Calculadora Pensional

Aquí tienes los pasos detallados para abrir y utilizar la Calculadora Pensional:
### Conexión a la base de datos:
**Opción 1: Descargar desde GitHub:**

1. **Descarga de Archivos:**
   - Descarga el archivo comprimido "CalculadoraPensional" desde el enlace proporcionado o desde donde te hayan entregado el archivo.

2. **Extracción de Archivos:**
   - Abre el archivo comprimido "PensionCalculatorProBD-main.zip" utilizando un programa de extracción de archivos, como WinRAR o 7-Zip.
   - Extrae todos los archivos de la carpeta en una ubicación de tu elección en tu computadora.

3. *Ubica el archivo pension_modelo.py el cual esta dentro de la carpeta modelo y tambien  Encuentra el método __init__(self), que se utiliza para inicializar objetos, generalmente ubicado al comienzo de una clase.

4. *Reemplaza los valores de conexión:* Dentro del método _init_(self), encontrarás un bloque de código donde se establece la conexión a la base de datos. Reemplaza los valores de host, database, user y password con los datos de tu propia base de datos.

5. *Guarda y ejecuta:* Guarda el archivo Python con los cambios realizados y ejecuta tu programa. Ahora, tu aplicación Python estará conectada a la base de datos utilizando los datos que proporcionaste.

**Abrir para ejecutar consola de base de datos:**
Para ejecutar el archivo pension_vista.py desde la terminal, sigue estos pasos:

6. Abre la terminal.
7. Utiliza el comando cd ruta_de_la_carpeta/PensionCalculatorProBD-main
Asegúrate de reemplazar ruta_de_la_carpeta con la ruta real de la carpeta "PensionCalculatorProBD-main" en tu sistema, navega dentro de la carpeta src, seguidamente vista y dentro de ella enontrarás el archivo pension_vista.py.
3- Una vez en el directorio correcto, puedes ejecutar el archivo pension_vista.py utilizando Python. Coloca el siguiente comando en tu terminal:
python pension_vista.py

8. Instale psycopg2:
8.1. *Abre tu terminal:* Si estás en Windows, abre el símbolo del sistema o PowerShell. En macOS o Linux, abre la terminal.

8.2. *Instala pip si no lo tienes:* Si no tienes pip instalado, puedes instalarlo ejecutando el siguiente comando en la terminal:
   
   python -m ensurepip --default-pip
   
8.3. *Instala psycopg2:* Usa pip para instalar psycopg2 ejecutando el siguiente comando en la terminal:
   
   pip install psycopg2
   

8.4. *Espera a que termine la instalación:* pip descargará e instalará psycopg2 y todas las dependencias necesarias. Espera a que termine el proceso.

8.5. *Verifica la instalación:* Después de que la instalación se complete, puedes verificar que psycopg2 esté instalado correctamente ejecutando el siguiente comando en la terminal:
   
   pip show psycopg2
   
8.6. *¡Listo para usar!:* Ahora puedes importar psycopg2 en tus scripts de Python y utilizarlo para conectarte y trabajar con bases de datos PostgreSQL.

**Abrir para ejecutar consola:**
3. navega dentro de la carpeta src, seguidamente vista y dentro de ella enontrarás el archivo pension_vista.py., una vez en el directorio correcto, puedes ejecutar el archivo pension_vista.py utilizando Python. Coloca el siguiente comando en tu terminal:
python pension_vista.py


3. **Ubicación del Ejecutable:**
   - Después de extraer los archivos, encontrarás una carpeta llamada "PensionCalculatorProBD-main".
   - Abre esta carpeta y localiza el archivo ejecutable llamado "Ejecutable_Calculadora". Este es el archivo que necesitas ejecutar para abrir la Calculadora Pensional.

**Opción 2: Clonar el Repositorio desde Github:**

1. **Clonar el Repositorio:**
   - Abre la terminal o línea de comandos en tu computadora.
   - Navega hasta el directorio donde deseas clonar el repositorio utilizando el comando cd.
   - Utiliza el siguiente comando para clonar el repositorio desde GitHub:

   git clone https://github.com/usuario/PensionCalculatorProBD.git

   Reemplaza usuario por el nombre de usuario de GitHub donde se encuentra el repositorio.

2. **Ubicación del ejecutable:**
   - Una vez que se haya completado la clonación, navega hasta la carpeta recién creada CalculadoraPensional.
   - Dentro de esta carpeta, navega una carpeta llamada build, encontrarás el archivo ejecutable llamado "Ejecutable_Calculadora". Este es el archivo que necesitas ejecutar para abrir la Calculadora Pensional.

**Abrir para ejecutar consola de base de datos:**
Para ejecutar el archivo main_consola.py desde la terminal, sigue estos pasos:

3. Abre la terminal.
4. Utiliza el comando cd ruta_de_la_carpeta/PensionCalculatorProBD-main

Asegúrate de reemplazar ruta_de_la_carpeta con la ruta real de la carpeta "PensionCalculatorProBD-main" en tu sistema.

3. Una vez en el directorio correcto, puedes ejecutar el archivo pension_vista.py utilizando Python. Coloca el siguiente comando en tu terminal:
python pension_vista.py
**Abrir para ejecutar consola:**

Para ejecutar el archivo pension_vista.py desde la terminal, sigue estos pasos:

3. Abre la terminal.
4. Utiliza el comando cd ruta_de_la_carpeta/PensionCalculatorProBD-main

Asegúrate de reemplazar ruta_de_la_carpeta con la ruta real de la carpeta "PensionCalculatorProBD-main" en tu sistema.

3. Una vez en el directorio correcto, puedes ejecutar el archivo pension_vista.py utilizando Python. Coloca el siguiente comando en tu terminal:
python pension_vista.py

4. **Ejecución del Ejecutable:**
   - Haz doble clic en el archivo "Ejecutable_Calculadora" para ejecutarlo.
   - Dependiendo de tu sistema operativo, es posible que necesites confirmar que deseas ejecutar el archivo.
   - Una vez que aparezca ventana de "Ejecutable_Calculadora", en la parte superior derecha de la ventana encontrarás 3 íconos, selecciona el de la mitad, el cuál es un cuadrado sobre otro cuadrado, llamado "Restore Down".

5. **Interfaz de la Calculadora:**
   - Una vez que se haya ejecutado el archivo, debería abrirse la interfaz de la Calculadora Pensional.
   - Puedes utilizar la interfaz para ingresar los datos necesarios y calcular la pensión.

6. **Uso de la Aplicación:**
   - Completa los campos requeridos con la información relevante, como la edad actual, el salario, las semanas laboradas, etc.
   - Haz clic en el botón "Calcular" para obtener los resultados de la pensión.
   - La aplicación mostrará los resultados en una nueva ventana o pantalla.



7. **Finalización de la Aplicación:**
   - Una vez que hayas utilizado la Calculadora Pensional y obtenido los resultados deseados, puedes cerrar la aplicación haciendo clic en el botón de cierre o saliendo del programa como lo harías con cualquier otra aplicación.

 ¡Espero que encuentres útil la aplicación!

## ¿Cómo se hizo el ejecutable? 
1. Instalamos PyInstaller usando el comando: pip install pyinstaller, una vez instalado
2. Abrimos la terminal en main.py e ingresamos el siguiente comando: pyinstaller --onefile --windowed main.py
3. Esto creó un archivo el cual llamamos Ejecutable_calculadora.exe


Bibliotecas Utilizadas:
El proyecto hace uso de las siguientes bibliotecas estándar de Python:

unittest: Utilizada para escribir y ejecutar pruebas unitarias.

Dependencias de Otros Proyectos:
El proyecto no tiene dependencias externas a otros proyectos. Todas las funcionalidades están implementadas dentro del propio proyecto sin requerir bibliotecas externas.

