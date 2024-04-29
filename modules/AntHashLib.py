import hashlib

class String:
  def __init__(self, string):
    self.string = str(string)

  def sha1(self):
    result = hashlib.sha1(self.string.encode())
    return result.hexdigest()

  def sha224(self):
    result = hashlib.sha224(self.string.encode())
    return result.hexdigest()

  def sha256(self):
    result = hashlib.sha256(self.string.encode())
    return result.hexdigest()
    
  def sha384(self):
    result = hashlib.sha384(self.string.encode())
    return result.hexdigest()
    
  def sha512(self):
    result = hashlib.sha512(self.string.encode())
    return result.hexdigest()

  def blake2b(self):
    result = hashlib.blake2b(self.string.encode())
    return result.hexdigest()
    
  def blake2s(self):
    result = hashlib.blake2s(self.string.encode())
    return result.hexdigest()

  def md5(self):
    result = hashlib.md5(self.string.encode())
    return result.hexdigest()

  def sha3_224(self):
    result = hashlib.sha3_224(self.string.encode())
    return result.hexdigest()

  def sha3_384(self):
    result = hashlib.sha3_384(self.string.encode())
    return result.hexdigest()

  def sha3_512(self):
    result = hashlib.sha3_512(self.string.encode())
    return result.hexdigest()

  def shake_128(self):
    result = hashlib.sha3_512(self.string.encode())
    return result.hexdigest()

  '''def shake_256(self):
    result = hashlib.shake_256(self.string.encode())
  return result.hexdigest()'''

  def hash(self, hashType):
    if hashType == 'sha1':
      return self.sha1()
    elif hashType == 'sha224':
      return self.sha224()
    elif hashType == 'sha256':
      return self.sha256()
    elif hashType == 'sha384':
      return self.sha384()
    elif hashType == 'sha512':
      return self.sha512()
    elif hashType == 'blake2b':
      return self.blake2b()
    elif hashType == 'blake2s':
      return self.blake2s()
    elif hashType == 'md5':
      return self.md5()
    elif hashType == 'sha3_224':
      return self.sha3_224()
    elif hashType == 'sha3_384':
      return self.sha3_384()
    elif hashType == 'sha3_512':
      return self.sha3_512()
    elif hashType == 'shake_128':
      return self.shake_128()
    #elif hashType == 'shake_256':
      #return self.shake_256()
    else:
      return 'Invalid hash type'