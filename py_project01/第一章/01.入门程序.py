# print("Hello World")
# print("Hello Python")
# print("-------------------")
def generate_gray_code(n):
    """
    使用分治法生成 n 位格雷码
    :param n: 格雷码的位数
    :return: 包含 n 位格雷码的列表
    """
    # 1. 边界条件（递归出口）：当 n=1 时，格雷码为 ['0', '1']
    if n == 1:
        return ['0', '1']

    # 2. 分治：递归获取 n-1 位的格雷码
    prev_gray = generate_gray_code(n - 1)

    # 3. 合并：
    # a. 前半部分：给 n-1 位格雷码前加 '0'
    first_half = ['0' + code for code in prev_gray]

    # b. 后半部分：将 n-1 位格雷码逆序，并在前面加 '1'
    second_half = ['1' + code for code in reversed(prev_gray)]

    # 4. 拼接结果
    return first_half + second_half


# 测试代码
if __name__ == "__main__":
    n = 3
    result = generate_gray_code(n)
    print(f"{n} 位格雷码序列：")
    for code in result:
        print(code)