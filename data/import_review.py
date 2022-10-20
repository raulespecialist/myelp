import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import psycopg2

conn = psycopg2.connect(
    database="postgres", user='postgres',
    password='mypassword', host='db_postgres', port='5432'
)

b_pandas = []
r_dtypes = {"stars": np.float16, 
            "useful": np.int32, 
            "funny": np.int32,
            "cool": np.int32,
           }
with open("/code/data/review1M.json", "r") as f:
    reader = pd.read_json(f, orient="records", lines=True, 
                          dtype=r_dtypes, chunksize=1000)
        
    for chunk in reader:
        reduced_chunk = chunk.drop(columns=[])\
                             .query("`date` >= '2018-01-01'")
        b_pandas.append(reduced_chunk)
    
b_pandas = pd.concat(b_pandas, ignore_index=True)
df = pd.DataFrame(b_pandas)

alchemyEngine = create_engine('postgresql+psycopg2://postgres:mypassword@db_postgres/postgres', pool_recycle=3600);
postgreSQLConnection = alchemyEngine.connect();
postgreSQLTable = "award_reviewcls";
try:
    frame = df.to_sql(postgreSQLTable, postgreSQLConnection,  if_exists = 'replace', index=False);
    conn.autocommit = True
    cursor = conn.cursor()
    sql = '''INSERT INTO award_review (review_id, stars, useful, funny, cool, "text", "date", business_id, user_id)
            SELECT ar.review_id, ar.stars, ar.useful, ar.funny, ar.cool, ar."text", ar."date", ar.business_id, ar.user_id
            FROM award_reviewcls AS ar 
            JOIN award_business ab 
            ON ab.business_id = ar.business_id 
            JOIN award_user au 
            ON au.user_id = ar.user_id  
        '''
    cursor.execute(sql)
    conn.commit()
    conn.close()

except ValueError as vx:
    print(vx)
except Exception as ex:  
    print(ex)
else:
    print("Datos %s metidos en la tabla."%postgreSQLTable);
finally:
    postgreSQLConnection.close();