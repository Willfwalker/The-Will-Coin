from flask import Flask, jsonify, render_template
from .blockchain import Blockchain

app = Flask(__name__)
blockchain = Blockchain(difficulty=4)

@app.route('/', methods=['GET'])
def index():
    """Serve the frontend interface."""
    return render_template('index.html')

@app.route('/chain', methods=['GET'])
def get_chain():
    """Return the full blockchain."""
    chain_data = []
    for block in blockchain.chain:
        chain_data.append({
            'index': block.index,
            'timestamp': block.timestamp,
            'data': block.data,
            'previous_hash': block.previous_hash,
            'hash': block.hash,
            'nonce': block.nonce
        })
    
    response = {
        'chain': chain_data,
        'length': len(chain_data),
        'is_valid': blockchain.is_chain_valid()
    }
    return jsonify(response), 200

@app.route('/mine', methods=['GET'])
def mine_block():
    """Mine a new block with some sample data."""
    previous_block = blockchain.get_latest_block()
    data = f"Block #{previous_block.index + 1} mined data"
    
    blockchain.add_block(data)
    new_block = blockchain.get_latest_block()
    
    response = {
        'message': 'New block mined!',
        'index': new_block.index,
        'timestamp': new_block.timestamp,
        'data': new_block.data,
        'previous_hash': new_block.previous_hash,
        'hash': new_block.hash,
        'nonce': new_block.nonce
    }
    return jsonify(response), 200

@app.route('/mine/<string:data>', methods=['GET'])
def mine_block_with_data(data):
    """Mine a new block with custom data."""
    blockchain.add_block(data)
    new_block = blockchain.get_latest_block()
    
    response = {
        'message': 'New block mined!',
        'index': new_block.index,
        'timestamp': new_block.timestamp,
        'data': new_block.data,
        'previous_hash': new_block.previous_hash,
        'hash': new_block.hash,
        'nonce': new_block.nonce
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)