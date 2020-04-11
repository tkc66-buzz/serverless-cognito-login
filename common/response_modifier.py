from decimal import Decimal


def decimal_to_float_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" %
                    obj.__class__.__name__)
