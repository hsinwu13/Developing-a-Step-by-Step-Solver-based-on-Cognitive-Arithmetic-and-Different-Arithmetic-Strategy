# 乘法注意力权重 加法(1)、乘法(1)、尾数0加总(1)、0次方~20次方(0)
# 将输入的各位数字转成list储存
def num_int_list(num):
    num_list = list(map(int, str(num)))
    num_list.reverse()

    return num_list

# 将两个数字的乘积以及进位，转成list储存
def carry_list(list1, list2):
    product_list = [0] * (len(list1) + len(list2))

    for i in range(len(list1)):
        carry = 0
        for j in range(len(list2)):
            product = list1[i] * list2[j] + product_list[i + j] + carry
            product_list[i + j] = product % 10
            carry = product // 10
        product_list[i + len(list2)] = carry

    product_list.reverse()

    return product_list

# 计算乘法
def calculate(a, b):
    # 储存a, b, ans的数字列表
    a_int_list = num_int_list(a)
    b_int_list = num_int_list(b)
    ans_int_list = num_int_list(a * b)

    # 处理进位
    product_int_list = carry_list(a_int_list, b_int_list)

    return a_int_list, b_int_list, ans_int_list, product_int_list

# 用''把字符串列表补足位数
def fill(num_str_list, max_len):
    for i in range(max_len - len(num_str_list)):
        num_str_list.append('')

    num_str_list.reverse()

    return num_str_list

# 将各位数数字、乘积、进位，转成字符串型态的list储存
def calculate_str(a, b):
    a_int_list, b_int_list, ans_int_list, product_int_list = calculate(a, b)

    a_str_list = list(map(str, a_int_list))
    b_str_list = list(map(str, b_int_list))
    ans_str_list = list(map(str, ans_int_list))
    product_str_list = list(map(str, product_int_list))

    # 记录各组数字位数
    a_len = len(a_str_list)
    b_len = len(b_str_list)
    ans_len = len(ans_str_list)

    max_len = max(a_len, b_len, ans_len)

    a_str_list = fill(a_str_list, max_len)
    b_str_list = fill(b_str_list, max_len)
    ans_str_list = fill(ans_str_list, max_len)

    return a_str_list, b_str_list, ans_str_list, product_str_list, max_len


if __name__ == '__main__':
    a_str_list, b_str_list, ans_str_list, product_str_list, max_len = calculate_str(913, 25)

    for i in range(max_len):
        line = f"{a_str_list[i]} × {b_str_list[i]} = {product_str_list[i]}"
        print(line)

    print("-------")

    ans_line = " " * (max_len - len(ans_str_list)) + "".join(ans_str_list)
    print(ans_line)
