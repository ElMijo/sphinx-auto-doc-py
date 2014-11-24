# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os, shutil
from terminal_text_color import TextColor,AlertTextColor

def get_files(ruta_origen,ext='py'):
    """Esta función nos permite obtener los archivos de una determinada extención dentro de una ruta"""
    cfiles = []
    for root, dirs, files in os.walk(ruta_origen):
        for file in files:
            if file.endswith('.'+ext):
                cfiles.append(os.path.join(root, file))

    return cfiles

def zip_dir(ruta_origen,ruta_destino):
    """Esta función permite crear un archivo .zip de una carpeta"""
    try:
        shutil.make_archive(ruta_destino, 'zip', ruta_origen)
    except EnvironmentError:
        return False
    else:
        return True    

def abspath(ruta_origen):
    """Esta función permite obtener la ruta absoluta de un path"""
    return os.path.abspath(ruta_origen)

def basename(ruta_origen):
    """Esta función permite obtener el nombre base de la ruta espesificada"""
    return os.path.basename(ruta_origen)

def move(ruta_origen,ruta_destino):
    """Esta función permite mover un archivo o directorio a otra locación"""
    try:
        shutil.move(ruta_origen,ruta_destino)
    except EnvironmentError:
        return False
    else:
        return True

def backup_files(ruta_origen):
    
    respuesta = False
    archivos = get_files(ruta_origen)
    zipname = './'+basename(ruta_origen)
    zipfilename = zipname+'.zip'
    backupfilename = abspath(ruta_origen)+'/'+zipfilename
    tc = TextColor()
    atc= AlertTextColor()

    print tc.default_cyan("Creando backup de del proyecto...")

    if zip_dir(ruta_origen,zipname):

        if move(zipfilename,backupfilename):

            respuesta = True

            print tc.default_green("Backup creado..")

        else:

            atc.error("No se Pudo mover el Archivo de Respaldos .zip a la carpeta destino")

    else:

        atc.error("No se Pudo crear el Archivo de Respaldos .zip")

    return respuesta


def pyment_files(ruta_origen):
    """Esta función permite estructurar una lista de archivos obtimos para utilizar los comandos de Pyment"""
    files = []
    for f in get_files(ruta_origen):
        files.append(dict(original=f,patch=f+".patch"))

    return files

def apply_patch(ruta_origen):
    os.system("patch -s -p1 < "+ruta_origen+" && rm "+ruta_origen)