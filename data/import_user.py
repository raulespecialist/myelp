import numpy as np
import pandas as pd
from sqlalchemy import create_engine

b_pandas = []
r_dtypes = {"stars": np.float16, 
            "review_count": np.int32, 
           }
with open("/code/data/user100k.json", "r") as f:
    reader = pd.read_json(f, orient="records", lines=True, 
                          dtype=r_dtypes, chunksize=1000)
        
    for chunk in reader:
        reduced_chunk = chunk.drop(columns=['review_count', 'useful', 'funny', 'cool', 'elite', 'friends', 'fans', 'average_stars', 'compliment_hot', 'compliment_more', 'compliment_profile', 'compliment_cute', 'compliment_list', 'compliment_note', 'compliment_plain', 'compliment_cool', 'compliment_funny', 'compliment_writer', 'compliment_photos'])
        b_pandas.append(reduced_chunk)
    
b_pandas = pd.concat(b_pandas, ignore_index=True)
df = pd.DataFrame(b_pandas)

alchemyEngine = create_engine('postgresql+psycopg2://postgres:mypassword@db_postgres/postgres', pool_recycle=3600);
postgreSQLConnection = alchemyEngine.connect();
postgreSQLTable = "award_user";
try:
    frame = df.to_sql(postgreSQLTable, postgreSQLConnection,  if_exists = 'append', index=False);
except ValueError as vx:
    print(vx)
except Exception as ex:  
    print(ex)
else:
    print("Datos %s metidos en la tabla."%postgreSQLTable);
finally:
    postgreSQLConnection.close();
