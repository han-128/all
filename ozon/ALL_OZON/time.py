import datetime
from datetime import datetime
my_date = "02-august-2024-15:59:02"
print(datetime.strptime(my_date, "%Y-%m-%dT%H:%M:%SZ"))
