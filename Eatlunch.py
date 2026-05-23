import streamlit as st

# 设置页面标题
st.title("📝 小测验")

# 题目1
st.subheader("问题 1")
q1 = "Python 中用于定义函数的关键字是？"
options1 = ["class", "def", "function", "define"]
ans1 = "def"
user_ans1 = st.radio(q1, options1, index=None)
st.divider()  # 分隔线

# 题目2
st.subheader("问题 2")
q2 = "以下哪个是 Streamlit 中用于显示标题的函数？"
options2 = ["st.header()", "st.title()", "st.text()", "st.markdown()"]
ans2 = "st.title()"
user_ans2 = st.radio(q2, options2, index=None)
st.divider()  # 分隔线

# 题目3
st.subheader("问题 3")
q3 = "3 + 5 * 2 的运算结果是？"
options3 = ["16", "13", "10", "8"]
ans3 = "13"
user_ans3 = st.radio(q3, options3, index=None)
st.divider()  # 分隔线

# 提交按钮
if st.button("📤 提交答案"):
    score = 0  # 初始化分数

    # 检查第一题
    st.subheader("✅ 第1题结果")
    if user_ans1 == ans1:
        st.success("回答正确！")
        score += 1
    else:
        st.error(f"回答错误，正确答案是：{ans1}")

    # 检查第二题
    st.subheader("✅ 第2题结果")
    if user_ans2 == ans2:
        st.success("回答正确！")
        score += 1
    else:
        st.error(f"回答错误，正确答案是：{ans2}")

    # 检查第三题
    st.subheader("✅ 第3题结果")
    if user_ans3 == ans3:
        st.success("回答正确！")
        score += 1
    else:
        st.error(f"回答错误，正确答案是：{ans3}")

    # 显示总分
    st.header(f"🏆 你的总分：{score} / 3")
    if score == 3:
        st.balloons()  # 满分特效
        st.success("太棒了，全部答对！")
    elif score >= 2:
        st.info("很不错，继续加油！")
    else:
        st.warning("还需要努力哦，再复习一下吧！")