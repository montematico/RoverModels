;; Auto-generated. Do not edit!


(when (boundp 'rover_msgs::ArmControl)
  (if (not (find-package "ROVER_MSGS"))
    (make-package "ROVER_MSGS"))
  (shadow 'ArmControl (find-package "ROVER_MSGS")))
(unless (find-package "ROVER_MSGS::ARMCONTROL")
  (make-package "ROVER_MSGS::ARMCONTROL"))
(unless (find-package "ROVER_MSGS::ARMCONTROLREQUEST")
  (make-package "ROVER_MSGS::ARMCONTROLREQUEST"))
(unless (find-package "ROVER_MSGS::ARMCONTROLRESPONSE")
  (make-package "ROVER_MSGS::ARMCONTROLRESPONSE"))

(in-package "ROS")





(defclass rover_msgs::ArmControlRequest
  :super ros::object
  :slots (_test ))

(defmethod rover_msgs::ArmControlRequest
  (:init
   (&key
    ((:test __test) "")
    )
   (send-super :init)
   (setq _test (string __test))
   self)
  (:test
   (&optional __test)
   (if __test (setq _test __test)) _test)
  (:serialization-length
   ()
   (+
    ;; string _test
    4 (length _test)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _test
       (write-long (length _test) s) (princ _test s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _test
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _test (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass rover_msgs::ArmControlResponse
  :super ros::object
  :slots (_test1 ))

(defmethod rover_msgs::ArmControlResponse
  (:init
   (&key
    ((:test1 __test1) nil)
    )
   (send-super :init)
   (setq _test1 __test1)
   self)
  (:test1
   (&optional __test1)
   (if __test1 (setq _test1 __test1)) _test1)
  (:serialization-length
   ()
   (+
    ;; bool _test1
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; bool _test1
       (if _test1 (write-byte -1 s) (write-byte 0 s))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; bool _test1
     (setq _test1 (not (= 0 (sys::peek buf ptr- :char)))) (incf ptr- 1)
   ;;
   self)
  )

(defclass rover_msgs::ArmControl
  :super ros::object
  :slots ())

(setf (get rover_msgs::ArmControl :md5sum-) "438c11d562dc9fa31889c10ff3e39023")
(setf (get rover_msgs::ArmControl :datatype-) "rover_msgs/ArmControl")
(setf (get rover_msgs::ArmControl :request) rover_msgs::ArmControlRequest)
(setf (get rover_msgs::ArmControl :response) rover_msgs::ArmControlResponse)

(defmethod rover_msgs::ArmControlRequest
  (:response () (instance rover_msgs::ArmControlResponse :init)))

(setf (get rover_msgs::ArmControlRequest :md5sum-) "438c11d562dc9fa31889c10ff3e39023")
(setf (get rover_msgs::ArmControlRequest :datatype-) "rover_msgs/ArmControlRequest")
(setf (get rover_msgs::ArmControlRequest :definition-)
      "string test
---
bool test1
")

(setf (get rover_msgs::ArmControlResponse :md5sum-) "438c11d562dc9fa31889c10ff3e39023")
(setf (get rover_msgs::ArmControlResponse :datatype-) "rover_msgs/ArmControlResponse")
(setf (get rover_msgs::ArmControlResponse :definition-)
      "string test
---
bool test1
")



(provide :rover_msgs/ArmControl "438c11d562dc9fa31889c10ff3e39023")


