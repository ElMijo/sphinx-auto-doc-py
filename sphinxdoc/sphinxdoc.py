# -*- coding: utf-8 -*-

from helpers.files import get_files, zip_dir, abspath,basename,move,pyment_files, backup_files,apply_patch
from pyment import PyComment
from terminal_text_color import TextColor,AlertTextColor
import os

proyecto = '../example-doc-project'

tc = TextColor()

if backup_files(proyecto):

    archivos = pyment_files(proyecto)

    tc.default_cyan("Creando documentación..")

    for archivo in archivos:
        c = PyComment(archivo['original'])
        c.proceed()
        c.diff_to_file(archivo['patch'])
        apply_patch(archivo['patch'])





# archivos = pyment_files(proyecto)

# zipname = './'+basename(proyecto)

# zipfilename = zipname+'.zip'



# if zip_dir(proyecto,zipname):
#     if move(zipfilename,abspath(proyecto)+'/'+zipfilename):
#         for archivo in archivos:
#             c = PyComment(archivo['original'])
#             c.proceed()
#             c.diff_to_file(archivo['patch'])