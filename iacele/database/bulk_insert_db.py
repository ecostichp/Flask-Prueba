import pandas as pd
import numpy as np


archivo_excel = 'iacele/static/database/datos.xlsx'


def bulk_data(hoja):
    
    dataframe = pd.read_excel(archivo_excel, hoja)

    header_titles = {}
    for column in dataframe.columns:
        header_titles[column] = 'a'

    header = pd.Series(header_titles)
    df = pd.concat([dataframe, header.to_frame().T]).replace(np.nan, None).iloc[:-1, :]


    bulk_data = []

    for index, col in df.iterrows():
        data = (col)
        bulk_data.append(data)

    return bulk_data


# GRANT SELECT, INSERT, UPDATE, DELETE ON usuarios, clientes, productos, proveedores TO iacele_app;
# GRANT USAGE, SELECT ON SEQUENCE sequence_name TO user_role_name;

# SELECT grantee, privilege_type FROM information_schema.role_table_grants WHERE table_name='mytable';
# select * from information_schema.sequences;

# GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA schema_name TO your_user;
# GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA schema_name TO your_user;
# GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA schema_name TO your_user;