# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.7
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.



from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_pixy', [dirname(__file__)])
        except ImportError:
            import _pixy
            return _pixy
        if fp is not None:
            try:
                _mod = imp.load_module('_pixy', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _pixy = swig_import_helper()
    del swig_import_helper
else:
    import _pixy
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class BlockArray(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BlockArray, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BlockArray, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _pixy.new_BlockArray(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pixy.delete_BlockArray
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _pixy.BlockArray___getitem__(self, *args)
    def __setitem__(self, *args): return _pixy.BlockArray___setitem__(self, *args)
    def cast(self): return _pixy.BlockArray_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _pixy.BlockArray_frompointer
    if _newclass:frompointer = staticmethod(_pixy.BlockArray_frompointer)
BlockArray_swigregister = _pixy.BlockArray_swigregister
BlockArray_swigregister(BlockArray)

def BlockArray_frompointer(*args):
  return _pixy.BlockArray_frompointer(*args)
BlockArray_frompointer = _pixy.BlockArray_frompointer


def pixy_init():
  return _pixy.pixy_init()
pixy_init = _pixy.pixy_init

def pixy_get_blocks(*args):
  return _pixy.pixy_get_blocks(*args)
pixy_get_blocks = _pixy.pixy_get_blocks

def pixy_close():
  return _pixy.pixy_close()
pixy_close = _pixy.pixy_close
class Block(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Block, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Block, name)
    __repr__ = _swig_repr
    __swig_setmethods__["type"] = _pixy.Block_type_set
    __swig_getmethods__["type"] = _pixy.Block_type_get
    if _newclass:type = _swig_property(_pixy.Block_type_get, _pixy.Block_type_set)
    __swig_setmethods__["signature"] = _pixy.Block_signature_set
    __swig_getmethods__["signature"] = _pixy.Block_signature_get
    if _newclass:signature = _swig_property(_pixy.Block_signature_get, _pixy.Block_signature_set)
    __swig_setmethods__["x"] = _pixy.Block_x_set
    __swig_getmethods__["x"] = _pixy.Block_x_get
    if _newclass:x = _swig_property(_pixy.Block_x_get, _pixy.Block_x_set)
    __swig_setmethods__["y"] = _pixy.Block_y_set
    __swig_getmethods__["y"] = _pixy.Block_y_get
    if _newclass:y = _swig_property(_pixy.Block_y_get, _pixy.Block_y_set)
    __swig_setmethods__["width"] = _pixy.Block_width_set
    __swig_getmethods__["width"] = _pixy.Block_width_get
    if _newclass:width = _swig_property(_pixy.Block_width_get, _pixy.Block_width_set)
    __swig_setmethods__["height"] = _pixy.Block_height_set
    __swig_getmethods__["height"] = _pixy.Block_height_get
    if _newclass:height = _swig_property(_pixy.Block_height_get, _pixy.Block_height_set)
    __swig_setmethods__["angle"] = _pixy.Block_angle_set
    __swig_getmethods__["angle"] = _pixy.Block_angle_get
    if _newclass:angle = _swig_property(_pixy.Block_angle_get, _pixy.Block_angle_set)
    def __init__(self): 
        this = _pixy.new_Block()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _pixy.delete_Block
    __del__ = lambda self : None;
Block_swigregister = _pixy.Block_swigregister
Block_swigregister(Block)

# This file is compatible with both classic and new-style classes.


