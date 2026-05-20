import bpy
import numpy as np
import re
context = bpy.context
scene = context.scene
rbw = scene.rigidbody_world
pc = rbw.point_cache
path = 'inform250.csv'
f = open(path, 'w')
# match bake to animation
print(pc.frame_start, pc.frame_end)

bpy.ops.ptcache.bake({"point_cache": pc}, bake=True)

scene.frame_set(250)

for ob in scene.objects:
    name = str(ob.name)
    x = str(ob.matrix_world.translation[0])
    y = str(ob.matrix_world.translation[1])
    z = str(ob.matrix_world.translation[2])
    degreex = str(ob.matrix_world.to_euler()[0])
    degreey = str(ob.matrix_world.to_euler()[1])
    degreez = str(ob.matrix_world.to_euler()[2])
    str_list = name + ',' + x + ','  + y + ',' + z + ',' + degreex+ ',' + degreey+ ',' + degreez
    f.write(str_list +'\n')

print('finish')


lineList = []
matchPattern = re.compile(r'Foundation')
matchPattern1 = re.compile(r'Con')
matchPattern2 = re.compile(r'Ground')
file = open('inform250.csv','r',encoding='UTF-8')

while 1:
    line = file.readline()
    if not line:
        print("Read file End or Error")
        break
    elif matchPattern.search(line):
        pass
    elif matchPattern1.search(line):
        pass
    elif matchPattern2.search(line):
        pass
    else:
        lineList.append(line)
file.close()
file = open(r'inform250.csv', 'w',encoding='UTF-8')

for i in lineList:
    file.write(i)
file.close()
