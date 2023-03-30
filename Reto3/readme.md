# info de la materia: ST0263 Topicos especiales en telematica
#
## Estudiante: Stiven Yepes Vanegas, esyepesv@eafit.educo
## Profesor: Edwin Nelson Montoya Munera, emontoya@eafit.edu.co

# Aplicación Monolítica con Balanceo y Datos Distribuidos (BD y archivos)
  
# 1. breve descripción de la actividad
Desplegar un CMS WordPress empleando la tecnología de contenedores en una arquitectura de alta disponibilidad con su propio dominio y certificado SSL. Se utilizará un balanceador de cargas de la capa de aplicación del WordPress, dos servidores adicionales para la base de datos y archivos distribuidos en NFS. Se desplegarán cinco VM en Google GCP para implementar esta arquitectura y mejorar la disponibilidad de la aplicación.
  
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

En general, se cumplieron con la mayoría de los requerimientos funcionales y no funcionales propuestos por el profesor. Sin embargo, no se pudo cumplir con el requisito de implementar un certificado SSL para las conexiones seguras a través de HTTPS.

Se desplegaron las cinco máquinas virtuales en Google Cloud, de las cuales dos correspondían al CMS WordPress, una a la base de datos MySQL, una al servidor NFS de archivos compartidos y una al balanceador de cargas basado en Nginx. Tres de estos servicios corren en contenedores de Docker (WordPress, base de datos y balanceador de carga).
  

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Como se mencionó anteriormente, del reto no se pudo cumplir con el requisito de el certificado SSL para las conexiones seguras, por lo que no se puede acceder por https sino solo por http.

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

El diseño implementado es el que plantea el profesor en el enunciado:
![image](https://user-images.githubusercontent.com/60147085/228666003-3a14e263-5e38-4af1-9fbe-53d850e3d282.png)


# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## como se compila y ejecuta.

- La mayoría de los componentes del reto están montados en contenedores de Docker. Para correr estos contenedores, se debe ir a la carpeta de cada uno de los componentes y ejecutar el archivo docker-compose.yml con el comando ´docker-compose -f <nombre del archivo> up´.

  
## detalles del desarrollo.
  Todo el desarrollo está desplegado en la nube de Google Cloud Platform (GCP) utilizando IaaS, específicamente las máquinas virtuales del servicio Compute Engine. Se utilizaron contenedores de Docker montados a través de Docker Compose para los componentes de la aplicación en WordPress, la base de datos y el balanceador de carga. Para el servidor NFS, se configuró el host directamente en la máquina virtual.
  
## detalles técnicos
  - Tipo de maquina virtual: e2-Small.
  - Sistema operativo: Ubuntu 18.04 LTS.
  - Docker version 20.10.21.
  - Docker-compose version 1.17.1.
  - Base de datos: MySQL 5.7.
  - Balanceador de carga: NGINX.
  - CMS :WordPress.

## descripción y como se configura los parámetros del proyecto (ej: ip, puertos, conexión a bases de datos, variables de ambiente, parámetros, etc)
  Los diferentes parámetros se configuran en los archivos de Docker Compose, donde se especifica la dirección IP, los puertos, la conexión a la base de datos, las variables de ambiente, entre otros. Se pueden editar estos parámetros según las necesidades de cada caso.
  ![image](https://user-images.githubusercontent.com/60147085/228716276-43859d68-8286-42c4-b63e-20bc9c9682cc.png)

  
## Organización del código por carpetas
  El código está organizado en varias carpetas, como se muestra en la siguiente imagen:
  
![image](https://user-images.githubusercontent.com/60147085/228677957-4e26466c-ac3f-469a-8973-93a21fbe6036.png)


## Resultados o pantallazos 
  
  Maquinas virtuales configuradas corriendo:
  ![image](https://user-images.githubusercontent.com/60147085/228716522-5cbb943d-6982-4c3b-9d60-bee0b515e567.png)



# 4. Descripción del ambiente de EJECUCIÓN (en producción) lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.

## IP o nombres de dominio en nube o en la máquina servidor.
  - IPs:
  LB: 34.30.3.196
  wordpress1:35.223.171.80
  wordpress2: 130.211.215.101
  
  - Dominio: reto3.stivenyepes.lat
  
    para hacer pruebas se estableció un dominio para acceder directamente a cada una de las instancias de wordpress:
    w1.stivenyepes.lat -
    w2.stivenyepes.lat

## como se lanza el servidor.
  Para lanzar el servidor solamente es necesario iniciar las maquinas virtuales en GCP.

## una mini guia de como un usuario utilizaría el software o la aplicación
El usuario debe entrar al dominio reto3.stivenyepes.lat, donde encontrará una página de "Hola mundo" de WordPress.

## Resultados o pantallazos 

reto3:
![image](https://user-images.githubusercontent.com/60147085/228669849-6d3d040d-f158-4f6d-909e-f5a980bbca82.png)

w1:
![image](https://user-images.githubusercontent.com/60147085/228668982-e8a30921-3cfc-456b-bea6-1ad36dc2102c.png)

w2:
![image](https://user-images.githubusercontent.com/60147085/228669924-597f8373-94ce-4fa9-bcfb-4f607b4d7c90.png)


# referencias:
Overview of docker compose CLI: https://docs.docker.com/compose/reference/
How To Set Up an NFS Mount on Ubuntu 22.04: https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nfs-mount-on-ubuntu-22-04
How to Connect a Domain to a Server or Hosting: https://www.namecheap.com/support/knowledgebase/article.aspx/9837/46/how-to-connect-a-domain-to-a-server-or-hosting/

