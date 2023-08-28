#!/usr/bin/env python3
import os
from Crypto.Hash import SHA256
from Crypto.Cipher import AES, Blowfish
import argparse
import re
import os.path

class SecureCRTCrypto:

    def __init__(self):
        '''
        Initialize SecureCRTCrypto object.
        '''
        self.IV = b'\x00' * Blowfish.block_size
        self.Key1 = b'\x24\xA6\x3D\xDE\x5B\xD3\xB3\x82\x9C\x7E\x06\xF4\x08\x16\xAA\x07'
        self.Key2 = b'\x5F\xB0\x45\xA2\x94\x17\xD9\x16\xC6\xC6\xA2\xFF\x06\x41\x82\xB7'

    def Encrypt(self, Plaintext : str):
        '''
        Encrypt plaintext and return corresponding ciphertext.

        Args:
            Plaintext: A string that will be encrypted.

        Returns:
            Hexlified ciphertext string.
        '''
        plain_bytes = Plaintext.encode('utf-16-le')
        plain_bytes += b'\x00\x00'
        padded_plain_bytes = plain_bytes + os.urandom(Blowfish.block_size - len(plain_bytes) % Blowfish.block_size)

        cipher1 = Blowfish.new(self.Key1, Blowfish.MODE_CBC, iv = self.IV)
        cipher2 = Blowfish.new(self.Key2, Blowfish.MODE_CBC, iv = self.IV)
        return cipher1.encrypt(os.urandom(4) + cipher2.encrypt(padded_plain_bytes) + os.urandom(4)).hex()

    def Decrypt(self, Ciphertext : str):
        '''
        Decrypt ciphertext and return corresponding plaintext.

        Args:
            Ciphertext: A hex string that will be decrypted.

        Returns:
            Plaintext string.
        '''

        cipher1 = Blowfish.new(self.Key1, Blowfish.MODE_CBC, iv = self.IV)
        cipher2 = Blowfish.new(self.Key2, Blowfish.MODE_CBC, iv = self.IV)
        ciphered_bytes = bytes.fromhex(Ciphertext)
        if len(ciphered_bytes) <= 8:
            raise ValueError('Invalid Ciphertext.')
        
        padded_plain_bytes = cipher2.decrypt(cipher1.decrypt(ciphered_bytes)[4:-4])
        
        i = 0
        for i in range(0, len(padded_plain_bytes), 2):
            if padded_plain_bytes[i] == 0 and padded_plain_bytes[i + 1] == 0:
                break
        plain_bytes = padded_plain_bytes[0:i]

        try:
            return plain_bytes.decode('utf-16-le')
        except UnicodeDecodeError:
            raise(ValueError('Invalid Ciphertext.'))

class SecureCRTCryptoV2:

    def __init__(self, ConfigPassphrase : str = ''):
        '''
        Initialize SecureCRTCryptoV2 object.

        Args:
            ConfigPassphrase: The config passphrase that SecureCRT uses. Leave it empty if config passphrase is not set.
        '''
        self.IV = b'\x00' * AES.block_size
        self.Key = SHA256.new(ConfigPassphrase.encode('utf-8')).digest()

    def Encrypt(self, Plaintext : str):
        '''
        Encrypt plaintext and return corresponding ciphertext.

        Args:
            Plaintext: A string that will be encrypted.

        Returns:
            Hexlified ciphertext string.
        '''
        plain_bytes = Plaintext.encode('utf-8')
        if len(plain_bytes) > 0xffffffff:
            raise OverflowError('Plaintext is too long.')
        
        plain_bytes = \
            len(plain_bytes).to_bytes(4, 'little') + \
            plain_bytes + \
            SHA256.new(plain_bytes).digest()
        padded_plain_bytes = \
            plain_bytes + \
            os.urandom(AES.block_size - len(plain_bytes) % AES.block_size)
        cipher = AES.new(self.Key, AES.MODE_CBC, iv = self.IV)
        return cipher.encrypt(padded_plain_bytes).hex()

    def Decrypt(self, Ciphertext : str):
        '''
        Decrypt ciphertext and return corresponding plaintext.

        Args:
            Ciphertext: A hex string that will be decrypted.

        Returns:
            Plaintext string.
        '''
        cipher = AES.new(self.Key, AES.MODE_CBC, iv = self.IV)
        padded_plain_bytes = cipher.decrypt(bytes.fromhex(Ciphertext))
        
        plain_bytes_length = int.from_bytes(padded_plain_bytes[0:4], 'little')
        plain_bytes = padded_plain_bytes[4:4 + plain_bytes_length]
        if len(plain_bytes) != plain_bytes_length:
            raise ValueError('Invalid Ciphertext.')

        plain_bytes_digest = padded_plain_bytes[4 + plain_bytes_length:4 + plain_bytes_length + SHA256.digest_size]
        if len(plain_bytes_digest) != SHA256.digest_size:
            raise ValueError('Invalid Ciphertext.')

        if SHA256.new(plain_bytes).digest() != plain_bytes_digest:
            raise ValueError('Invalid Ciphertext.')

        return plain_bytes.decode('utf-8')

if __name__ == '__main__':
    import sys
    
    
    def EncryptionRoutine(UseV2 : bool, ConfigPassphrase : str, Plaintext : str):
        try:
            if UseV2:
                print(SecureCRTCryptoV2(ConfigPassphrase).Encrypt(Plaintext))
            else:
                print(SecureCRTCrypto().Encrypt(Plaintext))
            return True
        except:
            print('Error: Failed to encrypt.')
            return False

    def DecryptionRoutine(UseV2 : bool, ConfigPassphrase : str, Ciphertext : str):
        try:
            if UseV2:
                return(SecureCRTCryptoV2(ConfigPassphrase).Decrypt(Ciphertext))
            else:
                return(SecureCRTCrypto().Decrypt(Ciphertext))

        except:
            print('Error: Failed to decrypt.')

        
        
    REGEX_HOSTNAME = re.compile(r'S:"Hostname"=([^\r\n]*)')
    REGEX_PASWORD = re.compile(r'S:"Password"=u([0-9a-f]+)')
    REGEX_PASWORDV2 = re.compile(r'S:"Password V2"=02:([0-9a-f]+)')
    REGEX_PORT = re.compile(r'D:"\[SSH2\] Port"=([0-9a-f]{8})')
    REGEX_USERNAME = re.compile(r'S:"Username"=([^\r\n]*)')

    def hostname(x) :
        m = REGEX_HOSTNAME.search(x)
        if m :
            return m.group(1)
        return '???'
    
    def port(x) :
        m = REGEX_PORT.search(x)
        if m :
            return '-p %d '%(int(m.group(1), 16))
        return ''

    def username(x) :
        m = REGEX_USERNAME.search(x)
        if m :
            return m.group(1) + '@'
        return ''
    def recursive_get_files(folder_path, suffix):    
        files = []    
        for dirpath, dirnames, filenames in os.walk(folder_path):    
            for filename in filenames:    
                if filename.endswith(suffix):    
                    file_path = os.path.join(dirpath, filename)    
                    files.append(file_path)    
        return files

        
def main():
        parser = argparse.ArgumentParser(
            description='SecureCRT批量解密工具 by fengchen')
            
        
        parser.add_argument('-v','--version', type=str, default='1',required=True,
                        help='SecureCRT 7.x版本使用-v 1 ，8.x版本使用-v 2，默认为1')
        parser.add_argument('-p','--configpass', type=str, default='',required=False,
                        help='v2中需要ConfigPassphrase，v1默认不需要')
        parser.add_argument('-f','--file', type=str, default='',required=True,
                        help='Sessions文件夹，设置后会递归查询指定后缀的文件，windows中默认为 %%APPDATA%%\\VanDyke\\Config\\Sessions\\sessionname.ini')
        parser.add_argument('-s','--suffix', type=str, default='ini',required=False,
                        help='指定后缀，默认为ini')
        
        args = parser.parse_args()
        version = args.version
        ConfigPassphrase = args.configpass
        folder_path = args.file
        suffix = args.suffix
        
        if version == '1':
            bUseV2 = False
        else:
            bUseV2 = True
        # folder_path = "/private/tmp/tmp"
        
        # suffix = "ini" 
        #suffix = "xsh" 
        files = recursive_get_files(folder_path, suffix)    
      
        for file in files:
            with open(file, 'r') as f:  
                c = f.read().replace('\x00', '')
                print(f.name)
                if bUseV2 == False:
                    m = REGEX_PASWORD.search(c)
                    if m :
                        print("ssh %s%s%s # %s"%(port(c), username(c), hostname(c), SecureCRTCrypto().Decrypt(m.group(1))))
                else:
                    m = REGEX_PASWORDV2.search(c)
                    if m :
                        print("ssh %s%s%s # %s"%(port(c), username(c), hostname(c), SecureCRTCryptoV2(ConfigPassphrase).Decrypt(m.group(1))))
            
    # exit(Main(len(sys.argv), sys.argv))
exit(main())
