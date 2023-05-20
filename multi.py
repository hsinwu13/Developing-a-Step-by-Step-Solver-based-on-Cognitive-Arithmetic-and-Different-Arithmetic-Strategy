# 乘法注意力權重 加法(1)、乘法(1)、尾數0加總(1)、0次方~20次方(0)
# 將輸入的各位數數字轉成list儲存
def num_int_list(num):
    num_list = list(map(int, str(num)))
    num_list.reverse()

    return num_list

# 將兩個數字的乘積以及進位，轉成list儲存
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

# 計算乘法
def calculate(a, b):
    # 儲存a, b, ans的數字列表
    a_int_list = num_int_list(a)
    b_int_list = num_int_list(b)
    ans_int_list = num_int_list(a * b)

    # 處理進位
    product_int_list = carry_list(a_int_list, b_int_list)

    return a_int_list, b_int_list, ans_int_list, product_int_list

# 用''把字串列表補足位數
def fill(num_str_list, max_len):
    for i in range(max_len - len(num_str_list)):
        num_str_list.append('')

    num_str_list.reverse()

    return num_str_list

# 將各位數數字、乘積、進位，轉成字串型態的list儲存
def calculate_str(a, b):
    a_int_list, b_int_list, ans_int_list, product_int_list = calculate(a, b)

    a_str_list = list(map(str, a_int_list))
    b_str_list = list(map(str, b_int_list))
    ans_str_list = list(map(str, ans_int_list))
    product_str_list = list(map(str, product_int_list))

    # 紀錄各組數字位數
    a_len = len(a_str_list)
    b_len = len(b_str_list)
    ans_len = len(ans_str_list)

    max_len = max(a_len, b_len, ans_len)

    a_str_list = fill(a_str_list, max_len)
    b_str_list = fill(b_str_list, max_len)
    ans_str_list = fill(ans_str_list, max_len)

    # 計算中間紀錄的列表
    intermediate_records = []
    for i in range(b_len):
        record = [''] * (max_len + i + 1)
        for j in range(a_len):
            product = b_int_list[i] * a_int_list[j]
            record[j + i] = str(product % 10)
            record[j + i + 1] = str(product // 10)
        record.reverse()
        intermediate_records.append(record)

    intermediate_records.reverse()

    return a_str_list, b_str_list, ans_str_list, intermediate_records, product_str_list, max_len


if __name__ == '__main__':
    a_str_list, b_str_list, ans_str_list, intermediate_records, product_str_list, max_len= calculate_str(913, 25)
    print(a_str_list, b_str_list, ans_str_list, intermediate_records, product_str_list, max_len)
