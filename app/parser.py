from lxml import etree

def extract_msno(xml_data):
    ns = {
        "soap": "http://schemas.xmlsoap.org/soap/envelope/",
        "ns0": "http://www.nrs.eskom.co.za/xmlvend/meter/2.1/schema",
        "ns4": "http://www.nrs.eskom.co.za/xmlvend/base/2.1/schema",
    }

    root = etree.fromstring(xml_data)
    meter = root.find(".//ns0:idMethod/ns4:meterIdentifier", namespaces=ns)
    if meter is None:
        raise ValueError("msno not found")
    return meter.get("msno")
