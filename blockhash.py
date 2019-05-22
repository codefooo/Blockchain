import hashlib

# block info
v = "20000000"
pHash = "0000000000000000001113e97e93bd818554382f16d089a81371c6873a0b92b6"
mroot = "f765e73e351ef8ed6c0f09c2b2c48b87fee449ac41582193f757f0327a1d65e3"
ts = 1558398995  # convert human readable time to timestamp in https://www.epochconverter.com/ 
bits = 388627269  
n = 3231819810

# convert hex
ts = hex(ts).rstrip("L")[2:]
bits = hex(bits).rstrip("L")[2:]
n = hex(n).rstrip("L")[2:]

# byte order is little endian
v = v.decode('hex')[::-1].encode('hex_codec')
pHash = pHash.decode('hex')[::-1].encode('hex_codec')
mroot = mroot.decode('hex')[::-1].encode('hex_codec')
ts = ts.decode('hex')[::-1].encode('hex_codec')
bits = bits.decode('hex')[::-1].encode('hex_codec')
n = n.decode('hex')[::-1].encode('hex_codec')

header = (v + pHash + mroot + ts + bits+n)

print("Header String={}".format(header))

hash = hashlib.sha256(hashlib.sha256(header.decode('hex')).digest()).digest()
#print(hash.encode('hex_codec'))

# byte order is little endian
print("Block Hash={}".format(hash[::-1].encode('hex_codec')))






