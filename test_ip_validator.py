from ip_validator import *
import string

class Tests(): 
    def test_ipv4_valid(self):
        val = Validate()
        for i in range(256):
            ip = (str(i) + '.') * 3 + str(i)
            assert val.validateIPAddress([ip])[i] == [ip, "Valid IPv4"]
    
    def test_ipv4_wrong(self):
        val = Validate()
        for i in range(256, 1000):
            ip = (str(i) + '.') * 3 + str(i)
            assert val.validateIPAddress([ip])[i-256] == [ip,"Wrong IPv4"]
    
    def test_ipv6_valid(self):
        val = Validate()
        for i in range(10):
            ip = (str(i) + ':') * 7 + str(i)
            assert val.validateIPAddress([ip])[i] == [ip, "Valid IPv6"]
        for c in string.ascii_lowercase[:6]:
            ip = (c + ':') * 7 + c
            assert val.validateIPAddress([ip])[ord(c) - 97 + 10] == [ip, "Valid IPv6"]
    
    def test_ipv6_wrong(self):
        val = Validate()
        for c in string.ascii_lowercase[6:]:
            ip = (c + ':') * 7 + c
            assert val.validateIPAddress([ip])[ord(c) - 97 - 7] == [ip, "Wrong IPv6"]
    
    def test_emptyip_wrong(self):
        val = Validate()
        verdict = val.validateIPAddress([""])[0]
        assert verdict != ["","Valid IPv4"] and verdict != ["","Valid IPv6"]