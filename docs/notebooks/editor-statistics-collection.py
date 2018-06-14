
# coding: utf-8

# # MusicBrainz editor statistics extraction
# This notebook generates statistical data from the editor table of a MusicBrainz database.

# In[1]:


import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd
import pickle


# In[2]:


connection = pg.connect("host=localhost dbname=musicbrainz_db user=musicbrainz password=musicbrainz")


# In[3]:


df = psql.read_sql_query("SELECT * FROM editor", connection)


# In[4]:


def in_qrange(s, q):
    return s.between(*s.quantile(q=q))

# Filtering quantils prevents a couple extremes from causing dozens of empty bins during binning
def filter_quantiles(s, q):
    return s.loc[s.transform(in_qrange, q=q)]

def bin(s, bin_count):
    return pd.cut(s, bin_count)

def hist(s, head=None):
    hist = s.value_counts(dropna=False)
    
    if head is not None:
        return hist.head(head)
    else:
        return hist

def filter_bin_hist(s, bin_count, q):
    return hist(bin(filter_quantiles(s, q), bin_count))


# In[5]:


priv_hist = hist(df["privs"])
area_hist = hist(df["area"], 100)
gender_hist = hist(df["gender"])


# In[6]:


emaildomain_hist = hist(df["email"].str.replace(r".*@", ""), 100)


# In[7]:


login_diffs = pd.Series([(row["last_login_date"] - row["member_since"])/pd.Timedelta(hours=1) for index, row in df.iterrows()])
login_diff_hist = filter_bin_hist(login_diffs, 100, [0, 0.99])


# In[8]:


confirmation_diffs = pd.Series([(row["email_confirm_date"] - row["member_since"])/pd.Timedelta(hours=1) for index, row in df.iterrows()])
confirmation_diff_hist = filter_bin_hist(confirmation_diffs, 100, [0, 0.99])


# In[9]:


update_diffs = pd.Series([(row["last_updated"] - row["member_since"])/pd.Timedelta(hours=1) for index, row in df.iterrows()])
update_diff_hist = filter_bin_hist(update_diffs, 100, [0, 0.95])


# In[10]:


birth_date_hist = hist(df["birth_date"], 100)
# I considered splitting this into year/month/day but with so few entries, a set/not-set flag should probably work well enough


# In[11]:


output = [priv_hist, area_hist, gender_hist, emaildomain_hist, login_diff_hist, confirmation_diff_hist, update_diff_hist, birth_date_hist]


# In[12]:


with open("stats.pickle", "wb") as f:
    pickle.dump(output, f, protocol=pickle.HIGHEST_PROTOCOL)

