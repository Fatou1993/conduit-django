from rest_framework.views import exception_handler

def core_exception_handler(exc, context):

    # If an exception is thrown that we don't explicitly handle here, we want
    # to delegate to the default exception handler offered by DRF. If we do
    # handle this exception type, we will still want access to the response
    # generated by DRF, so we get that response up front.
    response = exception_handler(exc, context)
    handlers = {
        'ValidationError': _handle_generic_error,
        'ProfileDoesNotExist': _handle_generic_error
    }
    # This is how we identify the type of the current exception. We will use
    # this in a moment to see whether we should handle this exception or let
    # Django REST Framework do its thing.
    exception_class = exc.__class__.__name__

    if exception_class in handlers :
        # If this exception is one that we can handle, handle it. Otherwise,
        # return the response generated earlier by the default exception
        # handler.
        return handlers[exception_class](exc, context, response)
    return response

def _handle_generic_error(exc, context, response):

    # This is the most straightforward exception handler we can create.
    # We take the response generated by DRF and wrap it in the `errors` key.
    response.data = {
        "errors": response.data
    }
    return response