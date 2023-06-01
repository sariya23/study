def lz77_encode(input_string):
    dictionary = ""
    encoded_data = []
    i = 0
    while i < len(input_string):
        longest_match_length = 0
        longest_match_distance = 0
        for j in range(1, len(dictionary) + 1):
            if input_string[i:i + j] in dictionary:
                longest_match_length = j
                longest_match_distance = len(dictionary) - dictionary.index(input_string[i:i + j])
        if i + longest_match_length < len(input_string):
            encoded_data.append((longest_match_distance, longest_match_length, input_string[i + longest_match_length]))
        else:
            encoded_data.append((longest_match_distance, longest_match_length, ""))
        dictionary += input_string[i:i + longest_match_length + 1]
        i += longest_match_length + 1
    return encoded_data
def decode_LZ77(encoded_list):
    text = ''
    for item in encoded_list:
        if item[0] == 0 and item[1] == 0:
            text += item[2]
        else:
            start = max(len(text) - item[0], 0)
            for j in range(item[1]):
                text += text[start + j]
            text += item[2]
    return text
input_string = "abbabaabbaa"
encoded_data = lz77_encode(input_string)
print(encoded_data)
print(decode_LZ77([(0, 0, 'a'), (0, 0, 'b'), (1, 1, 'a'), (2, 2, 'a'), (6, 3, 'a')]))
print(decode_LZ77([(0, 0, 'a'), (0, 0, 'b'), (2, 1, 'a'), (3, 2, 'b'), (0, 0, 'a')]))
