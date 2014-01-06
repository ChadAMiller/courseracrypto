import binascii

def hex_from(s):
    return binascii.hexlify(bytes(s, encoding='utf-8'))
    
def str_from(h):
    return str(binascii.unhexlify(h), encoding='utf-8')
    

class HexMessage:
    def __init__(self, msg):
        if type(msg) == bytes:
            # assumed already in hex
            self.msg = msg
        else:
            # assumed string
            self.msg = hex_from(msg)
            
    def __str__(self):
        return '"{}"'.format(str_from(self.msg))
        
    def __repr__(self):
        return repr(self.msg)
    
    def __xor__(self, other):
        a = binascii.unhexlify(self.msg)
        
        if type(other) == HexMessage:
            b = binascii.unhexlify(other.msg)
        elif type(other) == bytes:
            b = binascii.unhexlify(other)
        else:
            # assumed string
            b = bytes(other, encoding='utf-8')
        
        return HexMessage(binascii.hexlify(bytes(ai^bi for ai, bi in zip(a,b))))
        