import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

MBTI_FILE_NAME = "MBTI.csv"
MBTI_COMPATIBILITY_TABLE_FILE_NAME = "MBTI 궁합표.csv"
FONT_PATH = "C:\Windows\Fonts/gulim.ttc"

font = font_manager.FontProperties(fname=FONT_PATH).get_name()
rc('font', family=font)

MBTI = pd.read_csv(MBTI_FILE_NAME)
MBTI_COMPATIBILITY = pd.read_csv(MBTI_COMPATIBILITY_TABLE_FILE_NAME)

MBTI_COMPATIBILITY_KOR = ['매우 안 좋음', '안 좋음', '보통', '좋음', '매우 좋음']

MBTI_COMPATIBILITY_ROW = MBTI_COMPATIBILITY['MBTI'].tolist()

data = []

def GetMBTICompatibility(mbti1:str, mbti2:str):
    return MBTI_COMPATIBILITY[mbti1].iloc[MBTI_COMPATIBILITY_ROW.index(mbti2)]

for i in MBTI.index:
    MBTI_ROW_COMPATIBILITY = []
    for x in MBTI.index:
        print("analyzing " + MBTI.iloc[i]['이름'] + "(" + MBTI.iloc[i]['MBTI'] + ") with " + MBTI.iloc[x]['이름'] + "(" + MBTI.iloc[x]['MBTI'] + ")")
        result = GetMBTICompatibility(MBTI.iloc[i]['MBTI'], MBTI.iloc[x]['MBTI'])
        print("result " + str(result))
        MBTI_ROW_COMPATIBILITY.append(MBTI_COMPATIBILITY_KOR[result - 1])
    data.append(MBTI_ROW_COMPATIBILITY)

fig, ax =plt.subplots(1,1)
ax.axis('off')
table = ax.table(cellText=data, colLabels=MBTI['이름'],rowLabels=MBTI['이름'],loc="center")

plt.title(label='MBTI 관계표', fontsize=20)

plt.savefig('MBTI 관계표', dpi=300)