# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ga4gh/schemas/ga4gh/reads.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ga4gh.schemas.ga4gh import common_pb2 as ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ga4gh/schemas/ga4gh/reads.proto',
  package='ga4gh.schemas.ga4gh',
  syntax='proto3',
  serialized_pb=_b('\n\x1fga4gh/schemas/ga4gh/reads.proto\x12\x13ga4gh.schemas.ga4gh\x1a ga4gh/schemas/ga4gh/common.proto\"Y\n\tReadStats\x12\x1a\n\x12\x61ligned_read_count\x18\x01 \x01(\x03\x12\x1c\n\x14unaligned_read_count\x18\x02 \x01(\x03\x12\x12\n\nbase_count\x18\x03 \x01(\x03\"\xac\x03\n\tReadGroup\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12\x13\n\x0bsample_name\x18\x05 \x01(\t\x12\x14\n\x0c\x62iosample_id\x18\x06 \x01(\t\x12\x33\n\nexperiment\x18\x07 \x01(\x0b\x32\x1f.ga4gh.schemas.ga4gh.Experiment\x12\x1d\n\x15predicted_insert_size\x18\x08 \x01(\x05\x12-\n\x05stats\x18\x0b \x01(\x0b\x32\x1e.ga4gh.schemas.ga4gh.ReadStats\x12.\n\x08programs\x18\x0c \x03(\x0b\x32\x1c.ga4gh.schemas.ga4gh.Program\x12\x18\n\x10reference_set_id\x18\r \x01(\t\x12\x33\n\nattributes\x18\x0f \x01(\x0b\x32\x1f.ga4gh.schemas.ga4gh.Attributes\x12/\n\x08metadata\x18\x10 \x01(\x0b\x32\x1d.ga4gh.schemas.ga4gh.Metadata\"\x86\x02\n\x0cReadGroupSet\x12\n\n\x02id\x18\x01 \x01(\t\x12\x12\n\ndataset_id\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12-\n\x05stats\x18\x04 \x01(\x0b\x32\x1e.ga4gh.schemas.ga4gh.ReadStats\x12\x33\n\x0bread_groups\x18\x05 \x03(\x0b\x32\x1e.ga4gh.schemas.ga4gh.ReadGroup\x12\x33\n\nattributes\x18\x06 \x01(\x0b\x32\x1f.ga4gh.schemas.ga4gh.Attributes\x12/\n\x08metadata\x18\x07 \x01(\x0b\x32\x1d.ga4gh.schemas.ga4gh.Metadata\"\x8a\x01\n\x0fLinearAlignment\x12/\n\x08position\x18\x01 \x01(\x0b\x32\x1d.ga4gh.schemas.ga4gh.Position\x12\x17\n\x0fmapping_quality\x18\x02 \x01(\x05\x12-\n\x05\x63igar\x18\x03 \x03(\x0b\x32\x1e.ga4gh.schemas.ga4gh.CigarUnit\"\xb6\x04\n\rReadAlignment\x12\n\n\x02id\x18\x01 \x01(\t\x12\x15\n\rread_group_id\x18\x02 \x01(\t\x12\x15\n\rfragment_name\x18\x03 \x01(\t\x12\x1a\n\x12improper_placement\x18\x04 \x01(\x08\x12\x1a\n\x12\x64uplicate_fragment\x18\x05 \x01(\x08\x12\x14\n\x0cnumber_reads\x18\x06 \x01(\x05\x12\x17\n\x0f\x66ragment_length\x18\x07 \x01(\x05\x12\x13\n\x0bread_number\x18\x08 \x01(\x05\x12$\n\x1c\x66\x61iled_vendor_quality_checks\x18\t \x01(\x08\x12\x37\n\talignment\x18\n \x01(\x0b\x32$.ga4gh.schemas.ga4gh.LinearAlignment\x12\x1b\n\x13secondary_alignment\x18\x0b \x01(\x08\x12\x1f\n\x17supplementary_alignment\x18\x0c \x01(\x08\x12\x18\n\x10\x61ligned_sequence\x18\r \x01(\t\x12\x17\n\x0f\x61ligned_quality\x18\x0e \x03(\x05\x12\x39\n\x12next_mate_position\x18\x0f \x01(\x0b\x32\x1d.ga4gh.schemas.ga4gh.Position\x12\x33\n\nattributes\x18\x11 \x01(\x0b\x32\x1f.ga4gh.schemas.ga4gh.Attributes\x12/\n\x08metadata\x18\x12 \x01(\x0b\x32\x1d.ga4gh.schemas.ga4gh.Metadata\"\xb0\x02\n\tCigarUnit\x12;\n\toperation\x18\x01 \x01(\x0e\x32(.ga4gh.schemas.ga4gh.CigarUnit.Operation\x12\x18\n\x10operation_length\x18\x02 \x01(\x03\x12\x1a\n\x12reference_sequence\x18\x03 \x01(\t\"\xaf\x01\n\tOperation\x12\x19\n\x15OPERATION_UNSPECIFIED\x10\x00\x12\x13\n\x0f\x41LIGNMENT_MATCH\x10\x01\x12\n\n\x06INSERT\x10\x02\x12\n\n\x06\x44\x45LETE\x10\x03\x12\x08\n\x04SKIP\x10\x04\x12\r\n\tCLIP_SOFT\x10\x05\x12\r\n\tCLIP_HARD\x10\x06\x12\x07\n\x03PAD\x10\x07\x12\x12\n\x0eSEQUENCE_MATCH\x10\x08\x12\x15\n\x11SEQUENCE_MISMATCH\x10\tb\x06proto3')
  ,
  dependencies=[ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_CIGARUNIT_OPERATION = _descriptor.EnumDescriptor(
  name='Operation',
  full_name='ga4gh.schemas.ga4gh.CigarUnit.Operation',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OPERATION_UNSPECIFIED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ALIGNMENT_MATCH', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INSERT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DELETE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SKIP', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLIP_SOFT', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CLIP_HARD', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAD', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEQUENCE_MATCH', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SEQUENCE_MISMATCH', index=9, number=9,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1717,
  serialized_end=1892,
)
_sym_db.RegisterEnumDescriptor(_CIGARUNIT_OPERATION)


_READSTATS = _descriptor.Descriptor(
  name='ReadStats',
  full_name='ga4gh.schemas.ga4gh.ReadStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='aligned_read_count', full_name='ga4gh.schemas.ga4gh.ReadStats.aligned_read_count', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unaligned_read_count', full_name='ga4gh.schemas.ga4gh.ReadStats.unaligned_read_count', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='base_count', full_name='ga4gh.schemas.ga4gh.ReadStats.base_count', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=90,
  serialized_end=179,
)


_READGROUP = _descriptor.Descriptor(
  name='ReadGroup',
  full_name='ga4gh.schemas.ga4gh.ReadGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.schemas.ga4gh.ReadGroup.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.schemas.ga4gh.ReadGroup.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.schemas.ga4gh.ReadGroup.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='ga4gh.schemas.ga4gh.ReadGroup.description', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sample_name', full_name='ga4gh.schemas.ga4gh.ReadGroup.sample_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='biosample_id', full_name='ga4gh.schemas.ga4gh.ReadGroup.biosample_id', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='experiment', full_name='ga4gh.schemas.ga4gh.ReadGroup.experiment', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predicted_insert_size', full_name='ga4gh.schemas.ga4gh.ReadGroup.predicted_insert_size', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stats', full_name='ga4gh.schemas.ga4gh.ReadGroup.stats', index=8,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='programs', full_name='ga4gh.schemas.ga4gh.ReadGroup.programs', index=9,
      number=12, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_set_id', full_name='ga4gh.schemas.ga4gh.ReadGroup.reference_set_id', index=10,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ga4gh.schemas.ga4gh.ReadGroup.attributes', index=11,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='ga4gh.schemas.ga4gh.ReadGroup.metadata', index=12,
      number=16, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=182,
  serialized_end=610,
)


_READGROUPSET = _descriptor.Descriptor(
  name='ReadGroupSet',
  full_name='ga4gh.schemas.ga4gh.ReadGroupSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.schemas.ga4gh.ReadGroupSet.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dataset_id', full_name='ga4gh.schemas.ga4gh.ReadGroupSet.dataset_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='ga4gh.schemas.ga4gh.ReadGroupSet.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stats', full_name='ga4gh.schemas.ga4gh.ReadGroupSet.stats', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_groups', full_name='ga4gh.schemas.ga4gh.ReadGroupSet.read_groups', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ga4gh.schemas.ga4gh.ReadGroupSet.attributes', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='ga4gh.schemas.ga4gh.ReadGroupSet.metadata', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=613,
  serialized_end=875,
)


_LINEARALIGNMENT = _descriptor.Descriptor(
  name='LinearAlignment',
  full_name='ga4gh.schemas.ga4gh.LinearAlignment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='ga4gh.schemas.ga4gh.LinearAlignment.position', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mapping_quality', full_name='ga4gh.schemas.ga4gh.LinearAlignment.mapping_quality', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cigar', full_name='ga4gh.schemas.ga4gh.LinearAlignment.cigar', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=878,
  serialized_end=1016,
)


_READALIGNMENT = _descriptor.Descriptor(
  name='ReadAlignment',
  full_name='ga4gh.schemas.ga4gh.ReadAlignment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='ga4gh.schemas.ga4gh.ReadAlignment.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_group_id', full_name='ga4gh.schemas.ga4gh.ReadAlignment.read_group_id', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fragment_name', full_name='ga4gh.schemas.ga4gh.ReadAlignment.fragment_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='improper_placement', full_name='ga4gh.schemas.ga4gh.ReadAlignment.improper_placement', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duplicate_fragment', full_name='ga4gh.schemas.ga4gh.ReadAlignment.duplicate_fragment', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='number_reads', full_name='ga4gh.schemas.ga4gh.ReadAlignment.number_reads', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fragment_length', full_name='ga4gh.schemas.ga4gh.ReadAlignment.fragment_length', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='read_number', full_name='ga4gh.schemas.ga4gh.ReadAlignment.read_number', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='failed_vendor_quality_checks', full_name='ga4gh.schemas.ga4gh.ReadAlignment.failed_vendor_quality_checks', index=8,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alignment', full_name='ga4gh.schemas.ga4gh.ReadAlignment.alignment', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='secondary_alignment', full_name='ga4gh.schemas.ga4gh.ReadAlignment.secondary_alignment', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='supplementary_alignment', full_name='ga4gh.schemas.ga4gh.ReadAlignment.supplementary_alignment', index=11,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aligned_sequence', full_name='ga4gh.schemas.ga4gh.ReadAlignment.aligned_sequence', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aligned_quality', full_name='ga4gh.schemas.ga4gh.ReadAlignment.aligned_quality', index=13,
      number=14, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='next_mate_position', full_name='ga4gh.schemas.ga4gh.ReadAlignment.next_mate_position', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='ga4gh.schemas.ga4gh.ReadAlignment.attributes', index=15,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='metadata', full_name='ga4gh.schemas.ga4gh.ReadAlignment.metadata', index=16,
      number=18, type=11, cpp_type=10, label=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1019,
  serialized_end=1585,
)


_CIGARUNIT = _descriptor.Descriptor(
  name='CigarUnit',
  full_name='ga4gh.schemas.ga4gh.CigarUnit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operation', full_name='ga4gh.schemas.ga4gh.CigarUnit.operation', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation_length', full_name='ga4gh.schemas.ga4gh.CigarUnit.operation_length', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reference_sequence', full_name='ga4gh.schemas.ga4gh.CigarUnit.reference_sequence', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CIGARUNIT_OPERATION,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1588,
  serialized_end=1892,
)

_READGROUP.fields_by_name['experiment'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._EXPERIMENT
_READGROUP.fields_by_name['stats'].message_type = _READSTATS
_READGROUP.fields_by_name['programs'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._PROGRAM
_READGROUP.fields_by_name['attributes'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._ATTRIBUTES
_READGROUP.fields_by_name['metadata'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._METADATA
_READGROUPSET.fields_by_name['stats'].message_type = _READSTATS
_READGROUPSET.fields_by_name['read_groups'].message_type = _READGROUP
_READGROUPSET.fields_by_name['attributes'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._ATTRIBUTES
_READGROUPSET.fields_by_name['metadata'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._METADATA
_LINEARALIGNMENT.fields_by_name['position'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._POSITION
_LINEARALIGNMENT.fields_by_name['cigar'].message_type = _CIGARUNIT
_READALIGNMENT.fields_by_name['alignment'].message_type = _LINEARALIGNMENT
_READALIGNMENT.fields_by_name['next_mate_position'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._POSITION
_READALIGNMENT.fields_by_name['attributes'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._ATTRIBUTES
_READALIGNMENT.fields_by_name['metadata'].message_type = ga4gh_dot_schemas_dot_ga4gh_dot_common__pb2._METADATA
_CIGARUNIT.fields_by_name['operation'].enum_type = _CIGARUNIT_OPERATION
_CIGARUNIT_OPERATION.containing_type = _CIGARUNIT
DESCRIPTOR.message_types_by_name['ReadStats'] = _READSTATS
DESCRIPTOR.message_types_by_name['ReadGroup'] = _READGROUP
DESCRIPTOR.message_types_by_name['ReadGroupSet'] = _READGROUPSET
DESCRIPTOR.message_types_by_name['LinearAlignment'] = _LINEARALIGNMENT
DESCRIPTOR.message_types_by_name['ReadAlignment'] = _READALIGNMENT
DESCRIPTOR.message_types_by_name['CigarUnit'] = _CIGARUNIT

ReadStats = _reflection.GeneratedProtocolMessageType('ReadStats', (_message.Message,), dict(
  DESCRIPTOR = _READSTATS,
  __module__ = 'ga4gh.schemas.ga4gh.reads_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.ReadStats)
  ))
_sym_db.RegisterMessage(ReadStats)

ReadGroup = _reflection.GeneratedProtocolMessageType('ReadGroup', (_message.Message,), dict(
  DESCRIPTOR = _READGROUP,
  __module__ = 'ga4gh.schemas.ga4gh.reads_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.ReadGroup)
  ))
_sym_db.RegisterMessage(ReadGroup)

ReadGroupSet = _reflection.GeneratedProtocolMessageType('ReadGroupSet', (_message.Message,), dict(
  DESCRIPTOR = _READGROUPSET,
  __module__ = 'ga4gh.schemas.ga4gh.reads_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.ReadGroupSet)
  ))
_sym_db.RegisterMessage(ReadGroupSet)

LinearAlignment = _reflection.GeneratedProtocolMessageType('LinearAlignment', (_message.Message,), dict(
  DESCRIPTOR = _LINEARALIGNMENT,
  __module__ = 'ga4gh.schemas.ga4gh.reads_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.LinearAlignment)
  ))
_sym_db.RegisterMessage(LinearAlignment)

ReadAlignment = _reflection.GeneratedProtocolMessageType('ReadAlignment', (_message.Message,), dict(
  DESCRIPTOR = _READALIGNMENT,
  __module__ = 'ga4gh.schemas.ga4gh.reads_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.ReadAlignment)
  ))
_sym_db.RegisterMessage(ReadAlignment)

CigarUnit = _reflection.GeneratedProtocolMessageType('CigarUnit', (_message.Message,), dict(
  DESCRIPTOR = _CIGARUNIT,
  __module__ = 'ga4gh.schemas.ga4gh.reads_pb2'
  # @@protoc_insertion_point(class_scope:ga4gh.schemas.ga4gh.CigarUnit)
  ))
_sym_db.RegisterMessage(CigarUnit)


# @@protoc_insertion_point(module_scope)
