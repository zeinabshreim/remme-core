# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: certificate.proto

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
  name='certificate.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x63\x65rtificate.proto\"\xc6\x01\n\x16\x43\x65rtificateTransaction\x12/\n\x04type\x18\x01 \x01(\x0e\x32!.CertificateTransaction.Operation\x12\x17\n\x0f\x63\x65rtificate_raw\x18\x02 \x01(\t\x12\x15\n\rsignature_rem\x18\x03 \x01(\t\x12\x15\n\rsignature_crt\x18\x04 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x05 \x01(\t\"#\n\tOperation\x12\n\n\x06\x43REATE\x10\x00\x12\n\n\x06REVOKE\x10\x02\"B\n\x12\x43\x65rtificateStorage\x12\x0c\n\x04hash\x18\x01 \x01(\t\x12\r\n\x05owner\x18\x02 \x01(\t\x12\x0f\n\x07revoked\x18\x03 \x01(\x08\x62\x06proto3')
)



_CERTIFICATETRANSACTION_OPERATION = _descriptor.EnumDescriptor(
  name='Operation',
  full_name='CertificateTransaction.Operation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CREATE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REVOKE', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=185,
  serialized_end=220,
)
_sym_db.RegisterEnumDescriptor(_CERTIFICATETRANSACTION_OPERATION)


_CERTIFICATETRANSACTION = _descriptor.Descriptor(
  name='CertificateTransaction',
  full_name='CertificateTransaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='CertificateTransaction.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='certificate_raw', full_name='CertificateTransaction.certificate_raw', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature_rem', full_name='CertificateTransaction.signature_rem', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature_crt', full_name='CertificateTransaction.signature_crt', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='CertificateTransaction.address', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CERTIFICATETRANSACTION_OPERATION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=220,
)


_CERTIFICATESTORAGE = _descriptor.Descriptor(
  name='CertificateStorage',
  full_name='CertificateStorage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hash', full_name='CertificateStorage.hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='owner', full_name='CertificateStorage.owner', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='revoked', full_name='CertificateStorage.revoked', index=2,
      number=3, type=8, cpp_type=7, label=1,
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
  serialized_start=222,
  serialized_end=288,
)

_CERTIFICATETRANSACTION.fields_by_name['type'].enum_type = _CERTIFICATETRANSACTION_OPERATION
_CERTIFICATETRANSACTION_OPERATION.containing_type = _CERTIFICATETRANSACTION
DESCRIPTOR.message_types_by_name['CertificateTransaction'] = _CERTIFICATETRANSACTION
DESCRIPTOR.message_types_by_name['CertificateStorage'] = _CERTIFICATESTORAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CertificateTransaction = _reflection.GeneratedProtocolMessageType('CertificateTransaction', (_message.Message,), dict(
  DESCRIPTOR = _CERTIFICATETRANSACTION,
  __module__ = 'certificate_pb2'
  # @@protoc_insertion_point(class_scope:CertificateTransaction)
  ))
_sym_db.RegisterMessage(CertificateTransaction)

CertificateStorage = _reflection.GeneratedProtocolMessageType('CertificateStorage', (_message.Message,), dict(
  DESCRIPTOR = _CERTIFICATESTORAGE,
  __module__ = 'certificate_pb2'
  # @@protoc_insertion_point(class_scope:CertificateStorage)
  ))
_sym_db.RegisterMessage(CertificateStorage)


# @@protoc_insertion_point(module_scope)