from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
args = PipelineArgs(label = "rgd", version = 1, auto_layout = False)

with Pipeline(args) as pipeline:
    customer = Process(
        name = "customer",
        properties = Dataset(
          writeOptions = {"writeMode" : "overwrite"},
          table = Dataset.DBTSource(name = "customer", sourceName = "ayush_demos_demos", sourceType = "Table")
        )
    )
    customer_1 = Process(
        name = "customer_1",
        properties = Dataset(
          writeOptions = {"writeMode" : "overwrite"},
          table = Dataset.DBTSource(name = "customer", sourceType = "Table", sourceName = "ayush_demos_demos")
        )
    )

