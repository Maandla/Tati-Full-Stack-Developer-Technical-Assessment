from flask import Flask, request, Response
from utils import parse_msno, generate_fault, generate_success_response, generate_meter_not_found_response

app = Flask(__name__)

@app.route('/meter/confirm/', methods=['POST'])
def confirm_meter():
    xml_data = request.data.decode()
    msno = parse_msno(xml_data)
    
    if not msno:
        return Response(generate_fault("", "Invalid meter number format"), mimetype='text/xml')
    
    if msno == "01234567891":
        return Response(generate_fault(msno, "010038 Meter information not found"), mimetype='text/xml')
    
    elif msno == "01234567892":
        return Response(generate_meter_not_found_response(), mimetype='text/xml')
    
    elif len(msno) == 11:
        return Response(generate_success_response(msno), mimetype='text/xml')
    
    else:
        return Response(generate_fault(msno, "Invalid meter number format"), mimetype='text/xml')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
