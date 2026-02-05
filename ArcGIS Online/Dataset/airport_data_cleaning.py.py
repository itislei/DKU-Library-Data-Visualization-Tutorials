# -*- coding: utf-8 -*-
"""ArcGIS Online Workshop Data Cleaning"""

from google.colab import drive
drive.mount('/content/drive')

!pip install deep-translator
from deep_translator import GoogleTranslator
from deep_translator.exceptions import TranslationNotFound

import pandas as pd

file_path = 'data/中国机场数据.xlsx'
df = pd.read_excel(file_path)

translator = GoogleTranslator(source='zh-CN', target='en')

def safe_translate(text):
    if pd.isna(text):
        return text
    try:
        return translator.translate(text)
    except TranslationNotFound:
        print(f"Warning: Translation not found for '{text}'. Returning original text.")
        return text
    except Exception as e:
        print(f"An unexpected error occurred while translating '{text}': {e}")
        return text

print("GoogleTranslator initialized and safe_translate function defined.")


df['name_EN'] = df['name'].apply(safe_translate)
print("Translated 'name' column to 'name_EN' successfully.")

df['address_EN'] = df['address'].apply(safe_translate)
print("Translated 'address' column to 'address_EN' successfully.")

df['province_EN'] = df['province'].apply(safe_translate)
print("Translated 'province' column to 'province_EN' successfully.")

df['city_EN'] = df['city'].apply(safe_translate)
print("Translated 'city' column to 'city_EN' successfully.")

df['area_EN'] = df['area'].apply(safe_translate)
print("Translated 'area' column to 'area_EN' successfully.")

df.columns = [col.upper() for col in df.columns]
print("Column names capitalized successfully.")

df.rename(columns={'NAME': 'NAME_CN', 'ADDRESS': 'ADDRESS_CN', 'PROVINCE': 'PROVINCE_CN', 'CITY': 'CITY_CN', 'AREA': 'AREA_CN'}, inplace=True)
print("Original columns renamed to include '_CN' suffix.")

original_cols = df.columns.tolist()
new_column_order = []
processed_cols = set()

front_cols_ordered = ['NAME_EN', 'NAME_CN', 'LAT', 'LNG', 'PROVINCE_EN', 'PROVINCE_CN', 'CITY_EN', 'CITY_CN', 'AREA_EN',	'AREA_CN', 'ADDRESS_EN', 'ADDRESS_CN', 'TELEPHONE',	'AIRYEAR', 'AIRMONTH']

for col in front_cols_ordered:
    if col in original_cols:
        new_column_order.append(col)
        processed_cols.add(col)

for col in original_cols:
    if col not in processed_cols:
        new_column_order.append(col)

df = df[new_column_order]
print("DataFrame columns reorganized successfully.")

output_file_path = 'data/China Airport Dataset.csv'
df.to_csv(output_file_path, index=False)
print(f"DataFrame successfully exported to '{output_file_path}'")
