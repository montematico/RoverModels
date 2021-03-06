// Generated by gencpp from file rover_msgs/ArmControlRequest.msg
// DO NOT EDIT!


#ifndef ROVER_MSGS_MESSAGE_ARMCONTROLREQUEST_H
#define ROVER_MSGS_MESSAGE_ARMCONTROLREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace rover_msgs
{
template <class ContainerAllocator>
struct ArmControlRequest_
{
  typedef ArmControlRequest_<ContainerAllocator> Type;

  ArmControlRequest_()
    : test()  {
    }
  ArmControlRequest_(const ContainerAllocator& _alloc)
    : test(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _test_type;
  _test_type test;





  typedef boost::shared_ptr< ::rover_msgs::ArmControlRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::rover_msgs::ArmControlRequest_<ContainerAllocator> const> ConstPtr;

}; // struct ArmControlRequest_

typedef ::rover_msgs::ArmControlRequest_<std::allocator<void> > ArmControlRequest;

typedef boost::shared_ptr< ::rover_msgs::ArmControlRequest > ArmControlRequestPtr;
typedef boost::shared_ptr< ::rover_msgs::ArmControlRequest const> ArmControlRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::rover_msgs::ArmControlRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::rover_msgs::ArmControlRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::rover_msgs::ArmControlRequest_<ContainerAllocator1> & lhs, const ::rover_msgs::ArmControlRequest_<ContainerAllocator2> & rhs)
{
  return lhs.test == rhs.test;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::rover_msgs::ArmControlRequest_<ContainerAllocator1> & lhs, const ::rover_msgs::ArmControlRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace rover_msgs

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::rover_msgs::ArmControlRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::rover_msgs::ArmControlRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rover_msgs::ArmControlRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::rover_msgs::ArmControlRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rover_msgs::ArmControlRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::rover_msgs::ArmControlRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::rover_msgs::ArmControlRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "8d4693bd9512b94755470aae7830e048";
  }

  static const char* value(const ::rover_msgs::ArmControlRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x8d4693bd9512b947ULL;
  static const uint64_t static_value2 = 0x55470aae7830e048ULL;
};

template<class ContainerAllocator>
struct DataType< ::rover_msgs::ArmControlRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "rover_msgs/ArmControlRequest";
  }

  static const char* value(const ::rover_msgs::ArmControlRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::rover_msgs::ArmControlRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string test\n"
;
  }

  static const char* value(const ::rover_msgs::ArmControlRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::rover_msgs::ArmControlRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.test);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct ArmControlRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::rover_msgs::ArmControlRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::rover_msgs::ArmControlRequest_<ContainerAllocator>& v)
  {
    s << indent << "test: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.test);
  }
};

} // namespace message_operations
} // namespace ros

#endif // ROVER_MSGS_MESSAGE_ARMCONTROLREQUEST_H
