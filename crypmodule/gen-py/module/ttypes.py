#
# Autogenerated by Thrift Compiler (0.13.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class InitParame(object):
    """
    Attributes:
     - L

    """


    def __init__(self, L=None,):
        self.L = L

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.L = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('InitParame')
        if self.L is not None:
            oprot.writeFieldBegin('L', TType.STRING, 1)
            oprot.writeString(self.L.encode('utf-8') if sys.version_info[0] == 2 else self.L)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class GetKeypairs(object):
    """
    Attributes:
     - g1
     - g2
     - z
     - u1
     - u2
     - x1
     - x2
     - y1
     - y2

    """


    def __init__(self, g1=None, g2=None, z=None, u1=None, u2=None, x1=None, x2=None, y1=None, y2=None,):
        self.g1 = g1
        self.g2 = g2
        self.z = z
        self.u1 = u1
        self.u2 = u2
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.g1 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.g2 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.z = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.u1 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.u2 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.x1 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 7:
                if ftype == TType.STRING:
                    self.x2 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 8:
                if ftype == TType.STRING:
                    self.y1 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 9:
                if ftype == TType.STRING:
                    self.y2 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('GetKeypairs')
        if self.g1 is not None:
            oprot.writeFieldBegin('g1', TType.STRING, 1)
            oprot.writeString(self.g1.encode('utf-8') if sys.version_info[0] == 2 else self.g1)
            oprot.writeFieldEnd()
        if self.g2 is not None:
            oprot.writeFieldBegin('g2', TType.STRING, 2)
            oprot.writeString(self.g2.encode('utf-8') if sys.version_info[0] == 2 else self.g2)
            oprot.writeFieldEnd()
        if self.z is not None:
            oprot.writeFieldBegin('z', TType.STRING, 3)
            oprot.writeString(self.z.encode('utf-8') if sys.version_info[0] == 2 else self.z)
            oprot.writeFieldEnd()
        if self.u1 is not None:
            oprot.writeFieldBegin('u1', TType.STRING, 4)
            oprot.writeString(self.u1.encode('utf-8') if sys.version_info[0] == 2 else self.u1)
            oprot.writeFieldEnd()
        if self.u2 is not None:
            oprot.writeFieldBegin('u2', TType.STRING, 5)
            oprot.writeString(self.u2.encode('utf-8') if sys.version_info[0] == 2 else self.u2)
            oprot.writeFieldEnd()
        if self.x1 is not None:
            oprot.writeFieldBegin('x1', TType.STRING, 6)
            oprot.writeString(self.x1.encode('utf-8') if sys.version_info[0] == 2 else self.x1)
            oprot.writeFieldEnd()
        if self.x2 is not None:
            oprot.writeFieldBegin('x2', TType.STRING, 7)
            oprot.writeString(self.x2.encode('utf-8') if sys.version_info[0] == 2 else self.x2)
            oprot.writeFieldEnd()
        if self.y1 is not None:
            oprot.writeFieldBegin('y1', TType.STRING, 8)
            oprot.writeString(self.y1.encode('utf-8') if sys.version_info[0] == 2 else self.y1)
            oprot.writeFieldEnd()
        if self.y2 is not None:
            oprot.writeFieldBegin('y2', TType.STRING, 9)
            oprot.writeString(self.y2.encode('utf-8') if sys.version_info[0] == 2 else self.y2)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Enc(object):
    """
    Attributes:
     - g1
     - g2
     - z
     - u1
     - u2

    """


    def __init__(self, g1=None, g2=None, z=None, u1=None, u2=None,):
        self.g1 = g1
        self.g2 = g2
        self.z = z
        self.u1 = u1
        self.u2 = u2

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.g1 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.g2 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.z = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.u1 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.u2 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Enc')
        if self.g1 is not None:
            oprot.writeFieldBegin('g1', TType.STRING, 1)
            oprot.writeString(self.g1.encode('utf-8') if sys.version_info[0] == 2 else self.g1)
            oprot.writeFieldEnd()
        if self.g2 is not None:
            oprot.writeFieldBegin('g2', TType.STRING, 2)
            oprot.writeString(self.g2.encode('utf-8') if sys.version_info[0] == 2 else self.g2)
            oprot.writeFieldEnd()
        if self.z is not None:
            oprot.writeFieldBegin('z', TType.STRING, 3)
            oprot.writeString(self.z.encode('utf-8') if sys.version_info[0] == 2 else self.z)
            oprot.writeFieldEnd()
        if self.u1 is not None:
            oprot.writeFieldBegin('u1', TType.STRING, 4)
            oprot.writeString(self.u1.encode('utf-8') if sys.version_info[0] == 2 else self.u1)
            oprot.writeFieldEnd()
        if self.u2 is not None:
            oprot.writeFieldBegin('u2', TType.STRING, 5)
            oprot.writeString(self.u2.encode('utf-8') if sys.version_info[0] == 2 else self.u2)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class RetEnc(object):
    """
    Attributes:
     - symkey
     - ctx

    """


    def __init__(self, symkey=None, ctx=None,):
        self.symkey = symkey
        self.ctx = ctx

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.symkey = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.ctx = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('RetEnc')
        if self.symkey is not None:
            oprot.writeFieldBegin('symkey', TType.STRING, 1)
            oprot.writeString(self.symkey.encode('utf-8') if sys.version_info[0] == 2 else self.symkey)
            oprot.writeFieldEnd()
        if self.ctx is not None:
            oprot.writeFieldBegin('ctx', TType.STRING, 2)
            oprot.writeString(self.ctx.encode('utf-8') if sys.version_info[0] == 2 else self.ctx)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class Dec(object):
    """
    Attributes:
     - x1
     - x2
     - y1
     - y2
     - tag
     - ctx

    """


    def __init__(self, x1=None, x2=None, y1=None, y2=None, tag=None, ctx=None,):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.tag = tag
        self.ctx = ctx

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.x1 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.x2 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.STRING:
                    self.y1 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 4:
                if ftype == TType.STRING:
                    self.y2 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 5:
                if ftype == TType.STRING:
                    self.tag = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 6:
                if ftype == TType.STRING:
                    self.ctx = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('Dec')
        if self.x1 is not None:
            oprot.writeFieldBegin('x1', TType.STRING, 1)
            oprot.writeString(self.x1.encode('utf-8') if sys.version_info[0] == 2 else self.x1)
            oprot.writeFieldEnd()
        if self.x2 is not None:
            oprot.writeFieldBegin('x2', TType.STRING, 2)
            oprot.writeString(self.x2.encode('utf-8') if sys.version_info[0] == 2 else self.x2)
            oprot.writeFieldEnd()
        if self.y1 is not None:
            oprot.writeFieldBegin('y1', TType.STRING, 3)
            oprot.writeString(self.y1.encode('utf-8') if sys.version_info[0] == 2 else self.y1)
            oprot.writeFieldEnd()
        if self.y2 is not None:
            oprot.writeFieldBegin('y2', TType.STRING, 4)
            oprot.writeString(self.y2.encode('utf-8') if sys.version_info[0] == 2 else self.y2)
            oprot.writeFieldEnd()
        if self.tag is not None:
            oprot.writeFieldBegin('tag', TType.STRING, 5)
            oprot.writeString(self.tag.encode('utf-8') if sys.version_info[0] == 2 else self.tag)
            oprot.writeFieldEnd()
        if self.ctx is not None:
            oprot.writeFieldBegin('ctx', TType.STRING, 6)
            oprot.writeString(self.ctx.encode('utf-8') if sys.version_info[0] == 2 else self.ctx)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)


class RetDec(object):
    """
    Attributes:
     - symkey

    """


    def __init__(self, symkey=None,):
        self.symkey = symkey

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.STRING:
                    self.symkey = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('RetDec')
        if self.symkey is not None:
            oprot.writeFieldBegin('symkey', TType.STRING, 1)
            oprot.writeString(self.symkey.encode('utf-8') if sys.version_info[0] == 2 else self.symkey)
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(InitParame)
InitParame.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'L', 'UTF8', None, ),  # 1
)
all_structs.append(GetKeypairs)
GetKeypairs.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'g1', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'g2', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'z', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'u1', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'u2', 'UTF8', None, ),  # 5
    (6, TType.STRING, 'x1', 'UTF8', None, ),  # 6
    (7, TType.STRING, 'x2', 'UTF8', None, ),  # 7
    (8, TType.STRING, 'y1', 'UTF8', None, ),  # 8
    (9, TType.STRING, 'y2', 'UTF8', None, ),  # 9
)
all_structs.append(Enc)
Enc.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'g1', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'g2', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'z', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'u1', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'u2', 'UTF8', None, ),  # 5
)
all_structs.append(RetEnc)
RetEnc.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'symkey', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'ctx', 'UTF8', None, ),  # 2
)
all_structs.append(Dec)
Dec.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'x1', 'UTF8', None, ),  # 1
    (2, TType.STRING, 'x2', 'UTF8', None, ),  # 2
    (3, TType.STRING, 'y1', 'UTF8', None, ),  # 3
    (4, TType.STRING, 'y2', 'UTF8', None, ),  # 4
    (5, TType.STRING, 'tag', 'UTF8', None, ),  # 5
    (6, TType.STRING, 'ctx', 'UTF8', None, ),  # 6
)
all_structs.append(RetDec)
RetDec.thrift_spec = (
    None,  # 0
    (1, TType.STRING, 'symkey', 'UTF8', None, ),  # 1
)
fix_spec(all_structs)
del all_structs