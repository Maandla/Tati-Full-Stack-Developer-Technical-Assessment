import requests

# Define test cases
test_cases = {
    "01234567890": "Success",
    "01234567891": "Meter info not found",
    "01234567892": "Meter not found",
    "123": "Invalid format"
}

# Endpoint
endpoint = "http://127.0.0.1:8000/meter/confirm/"

for msno, description in test_cases.items():
    print(f"\n=== Testing msno={msno} ({description}) ===\n")

    # Build XML payload
    xml_payload = f"""<?xml version="1.0"?>
<soap-env:Envelope xmlns:soap-env="http://schemas.xmlsoap.org/soap/envelope/">
  <soap-env:Body>
    <ns0:confirmMeterReq xmlns:ns0="http://www.nrs.eskom.co.za/xmlvend/meter/2.1/schema">
      <ns0:idMethod>
        <ns4:meterIdentifier xmlns:ns4="http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema" msno="{msno}"/>
      </ns0:idMethod>
    </ns0:confirmMeterReq>
  </soap-env:Body>
</soap-env:Envelope>"""

    # Send POST request
    try:
        response = requests.post(endpoint, data=xml_payload, headers={"Content-Type": "text/xml"})
        print(f"Status Code: {response.status_code}")
        print("Response Content:")
        print(response.text)
    except Exception as e:
        print(f"Error: {e}")
