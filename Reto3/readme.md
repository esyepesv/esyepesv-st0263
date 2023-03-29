# info de la materia: ST0263 Topicos especiales en telematica
#
## Estudiante: Stiven Yepes Vanegas, esyepesv@eafit.educo
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

# Aplicación Monolítica con Balanceo y Datos Distribuidos (BD y archivos)
  
# 1. breve descripción de la actividad
Desplegar un CMS WordPress empleando la tecnología de contenedores en una arquitectura de alta disponibilidad con su propio dominio y certificado SSL. Se utilizará un balanceador de cargas de la capa de aplicación del WordPress, dos servidores adicionales para la base de datos y archivos distribuidos en NFS. Se desplegarán cinco VM en Google GCP para implementar esta arquitectura y mejorar la disponibilidad de la aplicación.
  
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

  En general se complió con casi todos los requisitos funcionales y no funcionales, excepto con el certificado SSL para la conexion HTPPS. Es decir, se desplegaron las 5 maquinas virtuales en Google Cloud, de las cuales 2 correspondian al CMS WordPress, 1 a la base de datos de mySQL, 1 al servidor NFS de archivos compartidos y 1 al balanceador de cargas de basado en nginx. 3 de estos servicios corren en contenedores de docker (wordpress, base de datos y balanceador de carga).
  

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Como se mencionó anteriormente, del reto no se pudo cumplir con el requisito de el certificado SSL para las conexiones seguras, por lo que no se puede acceder por https sino solo por http.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

El diseño implementado es el que plantea el profesor en el enunciado:
![image](https://user-images.githubusercontent.com/60147085/228666003-3a14e263-5e38-4af1-9fbe-53d850e3d282.png)


# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## como se compila y ejecuta.
## detalles del desarrollo.
## detalles técnicos
## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
## opcional - detalles de la organización del código por carpetas o descripción de algún archivo. (ESTRUCTURA DE DIRECTORIOS Y ARCHIVOS IMPORTANTE DEL PROYECTO, comando 'tree' de linux)
## 
## opcionalmente - si quiere mostrar resultados o pantallazos 
reto3:
![image](https://user-images.githubusercontent.com/60147085/228669849-6d3d040d-f158-4f6d-909e-f5a980bbca82.png)

w1:
![image](https://user-images.githubusercontent.com/60147085/228668982-e8a30921-3cfc-456b-bea6-1ad36dc2102c.png)

w2:
![image](https://user-images.githubusercontent.com/60147085/228669924-597f8373-94ce-4fa9-bcfb-4f607b4d7c90.png)


# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

# IP o nombres de dominio en nube o en la máquina servidor.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)

## como se lanza el servidor.

## una mini guia de como un usuario utilizaría el software o la aplicación

## opcionalmente - si quiere mostrar resultados o pantallazos 






# 5. otra información que considere relevante para esta actividad.

# referencias:
<debemos siempre reconocer los créditos de partes del código que reutilizaremos, así como referencias a youtube, o referencias bibliográficas utilizadas para desarrollar el proyecto o la actividad>
## sitio1-url 
## sitio2-url
## url de donde tomo info para desarrollar este proyecto

#### versión README.md -> 1.0 (2022-agosto)
