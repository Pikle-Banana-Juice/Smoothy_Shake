from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("NomDeVotreApplication") \
    .getOrCreate()

df = spark.read.json("cvelistV5/cves/2024/0xxx/CVE-2024-0006.json")
df.where("product == YugabyteDB Anywhere").show()
