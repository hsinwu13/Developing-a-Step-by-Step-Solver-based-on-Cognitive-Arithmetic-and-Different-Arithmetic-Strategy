# 減法注意力權重 借位(1)、相減(1)、N-N直接照抄(0)、N-0直接照抄(0)
# 將輸入的各位數數字轉成list儲存
def num_int_list(num):
    num_list = list(map(int, str(num)))
    num_list.reverse()
    
    return num_list

# 將各位數的diff、借位，轉成list儲存
def borrow_list(list1, list2):
    diff_int_list = []
    borrow_int_list = [0]

    if len(list1) < len(list2):
        list1, list2 = list2, list1

    for i in range(len(list2)):
        diff_int_list.append(list1[i] - list2[i] - borrow_int_list[i])
        borrow_int_list.append({True: 1, False: 0}[diff_int_list[i] < 0])
        
    for i in range(len(list2), len(list1)):
        diff_int_list.append(list1[i] - borrow_int_list[i])
        borrow_int_list.append({True: 1, False: 0}[diff_int_list[i] < 0])

    borrow_int_list.append(borrow_int_list.pop(0))

    return borrow_int_list

# 計算減法
def calculate_subtraction(a, b):    
    # 儲存a, b, diff的數字列表
    a_int_list = num_int_list(a)
    b_int_list = num_int_list(b)
    diff_int_list = num_int_list(a - b)

    # 處理借位
    borrow_int_list = borrow_list(a_int_list, b_int_list)

    return a_int_list, b_int_list, diff_int_list, borrow_int_list

# 用''把字串列表補足位數
def fill(num_str_list, max_len):
    for i in range(max_len - len(num_str_list)):
        num_str_list.append('')

    num_str_list.reverse()

    return num_str_list

# 將各位數數字、差值(含借位)、借位，轉成字串型態的list儲存
def calculate_subtraction_str(a, b):
    # 設定weight
    borrow_sub = 1
    sub = 1
    NsubN = 0.5
    Nsub0 = 0
    
    a_int_list, b_int_list, diff_int_list, borrow_int_list = calculate_subtraction(a, b)

    a_str_list = list(map(str, a_int_list))
    b_str_list = list(map(str, b_int_list))
    diff_str_list = list(map(str, diff_int_list))
    borrow_str_list = list(map(str, borrow_int_list))

    # 紀錄各組數字位數
    a_len = len(a_str_list)
    b_len = len(b_str_list)
    diff_len = len(diff_str_list)

    max_len = max(a_len, b_len, diff_len)

    a_str_list = fill(a_str_list, max_len)
    b_str_list = fill(b_str_list, max_len)
    diff_str_list = fill(diff_str_list, max_len)
    
    # 借位
    borrow = borrow_str_list.count('1') * borrow_sub
    # 無借位減法(還包含N-N及N-0)
    noborrow = (borrow_str_list.count('0') - 1) * sub
    # N-N
    subN = 0
    for i in range(max_len):
        subN += (a_str_list[i] == b_str_list[i])
    # N-0
    sub0 = 0
    for i in range(max_len):
        sub0 += (b_str_list[i] == '' or b_str_list[i] == '0')
    
    f_weight = borrow + noborrow - subN * NsubN - sub0
    print("借位: ", borrow)
    print("無借位減法(尚包含N-N與N-0): ", noborrow)
    print("N-N: ", subN * NsubN)
    print("N-0: ", Nsub0)
    print("減法隱含操作量: ", f_weight)
    
    return a_str_list, b_str_list, diff_str_list, borrow_str_list, max_len, f_weight
    
if __name__ == '__main__':
    a_str_list, b_str_list, diff_str_list, borrow_str_list, max_len, f_weight = calculate_subtraction_str(998, 9)
    print(a_str_list, b_str_list, diff_str_list, borrow_str_list, max_len, f_weight)
    print(type(a_str_list[0]))
