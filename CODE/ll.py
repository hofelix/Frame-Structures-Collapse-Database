import bpy
import numpy as np

context = bpy.context
scene = context.scene
rbw = scene.rigidbody_world
pc = rbw.point_cache

ll = list(bpy.data.objects)
l_num = np.size(ll)
path = 'inform.txt'
f = open(path, 'w')

bpy.ops.ptcache.bake({"point_cache": pc}, bake=True)

scene.frame_set(1)

for i in range(l_num):
    name = str(bpy.data.objects[i].name)
    size = str(bpy.data.objects[i].dimensions)
    str_list = name + ' ' + size
    f.write(str_list +'\n')

print(size)
