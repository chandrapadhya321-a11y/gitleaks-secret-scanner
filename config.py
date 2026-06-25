AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
with the safer version:

import os

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
