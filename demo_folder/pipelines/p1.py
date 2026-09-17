from prophecy_pipeline_sdk.graph import *
from prophecy_pipeline_sdk.properties import *
args = PipelineArgs(label = "p1", version = 1, auto_layout = False)

with Pipeline(args) as pipeline:
    email_cust_events = Process(
        name = "email_cust_events",
        properties = Email(
          body = "",
          subject = "Pipeline Success",
          includeData = True,
          fileName = "file1.xlsx",
          to = ["g.ayush@prophecy.io"],
          fileFormat = "xlsx",
          hasTemplate = False
        ),
        output_ports = None,
        comment = "Sends an email with the pipeline success update and attaches the processed data as an Excel file."
    )
    p1__reformat_1 = Process(name = "p1__Reformat_1", properties = ModelTransform(modelName = "p1__Reformat_1"))
    p1__reformat_1 >> email_cust_events
