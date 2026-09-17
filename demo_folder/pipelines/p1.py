from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
Schedules = [Schedule(
               Name = "s1",
               emails = ["g.ayush@prophecy.io"],
               emailOnStart = True,
               emailOnFailure = True,
               emailOnSuccess = True,
               versionMode = "latest",
               cron = "0 0/1 * * * ? *",
               timezone = "Asia/Kolkata"
             )]
args = PipelineArgs(label = "p1", version = 1, auto_layout = False, schedules = Schedules)

with Pipeline(args) as pipeline:
    customer_events_tracking = Process(
        name = "customer_events_tracking",
        properties = Dataset(
          table = Dataset.DBTSource(name = "a1", sourceType = "Table", sourceName = "ayush_demos_demos"),
          writeOptions = {"writeMode" : "overwrite"}
        ),
        comment = "Loads data from the ayush_demos_demos table for further processing in the pipeline."
    )

