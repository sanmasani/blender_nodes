import bpy
from node_s import *
from util import *

class StringNode(Node, SverchCustomTreeNode):
    ''' String '''
    bl_idname = 'StringNode'
    bl_label = 'String'
    bl_icon = 'OUTLINER_OB_EMPTY'
    
    str_ = bpy.props.StringProperty(name = 'str_', description='input string', default="", options={'ANIMATABLE'}, update=updateNode)
    
    def init(self, context):
        self.outputs.new('StringsSocket', "Str", "Str")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "str_", text="String")

    def update(self):
        StrOut = self.str_
        # outputs
        if 'Str' in self.outputs and self.outputs['Str'].links:
            SvSetSocketAnyType(self, 'Str',[[StrOut]])
            
    def update_socket(self, context):
        self.update()


def register():
    bpy.utils.register_class(StringNode)
    
def unregister():
    bpy.utils.unregister_class(StringNode)

if __name__ == "__main__":
    register()
