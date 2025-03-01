import ctypes

import nifake._visatype


class struct_CustomStructTypedef(ctypes.Structure):  # noqa N801
    _fields_ = [
        ('struct_int', nifake._visatype.ViInt32),
        ('struct_double', nifake._visatype.ViReal64),
    ]

    def __init__(self, data=None):
        super(ctypes.Structure, self).__init__()
        if data is not None:
            self.struct_int = data.struct_int
            self.struct_double = data.struct_double
        else:
            self.struct_int = 0
            self.struct_double = 0.0


class CustomStructTypedef(object):
    def __init__(self, data=None, struct_int=0, struct_double=0.0):
        if data is not None:
            self.struct_int = data.struct_int
            self.struct_double = data.struct_double
        else:
            self.struct_int = struct_int
            self.struct_double = struct_double

    def __repr__(self):
        return '{0}(data=None, struct_int={1}, struct_double={2})'.format(
            self.__class__.__name__,
            self.struct_int,
            self.struct_double
        )

    def __str__(self):
        return self.__repr__()
