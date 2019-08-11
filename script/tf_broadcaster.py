#!/usr/bin/env python  
import rospy
import tf

if __name__ == '__main__':
    rospy.init_node('tf_broadcaster')
    br = tf.TransformBroadcaster()
    while not rospy.is_shutdown():
        print("hello")
        br.sendTransform((10, 0, 0),tf.transformations.quaternion_from_euler(0, 0, 0),rospy.Time.now(),"base_link","odom")
        rospy.sleep(1)
