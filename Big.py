import streamlit as st

# 设置页面标题
st.title("🧮 简易计算器")

# 输入两个数字
num1 = st.number_input("请输入第一个数字", value=0.0, step=0.1)
num2 = st.number_input("请输入第二个数字", value=0.0, step=0.1)

# 选择运算方式
operation = st.selectbox(
    "请选择运算方式",
    ["加法", "减法", "乘法", "除法"]
)

# 计算按钮
if st.button("计算"):
    # 执行运算逻辑
    if operation == "加法":
        result = num1 + num2
        st.success(f"计算结果：{num1} + {num2} = {result}")
    elif operation == "减法":
        result = num1 - num2
        st.success(f"计算结果：{num1} - {num2} = {result}")
    elif operation == "乘法":
        result = num1 * num2
        st.success(f"计算结果：{num1} × {num2} = {result}")
    elif operation == "除法":
        if num2 == 0:
            # 除零错误提示
            st.error("错误：除数不能为零，请重新输入第二个数字！")
        else:
            result = num1 / num2
            st.success(f"计算结果：{num1} ÷ {num2} = {result}")