import time

import pymavlink.dialects.v20.all
from pymavlink import mavutil
from pymavlink import mavexpression
import math
import datetime

print("start")
connection = mavutil.mavlink_connection('/dev/serial0', baud=115200)


connection.wait_heartbeat()
print("hb receive")
print(connection.mav)

frequency_hz = 30
connection.mav.command_long_send(connection.target_system,
                                 connection.target_component,
                                 mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,
                                 0,
                                 pymavlink.dialects.v20.all.MAVLINK_MSG_ID_ATTITUDE,
                                 1e6 / frequency_hz,
                                 0, 0, 0, 0, 0)

connection.mav.command_long_send(connection.target_system,
                                 connection.target_component,
                                 mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,
                                 0,
                                 pymavlink.dialects.v20.all.MAVLINK_MSG_ID_GLOBAL_POSITION_INT,
                                 1e6 / frequency_hz,
                                 0, 0, 0, 0, 0)

# perv_distance = 0.22
# perv_time = 0

print("while")

while True:
    msg = connection.recv_msg()


    if msg is None:
        continue

    msg_type = msg.get_type()
    if msg_type == 'ATTITUDE':
        now = datetime.datetime.now()
        print(msg.roll)
        print(now)
    elif msg_type == 'GLOBAL_POSITION_INT':
        now = datetime.datetime.now()
        print('VX = ', msg.vx/100)
        print(now)

    #print(msg.get_type())


    # msg_GPS = connection.recv_match(type = ['GLOBAL_POSITION_INT'], blocking=True)
    
    # #msg = connection.recv_match(type = 'LOCAL_POSITION', blocking=False)
    # print(msg_GPS)

    # if msg_GPS.get_type() == 'GLOBAL_POSITION_INT':
    #     # ground_speed = msg.groundspeed
    #     print(msg_GPS)
    #     print('VX = ', msg_GPS.vx/100)
    #     print('VY = ', msg_GPS.vy/100)
    #     print('VZ = ', msg_GPS.vz/100)
    # if msg.get_type() == 'CONTROL_STATUS':
    #     print(msg.roll)
    #     print(msg.yaw)

    
    # msg = connection.recv_match(type = 'LOCAL_POSITION_NED', blocking=True)

    # if msg is not None:
    #     #ground_speed = msg.groundspeed
    #     print("VX = ", msg.vx)
    #     print("VY = ", msg.vy)
    #     print("VZ = ", msg.vz)

    # msg = connection.recv_match(type = 'ATTITUDE', blocking=True)
    # if msg is not None:
    #     print("roll = ", math.degrees(msg.roll))
    #     print("pitch = ", math.degrees(msg.pitch))
    #     print("yaw = ", math.degrees(msg.yaw))

    # msg_flow = connection.recv_match(type = 'OPTICAL_FLOW_RAD', blocking=True)
    # if msg_flow is not None:
    #    optical_flow_x = msg_flow.integration_time_us * msg_flow.pixel_flow_x_integral / 1e6
    #    optical_flow_y = msg_flow.integration_time_us * msg_flow.pixel_flow_y_integral / 1e6
    #    print(optical_flow_x)
    #    print(optical_flow_y)

    #msg_flow = connection.recv_match(type = 'OPTICAL_FLOW', blocking=False)
    #if msg_flow is not None:
       #print(msg_flow)
       
       #print('VX = ', msg_flow.flow_comp_m_x)
       #print('VY = ', msg_flow.flow_comp_m_y)


    # msg_distance = connection.recv_match(type = 'DISTANCE_SENSOR', blocking=False)
    # if msg_distance is not None:
    #     distance = msg_distance.current_distance/100
    #     current_time = msg_distance.time_boot_ms/1000
    #     vertical_velocity = (distance - perv_distance) / (current_time - perv_time)

    #     perv_distance = distance
    #     perv_time = current_time
    #     print('VZ = ', vertical_velocity)
        #print(current_time)

    
    
    # msg = connection.recv_msg()
    
    # if msg.get_type() == 'VFR_HUD':
    #     print('Горизонтальная скорость = ', msg.groundspeed)

    # elif msg.get_type() == 'GLOBAL_POSITION_INT':
    #     print('Вертикальная скорость = ', msg.vz)
    # msg = connection.recv_match(type="LOCAL_POSITION_NED", blocking=True)
    # if msg is not None:
    #     print("VX = ", msg.vx)
    #     print("VY = ", msg.vy)
    #     print("VZ = ", msg.vz)

    #msg = connection.recv_match(type="GLOBAL_POSITION_INT", blocking=True, timeout=1.0)

    # print(msg)

    # if msg:
    #     # groundspeed = msg.groundspeed
    #     # airspeed = msg.airspeed

    #     vx = msg.vx
    #     vy = msg.vy
    #     vz = msg.vz
        
        

    #     print("X", vx/100)
    #     print("Y", vy/100)
    #     print("Z", vz/100)

    #time.sleep(0.1)