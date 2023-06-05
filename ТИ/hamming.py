def hamming_coding(bit_message):
    from math import log

    msg_length = len(bit_message)
    control_bits = int(log(msg_length, 2)) + 1

    for control_bit in range(control_bits - 1, -1, -1):
        appereance = 2 ** control_bit - control_bit - 1 - 1

        # fix
        if appereance == -1:
            sm = 0
            for shift in range(1, 2 ** control_bit):
                sm += int(bit_message[appereance + shift])
            appereance += 2 ** (control_bit + 1)
        else:
            sm = - int(bit_message[appereance])
        #

        for shift in range(0, 2 ** control_bit):
            # bug
            for bit in bit_message[appereance + shift:msg_length:2 ** (control_bit + 1)]:
                sm += int(bit)
        # fix
        appereance = 2 ** control_bit - control_bit - 1 - 1
        #
        bit_message = bit_message[:appereance + 1] + str(sm % 2) + bit_message[appereance + 1:]
        msg_length += 1

    return bit_message


print(hamming_coding("1110"))
