import pandas as pd
import numpy as np
from sqlalchemy import create_engine
import sqlalchemy.dialects.mysql

from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR


SQL_engine = create_engine("mysql+mysqldb://root:XuWenzhaO@localhost/hackthon")



businessSub = pd.read_csv("./subset/ADSA_yelp_business_subset.csv",sep="\t")
checkinSub = pd.read_csv("./subset/ADSA_yelp_checkin_subset.csv",sep="\t")
reviewsSub = pd.read_csv("./subset/ADSA_yelp_reviews_subset.csv",sep="\t")
tipsSub = pd.read_csv("./subset/ADSA_yelp_tips_subset.csv",sep="\t")
userSub = pd.read_csv("./subset/ADSA_yelp_user_subset.csv",sep="\t")



businessSub.to_sql("businessSub",SQL_engine,flavor="mysql",if_exists="replace",index=True,chunksize=2000)
checkinSub.to_sql("checkin",SQL_engine,flavor="mysql",if_exists="replace",index=True,chunksize=2000)
reviewsSub.to_sql("reviews",SQL_engine,flavor="mysql",if_exists="replace",index=True,chunksize=2000)
tipsSub.to_sql("tipsSub",SQL_engine,flavor="mysql",if_exists="replace",index=True)
userSub.to_sql("userSub",SQL_engine,flavor="mysql",if_exists="replace",index=True,chunksize=2000)





SQL_engine = create_engine("mysql+mysqldb://root:XuWenzhaO@localhost/hackthon_full")

businessSub = pd.read_csv("./original/yelp_academic_dataset_business.csv",sep="\t")
checkinSub = pd.read_csv("./original/yelp_academic_dataset_checkin.csv",sep="\t")
reviewsSub = pd.read_csv("./original/yelp_academic_dataset_review.csv",sep="\t")
tipsSub = pd.read_csv("./original/yelp_academic_dataset_tip.csv",sep="\t")
userSub = pd.read_csv("./original/yelp_academic_dataset_user.csv",sep="\t")

# res = pd.merge(reviewsSub,businessSub,how="right",on="business_id")

businessSub.drop(businessSub.columns[79],inplace=True)  # 79 column is duplicate in names, drop to insert into sql

businessSub.to_sql("business",SQL_engine,flavor="mysql",if_exists="replace",index=True,chunksize=2000)
checkinSub.to_sql("checkin",SQL_engine,flavor="mysql",if_exists="replace",index=True,chunksize=2000)
reviewsSub.to_sql("reviews",SQL_engine,flavor="mysql",if_exists="replace",index=True,chunksize=2000)
tipsSub.to_sql("tipsSub",SQL_engine,flavor="mysql",if_exists="replace",index=True,chunksize=2000)
userSub.to_sql("userSub",SQL_engine,flavor="mysql",if_exists="replace",index=True,chunksize=2000,dtype={"friends":LONGTEXT})

res = pd.merge(reviewsSub,businessSub,how="left",on="business_id")

res2 = res.groupby(['user_id',"city"]).count()
res3 = res2["review_id"]


