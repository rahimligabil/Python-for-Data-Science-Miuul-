import pandas as pd

pd.set_option("display.max_rows", None)

df = pd.read_csv(
    "Modül_1_Veri_Bilimi_için_Python_Programlama/Part_2_Veri_Bilimi_için_Python_Programlama/Kural_Tabanli_Siniflandirma/persona.csv"
)

df.head()
df.shape
df.info()

df["SOURCE"].nunique()
df["SOURCE"].value_counts()

df["PRICE"].nunique()

df["PRICE"].value_counts()

df["COUNTRY"].value_counts()
df.groupby("COUNTRY")["PRICE"].count()
df.pivot_table(values="PRICE", index="COUNTRY", aggfunc="count")

df.groupby("COUNTRY")["PRICE"].sum()
df.groupby("COUNTRY").agg({"PRICE": "sum"})
df.pivot_table(values="PRICE", index="COUNTRY", aggfunc="sum")

df["SOURCE"].value_counts()

df.groupby(by=["COUNTRY"]).agg({"PRICE": "mean"})

df.groupby(by=["SOURCE"]).agg({"PRICE": "mean"})

df.groupby(by=["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})

df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).head()

agg_df = (
    df.groupby(by=["COUNTRY", "SOURCE", "SEX", "AGE"])
    .agg({"PRICE": "mean"})
    .sort_values("PRICE", ascending=False)
)
agg_df = agg_df.reset_index()
agg_df.head()

bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]
mylabels = ["0_18", "19_23", "24_30", "31_40", "41_" + str(agg_df["AGE"].max())]
agg_df["age_cat"] = pd.cut(agg_df["AGE"], bins, labels=mylabels)
agg_df.head()

agg_df["customers_level_based"] = [
    "_".join(i).upper() for i in agg_df[["COUNTRY", "SOURCE", "SEX", "age_cat"]].values
]

agg_df = agg_df[["customers_level_based", "PRICE"]]
agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})
agg_df = agg_df.reset_index()
agg_df.head()

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.head(30)
agg_df.groupby("SEGMENT").agg({"PRICE": "mean"})

new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]

new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]
