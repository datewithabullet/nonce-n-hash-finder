import hashlib
#хеш первой строки и сумма денег берутся из условия
initial_string = '00bc4e693a4848c4ebc3d95ed3c1f2bc70ef888ac31bd9ad5fad6c28a8da63e0' + hashlib.sha256(str(input('сумма денег из второй строки')).encode('utf-8')).hexdigest()
for nonce in range(1, 2001):
    result_hash = hashlib.sha256(str(initial_string + hashlib.sha256(str(nonce).encode('utf-8')).hexdigest()).encode('utf-8')).hexdigest()
    if result_hash[:2] == '00':
        print(nonce, result_hash)