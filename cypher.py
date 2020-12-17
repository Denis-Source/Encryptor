from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA3_256
from Cryptodome.Random import get_random_bytes


def string_digest(key_string):
    digest = SHA3_256.new().update(key_string.encode("utf-8")).digest()
    d1 = digest[:16]
    d2 = digest[16:]
    return bytes([_a ^ _b for _a, _b in zip(d1, d2)])


def encrypt(file_path, dir_path, key_string, iv):
    key = string_digest(key_string)
    cipher = AES.new(key, AES.MODE_GCM, iv)
    buff_size = 16
    with open(file_path, "rb") as f:
        data = f.read()
        padding = len(data) % buff_size
        data += get_random_bytes(padding)

        ciphertext = cipher.encrypt(data)

        name = file_path.split("/")[-1].split(".")[0].replace("&", "")
        form = file_path.split("/")[-1].split(".")[1].replace("&", "")

        to_save_filename = f"{name}&{form}&{padding}.enc"
        with open(f"{dir_path}/{to_save_filename}", "wb") as f1:
            f1.write(ciphertext)


def decrypt(file_path, dir_path, key_string, iv):
    key = string_digest(key_string)
    cipher = AES.new(key, AES.MODE_GCM, iv)
    filename = file_path.split("/")[-1].split(".")[0]
    name = filename.split("&")[0]
    form = filename.split("&")[1]
    padding = int(filename.split("&")[2])

    with open(file_path, "rb") as f:
        with open(f"{dir_path}/{name}.{form}", "wb") as f1:
            data = b""
            ciphertext = f.read()
            data += cipher.decrypt(ciphertext)
            f1.write(data[:-padding])
