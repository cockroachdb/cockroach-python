# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cockroach/proto/status.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import cockroach.proto.data_pb2
import cockroach.proto.config_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cockroach/proto/status.proto',
  package='cockroach.proto',
  serialized_pb=_b('\n\x1c\x63ockroach/proto/status.proto\x12\x0f\x63ockroach.proto\x1a\x1a\x63ockroach/proto/data.proto\x1a\x1c\x63ockroach/proto/config.proto\"\xb6\x01\n\x0bStoreStatus\x12.\n\x04\x64\x65sc\x18\x01 \x01(\x0b\x32 .cockroach.proto.StoreDescriptor\x12\x0f\n\x07node_id\x18\x02 \x01(\x05\x12\x13\n\x0brange_count\x18\x03 \x01(\x05\x12\x12\n\nstarted_at\x18\x04 \x01(\x03\x12\x12\n\nupdated_at\x18\x05 \x01(\x03\x12)\n\x05stats\x18\x06 \x01(\x0b\x32\x1a.cockroach.proto.MVCCStats\"\xb6\x01\n\nNodeStatus\x12-\n\x04\x64\x65sc\x18\x01 \x01(\x0b\x32\x1f.cockroach.proto.NodeDescriptor\x12\x11\n\tstore_ids\x18\x02 \x03(\x05\x12\x13\n\x0brange_count\x18\x03 \x01(\x05\x12\x12\n\nstarted_at\x18\x04 \x01(\x03\x12\x12\n\nupdated_at\x18\x05 \x01(\x03\x12)\n\x05stats\x18\x06 \x01(\x0b\x32\x1a.cockroach.proto.MVCCStatsB\x07Z\x05proto')
  ,
  dependencies=[cockroach.proto.data_pb2.DESCRIPTOR,cockroach.proto.config_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_STORESTATUS = _descriptor.Descriptor(
  name='StoreStatus',
  full_name='cockroach.proto.StoreStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='desc', full_name='cockroach.proto.StoreStatus.desc', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_id', full_name='cockroach.proto.StoreStatus.node_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='range_count', full_name='cockroach.proto.StoreStatus.range_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='started_at', full_name='cockroach.proto.StoreStatus.started_at', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='cockroach.proto.StoreStatus.updated_at', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stats', full_name='cockroach.proto.StoreStatus.stats', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=290,
)


_NODESTATUS = _descriptor.Descriptor(
  name='NodeStatus',
  full_name='cockroach.proto.NodeStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='desc', full_name='cockroach.proto.NodeStatus.desc', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='store_ids', full_name='cockroach.proto.NodeStatus.store_ids', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='range_count', full_name='cockroach.proto.NodeStatus.range_count', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='started_at', full_name='cockroach.proto.NodeStatus.started_at', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='updated_at', full_name='cockroach.proto.NodeStatus.updated_at', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stats', full_name='cockroach.proto.NodeStatus.stats', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=293,
  serialized_end=475,
)

_STORESTATUS.fields_by_name['desc'].message_type = cockroach.proto.config_pb2._STOREDESCRIPTOR
_STORESTATUS.fields_by_name['stats'].message_type = cockroach.proto.data_pb2._MVCCSTATS
_NODESTATUS.fields_by_name['desc'].message_type = cockroach.proto.config_pb2._NODEDESCRIPTOR
_NODESTATUS.fields_by_name['stats'].message_type = cockroach.proto.data_pb2._MVCCSTATS
DESCRIPTOR.message_types_by_name['StoreStatus'] = _STORESTATUS
DESCRIPTOR.message_types_by_name['NodeStatus'] = _NODESTATUS

StoreStatus = _reflection.GeneratedProtocolMessageType('StoreStatus', (_message.Message,), dict(
  DESCRIPTOR = _STORESTATUS,
  __module__ = 'cockroach.proto.status_pb2'
  # @@protoc_insertion_point(class_scope:cockroach.proto.StoreStatus)
  ))
_sym_db.RegisterMessage(StoreStatus)

NodeStatus = _reflection.GeneratedProtocolMessageType('NodeStatus', (_message.Message,), dict(
  DESCRIPTOR = _NODESTATUS,
  __module__ = 'cockroach.proto.status_pb2'
  # @@protoc_insertion_point(class_scope:cockroach.proto.NodeStatus)
  ))
_sym_db.RegisterMessage(NodeStatus)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\005proto'))
# @@protoc_insertion_point(module_scope)
