#!/usr/bin/env python

import rospy
import numpy as np



class Car_Detector():
  """  
  Currently it just broadcasts an identity transform from 'map' to
  'odom' and uses the gazebo pose to transform 'base_footprint' to 'odom'
  """
  def __init__(self):
    rospy.init_node('Car_detector')
    # Broadcast at 60 HZ
    rate = rospy.Rate(60.0)
    rospy.loginfo('node successfully started')
    while not rospy.is_shutdown():
      print("ciao")
      rate.sleep()
  
  def odom_cb(self, msg):
    self.odom_msg = msg


if __name__ == '__main__':
  try:
    det = Car_Detector()
  except rospy.ROSInterruptException:
    pass
