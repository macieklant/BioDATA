from email.mime import image  #导入streamlit库
import streamlit as st

# 1. 显示标题（这里我用Dola作为示例名字，你可以替换成自己的）
st.title("Dola")

# 2. 显示“About Me”标题
st.header("About Me")

# 3. 添加图片
# 你可以替换为本地图片路径，或者网络图片链接
# 方式一：使用网络图片链接（直接可用）


# 方式二：使用本地图片（把图片和代码放在同一文件夹，写文件名即可）

st.image("wudi.jpg", caption="This is me")

# 4. 使用st.text()显示3个个人信息
st.text("1. I love exploring new technologies and building small projects.")
st.text("2. I enjoy reading books and sharing interesting knowledge.")
st.text("3. I am always curious about the world around me.")

# 5. 显示成功提示信息
st.success("Welcome to my first Streamlit app!")