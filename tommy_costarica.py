import random
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException 
from getnames import names

# ------------ Tienen que instalar Selenium con pip3
# Lista de Nombres Falsos para introducir en los  Forms
# Creditos a JoshuaSotelo
nombres, apellidos = names()

direcciones = ["la casa de su madre, a ", "la casa de su esposa que no solo goza en visita conyugal", "pulperia celda 12",
               "Super culantro 76", "Guadalupe en el techo de el guadalupano", "cine magali en el melcochon", "fereteria hermanos ninguno"]
direccion = ["Frente de ", "Costado este de ", "Costado Norte de ",
             "Costado Sur de", "Costado oeste de ", "diagonal de ", "Sobre calle ", "Atras de "]
ciudades = ["Alajuela", "Su Madre", "San Jose", "Rico vivir en la carcel", "Te Van a Atrapar"]

mes = ["01","02","03","04","05","06","07","08","09","10","11","12"]
divPrincipalcarrusel = [1,2,3,4,5]

contador = 1


def jodiendo_tommy_costa(numero, cantidadArticulos):
    global contador
  

    while numero >= contador:
        contador += 1
        print(contador)
        # Datos procesados random =
        metros_random = str(random.randrange(999))
        direccion_random = (
            metros_random + " metros de " + random.choice(direccion) + random.choice(direcciones))

        ciudad_random = random.choice(ciudades)
        nombre_random = random.choice(nombres)
        apellido_random = random.choice(nombres)

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

        # Formulario de registro
        web.get('https://www.tommyhilfigercostaricas.com/create_account.html')
        time.sleep(0.3)

        nombre_web = WebDriverWait(web, 30).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div[10]/div/div[1]/div/div/form/fieldset/fieldset[1]/input[1]")))
        nombre_web.send_keys(nombre_random)
 
        apellido_web = web.find_element(
            "xpath", '/html/body/div[1]/div[10]/div/div[1]/div/div/form/fieldset/fieldset[1]/input[2]')
        apellido_web.send_keys(apellido_random)

        direccion_web = web.find_element(
            "xpath", '/html/body/div[1]/div[10]/div/div[1]/div/div/form/fieldset/fieldset[1]/input[3]')
        direccion_web.send_keys(direccion_random)

        ciudad_web = web.find_element(
            "xpath", '/html/body/div[1]/div[10]/div/div[1]/div/div/form/fieldset/fieldset[1]/input[4]')
        ciudad_web.send_keys(ciudad_random)        

        codigo_web = web.find_element(
            "xpath", '/html/body/div[1]/div[10]/div/div[1]/div/div/form/fieldset/fieldset[1]/input[6]')
        codigo_web.send_keys(codigo_postal_random)

        telefono_random_web = web.find_element(
            "xpath", '/html/body/div[1]/div[10]/div/div[1]/div/div/form/fieldset/fieldset[2]/input[1]')
        telefono_random_web.send_keys(telefono_random)

        correo_random_web = web.find_element(
            "xpath", '/html/body/div[1]/div[10]/div/div[1]/div/div/form/fieldset/fieldset[3]/input[1]')
        correo_random_web.send_keys(correo_falso)

        contrasena_random_web = web.find_element(
            "xpath", '/html/body/div[1]/div[10]/div/div[1]/div/div/form/fieldset/fieldset[3]/input[2]')
        contrasena_random_web.send_keys(contrasena_random)

        contrasena_random2_web = web.find_element(
            "xpath", '/html/body/div[1]/div[10]/div/div[1]/div/div/form/fieldset/fieldset[3]/input[3]')
        contrasena_random2_web.send_keys(contrasena_random)
        
        # Boton de registrar
        WebDriverWait(web, 30).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div[10]/div/div[1]/div/div/form/div[1]/input"))).click() 

        cantidadArticulosRandom = random.randint(1,cantidadArticulos);


        try:
            # Prueba para el pago de tarjeta y hacer el pedido.
            for x in range(cantidadArticulosRandom):             
                web.get('https://www.tommyhilfigercostaricas.com/')
                time.sleep(0.9)
                divPrincipalcarrusel_random = random.choice(divPrincipalcarrusel);

                # Boton de carrusel del 1 al 12 random
                WebDriverWait(web, 30).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div[9]/div/div[1]/div/div[2]/div[1]/div[1]/a/img"))).click() 
                #(By.XPATH, "/html/body/div[1]/div[9]/div/div[1]/div/div[2]/div["+ str(divPrincipalcarrusel_random)+"]/div[1]/a/img"))).click() 
                time.sleep(0.9)
            
                # Talla, controlar error cuando quitan inventario.
                WebDriverWait(web, 30).until(EC.element_to_be_clickable(
                (By.XPATH, "/html/body/div[1]/div[10]/div[1]/div/div[1]/div[1]/form/div[2]/div[2]/div[4]/div[2]/ul/li[1]"))).click()         
      

            # Boton agregar canasta
            WebDriverWait(web, 30).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/div[10]/div[1]/div/div[1]/div[1]/form/div[2]/div[2]/div[4]/div[3]/div[2]"))).click() 
            time.sleep(0.4)
         
        except:
            print ("Element is not clickable, si quitan el inventario de productos que controle el error y comience nuevamente")
            jodiendo_tommy_costa(numero, cantidadArticulos)

          
        time.sleep(0.4)
        #Boton de carrito para pagar
        WebDriverWait(web, 30).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div[2]/div[3]/div/div[1]/a[4]/i"))).click() 

        time.sleep(0.4)
        #Boton de realizar pedido
        WebDriverWait(web, 30).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div[10]/div/div[1]/div/div/div/form/div[3]/a"))).click() 


        WebDriverWait(web, 400).until(EC.element_to_be_clickable(
            (By.XPATH, '/html/body/div[1]/div[10]/div/div/div/div[1]/form/div[2]/div[1]/fieldset/div[1]/label/div/ul/li[1]/div/div[2]/div/div/div/input[1]'))).send_keys(tarjeta_random_random)

        ccv_web = web.find_element(
            "xpath", '/html/body/div[1]/div[10]/div/div/div/div[1]/form/div[2]/div[1]/fieldset/div[1]/label/div/ul/li[1]/div/div[2]/div/div/div/input[2]')
        ccv_web.send_keys(ccv_falso_random)        
 

        fecha_dia_web = web.find_element(
            "xpath", '/html/body/div[1]/div[10]/div/div/div/div[1]/form/div[2]/div[1]/fieldset/div[1]/label/div/ul/li[1]/div/div[2]/div/div/div/select[1]')
        fecha_dia_web.send_keys(random.choice(mes))


        fecha_anno_web = web.find_element(
            "xpath", '/html/body/div[1]/div[10]/div/div/div/div[1]/form/div[2]/div[1]/fieldset/div[1]/label/div/ul/li[1]/div/div[2]/div/div/div/select[2]')
        fecha_anno_web.send_keys(str(random.randint(2023,2040)))


        radiobutton_web = web.find_element(
            "xpath", '/html/body/div[1]/div[10]/div/div/div/div[1]/form/div[2]/div[1]/fieldset/div[2]/input')
        fecha_anno_web.send_keys(True)

        # Boton agregar canasta
        WebDriverWait(web, 30).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div[1]/div[10]/div/div/div/div[1]/form/div[2]/div[1]/div[2]/input"))).click() 

        time.sleep(0.9)
    



jodiendo_tommy_costa(5000,1)