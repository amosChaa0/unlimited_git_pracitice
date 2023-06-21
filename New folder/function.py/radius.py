pi=3.14
def area_circle(radius):
    area=pi*radius**2
    return area


all_area_of_circle=[]
list_radius=[7.5,8.97,20.39,100,12.9,13.9,600,1000,5.6,8.9,12.7,11.12,12.13]
for radius in list_radius:
    area=area_circle(radius)
    all_area_of_circle.append(area)
print(all_area_of_circle)