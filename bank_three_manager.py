SEED_SIZE = 16
MODULUS = 36389
GENERATOR = 1500
manager1 = []
manager2 = []
manager3 = []



def get_msg_len(msg):
    return int(SEED_SIZE*(len(msg)/2))



def function_H(first_half, second_half, g):
    mod_exp = bin(pow(g, int(first_half, 2), MODULUS)).replace('0b', '').zfill(SEED_SIZE)
    hard_core_bit = 0
    for i in range(len(first_half)):
        hard_core_bit = (hard_core_bit ^ (int(first_half[i]) & int(second_half[i]))) % 2
    return mod_exp + second_half + str(hard_core_bit)


def function_G(initial_seed, g, msg):
    binary_string = initial_seed
    result = ''
    for i in range(get_msg_len(msg)):
        first_half = binary_string[:int(len(binary_string)/2)]
        second_half = binary_string[int(len(binary_string)/2):]
        binary_string = function_H(first_half, second_half, g)
        result += binary_string[-1]
        binary_string = binary_string[:-1]
    return result


def my_xor(bin_txt, bin_pad):
    return ''.join([str(int(_a) ^ int(_b)) for _a, _b in zip(bin_txt, bin_pad)])

'''
def managers(one_m, tow_m):  # return the key
    if one_m == 1:
        if tow_m == 2:
            return my_xor(manager1[0], manager2[0])
        else:         # tow =3
            return my_xor(manager1[1], manager3[0])
    elif one_m == 2:
        if tow_m == 1:
            return my_xor(manager1[0], manager2[0])
        else:         # tow =3
            return my_xor(manager2[1], manager3[0])
    else:             # one = 3
        if tow_m == 2:
            return my_xor(manager2[1], manager3[0])
        else:         # tow = 1
            return my_xor(manager1[1], manager3[0])
'''

'''
def create_parts(k, g):
    print('k: ', k)
    k1 = function_G('0111100110110010', g)
    g = g - 1
    k2 = function_G('0111100110110010', g)
    k1t = my_xor(k, k1)
    print('k1: ', k1)
    print('k1t: ', k1t)
    k2t = my_xor(k, k2)
    print('k2: ', k2)
    print('k2t: ', k2t)
    #print('k1 ^ k1t', my_xor(k1t, k1))
    #print('k2 ^ k2t', my_xor(k2t, k2))
    manager1.append(k1)
    manager1.append(k2)
    manager2.append(k1t)
    manager2.append(k2)
    manager3.append(k2t)
'''


k = function_G('0111100110110010', GENERATOR, 'aba')
print(k)
k = function_G('0111100110110010', GENERATOR-1, 'aba')
print(k)
#create_parts(k, GENERATOR-1)

#print(f'we choose m1 and m3 and the key is: {managers(1, 3)}')
