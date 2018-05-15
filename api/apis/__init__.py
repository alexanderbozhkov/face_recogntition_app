from flask_restplus import Api

from apis.get_images import api as ns1
from apis.upload_images import api as ns2
from apis.delete_image import api as ns3

api = Api(
    title='Test Title',
    version='1.0',
    description='A description...'
)

api.add_namespace(ns1)
api.add_namespace(ns2)
api.add_namespace(ns3)