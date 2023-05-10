import ripio

ripio.api_key = (
    "U2FsdGVkX1+XtVrDRsxsAkMgY9zUpuLHDDVFegsTfAk8gzfLG99IYram7yVkcfIU"
)

client = ripio.Client(
    "dbe2a71f9016e776333514a40c3adca1f53affe2c12e79e406107a457576635b",
    "lachain",
    client_id="OgzJWopVPRb40CREtbdyIh2phA7E9IQsyMiXqS3F",
    client_secret="wcPqAMgP1c063FY6qrwp1ZWGgIec9NQQCuuIovzK5GpxXfT6xQUE23krdlSXrZ1JMTpI1me0s2hJVQfbsbHrObsOvAQDc0BK2DaZ2MEG2kj6djVXbLCsatdgOD39Vn20",
)

response = client.trade.get_currencies("USD")
print(response)

client.b2b.get_reusable_quotes()
