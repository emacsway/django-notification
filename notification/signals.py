import django.dispatch

should_deliver = django.dispatch.Signal(providing_args=["result", "recipient", "label", "extra_context", "sender_user", ])