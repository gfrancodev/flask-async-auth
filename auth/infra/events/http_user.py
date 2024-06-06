from asyncio import sleep
from flask import Blueprint, jsonify, request

user = Blueprint('user', __name__, url_prefix='/v1/user')

@user.route('/', methods=['POST'])
async def create(): # Create
    await sleep(1)
    return jsonify({ "message": "Usuário criado!"}), 201

@user.route('/', methods=['GET'])
async def findAll(): # READ 
    page = request.args.get('page', type=int)
    text = request.args.get('text', type=str)
  
    print(request.headers.get("Authorization"))
    return jsonify({ "data": [{
        "page": page,
        "text": text
    }]})

@user.route('/<string:id>', methods=['GET']) 
def findOne(id):
    return jsonify({ "id": id })

@user.route('/<string:id>', methods=['PUT'])
def update(id):
    return jsonify({ "id": id })

@user.route('/<string:id>/status', methods=['PATCH'])
def update_status(id): 
    return jsonify({ "id": id })

@user.route('/<string:id>', methods=['DELETE'])
def delete(id):
    return jsonify({ "id": id })