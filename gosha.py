import pioneer_sdk
from pioneer_sdk import Pioneer
import cv2
import math
import numpy as np


angle = float(0) # переменная отвечающая за текущий угол окружности
number_of_points = 24 # количество точек составляющих окружность
increment = float(360 / number_of_points) #расчёт приращения в градусах
radius = 0.6 #указываем радиус окружности в метрах
flight_height = float(1) #указываем высоту полёта в метраx
last_point_reached = False #флаг на достижение последней точки

command_x = radius * math.cos(math.radians(angle)) #координаты по оси X
command_y = radius * math.sin(math.radians(angle)) #Координаты по оси Y
command_yaw = math.radians(angle) #рысканье квадрокоптера

new_point = True #флаг на получение новой точки;
p_r = False #флаг срабатывающий на достижение точки.

if __name__ == '__main__':
    print('start')
    pioneer_mini = Pioneer()
    pioneer_mini.arm()
    pioneer_mini.takeoff()
    while True:
        if new_point:
            pioneer_mini.go_to_local_point(x=command_x, y=command_y, z=flight_height, yaw=command_yaw)
            new_point = False
        if p_r:
            if angle == 360:
                last_point_reached = True
            else:
                angle += increment
                command_x = radius * math.cos(math.radians(angle))
                command_y = radius * math.sin(math.radians(angle))
                command_yaw += math.radians(increment)
                new_point = True
            p_r = False
        key = cv2.waitKey(1) & 0xFF
        #if key == 27:  # esc
        pioneer_mini.land()
        exit(0)