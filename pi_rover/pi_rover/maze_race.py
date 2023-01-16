import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image, LaserScan
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
import cv2
import time
from time import sleep

class Lidar_Cam_Subscriber(Node):

    def __init__(self):
        super().__init__('qr_maze_node')
        #self.publisher = self.create_publisher(Twist, '/cmd_vel', 10)
        self.cam_sub = self.create_subscription(Image,'/udemy_bot_camera/image_raw',self.camera_cb,30)
        self.lidar_sub = self.create_subscription(LaserScan,'/scan',self.lidar_cb,30)
        self.bridge=CvBridge()
        self.frame=0
        #timer_period = 0.2;self.timer = self.create_timer(timer_period, self.send_cmd_vel)
        #self.linear_vel = 0.2 
        #self.velocity=Twist()
        
    def camera_cb(self, data):
        self.frame = self.bridge.imgmsg_to_cv2(data,'bgr8')
        cv2.imshow('Fpv from Udemy_rover',self.frame)
        cv2.waitKey(1)

    def lidar_cb(self, data):
        front_ray = min(data.ranges[179], 100)
        if (front_ray <= 1.700):
            self.qr_detector()
        else:
            print("Fahr Vorwärts",front_ray)
            
    def qr_detector(self):
        decoder = cv2.QRCodeDetector()
        data, points, _ = decoder.detectAndDecode(self.frame)
        print("QR Code Says = " , data )
        
   # def send_cmd_vel(self):
   #     if(data == 'left'):
   #         self.velocity.linear.x= 0.4 
   #         self.velocity.angular.z=0.57
   #     if(data == 'right'):
   #         self.velocity.linear.x= 0.4 
   #         self.velocity.angular.z=-0.57
   #     if(data == 'stop'):
   #         self.velocity.linear.x=0.0
   #         time.sleep(2)
   #         self.velocity.angular.z=3.14
   #         time.sleep(1)
   #         self.velocity.linear.x= 0.2 
   #         self.velocity.angular.z=0.0
   #     else:
   #         pass


def main(args=None):
    rclpy.init(args=args)

    lidar_cam_sub = Lidar_Cam_Subscriber()

    rclpy.spin(lidar_cam_sub)
    lidar_cam_sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()