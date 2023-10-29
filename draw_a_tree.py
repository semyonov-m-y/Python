import simple_draw as sd
 
 
sd.resolution = (1200, 900)
 
def branch(point, angle, length, delta=30, width=3):
    if length < 7:
        return
    vector = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    vector.draw()
    point_2 = vector.end_point
    angle_2 = angle - delta
    length_2 = length * .7
    branch(point=point_2, angle=angle_2, length=length_2, delta=delta)
 
 
point_0 = sd.get_point(600, 5)
 
branch(point=point_0, angle=90, length=200, delta=10)
branch(point=point_0, angle=90, length=200, delta=20)
branch(point=point_0, angle=90, length=200, delta=30)
branch(point=point_0, angle=90, length=200, delta=40)
branch(point=point_0, angle=90, length=200, delta=50)
 
sd.pause()



