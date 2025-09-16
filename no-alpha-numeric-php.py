#!/usr/bin/env python3

def generate_php_string_code(input_string):
    """
    输入字符串，输出对应的PHP无字母数字代码
    格式: $_____.=$__; 用于每个字符
    """
    if not input_string:
        return "请输入字符串", ""
    
    base_code = generate_base_code()
    char_codes, clean_char_codes = generate_character_codes(input_string)
    
    full_code = assemble_full_code(base_code, char_codes, input_string)
    clean_code = assemble_clean_code(base_code, clean_char_codes)
    
    return full_code, clean_code

# 新增的独立函数模块
def generate_base_code():
    """生成PHP基础代码框架"""
    return "<?php\n$_=[];$_=@\"$_\";echo($_);\n$__________++;$__________++;$__________++;\n$_=$_[$__________];\n$________;\n\n$_____='';\n"

def generate_char_code(char):
    """生成单个字符的构造代码"""
    if char.isalpha():
        return generate_alpha_code(char)
    elif char.isdigit():  # 新增数字处理分支
        return generate_digit_code(char)
    else:
        return generate_non_alpha_code(char)

def generate_digit_code(char):
    """生成数字字符的递增代码"""
    digit = int(char)
    code = f"// 构造数字 '{char}'\n$__=$________;"
    clean = "$__=$________;"
    
    # 从0开始递增到目标数字
    code += "\n".join(["$__++;"] * digit)
    clean += "".join(["$__++;"] * digit)
    
    code += "\n$_____.=$__;"
    clean += "\n$_____.=$__;"
    return code, clean

def generate_alpha_code(char):
    """生成字母字符的递增代码"""
    base_char = 'a'  # 从a开始
    increment_count = ord(char.lower()) - ord(base_char)
    code = f"// 构造字符 '{char}'\n$__=$_;"
    clean = "$__=$_;"
    
    code += "\n".join(["$__++;"] * increment_count)
    clean += "".join(["$__++;"] * increment_count)
    
    code += "\n$_____.=$__;"
    clean += "\n$_____.=$__;"
    return code, clean

def generate_character_codes(input_string):
    """生成所有字符的构造代码"""
    char_codes = []
    clean_char_codes = []
    
    for char in input_string.upper():
        code, clean = generate_char_code(char)
        char_codes.append(code)
        clean_char_codes.append(clean)
    
    return char_codes, clean_char_codes

def generate_alpha_code(char):
    """生成字母字符的递增代码"""
    increment_count = ord(char) - ord('A')
    code = f"// 构造字符 '{char}'\n$__=$_;"
    clean = "$__=$_;"
    
    code += "\n".join(["$__++;"] * increment_count)
    clean += "".join(["$__++;"] * increment_count)
    
    code += "\n$_____.=$__;"
    clean += "\n$_____.=$__;"
    return code, clean

def generate_non_alpha_code(char):
    """生成非字母字符的代码"""
    code = f"// 直接添加字符 '{char}'\n$_____.='{char}';"
    clean = f"$_____.='{char}';"
    return code, clean

def assemble_full_code(base_code, char_codes, input_string):
    """组装完整带注释的代码"""
    return f"{base_code}\n\n" + "\n\n".join(char_codes) + f"\n\n// 最终字符串: '{input_string.upper()}'\n?>"

def assemble_clean_code(base_code, clean_char_codes):
    """组装清理后的代码"""
    return f"{base_code}\n" + "\n".join(clean_char_codes) + "\n?>"

# 使用示例
if __name__ == "__main__":
    while True:
        text = input("请输入要构造的字符串 (输入q退出): ").strip()
        if text.upper() == 'Q':
            break
        if not text:
            print("请输入字符串")
            continue
        
        code, clean_code = generate_php_string_code(text)
        print(f"\n生成的代码:")
        print(code)
        print("\n" + "="*60)
        print("\n清理注释后的代码 (可直接复制使用):")
        print(clean_code)
        print("\n" + "="*60 + "\n")