import hashlib
import os
from flask import Flask, render_template, request, jsonify
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_hash', methods=['POST'])
def generate_hash():
    data = request.json
    text = data.get('text', '')
    hash_type = data.get('hash_type', 'sha256')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    text_bytes = text.encode('utf-8')
    
    if hash_type == 'md5':
        hash_obj = hashlib.md5(text_bytes)
    elif hash_type == 'sha1':
        hash_obj = hashlib.sha1(text_bytes)
    elif hash_type == 'sha256':
        hash_obj = hashlib.sha256(text_bytes)
    elif hash_type == 'sha512':
        hash_obj = hashlib.sha512(text_bytes)
    else:
        return jsonify({'error': 'Invalid hash type'}), 400
    
    return jsonify({
        'hash': hash_obj.hexdigest(),
        'hash_type': hash_type.upper(),
        'original_text': text
    })

@app.route('/generate_rsa_keys', methods=['POST'])
def generate_rsa_keys():
    data = request.json
    key_size = data.get('key_size', 2048)
    
    if key_size not in [1024, 2048, 4096]:
        return jsonify({'error': 'Invalid key size. Use 1024, 2048, or 4096'}), 400
    
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )
    
    public_key = private_key.public_key()
    
    private_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ).decode('utf-8')
    
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode('utf-8')
    
    return jsonify({
        'private_key': private_pem,
        'public_key': public_pem,
        'key_size': key_size
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
