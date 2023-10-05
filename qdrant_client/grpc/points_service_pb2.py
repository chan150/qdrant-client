# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: points_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import points_pb2 as points__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14points_service.proto\x12\x06qdrant\x1a\x0cpoints.proto\x1a\x1cgoogle/protobuf/struct.proto2\xc2\x0b\n\x06Points\x12\x41\n\x06Upsert\x12\x14.qdrant.UpsertPoints\x1a\x1f.qdrant.PointsOperationResponse\"\x00\x12\x41\n\x06\x44\x65lete\x12\x14.qdrant.DeletePoints\x1a\x1f.qdrant.PointsOperationResponse\"\x00\x12/\n\x03Get\x12\x11.qdrant.GetPoints\x1a\x13.qdrant.GetResponse\"\x00\x12N\n\rUpdateVectors\x12\x1a.qdrant.UpdatePointVectors\x1a\x1f.qdrant.PointsOperationResponse\"\x00\x12N\n\rDeleteVectors\x12\x1a.qdrant.DeletePointVectors\x1a\x1f.qdrant.PointsOperationResponse\"\x00\x12I\n\nSetPayload\x12\x18.qdrant.SetPayloadPoints\x1a\x1f.qdrant.PointsOperationResponse\"\x00\x12O\n\x10OverwritePayload\x12\x18.qdrant.SetPayloadPoints\x1a\x1f.qdrant.PointsOperationResponse\"\x00\x12O\n\rDeletePayload\x12\x1b.qdrant.DeletePayloadPoints\x1a\x1f.qdrant.PointsOperationResponse\"\x00\x12M\n\x0c\x43learPayload\x12\x1a.qdrant.ClearPayloadPoints\x1a\x1f.qdrant.PointsOperationResponse\"\x00\x12Y\n\x10\x43reateFieldIndex\x12\".qdrant.CreateFieldIndexCollection\x1a\x1f.qdrant.PointsOperationResponse\"\x00\x12Y\n\x10\x44\x65leteFieldIndex\x12\".qdrant.DeleteFieldIndexCollection\x1a\x1f.qdrant.PointsOperationResponse\"\x00\x12\x38\n\x06Search\x12\x14.qdrant.SearchPoints\x1a\x16.qdrant.SearchResponse\"\x00\x12G\n\x0bSearchBatch\x12\x19.qdrant.SearchBatchPoints\x1a\x1b.qdrant.SearchBatchResponse\"\x00\x12I\n\x0cSearchGroups\x12\x19.qdrant.SearchPointGroups\x1a\x1c.qdrant.SearchGroupsResponse\"\x00\x12\x38\n\x06Scroll\x12\x14.qdrant.ScrollPoints\x1a\x16.qdrant.ScrollResponse\"\x00\x12\x41\n\tRecommend\x12\x17.qdrant.RecommendPoints\x1a\x19.qdrant.RecommendResponse\"\x00\x12P\n\x0eRecommendBatch\x12\x1c.qdrant.RecommendBatchPoints\x1a\x1e.qdrant.RecommendBatchResponse\"\x00\x12R\n\x0fRecommendGroups\x12\x1c.qdrant.RecommendPointGroups\x1a\x1f.qdrant.RecommendGroupsResponse\"\x00\x12\x35\n\x05\x43ount\x12\x13.qdrant.CountPoints\x1a\x15.qdrant.CountResponse\"\x00\x12G\n\x0bUpdateBatch\x12\x19.qdrant.UpdateBatchPoints\x1a\x1b.qdrant.UpdateBatchResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'points_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_POINTS']._serialized_start=77
  _globals['_POINTS']._serialized_end=1551
# @@protoc_insertion_point(module_scope)
