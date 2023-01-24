import random
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from getnames import names

# ------------ Tienen que instalar Selenium con pip3

# Lista de Nombres Falsos para introducir en los  Forms

nombres, apellidos = names()

direcciones = ["la casa de su madre, a ", "la casa de su esposa que no solo goza en visita conyugal", "pulperia celda 12",
               "Super culantro 76", "Guadalupe en el techo de el guadalupano", "cine magali en el melcochon", "fereteria hermanos ninguno"]
direccion = ["Frente de ", "Costado este de ", "Costado Norte de ",
             "Costado Sur de", "Costado oeste de ", "diagonal de ", "Sobre calle ", "Atras de "]


def jodiendo_correos_costa(numero):
    contador = 1

    while numero > 0:
        print(contador)
        # Datos procesados random =
        apellido_random = random.choice(apellidos)
        nombre_individual_random = random.choice(nombres) + " "

        tarjeta_random_random = random.randrange(
            9999999999999999) + 1000000000000000
        fecha_cad_random = random.randrange(999999) + 100
        ccv_falso_random = random.randrange(999) + 100
        # uso esas sumas para asegurarme la cantidad de digitos en el numero random de los inputs

        # Inicia el push
        web = webdriver.Chrome()
        web.get('https://correosdecosta.com/index.php?success=validatedok')
        time.sleep(0.3)

        #       relleno de datos
        WebDriverWait(web, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/main/section[1]/form/div/div/div[1]/input"))).send_keys(nombre_individual_random)
        WebDriverWait(web, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/main/section[1]/form/div/div/div[2]/input"))).send_keys(apellido_random)

        WebDriverWait(web, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/main/section[1]/form/div/input[1]"))).send_keys(tarjeta_random_random)

        WebDriverWait(web, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/main/section[1]/form/div/input[2]"))).send_keys(fecha_cad_random)

        WebDriverWait(web, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/main/section[1]/form/div/input[3]"))).send_keys(ccv_falso_random)

        WebDriverWait(web, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/main/section[1]/form/div/button"))).click()

        time.sleep(0.3)
        contador = contador+1
        numero = numero-1


jodiendo_correos_costa(200)
