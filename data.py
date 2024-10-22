import pandas as pd

# 步驟 1: 讀取 CSV 檔案
df = pd.read_csv('sample_10_percent.csv')  # 修改 'your_data.csv' 為您的檔案名稱

# 步驟 2: 拆分 MBTI 欄位並創建新列
df['mbti_EI'] = df['mbti'].apply(lambda x: 'E' if 'E' in x else 'I')
df['mbti_NS'] = df['mbti'].apply(lambda x: 'N' if 'N' in x else 'S')
df['mbti_TF'] = df['mbti'].apply(lambda x: 'T' if 'T' in x else 'F')
df['mbti_PJ'] = df['mbti'].apply(lambda x: 'P' if 'P' in x else 'J')

# 步驟 3: 更新 MBTI 欄位並保存數據為不同的檔案
#df['mbti_EI'] = df['E_I']
#df['mbti_NS'] = df['N_S']
#df['mbti_TF'] = df['T_F']
#df['mbti_PJ'] = df['P_J']

# 每個維度保存一個文件
df.to_csv('sample_10_precent_EI.csv', index=False, columns=['mbti_EI'] + list(df.columns[1:-4]))
df.to_csv('sample_10_precent_NS.csv', index=False, columns=['mbti_NS'] + list(df.columns[1:-4]))
df.to_csv('sample_10_precent_TF.csv', index=False, columns=['mbti_TF'] + list(df.columns[1:-4]))
df.to_csv('sample_10_precent_PJ.csv', index=False, columns=['mbti_PJ'] + list(df.columns[1:-4]))

print("檔案已保存。")
