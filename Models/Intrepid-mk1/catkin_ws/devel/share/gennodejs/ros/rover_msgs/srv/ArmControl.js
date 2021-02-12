// Auto-generated. Do not edit!

// (in-package rover_msgs.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class ArmControlRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.test = null;
    }
    else {
      if (initObj.hasOwnProperty('test')) {
        this.test = initObj.test
      }
      else {
        this.test = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ArmControlRequest
    // Serialize message field [test]
    bufferOffset = _serializer.string(obj.test, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ArmControlRequest
    let len;
    let data = new ArmControlRequest(null);
    // Deserialize message field [test]
    data.test = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.test.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'rover_msgs/ArmControlRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '8d4693bd9512b94755470aae7830e048';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string test
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ArmControlRequest(null);
    if (msg.test !== undefined) {
      resolved.test = msg.test;
    }
    else {
      resolved.test = ''
    }

    return resolved;
    }
};

class ArmControlResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.test1 = null;
    }
    else {
      if (initObj.hasOwnProperty('test1')) {
        this.test1 = initObj.test1
      }
      else {
        this.test1 = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type ArmControlResponse
    // Serialize message field [test1]
    bufferOffset = _serializer.bool(obj.test1, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type ArmControlResponse
    let len;
    let data = new ArmControlResponse(null);
    // Deserialize message field [test1]
    data.test1 = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'rover_msgs/ArmControlResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '409c04b93fd34a3758e2f0f86aa57c1a';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool test1
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new ArmControlResponse(null);
    if (msg.test1 !== undefined) {
      resolved.test1 = msg.test1;
    }
    else {
      resolved.test1 = false
    }

    return resolved;
    }
};

module.exports = {
  Request: ArmControlRequest,
  Response: ArmControlResponse,
  md5sum() { return '438c11d562dc9fa31889c10ff3e39023'; },
  datatype() { return 'rover_msgs/ArmControl'; }
};
