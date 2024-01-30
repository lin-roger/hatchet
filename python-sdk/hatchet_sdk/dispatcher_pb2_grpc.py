# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import dispatcher_pb2 as dispatcher__pb2

class DispatcherStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Register = channel.unary_unary(
                '/Dispatcher/Register',
                request_serializer=dispatcher__pb2.WorkerRegisterRequest.SerializeToString,
                response_deserializer=dispatcher__pb2.WorkerRegisterResponse.FromString,
                )
        self.Listen = channel.unary_stream(
                '/Dispatcher/Listen',
                request_serializer=dispatcher__pb2.WorkerListenRequest.SerializeToString,
                response_deserializer=dispatcher__pb2.AssignedAction.FromString,
                )
        self.SendStepActionEvent = channel.unary_unary(
                '/Dispatcher/SendStepActionEvent',
                request_serializer=dispatcher__pb2.StepActionEvent.SerializeToString,
                response_deserializer=dispatcher__pb2.ActionEventResponse.FromString,
                )
        self.SendGroupKeyActionEvent = channel.unary_unary(
                '/Dispatcher/SendGroupKeyActionEvent',
                request_serializer=dispatcher__pb2.GroupKeyActionEvent.SerializeToString,
                response_deserializer=dispatcher__pb2.ActionEventResponse.FromString,
                )
        self.Unsubscribe = channel.unary_unary(
                '/Dispatcher/Unsubscribe',
                request_serializer=dispatcher__pb2.WorkerUnsubscribeRequest.SerializeToString,
                response_deserializer=dispatcher__pb2.WorkerUnsubscribeResponse.FromString,
                )


class DispatcherServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Register(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Listen(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendStepActionEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendGroupKeyActionEvent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Unsubscribe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DispatcherServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Register': grpc.unary_unary_rpc_method_handler(
                    servicer.Register,
                    request_deserializer=dispatcher__pb2.WorkerRegisterRequest.FromString,
                    response_serializer=dispatcher__pb2.WorkerRegisterResponse.SerializeToString,
            ),
            'Listen': grpc.unary_stream_rpc_method_handler(
                    servicer.Listen,
                    request_deserializer=dispatcher__pb2.WorkerListenRequest.FromString,
                    response_serializer=dispatcher__pb2.AssignedAction.SerializeToString,
            ),
            'SendStepActionEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.SendStepActionEvent,
                    request_deserializer=dispatcher__pb2.StepActionEvent.FromString,
                    response_serializer=dispatcher__pb2.ActionEventResponse.SerializeToString,
            ),
            'SendGroupKeyActionEvent': grpc.unary_unary_rpc_method_handler(
                    servicer.SendGroupKeyActionEvent,
                    request_deserializer=dispatcher__pb2.GroupKeyActionEvent.FromString,
                    response_serializer=dispatcher__pb2.ActionEventResponse.SerializeToString,
            ),
            'Unsubscribe': grpc.unary_unary_rpc_method_handler(
                    servicer.Unsubscribe,
                    request_deserializer=dispatcher__pb2.WorkerUnsubscribeRequest.FromString,
                    response_serializer=dispatcher__pb2.WorkerUnsubscribeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Dispatcher', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Dispatcher(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Register(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Dispatcher/Register',
            dispatcher__pb2.WorkerRegisterRequest.SerializeToString,
            dispatcher__pb2.WorkerRegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Listen(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Dispatcher/Listen',
            dispatcher__pb2.WorkerListenRequest.SerializeToString,
            dispatcher__pb2.AssignedAction.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendStepActionEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Dispatcher/SendStepActionEvent',
            dispatcher__pb2.StepActionEvent.SerializeToString,
            dispatcher__pb2.ActionEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendGroupKeyActionEvent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Dispatcher/SendGroupKeyActionEvent',
            dispatcher__pb2.GroupKeyActionEvent.SerializeToString,
            dispatcher__pb2.ActionEventResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Unsubscribe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Dispatcher/Unsubscribe',
            dispatcher__pb2.WorkerUnsubscribeRequest.SerializeToString,
            dispatcher__pb2.WorkerUnsubscribeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
