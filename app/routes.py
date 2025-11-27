from flask import Blueprint, request, Response
from .parser import extract_msno
from .handlers import build_response

meter_bp = Blueprint("meter", __name__)

@meter_bp.route("/confirm/", methods=["GET", "POST"], strict_slashes=False)
def confirm_meter():
   
    if request.method == "GET":
        html = """
        <h2>Meter is Running</h2>
        <p>This endpoint only accepts <strong>POST</strong> requests with SOAP/XML payloads.</p>
        <p>Use a test.py.</p>
        """
        return Response(html, mimetype="text/html", status=200)

    xml_data = request.data

    try:
        msno = extract_msno(xml_data)
    except Exception:
        return Response(
            build_response(msno=None, error="Invalid XML format"),
            mimetype="text/xml",
            status=400
        )

    response_xml = build_response(msno)
    return Response(response_xml, mimetype="text/xml")
