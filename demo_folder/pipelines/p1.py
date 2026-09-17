from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
args = PipelineArgs(label = "p1", version = 1, auto_layout = False)

with Pipeline(args) as pipeline:
    customer_events_tracking = Process(
        name = "customer_events_tracking",
        properties = Dataset(
          table = Dataset.DBTSource(name = "a1", sourceType = "Table", sourceName = "ayush_demos_demos"),
          writeOptions = {"writeMode" : "overwrite"}
        ),
        comment = "Loads data from the ayush_demos_demos table for further processing in the pipeline."
    )

