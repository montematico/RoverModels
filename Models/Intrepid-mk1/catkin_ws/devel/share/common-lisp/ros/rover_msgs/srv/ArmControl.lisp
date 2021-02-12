; Auto-generated. Do not edit!


(cl:in-package rover_msgs-srv)


;//! \htmlinclude ArmControl-request.msg.html

(cl:defclass <ArmControl-request> (roslisp-msg-protocol:ros-message)
  ((test
    :reader test
    :initarg :test
    :type cl:string
    :initform ""))
)

(cl:defclass ArmControl-request (<ArmControl-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ArmControl-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ArmControl-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rover_msgs-srv:<ArmControl-request> is deprecated: use rover_msgs-srv:ArmControl-request instead.")))

(cl:ensure-generic-function 'test-val :lambda-list '(m))
(cl:defmethod test-val ((m <ArmControl-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rover_msgs-srv:test-val is deprecated.  Use rover_msgs-srv:test instead.")
  (test m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ArmControl-request>) ostream)
  "Serializes a message object of type '<ArmControl-request>"
  (cl:let ((__ros_str_len (cl:length (cl:slot-value msg 'test))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) __ros_str_len) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) __ros_str_len) ostream))
  (cl:map cl:nil #'(cl:lambda (c) (cl:write-byte (cl:char-code c) ostream)) (cl:slot-value msg 'test))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ArmControl-request>) istream)
  "Deserializes a message object of type '<ArmControl-request>"
    (cl:let ((__ros_str_len 0))
      (cl:setf (cl:ldb (cl:byte 8 0) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) __ros_str_len) (cl:read-byte istream))
      (cl:setf (cl:slot-value msg 'test) (cl:make-string __ros_str_len))
      (cl:dotimes (__ros_str_idx __ros_str_len msg)
        (cl:setf (cl:char (cl:slot-value msg 'test) __ros_str_idx) (cl:code-char (cl:read-byte istream)))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ArmControl-request>)))
  "Returns string type for a service object of type '<ArmControl-request>"
  "rover_msgs/ArmControlRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ArmControl-request)))
  "Returns string type for a service object of type 'ArmControl-request"
  "rover_msgs/ArmControlRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ArmControl-request>)))
  "Returns md5sum for a message object of type '<ArmControl-request>"
  "438c11d562dc9fa31889c10ff3e39023")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ArmControl-request)))
  "Returns md5sum for a message object of type 'ArmControl-request"
  "438c11d562dc9fa31889c10ff3e39023")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ArmControl-request>)))
  "Returns full string definition for message of type '<ArmControl-request>"
  (cl:format cl:nil "string test~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ArmControl-request)))
  "Returns full string definition for message of type 'ArmControl-request"
  (cl:format cl:nil "string test~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ArmControl-request>))
  (cl:+ 0
     4 (cl:length (cl:slot-value msg 'test))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ArmControl-request>))
  "Converts a ROS message object to a list"
  (cl:list 'ArmControl-request
    (cl:cons ':test (test msg))
))
;//! \htmlinclude ArmControl-response.msg.html

(cl:defclass <ArmControl-response> (roslisp-msg-protocol:ros-message)
  ((test1
    :reader test1
    :initarg :test1
    :type cl:boolean
    :initform cl:nil))
)

(cl:defclass ArmControl-response (<ArmControl-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <ArmControl-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'ArmControl-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name rover_msgs-srv:<ArmControl-response> is deprecated: use rover_msgs-srv:ArmControl-response instead.")))

(cl:ensure-generic-function 'test1-val :lambda-list '(m))
(cl:defmethod test1-val ((m <ArmControl-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader rover_msgs-srv:test1-val is deprecated.  Use rover_msgs-srv:test1 instead.")
  (test1 m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <ArmControl-response>) ostream)
  "Serializes a message object of type '<ArmControl-response>"
  (cl:write-byte (cl:ldb (cl:byte 8 0) (cl:if (cl:slot-value msg 'test1) 1 0)) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <ArmControl-response>) istream)
  "Deserializes a message object of type '<ArmControl-response>"
    (cl:setf (cl:slot-value msg 'test1) (cl:not (cl:zerop (cl:read-byte istream))))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<ArmControl-response>)))
  "Returns string type for a service object of type '<ArmControl-response>"
  "rover_msgs/ArmControlResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ArmControl-response)))
  "Returns string type for a service object of type 'ArmControl-response"
  "rover_msgs/ArmControlResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<ArmControl-response>)))
  "Returns md5sum for a message object of type '<ArmControl-response>"
  "438c11d562dc9fa31889c10ff3e39023")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'ArmControl-response)))
  "Returns md5sum for a message object of type 'ArmControl-response"
  "438c11d562dc9fa31889c10ff3e39023")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<ArmControl-response>)))
  "Returns full string definition for message of type '<ArmControl-response>"
  (cl:format cl:nil "bool test1~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'ArmControl-response)))
  "Returns full string definition for message of type 'ArmControl-response"
  (cl:format cl:nil "bool test1~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <ArmControl-response>))
  (cl:+ 0
     1
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <ArmControl-response>))
  "Converts a ROS message object to a list"
  (cl:list 'ArmControl-response
    (cl:cons ':test1 (test1 msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'ArmControl)))
  'ArmControl-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'ArmControl)))
  'ArmControl-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'ArmControl)))
  "Returns string type for a service object of type '<ArmControl>"
  "rover_msgs/ArmControl")