bl_info = {
    "name": "Universal Exporter",
    "category": "Import & Export",
}

import bpy


class Export(bpy.types.Operator):
    """Export blender project"""
    bl_idname = "object.export_scene"
    bl_label = "Export Blender Scene"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        cursor = scene.cursor_location
        obj = scene.objects.active

        # Add stuff here
        
        # This script converts all objects to  .obj files
        for obj in bpy.data.objects:
          bpy.ops.object.select_name(name=obj.name)
          bpy.ops.export_scene.obj(filepath=file_path, # the filepath
                                check_existing=True, 
                                filter_glob="*.obj;*.mtl", 
                                use_selection=True, 
                                use_all_scenes=False, 
                                use_animation=False, 
                                use_modifiers=True, 
                                use_rotate_x90=True, 
                                use_edges=True, 
                                use_normals=False, 
                                use_hq_normals=True, 
                                use_uvs=True, 
                                use_materials=True, 
                                copy_images=False, 
                                use_triangles=False, 
                                use_vertex_groups=False, 
                                use_nurbs=False, 
                                use_blen_objects=True, 
                                group_by_object=False, 
                                group_by_material=False, 
                                keep_vertex_order=False
                                global_scale=1)

        return {'FINISHED'}

def register():
    bpy.utils.register_class(Export)


def unregister():
    bpy.utils.unregister_class(Export)


if __name__ == "__main__":
    register()
