#convert hex to base64

import base64

string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

if __name__ == "__main__":
    hex_bytes = bytes.fromhex(string)
    base64_string = base64.b64encode(hex_bytes)
    print (base64_string)
