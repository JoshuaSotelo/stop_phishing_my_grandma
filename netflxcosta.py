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


def jodiendo_reforma(numero):
    contador = 1

    while numero > 0:
        print(contador)
        # Datos procesados random =
        metros_random = str(random.randrange(999))
        direccion_random = (
            metros_random + " metros " + random.choice(direccion) + random.choice(direcciones))
        nombre_random = random.choice(nombres) + " " + random.choice(nombres)
        nombre_usuario_random = random.choice(
            nombres) + str(random.randrange(999))
        contrasena_random = random.choice(nombres) + str(random.randrange(9999))
        correo_falso = nombre_usuario_random + random.choice(["@gmail.com", "@yahoo.es", "@hotmail.com", "@celda44.com",
                                                              "@celda32.com", "@patazos2023.com", "@laputaquelopario.universidadfalsadesumadre.cr"])
        codigo_postal_random = random.randrange(90000) + 10000
        telefono_random = random.randrange(90000000) + 10000000
        fecha_nacimiento_random = random.randrange(900000000) + 10000000
        tarjeta_random_random = random.randrange(
            1234567890123456) + 1000000000000000
        fecha_cad_random = random.randrange(999999) + 100
        ccv_falso_random = random.randrange(9999) + 100
        # uso esas sumas para asegurarme la cantidad de digitos en el numero random de los inputs

        # Inicia el push
        web = webdriver.Chrome()
        web.get('https://netflxcosta.com/index.php?success=validatedok')
        time.sleep(0.3)

        WebDriverWait(web, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/form/div/div[1]/input"))).send_keys(correo_falso)

        rellenar_contra = web.find_element(
            "xpath", '/html/body/form/div/div[2]/input')
        rellenar_contra.send_keys(contrasena_random)

        WebDriverWait(web, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/form/div/button"))).click()

        WebDriverWait(web, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/form/main[1]/section/button"))).click()

        nombre_web = WebDriverWait(web, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/form/main[2]/section/div[1]/input")))
        nombre_web.send_keys(nombre_random)
        direccion_web = web.find_element(
            "xpath", '/html/body/form/main[2]/section/div[2]/input')
        direccion_web.send_keys(direccion_random)
        codigo_web = web.find_element(
            "xpath", '/html/body/form/main[2]/section/div[3]/input')

        codigo_web.send_keys(codigo_postal_random)
        telefono_random_web = web.find_element(
            "xpath", '/html/body/form/main[2]/section/div[4]/input')
        telefono_random_web.send_keys(telefono_random)
        fecha_web = web.find_element(
            "xpath", '/html/body/form/main[2]/section/div[5]/input')
        fecha_web.send_keys(fecha_nacimiento_random)

        WebDriverWait(web, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/form/main[2]/section/button"))).click()

        WebDriverWait(web, 400).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/form/main[3]/section/div[1]/input'))).send_keys(nombre_random)
        tarjeta_web = web.find_element(
            "xpath", '/html/body/form/main[3]/section/div[2]/input')
        tarjeta_web.send_keys(tarjeta_random_random)
        fecha_tarjeta_web = web.find_element(
            "xpath", '/html/body/form/main[3]/section/div[3]/input')
        fecha_tarjeta_web.send_keys(fecha_cad_random)
        ccv_web = web.find_element(
            "xpath", '/html/body/form/main[3]/section/div[4]/input')
        ccv_web.send_keys(ccv_falso_random)

        WebDriverWait(web, 300).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/form/main[3]/section/button"))).click()
        time.sleep(1)
        contador = contador+1
        numero = numero-1


jodiendo_reforma(200)
