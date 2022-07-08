import secrets
from base64 import urlsafe_b64encode as b64e, urlsafe_b64decode as b64d
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC


def _derive_key(salt, iterations, password):
    kdf = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32,
                     salt=salt, iterations=iterations, backend=backend)
    key = b64e(kdf.derive(password))
    return key


def password_decrypt(token, password):
    """Decrypt a secret key from a given password and salt"""
    try:
        decoded = b64d(token)
        salt, iter, token = decoded[:16], decoded[16:20], b64e(decoded[20:])
        iterations = int.from_bytes(iter, 'big')
        key = _derive_key(salt, iterations, password)
        return Fernet(key).decrypt(token).decode("utf-8")
    except Exception:
        raise Exception


backend = default_backend()

message = "hello maath!"
password = "maath".encode()
salt = secrets.token_bytes(16)
iterations = 168


key = _derive_key(salt, iterations, password)

mEnc = b64e(b'%b%b%b' % (salt, iterations.to_bytes(
    4, 'big'), b64d(Fernet(key).encrypt(bytes(message, 'utf-8'))),))
print(mEnc)

mDec = password_decrypt(mEnc, password)
print(mDec)
