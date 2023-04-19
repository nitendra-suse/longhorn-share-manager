# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import sm_pb2 as sm__pb2


class ShareManagerServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.FilesystemTrim = channel.unary_unary(
        '/ShareManagerService/FilesystemTrim',
        request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
        response_deserializer=sm__pb2.FilesystemTrimResponse.FromString,
        )


class ShareManagerServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def FilesystemTrim(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ShareManagerServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'FilesystemTrim': grpc.unary_unary_rpc_method_handler(
          servicer.FilesystemTrim,
          request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
          response_serializer=sm__pb2.FilesystemTrimResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ShareManagerService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))