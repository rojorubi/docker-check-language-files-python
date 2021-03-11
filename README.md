# docker-check-language-files-python
Proyecto para chequear ficheros de idiomas en formato json dentro de un dockerfile basado en python 3


Run in command line

docker build --no-cache --tag image-docker-name -f ./Dockerfile_i18n .



Run in JenkinsFile

sh(script: "docker build --no-cache --tag image-docker-name -f ./Dockerfile_i18n .", returnStdout: false)
sh(script: "docker run image-docker-name", returnStdout: false)