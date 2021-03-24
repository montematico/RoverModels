;; Auto-generated. Do not edit!


(when (boundp 'rover_msgs::JointState)
  (if (not (find-package "ROVER_MSGS"))
    (make-package "ROVER_MSGS"))
  (shadow 'JointState (find-package "ROVER_MSGS")))
(unless (find-package "ROVER_MSGS::JOINTSTATE")
  (make-package "ROVER_MSGS::JOINTSTATE"))

(in-package "ROS")
;;//! \htmlinclude JointState.msg.html


(defclass rover_msgs::JointState
  :super ros::object
  :slots (_name _parentName _idx _position _torque ))

(defmethod rover_msgs::JointState
  (:init
   (&key
    ((:name __name) "")
    ((:parentName __parentName) "")
    ((:idx __idx) 0)
    ((:position __position) 0.0)
    ((:torque __torque) 0.0)
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _parentName (string __parentName))
   (setq _idx (round __idx))
   (setq _position (float __position))
   (setq _torque (float __torque))
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:parentName
   (&optional __parentName)
   (if __parentName (setq _parentName __parentName)) _parentName)
  (:idx
   (&optional __idx)
   (if __idx (setq _idx __idx)) _idx)
  (:position
   (&optional __position)
   (if __position (setq _position __position)) _position)
  (:torque
   (&optional __torque)
   (if __torque (setq _torque __torque)) _torque)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; string _parentName
    4 (length _parentName)
    ;; int8 _idx
    1
    ;; float32 _position
    4
    ;; float32 _torque
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; string _parentName
       (write-long (length _parentName) s) (princ _parentName s)
     ;; int8 _idx
       (write-byte _idx s)
     ;; float32 _position
       (sys::poke _position (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _torque
       (sys::poke _torque (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _parentName
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _parentName (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int8 _idx
     (setq _idx (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _idx 127) (setq _idx (- _idx 256)))
   ;; float32 _position
     (setq _position (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _torque
     (setq _torque (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get rover_msgs::JointState :md5sum-) "e5052bf8979554b0657f495e0fbf5ca4")
(setf (get rover_msgs::JointState :datatype-) "rover_msgs/JointState")
(setf (get rover_msgs::JointState :definition-)
      "string name
string parentName
int8 idx
float32 position
float32 torque

")



(provide :rover_msgs/JointState "e5052bf8979554b0657f495e0fbf5ca4")


