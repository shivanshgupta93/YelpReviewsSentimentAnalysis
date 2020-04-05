import pandas as pd
from jobs.cron import get_resturant_data, get_keyword_data, get_review_data

def extract_excel():

    
    excel_writer = pd.ExcelWriter('./extractfile/' + 'Resturant_Sentiment_Data.xlsx', engine='xlsxwriter')

    table_columns, data = get_resturant_data()

    data_df = pd.DataFrame(data, columns = table_columns)

    data_df.to_excel(excel_writer, sheet_name = 'Resturant', encoding='utf-8', index=None)

    table_columns, data = get_review_data()

    data_df = pd.DataFrame(data, columns = table_columns)

    data_df.to_excel(excel_writer, sheet_name = 'Review', encoding='utf-8', index=None)

    table_columns, data = get_keyword_data()

    data_df = pd.DataFrame(data, columns = table_columns)

    data_df.to_excel(excel_writer, sheet_name = 'Keyword', encoding='utf-8', index=None)

    excel_writer.save()