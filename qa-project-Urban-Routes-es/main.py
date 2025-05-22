import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
import time

# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""

    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    request_taxi_button = (By.CSS_SELECTOR, ".button.round")
    comfort_rate_option = (By.XPATH, "//div[contains(@class, 'tcard')]//div[contains(text(), 'Comfort')]")
    phone_number_control = phone_number_control = (By.XPATH, "//div[@class='np-button']//div[contains(text(), 'Número de teléfono')]")
    phone_number_input = (By.ID, 'phone')
    phone_number_code_input = (By.ID, 'phone')
    phone_number_next_button = (By.CSS_SELECTOR, '.full')
    phone_number_confirm_button = (By.XPATH, "//button[contains(text(), 'Confirm')]")
    phone_number = (By.CLASS_NAME, 'np-text')
    payment_method_select = (By.XPATH, "//div[@class='pp-button filled']")
    add_card_control = (By.XPATH, "//div[contains(text(), 'Agregar tarjeta')]")
    card_number_input = (By.ID, "number")
    card_code_input = (By.ID, "code")
    card_pic_image = (By.CLASS_NAME, 'plc')
    card_credentials_confirm_button = (By.XPATH, "//button[contains(text(), 'Agregar')]")
    close_button_payment_method = (By.XPATH, "//div[@class='payment-picker open']//button")
    current_payment_method = (By.CLASS_NAME, 'pp-value-text')
    message_for_driver = (By.ID, 'comment')
    option_switches = (By.CLASS_NAME, 'switch')
    option_switches_inputs = (By.CLASS_NAME, 'switch-input')
    add_enumerable_option = (By.CLASS_NAME, 'counter-plus')
    amount_of_enumerable_option = (By.CLASS_NAME, 'counter-value')
    order_car_button = (By.CLASS_NAME, 'smart-button-wrapper')
    order_popup = (By.CLASS_NAME, 'order-body')
    progress_bar = (By.CSS_SELECTOR, '.order-progress.visible')
    driver_wait_time = (By.CLASS_NAME, 'order-header-time')
    order_driver_rating = (By.CLASS_NAME, 'order-btn-rating')
    order_driver_image = (By.XPATH, '//div[@class="order-button"]//img')
    order_driver_name = (By.XPATH, '//div[@class="order-btn-group"][1]/div[2]')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        #self.driver.find_element(*self.from_field).send_keys(from_address)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.from_field)
        ).send_keys(from_address)

    def set_to(self, to_address):
        #self.driver.find_element(*self.to_field).send_keys(to_address)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(self.to_field)
        ).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def set_route(self, from_address, to_address):
        self.set_from(from_address)
        self.set_to(to_address)

    def get_request_taxi_button(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.request_taxi_button)
        )

    def click_on_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_rate_option(self):
        return WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.comfort_rate_option)
        )

    def click_on_comfort_rate_option(self):
        self.get_comfort_rate_option().click()

# Phone number
    def get_phone_number_control(self):
        return WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.phone_number_control)
        )

    def click_on_phone_number_control(self):
        self.get_phone_number_control().click()

    def get_phone_number_input(self):
        return WebDriverWait(self.driver,10).until(
            EC.element_to_be_clickable(self.phone_number_input)
        )

    def click_on_phone_number_input(self):
        self.get_phone_number_input().click()

    def enter_phone_number(self, phone_number):
        # Primero clic en el label para activar el input
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.phone_number_label)
        ).click()


        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.phone_number_input)
        ).send_keys(phone_number)

    def click_on_phone_number_label(self):
        phone_label = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='phone']"))
        )
        phone_label.click()

    def click_on_phone_number_next_button(self):
        next_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.phone_number_next_button)
        )
        next_button.click()

    def enter_sms_code(self, code):
        input_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "code"))  # input visible en tu imagen
        )
        input_field.send_keys(code)

    def click_on_phone_number_confirm_button(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.phone_number_confirm_button)
        ).click()

#Credit Card
    def open_payment_method_modal(self):
        element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.payment_method_select)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        element.click()

    def click_add_card_option(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_card_control)
        ).click()

    def enter_card_details(self, number, code):
        number_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.card_number_input)
        )
        number_input.send_keys(number)

        # Sleep opcional para depurar delays visuales
        import time
        time.sleep(1.5)

        # Espera visibilidad (no clickable)
        cvv_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.card_code_input)
        )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", cvv_input)
        cvv_input.send_keys(code)
        cvv_input.send_keys(Keys.TAB)

        # También podrías hacer clic en otro elemento para perder foco
        try:
            other = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "plc"))
            )
            other.click()
        except:
            pass

    def click_confirm_card_credentials(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.card_credentials_confirm_button)
        ).click()

    def enter_driver_message(self, message):
        message_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.message_for_driver)
        )
        message_input.clear()
        message_input.send_keys(message)

    # Opciones adicionales
    def enable_all_switches(self):
        switches = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(self.option_switches)
        )
        inputs = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(self.option_switches_inputs)
        )
        for switch, checkbox in zip(switches, inputs):
            if not checkbox.is_selected():
                self.driver.execute_script("arguments[0].click();", switch)

    def add_ice_creams(self, count=2):
        plus_buttons = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(self.add_enumerable_option)
        )
        ice_cream_button = plus_buttons[-1]
        for _ in range(count):
            ice_cream_button.click()
            time.sleep(0.3)

    # Paso 1: Confirmar pedido
    def click_order_car_button(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.order_car_button)
        )
        button.click()

    # Paso 2: Esperar a que aparezca el modal de pedido (búsqueda activa)
    def wait_for_order_popup(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.order_popup)
        )

    # Paso 3: Esperar a que aparezca la barra de progreso (búsqueda del conductor)
    def wait_for_progress_bar(self):
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(self.progress_bar)
        )

    # Paso 4: Esperar a que se muestre la información del conductor
    def wait_for_driver_info(self):
        import time

        # Espera a que aparezca el bloque de info del conductor
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'order-btn-group'))
        )

        # Guarda una captura para inspección visual
        self.driver.save_screenshot("pantalla_final.png")

        # Opcional: imprime la info visible
        try:
            name = self.driver.find_element(By.XPATH, '//div[@class="order-btn-group"][1]/div[2]').text
            rating = self.driver.find_element(By.CLASS_NAME, 'order-btn-rating').text
            print(f"✅ Conductor asignado: {name}, rating: {rating}")
        except Exception as e:
            print("⚠️ No se pudo leer el nombre o rating:", e)

        # Espera un poco para ver el resultado final si corres en navegador visible
        time.sleep(3)


class TestUrbanRoutes:

    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})

        cls.driver = webdriver.Chrome(service=Service(), options=options)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_comfort_rate_option(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_request_taxi_button()
        routes_page.click_on_comfort_rate_option()

        comfort_rate = routes_page.get_comfort_rate_option().text
        comfort_text = "comfort"

    def test_phone_number_control(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_on_request_taxi_button()
        routes_page.click_on_comfort_rate_option()
        routes_page.click_on_phone_number_control()
        routes_page.click_on_phone_number_label()
        input_element = routes_page.get_phone_number_input()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", input_element)
        self.driver.execute_script("arguments[0].click();", input_element)
        input_element.send_keys(data.phone_number)

        assert input_element.get_attribute("value") == data.phone_number

    def test_phone_number_control(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.click_on_request_taxi_button()
        routes_page.click_on_comfort_rate_option()
        routes_page.click_on_phone_number_control()


        routes_page.click_on_phone_number_label()


        phone_input = routes_page.get_phone_number_input()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", phone_input)
        phone_input.send_keys(data.phone_number)

        routes_page.click_on_phone_number_next_button()

    def test_phone_number_control(self):
        self.test_set_route()
        routes_page = UrbanRoutesPage(self.driver)

        routes_page.click_on_request_taxi_button()
        routes_page.click_on_comfort_rate_option()
        routes_page.click_on_phone_number_control()

        routes_page.click_on_phone_number_label()
        input_field = routes_page.get_phone_number_input()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", input_field)
        input_field.send_keys(data.phone_number)

        routes_page.click_on_phone_number_next_button()

        # Obtener e ingresar el código de confirmación
        code = retrieve_phone_code(self.driver)
        routes_page.enter_sms_code(code)
        routes_page.click_on_phone_number_confirm_button()

    def test_add_credit_card(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_on_request_taxi_button()
        routes_page.click_on_comfort_rate_option()
        routes_page.click_on_phone_number_control()
        routes_page.click_on_phone_number_label()
        phone_input = routes_page.get_phone_number_input()
        phone_input.send_keys(data.phone_number)
        routes_page.click_on_phone_number_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.enter_sms_code(code)
        routes_page.click_on_phone_number_confirm_button()

        routes_page.open_payment_method_modal()
        routes_page.click_add_card_option()
        routes_page.enter_card_details(data.card_number, data.card_code)
        routes_page.click_confirm_card_credentials()

    def test_driver_message(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Configura dirección
        routes_page.set_route(data.address_from, data.address_to)

        # Selecciona tarifa
        routes_page.click_on_request_taxi_button()
        routes_page.click_on_comfort_rate_option()

        # Número de teléfono
        routes_page.click_on_phone_number_control()
        routes_page.click_on_phone_number_label()
        phone_input = routes_page.get_phone_number_input()
        phone_input.send_keys(data.phone_number)
        routes_page.click_on_phone_number_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.enter_sms_code(code)
        routes_page.click_on_phone_number_confirm_button()

        # Salta paso de tarjeta si falla, y avanza al mensaje
        message = "Por favor, toque el claxon al llegar."
        routes_page.enter_driver_message(message)

        # Validación
        message_box = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, 'comment'))
        )
        assert message_box.get_attribute("value") == message

    def test_extra_options(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Flujo hasta aquí
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_on_request_taxi_button()
        routes_page.click_on_comfort_rate_option()

        routes_page.click_on_phone_number_control()
        routes_page.click_on_phone_number_label()
        phone_input = routes_page.get_phone_number_input()
        phone_input.send_keys(data.phone_number)
        routes_page.click_on_phone_number_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.enter_sms_code(code)
        routes_page.click_on_phone_number_confirm_button()

        # Agrega mensaje
        routes_page.enter_driver_message("Trae una manta, por favor.")

        # Activar switches (manta y pañuelos)
        routes_page.enable_all_switches()

        # Agregar 2 helados
        routes_page.add_ice_creams(2)

        # Validar número de helados seleccionados
        value_elements = WebDriverWait(self.driver, 5).until(
            EC.presence_of_all_elements_located(routes_page.amount_of_enumerable_option)
        )
        ice_cream_count = value_elements[-1].text
        assert ice_cream_count == "2"

    def test_confirm_order_and_driver_info(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)

        # Flujo completo hasta el botón de pedido
        routes_page.set_route(data.address_from, data.address_to)
        routes_page.click_on_request_taxi_button()
        routes_page.click_on_comfort_rate_option()

        routes_page.click_on_phone_number_control()
        routes_page.click_on_phone_number_label()
        phone_input = routes_page.get_phone_number_input()
        phone_input.send_keys(data.phone_number)
        routes_page.click_on_phone_number_next_button()
        code = retrieve_phone_code(self.driver)
        routes_page.enter_sms_code(code)
        routes_page.click_on_phone_number_confirm_button()

        routes_page.enter_driver_message("Hola, toca claxon por favor.")
        routes_page.enable_all_switches()
        routes_page.add_ice_creams(2)

        # Paso: Confirmar el pedido
        routes_page.click_order_car_button()

        # Esperar modal de búsqueda
        routes_page.wait_for_order_popup()
        routes_page.wait_for_progress_bar()

        # Esperar información del conductor
        self.driver.save_screenshot("pantalla_final.png")
        routes_page.wait_for_driver_info()

        # Validaciones opcionales (verifica si la info se carga en el DOM)
        assert "4.9" in self.driver.page_source
        assert "Leon" in self.driver.page_source or "order-btn-group" in self.driver.page_source

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
