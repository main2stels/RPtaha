import cv2
from picamera2 import Picamera2
from libcamera import Transform
from dronekit import connect, VehicleMode




vehicle = connect('/dev/ttyAMA0', wait_ready=True, baud=115200)

picam2 = Picamera2()
video_config = picam2.create_video_configuration({"size": (1024, 768), 
                                                  "format": "RGB888"}, 
                                                  transform = Transform(vflip = 1, hflip=1))
picam2.configure(video_config)
picam2.start()

marker_size = 2
try:
    while True:
        image = picam2.capture_array()
        center_x, center_y = image.shape[1] // 2, image.shape[0] // 2

        pitch = vehicle.attitude.pitch
        roll = vehicle.attitude.roll
        yaw = vehicle.attitude.yaw
        velocity_x = vehicle.velocity[0]
        velocity_y = vehicle.velocity[1]
        velocity_z = vehicle.velocity[2]
        altitude = vehicle.location.global_relative_frame.alt

        cv2.drawMarker(image, 
                       (center_x, center_y), 
                       (0, 0, 255), 
                       cv2.MARKER_CROSS, 
                       marker_size)

        cv2.imshow("Image_camera", image)
        cv2.waitKey(1)
        

except KeyboardInterrupt:
    vehicle.close()
    cv2.destroyAllWindows()
    print('Exit capture')
