import socket
import struct
import binascii

class Udphdr:

    def __init__(self, sport, dport, len, checksum):
        self.sport = sport
        self.dport = dport
        self.len = len
        self.checksum = checksum

    def pack_Udphdr(self):         # UDP 헤더를 unpack 하는 함수
        packed = b''
        packed += struct.pack('!4H', self.sport, self.dport, self.len, self.checksum)
        return packed


def unpack_Udphdr(buffer):
    unpacked = struct.unpack('!4H', buffer[:20])
    return unpacked

def getSourcePort(unpacked_udphdr):
    return unpacked_udphdr[0]

def getDestinationPort(unpacked_udphdr):
    return unpacked_udphdr[1]

def getLength(unpacked_udphdr):
    return unpacked_udphdr[2]

def getChecksum(unpacked_udphdr):
    return unpacked_udphdr[3]



udp = Udphdr(5555, 80, 1000, 0xFFFF)
packed_udphdr = udp.pack_Udphdr()
print(binascii.b2a_hex(packed_udphdr))

unpacked_udphdr = unpack_Udphdr(packed_udphdr)
print(unpacked_udphdr)
print('Source Port:{} Destination Port:{} Length:{} Checksum:{}' 
    .format(getSourcePort(unpacked_udphdr),
     getDestinationPort(unpacked_udphdr),
     getLength(unpacked_udphdr),
     getChecksum(unpacked_udphdr)))