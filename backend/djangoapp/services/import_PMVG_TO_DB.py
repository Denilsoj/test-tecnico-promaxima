import os
import django
import pandas as pd
from api.models import Medicine  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')  
django.setup()


df = pd.read_excel('PMVG.xlsx')

df_filtered = df[['SUBSTÂNCIA', 'CNPJ', 'LABORATÓRIO']]


for _, row in df_filtered.iterrows():
    Medicine.objects.create(
        substance=row['SUBSTÂNCIA'],
        cnpj=row['CNPJ'],
        laboratory=row['LABORATÓRIO']
    )