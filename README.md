#Urban Routes – Automatización de Pruebas con Selenium

Este proyecto automatiza el proceso completo de solicitud de un taxi en la plataforma **Urban Routes. Las pruebas están desarrolladas en Python utilizando Selenium WebDriver y Pytest.

# Estructura del proyecto

qa-project-Urban-Routes-es/

main.py             # Contiene clases y pruebas automatizadas
data.py             # Variables de prueba como direcciones, tarjeta y teléfono
README.md           # Este archivo con documentación del proyecto

#Descripción del Proyecto

El objetivo principal es validar, de forma automática, que el flujo de solicitud de taxis funcione correctamente desde el navegador web. Las pruebas abarcan:

- Ingreso de direcciones de origen y destino.
- Selección de tipo de tarifa.
- Registro y verificación del número de teléfono mediante código SMS.
- Agregado de método de pago (tarjeta de crédito).
- Envío de mensaje personalizado al conductor.
- Selección de servicios adicionales como mantas, pañuelos o helados.
- Confirmación del pedido y validación de asignación del conductor.

---

#Tecnologías y Herramientas Utilizadas

Python 3.13
Selenium WebDriver
Pytest para orquestar y ejecutar las pruebas
Google Chrome y ChromeDriver
XPath, CSS Selectors** y **Expected Conditions (EC) para selección y espera de elementos



#Autor

Nombre completo: Andres Felipe Arteaga Cruz
Cohorte: Andres Arteaga, 27. grupo - 8vo sprint



#Instalación y Configuración

#1. Clona este repositorio:

bash
git clone https://github.com/tuusuario/qa-project-Urban-Routes-es.git
cd qa-project-Urban-Routes-es

#Instala selenium

pip install selenium pytest

#Como ejecutar las pruebas

pytest main.py
O, Click en el icono de play
#nota
Asegurate de tener seleccionado el current file

# es posible ejecutar pruebas individuales
pytest main.py::TestUrbanRoutes::test_modal_taxi
O, Click en el icono de play
