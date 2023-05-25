def add_parity_bits(data):
    m = len(data)
    r = 0
    
    while 2 ** r < m + r + 1:
        r += 1
        
    encoded_data = ""
    j = 0
    
    for i in range(1, m + r + 1):
        if i == 2 ** j:
            encoded_data += "0"
            j += 1
        else:
            encoded_data += data[m - 1 - (i - j - 1)]
            
    for i in range(r):
        pos = 2 ** i - 1
        count = 0
        
        for j in range(pos, m + r, 2 * pos + 1):
            for k in range(j, min(j + pos + 1, m + r)):
                if encoded_data[m + r - 1 - k] == "1":
                    count += 1
        if count % 2 == 1:
            encoded_data = encoded_data[:pos] + "1" + encoded_data[pos + 1:]
            
    return encoded_data


def correct_errors(data):
    r = 0
    
    while 2 ** r < len(data) + 1:
        r += 1
    error_pos = 0
    
    for i in range(r):
        pos = 2 ** i - 1
        count = 0
        
        for j in range(pos, len(data), 2 * pos + 1):
            for k in range(j, min(j + pos + 1, len(data))):
                if data[len(data) - k - 1] == "1":
                    count += 1
            if count % 2 == 1:
                error_pos += pos
        if error_pos > 0:
            data = data[:len(data) - error_pos] \
                   + str(1 - int(data[len(data) - error_pos])) \
                   + data[len(data) - error_pos + 1:]
    return data


data = '101101'
print()
encoded = add_parity_bits(data)
print('encoded: ', encoded)
data2 = encoded[:5] + '0' + encoded[6:]
print('wrong seq', data2)
corrected = correct_errors(data2)
print('correct seq', corrected)
