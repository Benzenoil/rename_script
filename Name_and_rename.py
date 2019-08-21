#!/usr/bin/env python
# coding: utf-8

# In[169]:


import glob
import os
import pandas as pd
import numpy as np

focus_sentense_dir = '../Untitled Folder/name_and_rename/F/ID-csv.xlsx'
shigeki_dir = '../Untitled Folder/name_and_rename/F/shigeki.xlsx'

# root = "../Untitled Folder/name_and_rename/temp-1/"
# files = glob.glob("../Untitled Folder/name_and_rename/temp-1/*.csv")
# files.sort(key=os.path.getmtime)
# print("\n".join(files))


# In[166]:


focus_to_senid = pd.read_excel(focus_sentense_dir)
print(focus_to_senid.head())


# In[167]:


dict_content_id = dict(zip(focus_to_senid['sentense_content'].tolist(), focus_to_senid['sentense_id'].tolist()))


# In[168]:


dict_content_focus = dict(zip(focus_to_senid['sentense_content'].tolist(), focus_to_senid['focus'].tolist()))


# In[193]:


def convert_noduplite(before):
    after=[]
    for item in before:
        if item not in after:
            after.append(item)
        else:
            after.append(item + '2')
    return after

def create_label(sentense_list):
    label=[]
    for item in sentense_list:
        target = dict_content_id.get(item, None)
        if target:
            label.append(target)
        else:
            label.append('NAN')
    return label

def create_focus(sentense_list):
    label_focus = []
    for item in sentense_list:
        target = dict_content_focus.get(item, None)
        if target:
            label_focus.append(target)
        else:
            label_focus.append('NAN')
    return label_focus


# In[194]:


shigeki = pd.read_excel(shigeki_dir, index_col=0)

target_1 = shigeki['list1'].tolist()
target_2 = shigeki['list2'].tolist()
target_3 = shigeki['list3'].tolist()
        
target_1_new = convert_noduplite(before=target_1)
target_2_new = convert_noduplite(before=target_2)
target_3_new = convert_noduplite(before=target_3)

# print(target_1_new)
# print(target_2_new)
# print(target_3_new)


# In[188]:


print(len(target_1))
print(len(target_1_new))


# In[195]:


label_1 = create_label(target_1_new)
label_2 = create_label(target_2_new)
label_3 = create_label(target_3_new)


# In[192]:


print(len(label_1))
print(len(target_1_new))


# In[197]:


label_focus_1 = create_focus(target_1_new)
label_focus_2 = create_focus(target_2_new)
label_focus_3 = create_focus(target_3_new)


# In[199]:


print(label_focus_1)
print(label_focus_2)
print(label_focus_3)


# In[200]:


df_1 = pd.DataFrame(list(zip(label_focus_1, target_1_new, label_1)), 
               columns =['focus', 'sentense_name', 'sentense_id'])

df_2 = pd.DataFrame(list(zip(label_focus_2, target_2_new, label_2)), 
               columns =['focus', 'sentense_name', 'sentense_id'])

df_3 = pd.DataFrame(list(zip(label_focus_3, target_3_new, label_3)), 
               columns =['focus', 'sentense_name', 'sentense_id'])


# In[203]:


print(df_1.head())
print(df_2.head())
print(df_3.head())


# In[204]:


df_1.to_csv('mode_1.csv')
df_2.to_csv('mode_2.csv')
df_3.to_csv('mode_3.csv')


# In[164]:


# df_bk = pd.read_csv('backup.csv', index_col=0)
# print(df_bk.head())


# In[ ]:


# for a,b in zip(id_['attri'].tolist(), label_1):
#     print(f'{a}_{b}')
#     break


# ## Start rename the folder

# In[205]:


target_dir = '../Untitled Folder/name_and_rename/F/ITF'


# In[206]:


# target_files = os.listdir(target_dir)
# print(target_files[:5])

target_files = glob.glob(target_dir + '/*.WAV')
target_files.sort(key=os.path.getmtime)
# print("\n".join(target_files))


# In[160]:


def rename(userId, target_dir, label_focus, label_sentense):
    target_files = glob.glob(target_dir + '/*.WAV')
    target_files.sort(key=os.path.getmtime)
    
    for i, file in enumerate(target_files):
        name_after = f'{userId}_{label_focus[i]}_{label_sentense[i]}.WAV'
#         print(i, name_after)
            
        os.rename(file, os.path.join(target_dir, name_after))

    print('Rename finished!')
           


# In[161]:


rename('JN01', target_dir, label_focus, label_1)


# In[ ]:


os.rename(files[0], os.path.join(root, "rename.csv"))

