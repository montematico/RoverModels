;; Auto-generated. Do not edit!


(when (boundp 'rover-control::JointState)
  (if (not (find-package "ROVER-CONTROL"))
    (make-package "ROVER-CONTROL"))
  (shadow 'JointState (find-package "ROVER-CONTROL")))
(unless (find-package "ROVER-CONTROL::JOINTSTATE")
  (make-package "ROVER-CONTROL::JOINTSTATE"))

(in-package "ROS")
;;//! \htmlinclude JointState.msg.html


(defclass rover-control::JointState
  :super ros::object
  :slots (_name _idx _torque ))

(defmethod rover-control::JointState
  (:init
   (&key
    ((:name __name) "")
    ((:idx __idx) 0)
    ((:torque __torque) 0.0)
    )
   (send-super :init)
   (setq _name (string __name))
   (setq _idx (round __idx))
   (setq _torque (float __torque))
   self)
  (:name
   (&optional __name)
   (if __name (setq _name __name)) _name)
  (:idx
   (&optional __idx)
   (if __idx (setq _idx __idx)) _idx)
  (:torque
   (&optional __torque)
   (if __torque (setq _torque __torque)) _torque)
  (:serialization-length
   ()
   (+
    ;; string _name
    4 (length _name)
    ;; int8 _idx
    1
    ;; float32 _torque
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _name
       (write-long (length _name) s) (princ _name s)
     ;; int8 _idx
       (write-byte _idx s)
     ;; float32 _torque
       (sys::poke _torque (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _name
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _name (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; int8 _idx
     (setq _idx (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _idx 127) (setq _idx (- _idx 256)))
   ;; float32 _torque
     (setq _torque (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get rover-control::JointState :md5sum-) "abc73a675a2cc1c1895a87001a3b1393")
(setf (get rover-control::JointState :datatype-) "rover-control/JointState")
(setf (get rover-control::JointState :definition-)
      "string name
int8 idx
float32 torque

")



(provide :rover-control/JointState "abc73a675a2cc1c1895a87001a3b1393")


