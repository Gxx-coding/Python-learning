import streamlit as st


#大标题
st.title("Streamlit入门演示")
st.header("Streamlit一级标题")
st.subheader("Streamlit一级标题")
# 段落文字
st.write("布偶猫。被誉为“猫中仙女”，以其优雅的外表和温顺的性格成为最受欢迎的宠物猫之一。")
st.write("它们体型较大，成年后可达10-20斤，拥有深邃的蓝色眼眸和柔顺的中长毛，毛色多为双色、手套色或重点色，宛如戴着一副可爱的面具。最迷人的是其松弛柔软的体态，当你抱起它时，它会像布偶一样全身放松，信赖地偎依在主人怀中，“布偶”之名便由此而来。")
st.write("性格是布偶猫最大的魅力。它们极度温顺、安静且粘人，被称为“小狗猫”，喜欢跟随主人走动，享受陪伴。它们通常脾气极好，忍耐力强，能与儿童和其他宠物友好相处，是理想的家庭伴侣。其轻柔的叫声和爱撒娇的天性，能带给主人无尽的温暖与治愈。")
st.write("养护方面，需要定期梳理其丰厚毛发以防止打结，并提供足够的关注与互动。拥有一只布偶猫，就如同拥有了一位温柔优雅、终生依恋的毛茸茸家人。")
# 图片
st.image("resources/cat.png")
st.image("./resources/微信图片_20240912120122.jpg", width = 300)
# 音频
st.audio("./resources/康神开播了_爱给网_aigei_com.mp3")
# 视频
st.video("./resources/美丽的海上日出_爱给网_aigei_com.mp4")
#Logo
st.logo("./resources/logo.jpg")