
(cl:in-package :asdf)

(defsystem "rover_msgs-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "ArmControl" :depends-on ("_package_ArmControl"))
    (:file "_package_ArmControl" :depends-on ("_package"))
  ))