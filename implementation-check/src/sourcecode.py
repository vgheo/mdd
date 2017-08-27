'''

Software source code model

Inspired from UML

Serialized to XML using dexml


NOTE: It looks like we end up at EMF...
- esp the reference implementation


references:
https://stackoverflow.com/questions/8534256/find-first-element-in-a-sequence-that-matches-a-predicate

Created on Aug 26, 2017
@author: vlad
'''

import dexml
from dexml import fields
from itertools import ifilter


class Element(dexml.Model):
    """
    Model Element
    
    Uniquely identified in the scope of the containing model by id.
    """
    id=fields.String()

    def __init__(self, identifier):
        self.id=identifier
    
    def find(self, ident):
        return self if self.id==ident else None
    
class ElementRef(dexml.Model):
    """
        Reference to an element
        Reference is by id unique in the model
    """
    tagname="ref"
    targetId=fields.String()
    
    def __init__(self, targetId):
        self.targetId=targetId
    
    def get(self, model):
        """
        Resolve the reference in the scope of the given model
        """
        return model.find(self.targetId)

class CompositeElement(Element):
    children=fields.Dict(Element, key="id")

    def add(self,e):
        self.children[e.id]=e

    def find(self, ident):
        e = super(CompositeElement,self).find(ident)
        if e!=None:
            return e
        else:
            cond=lambda e: e!=None
            return next(
                ifilter(cond, [c.find(ident) for c in self.children.values()]), 
                None)

class NamedElement(CompositeElement):
    name=fields.String(default="")
    
    def __init__(self, ident, name):
        super(NamedElement,self).__init__(ident)
        self.name=name
    
class Model(NamedElement):
    """
    A model for source code
    It contains model elements
    """
    tagname="model"
    
    def __init__(self,ident=None,name=None):
        super(Model,self).__init__(ident, name)



class Module(NamedElement):
    """
    A source code module
    """
    def __init__(self,ident,name):
        super(Module,self).__init__(ident,name)

class Relationship(Element):
    source=fields.Model(ElementRef)
    target=fields.Model(ElementRef)

    def __init__(self,i,s,t):
        super(Relationship,self).__init__(i)
        self.source=s
        self.target=t
        
class Uses(Relationship):
    """
    Uses relationship
    """
    def __init__(self,i,srcId,trgId):
        super(Uses,self).__init__(i,ElementRef(srcId),ElementRef(trgId))



