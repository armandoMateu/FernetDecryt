#!/usr/bin/env python3
from cryptography.fernet import Fernet as frt

key="" #Add key
token="" #Add toke

print('key: {0}, type: {1}'.format(key, type(key)))
print('token: {0}, type: {1}'.format(token, type(token)))

f=frt(key)
output = f.decrypt(bytes(token, 'utf-8'))
output_decoded = output.decode('utf-8')
print ('decrypted: {0}'.format(output_decoded))
