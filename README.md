# Jodiendo-a-la-reforma
Código simple de Python que ataca página de phishing falsas costarricenses

# Tabla de contenido

- [Jodiendo-a-la-reforma](#jodiendo-a-la-reforma)
- [Requisitos](#requisitos)
- [Páginas que atacamos](#páginas-que-atacamos)
- [Como puedo contribuir al proyecto](#como-puedo-contribuir-al-proyecto)





# Requisitos
Luego simplemente corre el código(dependiendo del archivo .py que quiera correr) con el comando de correr de Python desde la terminal abierta (la terminal debe de estar abierta en la carpeta donde tiene los archivos .py)

1. Python 3
2. Selenium
3. Faker
 

Para activar la script ejecuta este comando
1. linux: `chmod +x instalador.sh`
2. Windows: `attrib +x instalador.sh`

Puedes instalar estas librerías simplemente ejecutando el script en bash con el comando `./instalador`

# Páginas que atacamos
Actualmente, este repositorio ataca las siguientes páginas falsas de phishing:

1. netflxcosta.com
2. correosdecosta.com
3. tommyhilfigercostaricas.com

Todas estas son páginas que se hacen pasar por las oficiales para hacer phishing.

Cualquier PR que quieran hacer para incluir código que ataque otras páginas maliciosas bienvenidas sea :)

# Como puedo contribuir al proyecto

Para contribuir al proyecto es preferible que utilicemos el siguiente workflow

1. Clone el repositorio
2. Crea una issue y nómbrala con un nombre descriptivo
    - ejemplo: Agregar nueva página
3. Crea una nueva rama con el número de issue 
    - ejemplo: `git checkout -b story-23`
4. Crea los cambios que crees pertinentes
5. tiliza convencional commits para tu commit
   - ejemplo: `fix: issue #34 realice los cambios para solucionar ese problema`
6. Ahora has tu push al repositorio remoto
7. Crea un `merge-request`
8. Una vez tu merge-request sea aprovado elimina la rama que creaste

Recomiendo seguir este workflow para que el proyecto sea más seguro.


#!
El código que se encuentra aquí es proporcionado con fines educativos y se proporciona "tal cual" sin garantía de ningún tipo, expresa o implícita. El o los autores no asumen ninguna responsabilidad por el uso que se le dé al código aquí contenido. Cada usuario es responsable de usar este código de manera discrecional y bajo su propia responsabilidad. El uso indebido del código y sus consecuencias serán responsabilidad exclusiva del usuario. Si decide utilizar el código, acepta estos términos y condiciones.
