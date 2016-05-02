from . meshvertexintproperty import MeshVertexIntProperty
from . struct import Struct
from . bpy_struct import bpy_struct
import mathutils

class MeshVertexIntPropertyLayer(bpy_struct):
    @property
    def rna_type(self):
        '''(Struct) RNA type definition'''
        return Struct()
    @property
    def name(self):
        '''(String)'''
        return str()
    @property
    def data(self):
        '''(Sequence of MeshVertexIntProperty)'''
        return (MeshVertexIntProperty(),)