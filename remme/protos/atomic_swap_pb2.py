# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: atomic_swap.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='atomic_swap.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x61tomic_swap.proto\"_\n\x10\x41tomicSwapMethod\"K\n\x06Method\x12\x08\n\x04INIT\x10\x00\x12\x0b\n\x07\x41PPROVE\x10\x01\x12\n\n\x06\x45XPIRE\x10\x02\x12\x13\n\x0fSET_SECRET_LOCK\x10\x03\x12\t\n\x05\x43LOSE\x10\x04\"\xd8\x01\n\x15\x41tomicSwapInitPayload\x12\x18\n\x10receiver_address\x18\x01 \x01(\t\x12 \n\x18sender_address_non_local\x18\x07 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x04\x12\x0f\n\x07swap_id\x18\x03 \x01(\t\x12 \n\x18secret_lock_by_solicitor\x18\x04 \x01(\t\x12,\n$email_address_encrypted_by_initiator\x18\x05 \x01(\t\x12\x12\n\ncreated_at\x18\x06 \x01(\r\"+\n\x18\x41tomicSwapApprovePayload\x12\x0f\n\x07swap_id\x18\x01 \x01(\t\"*\n\x17\x41tomicSwapExpirePayload\x12\x0f\n\x07swap_id\x18\x01 \x01(\t\"F\n\x1e\x41tomicSwapSetSecretLockPayload\x12\x0f\n\x07swap_id\x18\x01 \x01(\t\x12\x13\n\x0bsecret_lock\x18\x02 \x01(\t\"=\n\x16\x41tomicSwapClosePayload\x12\x0f\n\x07swap_id\x18\x01 \x01(\t\x12\x12\n\nsecret_key\x18\x02 \x01(\t\"\xaa\x02\n\x0e\x41tomicSwapInfo\x12\x11\n\tis_closed\x18\x01 \x01(\x08\x12\x13\n\x0bis_approved\x18\x0b \x01(\x08\x12\x16\n\x0esender_address\x18\x02 \x01(\t\x12 \n\x18sender_address_non_local\x18\x0c \x01(\t\x12\x18\n\x10receiver_address\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x04\x12(\n email_address_encrypted_optional\x18\x05 \x01(\t\x12\x0f\n\x07swap_id\x18\x06 \x01(\t\x12\x13\n\x0bsecret_lock\x18\x07 \x01(\t\x12\x12\n\nsecret_key\x18\x08 \x01(\t\x12\x12\n\ncreated_at\x18\t \x01(\r\x12\x14\n\x0cis_initiator\x18\n \x01(\x08\x62\x06proto3')
)



_ATOMICSWAPMETHOD_METHOD = _descriptor.EnumDescriptor(
  name='Method',
  full_name='AtomicSwapMethod.Method',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INIT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='APPROVE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXPIRE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SET_SECRET_LOCK', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLOSE', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=41,
  serialized_end=116,
)
_sym_db.RegisterEnumDescriptor(_ATOMICSWAPMETHOD_METHOD)


_ATOMICSWAPMETHOD = _descriptor.Descriptor(
  name='AtomicSwapMethod',
  full_name='AtomicSwapMethod',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ATOMICSWAPMETHOD_METHOD,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=21,
  serialized_end=116,
)


_ATOMICSWAPINITPAYLOAD = _descriptor.Descriptor(
  name='AtomicSwapInitPayload',
  full_name='AtomicSwapInitPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='receiver_address', full_name='AtomicSwapInitPayload.receiver_address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender_address_non_local', full_name='AtomicSwapInitPayload.sender_address_non_local', index=1,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='AtomicSwapInitPayload.amount', index=2,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='swap_id', full_name='AtomicSwapInitPayload.swap_id', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secret_lock_by_solicitor', full_name='AtomicSwapInitPayload.secret_lock_by_solicitor', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email_address_encrypted_by_initiator', full_name='AtomicSwapInitPayload.email_address_encrypted_by_initiator', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='AtomicSwapInitPayload.created_at', index=6,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=119,
  serialized_end=335,
)


_ATOMICSWAPAPPROVEPAYLOAD = _descriptor.Descriptor(
  name='AtomicSwapApprovePayload',
  full_name='AtomicSwapApprovePayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='swap_id', full_name='AtomicSwapApprovePayload.swap_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=337,
  serialized_end=380,
)


_ATOMICSWAPEXPIREPAYLOAD = _descriptor.Descriptor(
  name='AtomicSwapExpirePayload',
  full_name='AtomicSwapExpirePayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='swap_id', full_name='AtomicSwapExpirePayload.swap_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=382,
  serialized_end=424,
)


_ATOMICSWAPSETSECRETLOCKPAYLOAD = _descriptor.Descriptor(
  name='AtomicSwapSetSecretLockPayload',
  full_name='AtomicSwapSetSecretLockPayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='swap_id', full_name='AtomicSwapSetSecretLockPayload.swap_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secret_lock', full_name='AtomicSwapSetSecretLockPayload.secret_lock', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=426,
  serialized_end=496,
)


_ATOMICSWAPCLOSEPAYLOAD = _descriptor.Descriptor(
  name='AtomicSwapClosePayload',
  full_name='AtomicSwapClosePayload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='swap_id', full_name='AtomicSwapClosePayload.swap_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secret_key', full_name='AtomicSwapClosePayload.secret_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=498,
  serialized_end=559,
)


_ATOMICSWAPINFO = _descriptor.Descriptor(
  name='AtomicSwapInfo',
  full_name='AtomicSwapInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_closed', full_name='AtomicSwapInfo.is_closed', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_approved', full_name='AtomicSwapInfo.is_approved', index=1,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender_address', full_name='AtomicSwapInfo.sender_address', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sender_address_non_local', full_name='AtomicSwapInfo.sender_address_non_local', index=3,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receiver_address', full_name='AtomicSwapInfo.receiver_address', index=4,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='AtomicSwapInfo.amount', index=5,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email_address_encrypted_optional', full_name='AtomicSwapInfo.email_address_encrypted_optional', index=6,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='swap_id', full_name='AtomicSwapInfo.swap_id', index=7,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secret_lock', full_name='AtomicSwapInfo.secret_lock', index=8,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secret_key', full_name='AtomicSwapInfo.secret_key', index=9,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='created_at', full_name='AtomicSwapInfo.created_at', index=10,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_initiator', full_name='AtomicSwapInfo.is_initiator', index=11,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=562,
  serialized_end=860,
)

_ATOMICSWAPMETHOD_METHOD.containing_type = _ATOMICSWAPMETHOD
DESCRIPTOR.message_types_by_name['AtomicSwapMethod'] = _ATOMICSWAPMETHOD
DESCRIPTOR.message_types_by_name['AtomicSwapInitPayload'] = _ATOMICSWAPINITPAYLOAD
DESCRIPTOR.message_types_by_name['AtomicSwapApprovePayload'] = _ATOMICSWAPAPPROVEPAYLOAD
DESCRIPTOR.message_types_by_name['AtomicSwapExpirePayload'] = _ATOMICSWAPEXPIREPAYLOAD
DESCRIPTOR.message_types_by_name['AtomicSwapSetSecretLockPayload'] = _ATOMICSWAPSETSECRETLOCKPAYLOAD
DESCRIPTOR.message_types_by_name['AtomicSwapClosePayload'] = _ATOMICSWAPCLOSEPAYLOAD
DESCRIPTOR.message_types_by_name['AtomicSwapInfo'] = _ATOMICSWAPINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AtomicSwapMethod = _reflection.GeneratedProtocolMessageType('AtomicSwapMethod', (_message.Message,), dict(
  DESCRIPTOR = _ATOMICSWAPMETHOD,
  __module__ = 'atomic_swap_pb2'
  # @@protoc_insertion_point(class_scope:AtomicSwapMethod)
  ))
_sym_db.RegisterMessage(AtomicSwapMethod)

AtomicSwapInitPayload = _reflection.GeneratedProtocolMessageType('AtomicSwapInitPayload', (_message.Message,), dict(
  DESCRIPTOR = _ATOMICSWAPINITPAYLOAD,
  __module__ = 'atomic_swap_pb2'
  # @@protoc_insertion_point(class_scope:AtomicSwapInitPayload)
  ))
_sym_db.RegisterMessage(AtomicSwapInitPayload)

AtomicSwapApprovePayload = _reflection.GeneratedProtocolMessageType('AtomicSwapApprovePayload', (_message.Message,), dict(
  DESCRIPTOR = _ATOMICSWAPAPPROVEPAYLOAD,
  __module__ = 'atomic_swap_pb2'
  # @@protoc_insertion_point(class_scope:AtomicSwapApprovePayload)
  ))
_sym_db.RegisterMessage(AtomicSwapApprovePayload)

AtomicSwapExpirePayload = _reflection.GeneratedProtocolMessageType('AtomicSwapExpirePayload', (_message.Message,), dict(
  DESCRIPTOR = _ATOMICSWAPEXPIREPAYLOAD,
  __module__ = 'atomic_swap_pb2'
  # @@protoc_insertion_point(class_scope:AtomicSwapExpirePayload)
  ))
_sym_db.RegisterMessage(AtomicSwapExpirePayload)

AtomicSwapSetSecretLockPayload = _reflection.GeneratedProtocolMessageType('AtomicSwapSetSecretLockPayload', (_message.Message,), dict(
  DESCRIPTOR = _ATOMICSWAPSETSECRETLOCKPAYLOAD,
  __module__ = 'atomic_swap_pb2'
  # @@protoc_insertion_point(class_scope:AtomicSwapSetSecretLockPayload)
  ))
_sym_db.RegisterMessage(AtomicSwapSetSecretLockPayload)

AtomicSwapClosePayload = _reflection.GeneratedProtocolMessageType('AtomicSwapClosePayload', (_message.Message,), dict(
  DESCRIPTOR = _ATOMICSWAPCLOSEPAYLOAD,
  __module__ = 'atomic_swap_pb2'
  # @@protoc_insertion_point(class_scope:AtomicSwapClosePayload)
  ))
_sym_db.RegisterMessage(AtomicSwapClosePayload)

AtomicSwapInfo = _reflection.GeneratedProtocolMessageType('AtomicSwapInfo', (_message.Message,), dict(
  DESCRIPTOR = _ATOMICSWAPINFO,
  __module__ = 'atomic_swap_pb2'
  # @@protoc_insertion_point(class_scope:AtomicSwapInfo)
  ))
_sym_db.RegisterMessage(AtomicSwapInfo)


# @@protoc_insertion_point(module_scope)
