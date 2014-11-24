# -*- coding: utf-8 -*-
# 
def get_files(path,ext='py'):
    """Esta función nos permite obtener los archivos de una determinada extención dentro de una ruta"""
    import os
    cfiles = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.'+ext):
                cfiles.append(os.path.join(root, file))

    return cfiles