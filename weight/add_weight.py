# 加法注意力權重 進位加法(1.5)、無進位加法(1) 、N+0直接照抄(0)

# 將輸入的各位數數字轉成list儲存
def num_int_list(num):
    num_list=list(map(int,str(num)))
    num_list.reverse()
    
    return num_list

# 將各位數的加總(含進位)、進位，轉成list儲存
def carry_list(list1, list2):
    sum_int_list=[]
    carry_int_list=[0]

    if len(list1) < len(list2):
        list1, list2 = list2, list1

    for i in range(len(list2)):
        sum_int_list.append(list1[i]+list2[i]+carry_int_list[i])
        carry_int_list.append({True:1,False:0}[sum_int_list[i]>=10])
        
    for i in range(len(list2),len(list1)):
        sum_int_list.append(list1[i]+carry_int_list[i])
        carry_int_list.append({True:1,False:0}[sum_int_list[i]>=10])

    carry_int_list.append(carry_int_list.pop(0))

    return carry_int_list

# 計算加法
def calculate(a, b):
    
    # 儲存a,b,ans的數字列表
    a_int_list = num_int_list(a)
    b_int_list = num_int_list(b)
    ans_int_list = num_int_list(a+b)

    # 處理進位
    carry_int_list = carry_list(a_int_list, b_int_list)

    return a_int_list, b_int_list, ans_int_list, carry_int_list

# 用''把字串列表補足位數
def fill(num_str_list, max_len):
    for i in range(max_len-len(num_str_list)):
        num_str_list.append('')

    num_str_list.reverse()

    return num_str_list

# 將各位數數字、加總(含進位)、進位，轉成字串型態的list儲存
def calculate_str(a, b):
    # 設定weight
    carry_add = 1.5
    nocarry_add = 1
    Nadd0 = 0
    
    a_int_list, b_int_list, ans_int_list, carry_int_list = calculate(a,b)

    a_str_list = list(map(str,a_int_list))
    b_str_list = list(map(str,b_int_list))
    ans_str_list = list(map(str,ans_int_list))
    carry_str_list = list(map(str,carry_int_list))
    
    # 紀錄各組數字位數
    a_len = len(a_str_list)
    b_len = len(b_str_list)
    ans_len = len(ans_str_list)
    
    max_len = max(a_len, b_len, ans_len)
    
    a_str_list = fill(a_str_list, max_len)
    b_str_list = fill(b_str_list, max_len)
    ans_str_list = fill(ans_str_list, max_len)
    
    # 計算加法注意力權重
    # 進位加法(1.5) 
    carry = carry_str_list.count('1') * carry_add 
    # 無進位加法(1)，此處尚包含N+0
    nocarry = (carry_str_list.count('0') - 1) * nocarry_add
    # N+0直接照抄(0)
    nadd0 = 0
    if max_len == len(carry_str_list):
        for i in range(max_len):
            if(carry_str_list[i] == '0'):
                nadd0 += (a_str_list[i] == '0' or a_str_list[i] == '')
                nadd0 += (b_str_list[i] == '0' or b_str_list[i] == '')
                nadd0 -= ((a_str_list[i] == '0' or a_str_list[i] == '') and (b_str_list[i] == '0' or b_str_list[i] == ''))

    if max_len != len(carry_str_list):
        for i in range(max_len):
            if(carry_str_list[i+1] == '0'):
                nadd0 += (a_str_list[i] == '0' or a_str_list[i] == '')
                nadd0 += (b_str_list[i] == '0' or b_str_list[i] == '')
                nadd0 -= ((a_str_list[i] == '0' or a_str_list[i] == '') and (b_str_list[i] == '0' or b_str_list[i] == ''))
           
    f_weight = carry + nocarry - nadd0
    
    print("進位加法: ", carry)
    print("無近位加法(尚包含N+0): ", nocarry)
    print("N+0直接照抄: ", nadd0)
    print("加法注意力權重: ", f_weight)
    return a_str_list, b_str_list, ans_str_list, carry_str_list, max_len, f_weight
    
if __name__ == '__main__':
    a_str_list, b_str_list, ans_str_list, carry_str_list, max_len, f_weight = calculate_str(999,5)
    print(a_str_list, b_str_list, ans_str_list, carry_str_list, max_len, f_weight)
