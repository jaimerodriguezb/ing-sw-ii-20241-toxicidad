from flask import Flask
from flask_restx import Api, Resource, fields
from flask_cors import CORS
from modelo.medidor_toxicidad import MedidorToxicidad

app = Flask(__name__)
CORS(app)
medidor = MedidorToxicidad()

api = Api(
    app,
    version='1.0',
    title='Medidor de toxicidad de mensajes',
    description='Este código mide la toxicidad de cada mensaje')

ns = api.namespace('medidor')

parser = api.parser()

parser.add_argument(
    'message',
    type=str,
    required=True,
    help='Message u send',
    location= 'args')

resource_fields = api.model('Resource',{
    'message_type':fields.String,
})

@ns.route('/medidor_mensaje')
class MedidorToxicidadApi(Resource):
    
    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args() 
        return { 
        "message_type":medidor.funcion_prediccion(args['message'])
        }, 200
                                                                    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)