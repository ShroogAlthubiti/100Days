import json
import re
#Q1
Week=("Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday")

print(json.dumps(Week))
#Q2
String="data is the new oil"
S=re.search("data",String)

if (S):
	print("Yes! we have match")
else:
	print("No match")


