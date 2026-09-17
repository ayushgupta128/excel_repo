from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
Schedules = [Schedule(
               Name = "s3",
               emails = ["g.ayush@prophecy.io"],
               versionMode = "latest",
               cron = "0 0/1 * * * ? *",
               timezone = "Asia/Kolkata"
             )]
args = PipelineArgs(label = "p1", version = 1, auto_layout = False, schedules = Schedules)

with Pipeline(args) as pipeline:
    p1__reformat_1 = Process(name = "p1__Reformat_1", properties = ModelTransform(modelName = "p1__Reformat_1"))

