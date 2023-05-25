def lz77_encode(text):
    encoded = []
    window_size = 10
    lookahead_buffer_size = 5

    i = 0
    while i < len(text):
        search_buffer = text[max(0, i - window_size):i]
        lookahead_buffer = text[i:i + lookahead_buffer_size]

        match_length = 0
        match_distance = 0

        if lookahead_buffer:
            max_match_length = 0
            max_match_distance = 0

            for j in range(1, min(len(lookahead_buffer) + 1, window_size + 1)):
                pattern = lookahead_buffer[:j]
                match_index = search_buffer.rfind(pattern)

                if match_index != -1 and i - match_index <= window_size:
                    current_match_length = len(pattern)
                    current_match_distance = i - match_index

                    if current_match_length > max_match_length:
                        max_match_length = current_match_length
                        max_match_distance = current_match_distance

            match_length = max_match_length
            match_distance = max_match_distance

        encoded.append((match_distance, match_length,
                        lookahead_buffer[match_length] if match_length > 0 else lookahead_buffer[0]))
        i += match_length + 1

    return encoded


def lz77_decode(encoded_text):
    decoded = ""

    for token in encoded_text:
        match_distance, match_length, next_char = token

        if match_length == 0:
            decoded += next_char
        else:
            start_index = len(decoded) - match_distance
            for _ in range(match_length):
                decoded += decoded[start_index]
                start_index += 1

            decoded += next_char

    return decoded


text = "abbabaabbaa"
encoded_text = lz77_encode(text)

decoded_text = lz77_decode([ (0,0,'a'),(0,0,'b'),(2,1,'a'),(3,2,'b'),(0,0,'a')])
print(encoded_text)
print(decoded_text)
