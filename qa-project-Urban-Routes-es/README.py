# Urban Routes – Pruebas Automatizadas con Selenium

Este proyecto contiene pruebas automatizadas del proceso de solicitud de taxis en la plataforma Urban Routes, utilizando Python, Pytest y Selenium WebDriver.


#Descripción del Proyecto

El objetivo del proyecto es automatizar el flujo completo de solicitud de un taxi desde la web de Urban Routes, incluyendo:

Ingreso de direcciones de origen y destino.
Selección de la tarifa de viaje.
Registro del número de teléfono y verificación con código SMS.
Agregado de método de pago (tarjeta de crédito).
Envío de mensaje al conductor.
Solicitud de servicios adicionales (mantas, pañuelos, helados).
Confirmación del pedido y validación de asignación del conductor.

#Tecnologías y Herramientas Utilizadas

Python 3.13**
Selenium WebDriver**
Pytest** para la ejecución de las pruebas
Google Chrome** y **ChromeDriver**
Uso de **XPath**, **CSS Selectors** y **Expected Conditions (EC)** de Selenium
Captura de pantalla y depuración con `save_screenshot()`
Manejo de errores dinámico con `try/except`



#Cómo ejecutar las pruebas

#Instalar dependencias

Instala los paquetes necesarios (usa un entorno virtual si prefieres):

bash
pip install selenium pytest


#Ejecutar pruebas

Desde el directorio raíz del proyecto, corre el siguiente comando para ejecutar todas las pruebas:

bash
pytest main.py
O bien, puedes correr una prueba específica:

bash
pytest main.py::TestUrbanRoutes::test_confirm_order_and_driver_info


#Estructura del Proyecto


qa-project-Urban-Routes-es/

main.py             # Contiene clases y pruebas automatizadas
README.md           # Este archivo
data.py             #datos de importación


