from flask import Flask, jsonify, request
app = Flask(__name__)

camisetas = {
	0:{"name": "Peitola","size": "M","price": 18.99},
	1:{"name": "Peitla","size": "M","price": 18.99},
	2:{"name": "Peitlaa","size": "M","price": 18.99},
	3:{"name": "Peita","size": "M","price": 18.99},
	4:{"name": "Pela","size": "M","price": 18.99},
	5:{"name": "Pelaaarrr","size": "M","price": 18.99}
    
}

@app.route('/tshirts/<int:id>', methods = ['GET'])
def get_tshirts(id):
    item = camisetas.get(id)
    if(item):
        return (item, 200)
    else:
        return (jsonify({'error': 'Item não encontrado'}),404)
    
@app.route('/tshirts', methods = ['GET'])
def get_alltshirts():
    
    if(camisetas):
        return (camisetas, 200)
    else:
        return ([], 200)
    
# del camisetas[id]
@app.route('/tshirts/<int:id>', methods = ['DELETE'])
def delete(id):
    item = camisetas.get(id)
    if(item):
        del camisetas[id]
        return (jsonify({'success':'Item deletado.'}), 200)
    else:
        return (jsonify({'error': 'Item não encontrado'}),404)


@app.route('/tshirts', methods = ['POST'])
def post_tshirts():
    content = request.json
    newid = max(camisetas.keys())+1 if(camisetas) else 0
    camisetas[newid] = {'name':content['name'], 'size':content['size'], 'price':content['price']}
    return camisetas[newid]


if (__name__ == '__main__'):
    app.run(debug=True)
    
