# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import  os
from string import find

class FileDir(object):
    """docstring for FileDir"""
    def __init__(self,root_path=''):
        self.__root_path__ = root_path if os.path.exists(root_path) else '.'

    @property
    def abspath(self):
        """Devuelve una versión normalizada de la ruta absoluta del archivo o directorio"""
        return os.path.abspath(self.__root_path__)

    @property
    def basename(self):
        """Devuelve el nombre base del archivo o directorio"""
        return os.path.basename(self.__root_path__)

    @property
    def dirname(self):
        """Devuelve el nombre del directorio"""
        return os.path.dirname(self.__root_path__)

    @property
    def split(self):
        """Devuelve un arreglo con del dirname y el base basename de la ruta del archivo o directorio"""
        return os.path.split(self.__root_path__)                     

    @property
    def getatime(self):
        """Devuelve el timestamp de la ultima vez que se acceso el archivo o directorio"""
        return os.path.getatime(self.__root_path__)  

    @property
    def getmtime(self):
        """Devuelve el timestamp de la ultima modificación de el archivo o directorio"""
        return os.path.getmtime(self.__root_path__)  

    @property
    def getsize(self):
        """Devuelve el tamaño del archivo o directorio en bytes"""
        return os.path.getsize(self.__root_path__)                   

    @property
    def splitunc(self):
        """Devuelve un arreglo con del dirname y el base basename de la ruta del archivo o directorio"""
        return os.path.splitunc(self.__root_path__)  

    @property
    def isfile(self):
        """Valida si la ruta es de un archivo"""
        return os.path.isfile(self.__root_path__)

    @property
    def isfilebinary(self):
        """Valida si la ruta del archivo es deun archivo binario"""

        if self.isfile:

            archivo = open(self.__root_path__, 'rb' )
            try:
                CHUNKSIZE = 1024
                while 1:
                    chunk = archivo.read(CHUNKSIZE)
                    if '\0' in chunk: 
                        return True
                    if len(chunk) < CHUNKSIZE:
                        break 
            finally:
                archivo.close()

        return False         

    @property
    def isdir(self):
        """Valida si la ruta es de un directorio"""
        return os.path.isdir(self.__root_path__)

    @property
    def islink(self):
        """Valida si la ruta es un enlace simbolico"""
        return os.path.islink(self.__root_path__)    

    @property
    def isabs(self):
        """Valida si la ruta es absoluta"""
        return os.path.isabs(self.__root_path__)

    @property
    def ismount(self):
        """Valida si la ruta es un punto de montaje"""
        return os.path.ismount(self.__root_path__)

    def remove(self):
        if self.isdir:
            shutil.rmtree(self.abspath)
        else:
            os.remove(self.abspath)

        del self
    


class Dir(FileDir):
    """docstring for Dir"""
    def __init__(self, filename):
        super(Dir, self).__init__(filename)
                        
    def get_files(self,ext='*'):
        """Esta función nos permite obtener los archivos de una determinada extención dentro de una ruta"""

        lista_archivos = []

        if self.isdir:
            for raiz, directorios, archivos in os.walk(self.__root_path__):
                for archivo in archivos:
                    if ext == '*' or archivo.endswith('.'+ext):
                        lista_archivos.append(os.path.join(raiz, archivo))

        return lista_archivos


class File(FileDir):
    """docstring for File"""
    def __init__(self, filename):
        super(File, self).__init__(filename)

    @property
    def content_lines(self):
        """Permite ontener el contenido de un archivo"""
        content = None

        try:
            if not self.isfilebinary:
                content = open(self.abspath, 'r').readlines()
                content.insert(0,None)

        except:
            pass

        return content

    @property
    def content(self):
        """Permite ontener el contenido de un archivo"""
        content = None

        try:
            if not self.isfilebinary:
                content = open(self.abspath, 'r').read()

        except:
            pass

        return content

    def write_content(self,content):
        """Permite escribir un nuevo contenido en el archivo"""
        write = False

        try:
            if not self.isfilebinary:
                archivo = open(self.abspath, 'w')
                archivo.write(content)
                archivo.close()
                write = True

        except:
            pass

        return write

    def write_content_lines(self,lines):
        """Permite escribir determinado contenido separado por lines dentro del archivo"""
        write = False

        try:
            if not self.isfilebinary:
                if lines[0] is None:
                    lines.pop(0)

                archivo = open(self.abspath, 'w')
                archivo.writelines(lines)
                archivo.close()
                write = True

        except:
            pass

        return write

    def strip_end_lines(self):
        """Permite eliminar los espacios en blanco que pueda contener el archivo al final del mismo"""
        strip = False

        try:
            if not self.isfilebinary:
                content = self.content.rstrip()
                self.write_content(content)
                strip = True

        except:
            pass

        return strip        

    def replace_line(self, nline, cline):
        """Permite remplazar el contenido de una linea en el archivo"""

        replace = False
        nline = nline if isinstance(nline,int) else None

        try:
            if not self.isfilebinary and nline:
                lines = self.content_lines
                lines[nline] = cline
                replace = self.write_content_lines(lines)

        except:
            pass
        
        return replace

    def serach_line_by_text(self,text,init = 0,result = 0):

        search = []
        text = text if isinstance(text,basestring) else None
        result = result if isinstance(result,int) and result >= 0 else 0
        init = init if isinstance(init,int) else 0

        try:

            if not self.isfilebinary and text:

                lines = self.content_lines[init:]
                for inx,val in enumerate(lines):
                    if val and find(val,text)>-1:
                        search.append(inx+init)

                search = search if result == 0 else search[:result]
                search = search[0] if result == 1 and len(search) else search

        finally:
            pass
        
        return search

    def append_lines_after_line(self,nline,clines=[]):
        """Permite agregar una o mas lines a un archivo despues de una posición de linea del archivo"""
        
        append = False
        clines = clines if isinstance(clines,list) else []
        nline = nline if isinstance(nline,int) else 0

        try:
            if not self.isfilebinary:
                lines = self.content_lines
                lines = lines[:nline+1]+clines+lines[nline+1:]
                append = self.write_content_lines(lines)

        except:
            pass
        
        return append

    def remove_line(self,nline):

        remove = False
        nline = nline if isinstance(nline,int) else None

        try:
            if not self.isfilebinary and nline:
                lines = self.content_lines
                lines = lines[:nline]+lines[nline+1:]
                remove = self.write_content_lines(lines)

        except:
            pass
        
        return remove

    def remove_lines_between(self,init,end = None):
        """Permite eliminar las lineas que estan entre la linea init y la linea end (no inclusive)"""
        remove = False
        init = init if isinstance(init,int) else None
        end = end if isinstance(end,int) else None

        try:
            if not self.isfilebinary and init:
                lines = self.content_lines
                if not end:
                    lines = lines[:init]
                elif init < end:
                    lines = lines[:init+1]+lines[end:]

                remove = self.write_content_lines(lines)

        except:
            pass
        
        return remove