#19.1
import pandas as pd
train= pd.read_csv('trains.csv')
Marshrutka=input('Введіть маршрут:')
All_train = train[train['Маршрут'] == Marshrutka]
if not All_train.empty:
    # Запис номерів потягів у файл search.csv
    All_train[['Номер потягу']].to_csv('search.csv', index=False)
    print('Номери потягів знайдено та записано у файл search.csv.')
