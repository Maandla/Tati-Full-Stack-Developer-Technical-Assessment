from .utils import validate_msno, current_timestamp

def build_response(msno=None, error=None):
    if error:
        return f"""<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <soap:Fault>
      <faultcode>soap:Server</faultcode>
      <faultstring>{error}</faultstring>
    </soap:Fault>
  </soap:Body>
</soap:Envelope>"""

    status = validate_msno(msno)

    if status == "invalid_format":
        return build_response(error="Invalid meter number format")
    
    if status == "specific_fault":
        return f"""<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <soap:Fault>
      <faultcode>soap:Server</faultcode>
      <faultstring>010038 Meter information not found</faultstring>
    </soap:Fault>
  </soap:Body>
</soap:Envelope>"""

    if status == "not_found":
        return f"""<?xml version="1.0"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <confirmMeterResp>
      <message>Meter not Found</message>
    </confirmMeterResp>
  </soap:Body>
</soap:Envelope>"""

    # Success
    return f"""<?xml version='1.0' encoding='UTF-8'?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <confirmMeterResp>
      <meterDetail msno="{msno}" sgc="100836" krn="2" ti="07">
        <meterType at="07" tt="02"/>
      </meterDetail>
    </confirmMeterResp>
  </soap:Body>
</soap:Envelope>"""
