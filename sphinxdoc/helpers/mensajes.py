# -*- coding: utf-8 -*-
from inspect import stack
from sphinxdoc import importar_config
from terminal_text_color import TextColor,AlertTextColor

class Mensajes(object):
    def __init__(self):
        mensajes = importar_config('mensajes')
        self.__ui__ = mensajes["ui"]
        self.__error__ = mensajes["error"]

    def __compilar__(self,id_mensaje,*args):
        return self.__ui__[id_mensaje].format(*args) if id_mensaje in self.__ui__ else None

class Alerta(Mensajes):
    """docstring for Alerta"""
    def __init__(self):
        super(self.__class__, self).__init__()
        self.atc = AlertTextColor()

    def __alert__(self,mensaje,**kwargs):
        getattr(self.atc, stack()[1][3])(mensaje,**kwargs)

    def info(self,id_mensaje,*args,**kwargs):
        self.__alert__(self.__compilar__(id_mensaje),**kwargs)

    def success(self,id_mensaje,*args,**kwargs):
        self.__alert__(self.__compilar__(id_mensaje),**kwargs)

    def error(self,id_mensaje,*args,**kwargs):
        self.__alert__(self.__compilar__(id_mensaje),**kwargs)

    def warning(self,id_mensaje,*args,**kwargs):
        self.__alert__(self.__compilar__(id_mensaje),**kwargs)

    def info_alt(self,id_mensaje,*args,**kwargs):
        self.__alert__(self.__compilar__(id_mensaje),**kwargs)

class InterfazUsuario(Mensajes):
    def __init__(self):    
        super(self.__class__, self).__init__()
        self.tc = TextColor()

    def mensaje(self,id_mensaje,*args):

        return self.__compilar__(id_mensaje,args)


