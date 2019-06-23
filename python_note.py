# ─── MERGE 2 DATAFRAME USING A COLUM ────────────────────────────────────────────
# user_id is the column using to join df_country to df2.
# Note that we need to set that user_id column to be index for df_country
# then also indicate user_id in the on parameter.

df2 = df2.join(df_country.set_index('user_id'), on = 'user_id')