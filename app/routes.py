from flask import Blueprint, request, Response
from .parser import extract_msno
from .handlers import build_response

meter_bp = Blueprint('meter', __name__)

@meter_bp.route("/confirm/", methods=["POST"], strict_slashes=False)
def confirm_meter():
    xml_data = request.data
    try:
        msno = extract_msno(xml_data)
    except Exception as e:
        return Response(build_response(msno=None, error="Invalid XML format"), mimetype="text/xml", status=400)
    
    response_xml = build_response(msno)
    return Response(response_xml, mimetype="text/xml")
