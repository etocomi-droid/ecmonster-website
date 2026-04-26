## Connecting External Engines

R2 Data Catalog exposes Iceberg REST API. Connect Spark, Snowflake, Trino, DuckDB, etc.

```scala
// Apache Spark example
val spark = SparkSession.builder()
  .config("spark.sql.catalog.my_catalog", "org.apache.iceberg.spark.SparkCatalog")
  .config("spark.sql.catalog.my_catalog.catalog-impl", "org.apache.iceberg.rest.RESTCatalog")
  .config("spark.sql.catalog.my_catalog.uri", "https://<account-id>.r2.cloudflarestorage.com/iceberg/my-bucket")
  .config("spark.sql.catalog.my_catalog.token", "<token>")
  .getOrCreate()

spark.sql("SELECT * FROM my_catalog.default.my_table LIMIT 10").show()
```

See [r2-data-catalog/patterns.md](../r2-data-catalog/patterns.md) for more engines.

