import streamlit as st

# 设置页面标题
st.set_page_config(page_title="抑郁症自助检测", page_icon=":guardsman:", layout="wide")

# 定义问卷题目和选项
questions = [
    {"question": "1.抑郁心境", "options": ["没有", "仅在询问时承认", "自发地口述", "面部表情和行为均可察觉", "完全明显"]},
    {"question": "2.有罪感", "options": ["没有", "自责,觉得给别人添麻烦", "为过去的错误行为而自责", "现在的病是一种惩罚,有被惩罚感", "有罪妄想或被控妄想"]},
    {"question": "3.自杀", "options": ["没有", "感到生活不值得继续", "希望自己已经死了,或有轻生的想法", "有自杀企图", "企图自杀"]},
    {"question": "4.入睡困难", "options": ["没有困难", "有时困难", "每晚困难"]},
    {"question": "5.睡眠不深", "options": ["没有", "睡眠不安", "夜间易醒", "醒后难以再入睡"]},
    {"question": "6.早醒", "options": ["没有", "偶尔早醒", "经常早醒"]},
    {"question": "7.工作和兴趣", "options": ["没有困难", "感到乏味、兴趣不大", "兴趣明显减退", "丧失兴趣"]},
    {"question": "8.阻滞", "options": ["思维和语言正常", "交谈时感到困难", "交谈明显困难", "交谈极其困难"]},
    {"question": "9.激越", "options": ["没有", "有些烦躁不安", "身体动作频繁", "扭动不停"]},
    {"question": "10.精神性焦虑", "options": ["没有", "主观紧张感", "过分关心小事", "表现出忧虑、恐惧或惊恐"]},
    {"question": "11.躯体性焦虑", "options": ["没有", "轻度", "中度", "重度"]},
    {"question": "12.胃肠道症状", "options": ["没有", "食欲不振", "需要勉强自己进食", "需要别人劝导或强迫才能进食"]},
    {"question": "13.全身症状", "options": ["没有", "感到身体沉重", "肢体酸痛", "明显的疲乏无力"]},
    {"question": "14.性症状", "options": ["没有", "性欲轻度减退", "性欲明显减退"]},
    {"question": "15.疑病", "options": ["没有", "自身体健康过分关心", "对自身健康存在种种顾虑", "坚持认为自己有严重的疾病"]},
    {"question": "16.体重减轻", "options": ["没有", "可能有体重减轻", "明显体重减轻"]},
    {"question": "17.自知力", "options": ["认识到自己有抑郁症", "认识到自己有病,将其归因于饮食、气候、过度工作、病毒感染、需要休息等", "完全否认自己有病"]}
]

# 定义每一题的得分规则
scoring_rules = {
    "1.抑郁心境": [0, 1, 2, 3, 4],
    "2.有罪感": [0, 1, 2, 3, 4],
    "3.自杀": [0, 1, 2, 3, 4],
    "4.入睡困难": [0, 1, 2],
    "5.睡眠不深": [0, 1, 2, 3],
    "6.早醒": [0, 1, 2],
    "7.工作和兴趣": [0, 1, 2, 3],
    "8.阻滞": [0, 1, 2, 3],
    "9.激越": [0, 1, 2, 3],
    "10.精神性焦虑": [0, 1, 2, 3],
    "11.躯体性焦虑": [0, 1, 2, 3],
    "12.胃肠道症状": [0, 1, 2, 3],
    "13.全身症状": [0, 1, 2, 3],
    "14.性症状": [0, 1, 2],
    "15.疑病": [0, 1, 2, 3],
    "16.体重减轻": [0, 1, 2],
    "17.自知力": [0, 1, 2]
}

# 定义函数来计算总分
def calculate_score(responses):
    total_score = 0
    for question, response in responses.items():
        total_score += scoring_rules[question][response]
    return total_score

# Streamlit应用
def main():
    #st.title("抑郁症自助检测")
    st.markdown("<h2 style='color: #F63366;'>抑郁症自助检测</h2>", unsafe_allow_html=True)
    
    # 添加对汉密尔顿抑郁量表的介绍
    st.caption("""
    #### 关于汉密尔顿抑郁量表
    汉密尔顿抑郁量表(Hamilton Depression Rating Scale,简称HAMD)是由马克斯·汉密尔顿于1960年编制的,是临床上最常用的抑郁症严重程度评定量表之一。该量表主要通过询问患者的主观感受,结合临床观察作出评定,以评估抑郁症状的性质和严重程度。
    HAMD包含17个题目,分别评估抑郁心境、有罪感、自杀、入睡困难、睡眠不深、早醒、工作和兴趣、阻滞、激越、精神性焦虑、躯体性焦虑、胃肠道症状、全身症状、性症状、疑病、体重减轻和自知力等。每个题目根据严重程度评分,总分为0-52分。得分越高,表明抑郁症状越严重。
    """)
    
    #st.write("请根据您最近一周的状态如实回答以下问题,帮助评估您的抑郁状况:")
    st.markdown("<h6 style='color: #F63366;'>请根据您最近一周的状态如实回答以下问题,帮助评估您的抑郁状况:</h6>", unsafe_allow_html=True)
    
    # 显示每个问题并记录用户的回答
    responses = {}
    for i, q in enumerate(questions):
        question = q["question"]
        options = q["options"]
        response = st.radio(f"{i+1}. {question}", options)
        responses[question] = options.index(response)
    
    # 计算总分并显示结果
    if st.button("提交"):
        score = calculate_score(responses)
        st.write(f"你的汉密尔顿抑郁量表得分为: {score}")
        
        if score <= 7:
            st.write("你没有抑郁症状")
        elif score <= 17:
            st.write("你可能有轻度抑郁")
        elif score <= 24:
            st.write("你可能有中度抑郁")
        else:
            st.write("你可能有严重抑郁,建议及时就医")
        
        st.caption("请注意,这只是初步筛查结果,不能作为诊断依据。如果您的得分较高或有严重的抑郁倾向,建议您去医院进行进一步的专业评估和诊断。")

if __name__ == "__main__":
    main()
