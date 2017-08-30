'''
Created on 29 aug. 2017

@author: vgheo

Design model

'''
import dexml
from dexml import fields

class Element(dexml.Model):
    """ """
    
class NamedElement(dexml.Model):
    name=fields.String()
    
class use(Element):
    ref=fields.String()
    def __init__(self, ref=None):
        self.ref=ref

class module(NamedElement):
    type=fields.String()
    uses=fields.List(use)
    
class model(dexml.Model):
    modules=fields.List(module)
