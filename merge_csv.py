import pandas as pd

data_dev = pd.read_csv("WhatsApp_2_Devansh.csv")
data_rau = pd.read_csv("WhatsApp_2_Raunak.csv")
data_sai = pd.read_csv("WhatsApp_2_Sai.csv")
data_abh = pd.read_csv("WhatsApp_2_Abhav.csv")
data_orig = pd.read_csv("WhatsApp_2.csv")
#data_voted = data_orig.copy(deep=True)

abhav_changes = 0
devansh_changes = 0
sai_changes = 0
raunak_changes = 0

dev_inconsistency = 0
abh_inconsistency = 0
sai_inconsistency = 0
rau_inconsistency = 0

for data in data_orig.axes[0]:
    msg = data_orig.iloc[data]['message']
    msg_dispam_count = 0
    msg_non_dispam_count = 0

    #if data_dev.iloc[data]['message'] == msg:
    if data_dev.iloc[data]['label'] != data_orig.iloc[data]['label']:
        devansh_changes += 1
        if data_dev.iloc[data]['label'] == '1' or data_dev.iloc[data]['label'] == 1:
            msg_non_dispam_count += 1
        elif data_dev.iloc[data]['label'] == '0' or data_dev.iloc[data]['label'] == 0:
            msg_dispam_count += 1
        else:
            print("some other label,dev")
            print(data_dev.iloc[data]['label'])
    # else:
    #     #print("inconsistency in devansh",data_orig.iloc[data]['message'],"and",data_dev.iloc[data]['message'])
    #     dev_inconsistency+=1
    
    #if data_abh.iloc[data]['message'] == msg:
    if data_abh.iloc[data]['label'] != data_orig.iloc[data]['label']:
        abhav_changes += 1
        if data_abh.iloc[data]['label'] == '1' or data_abh.iloc[data]['label'] == 1:
            msg_non_dispam_count += 1
        elif data_abh.iloc[data]['label'] == '0' or data_abh.iloc[data]['label'] == 0:
            msg_dispam_count += 1
        else:
            print("some other label, abhav")
            print(data_abh.iloc[data]['label'])
    
    # else:
    #     #print("inconsistency in abhav",data_orig.iloc[data],"and",data_abh.iloc[data])
    #     abh_inconsistency += 1
        
    #if data_sai.iloc[data]['message'] == msg:
    if data_sai.iloc[data]['label'] != data_orig.iloc[data]['label']:
        sai_changes += 1
        if data_sai.iloc[data]['label'] == '1' or data_sai.iloc[data]['label'] == 1:
            msg_non_dispam_count += 1
        elif data_sai.iloc[data]['label'] == '0' or data_sai.iloc[data]['label'] == 0:
            msg_dispam_count += 1
        else:
            print("some other label,sai")
            print(data_sai.iloc[data]['label'])
    # else:
    #     #print("inconsistency in sai ",data_orig.iloc[data],"and",data_sai.iloc[data])
    #     sai_inconsistency += 1
    
    #if data_rau.iloc[data]['message'] == msg:
    if data_rau.iloc[data]['label'] != data_orig.iloc[data]['label']:
        raunak_changes += 1
        if data_rau.iloc[data]['label'] == '1' or data_rau.iloc[data]['label'] == 1:
            msg_non_dispam_count += 1
        elif data_rau.iloc[data]['label'] == '0' or data_rau.iloc[data]['label'] == 0:
            msg_dispam_count += 1
        else:
            print("some other label,rau")
            print(data_rau.iloc[data]['label'])
    # else:
    #     #print("inconsistency in raunac",data_orig.iloc[data],"and",data_rau.iloc[data])
    #     rau_inconsistency += 1
    
    if msg_dispam_count>=msg_non_dispam_count:
        data_orig.iloc[data]['label'] = 0
    else:
        data_orig.iloc[data]['label'] = 1

data_orig.to_csv("whatsapp_voted.csv")

print(abhav_changes,devansh_changes,sai_changes,raunak_changes)
print(abh_inconsistency,dev_inconsistency,sai_inconsistency,rau_inconsistency)