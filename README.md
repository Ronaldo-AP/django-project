# Django Project

El proyecto consiste en una aplicación web que permite publicar mensajes en un feed al estilo de Twitter. Los mensajes pueden ser publicados por cualquier usuario, pero solo pueden ser editados o eliminados por el usuario que los publicó. Los usuarios pueden seguir a otros usuarios, y ver un feed con los mensajes de los usuarios que siguen.

Actualmente, la aplicación cuenta con las siguientes funcionalidades:

- Registro de usuarios
- Inicio de sesión
- Cierre de sesión
- Feed principal con los mensajes de los usuarios que sigue el usuario actual (en desarrollo)

## Comenzando 🚀

Para aumentar la dificultad del proyecto, se ha decidido utilizar mongo como base de datos. Para ello, se ha utilizado la librería `djongo` que permite utilizar mongo como base de datos en un proyecto de Django.

De manera nativa Django utiliza bases de datos relacionales como MySQL, PostgreSQL, SQLite, etc. Para utilizar mongo como base de datos, se debe instalar la librería `djongo` y configurar el proyecto para que utilice mongo como base de datos. 

Para este tipo de aplicaciones, se recomienda utilizar una base de datos relacional como MySQL o PostgreSQL, ya que mongo no es una base de datos relacional, y por lo tanto no es la mejor opción para este tipo de aplicaciones. Pero para este proyecto se ha decidido utilizar mongo para aumentar la dificultad del proyecto.

## Pre-requisitos 📋

La aplicación está desarrollada para que pueda ser levantada con dos contenedores de Docker. Uno para la aplicación web y otro para la base de datos. Por lo tanto, para poder levantar la aplicación, es necesario tener instalado Docker y Docker Compose.

## Instalación 🔧

Para instalar la aplicación, es necesario clonar el repositorio y ejecutar el siguiente comando:

```
docker-compose build
docker-compose up
```

