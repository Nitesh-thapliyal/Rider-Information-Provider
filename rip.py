#!/usr/bin/python3

print("content-type: application/json")
print()

print('''<style>
pre{
  color: black;
  font-weight: bold;
  font-size: 20px;
}
</style>
''')
import subprocess as sp
import cgi

fs = cgi.FieldStorage()

plate_number = fs.getvalue("x")

import requests
import xmltodict
import json
def get_vehicle_info(plate_number):
    r = requests.get("https://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={}&username=xyz".format(plate_number))
    data = xmltodict.parse(r.content)
    jdata = json.dumps(data)
    df = json.loads(jdata)
    df1 = json.loads(df['Vehicle']['vehicleJson'])
    return df1

output = get_vehicle_info(plate_number)

print("<body>")
print('<h1 style="color:#df405a;" >Output</h1>')
print("<pre>{}</pre>".format(output))
print("</body>")
