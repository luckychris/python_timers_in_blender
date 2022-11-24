import bpy
import random
import functools

counter = 0


def moveObject (object, step):
    
    object.location.y -= step
    
    a = random.uniform(0.1,1)
    
    if a < .2:
        return None
    
    return a
    

def timerFunc():
    
    global counter
    
    bpy.ops.mesh.primitive_monkey_add()
    
    bpy.context.object.color = (random.uniform(0,1), random.uniform(0,1), random.uniform(0,1), 1)

    bpy.context.active_object.location.x += (counter + 1) * 2
    
    
    bpy.app.timers.register(functools.partial(moveObject, bpy.context.object, random.uniform(.5,1.5)),first_interval = .2)

    counter += 1

    if counter <= 4:
        return 1

    return None

bpy.app.timers.register(timerFunc, first_interval = .5)
