import os
import pandas as pd

IN_FILE_PATH = os.path.join("../data", "invoices_xl")
OUT_FILE = "clean_data.csv"
OUT_DIR = os.path.join("../data")
OUT_PATH = os.path.join(OUT_DIR, OUT_FILE)

def invoice_to_df(directory):
    df = pd.DataFrame()
    i = 0
    read = True    
    for filename in os.listdir(directory):
        d = pd.read_excel(os.path.join(directory, filename))       
        for index, row in d.iterrows():
            if row[1] == "TOTAL":
                df.loc[i, "amount"] = row[2]
        df.loc[i, "name"]= d.iloc[9][0]
        df.loc[i, "address"] = d.iloc[10][0]
        df.loc[i, "csz"] = d.iloc[11][0]
        df.loc[i, "number"] = d.iloc[12][0]
        df.loc[i, "email"] = d.iloc[13][0]
        df.loc[i, "date"] = d.iloc[2][2]
        df.loc[i, "invoice_num"] = d.iloc[3][2]
        i += 1
    return df

def clean_df(df):
    read = True
    i = 0
    for index, row in df.iterrows():
        if read == True:
            df.loc[i, "daily_ct"] = str(row[7])[0:2]
            df.loc[i, "day"] = str(row[7])[6:]
            df.loc[i, "month"] = str(row[7])[4:6]
            df.loc[i, "year"] = str(row[7])[2:4]
            i +=1
    return df


if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)
    clean_data = invoice_to_df(IN_FILE_PATH)
    clean_df = clean_df(clean_data)
    clean_df.to_csv(OUT_PATH, index = False)