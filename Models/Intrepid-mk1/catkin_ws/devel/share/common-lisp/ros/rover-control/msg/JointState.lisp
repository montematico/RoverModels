; Auto-generated. Do not edit!


(cl:in-package rover-control-msg)


;//! \htmlinclude JointState.msg.html

(cl:defclass <JointState> (roslisp-msg-protocol:ros-message)
  ((name
    :reader name
    :initarg :name
    :type cl:string
    :initform "")
   (idx
    :reader idx
    :initarg :idx
    :type cl:fixnum
    :initform 0)
   (torque
    :reader torque
    :initarg :torque
    :type cl:float
    :initform 0.0))
)

(cl:defclass JointState (<JointState>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <JointState>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'JointState)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rover-control-msg:<JointState> is deprecated: use rover-control-msg:JointState instead.")))

(cl:ensure-generic-function 'name-val :lambda-list '(m))
(cl:defmethod name-val ((m <JointState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rover-control-msg:name-val is deprecated.  Use rover-control-msg:name instead.")
  (name m))

(cl:ensure-generic-function 'idx-val :lambda-list '(m))
(cl:defmethod idx-val ((m <JointState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rover-control-msg:idx-val is deprecated.  Use rover-control-msg:idx instead.")
  (idx m))

(cl:ensure-generic-function 'torque-val :lambda-list '(m))
(cl:defmethod torque-val ((m <JointState>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rover-control-msg:torque-val is deprecated.  Use rover-control-msg:torque instead.")
  (torque m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <JointState>) ostream)
  "Serializes a message object of type '<JointState>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'name))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'name))
  (cl:let* ((signed (cl:slot-value msg 'idx)) (unsigned (cl:if (cl:< signed 0) (cl:+ signed 256) signed)))
    (cl:write-byte (cl:ldb (cl:byte 8 0) unsigned) ostream)
    )
  (cl:let ((bits (roslisp-utils:encode-single-float-bits (cl:slot-value msg 'torque))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <JointState>) istream)
  "Deserializes a message object of type '<JointState>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'name) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'name) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
    (cl:let ((unsigned 0))
      (cl:setf (cl:ldb (cl:byte 8 0) unsigned) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'idx) (cl:if (cl:< unsigned 128) unsigned (cl:- unsigned 256))))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'torque) (roslisp-utils:decode-single-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<JointState>)))
  "Returns string type for a message object of type '<JointState>"
  "rover-control/JointState")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'JointState)))
  "Returns string type for a message object of type 'JointState"
  "rover-control/JointState")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<JointState>)))
  "Returns md5sum for a message object of type '<JointState>"
  "abc73a675a2cc1c1895a87001a3b1393")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'JointState)))
  "Returns md5sum for a message object of type 'JointState"
  "abc73a675a2cc1c1895a87001a3b1393")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<JointState>)))
  "Returns full string definition for message of type '<JointState>"
  (cl:format cl:nil "string name~%int8 idx~%float32 torque~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'JointState)))
  "Returns full string definition for message of type 'JointState"
  (cl:format cl:nil "string name~%int8 idx~%float32 torque~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <JointState>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'name))
     1
     4
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <JointState>))
  "Converts a ROS message object to a list"
  (cl:list 'JointState
    (cl:cons ':name (name msg))
    (cl:cons ':idx (idx msg))
    (cl:cons ':torque (torque msg))
))
