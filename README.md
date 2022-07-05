# jvcms

Proyecto de un CMS utilizando Wagtail y  para el Frontend utilizar Material UI (MUI) sin proyecto compilado de frontend, integrado en el mismo HTML desde CDN, cuenta con un portafolio y un diseño de blog anidando paginas como CMS

## Variables de Entorno
```py
APP_BASE_URL = "http://example.com"
APP_DB_ROOT= "/home/site/db"
APP_STATIC_ROOT= "/home/site/static"
APP_MEDIA_ROOT= "/home/site/media"
APP_SECRET_KEY= "django-insecure-*sl%whcx#i*k+gqy+(^2c(b57v22##+ks4*$zyilfxpz^gnny("
```


## Para levantar todo el Stack de Produccion
```sh
# Construir la imagen de la aplicacion
docker-compose  -f .\docker-compose-prod.yml build app
# Lventar todos los componentes
docker-compose  -f .\docker-compose-prod.yml up -d
# Migrar los modelos a la base de datos
docker-compose  -f .\docker-compose-prod.yml exec  app python manage.py migrate
# Para crear super user
docker-compose  -f .\docker-compose-prod.yml exec  app python manage.py createsuperuser 
```

## Administrar los componentes por separado
```sh
# Levantar la base de datos
docker-compose  -f .\docker-compose-prod.yml up -d database
# Levantar el webserver
docker-compose  -f .\docker-compose-prod.yml up -d web
# Levantar la aplicación
docker-compose  -f .\docker-compose-prod.yml up -d app
```