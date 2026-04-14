import hmac
import base64
import time
import struct

def hotp(secret, counter, digits=6):
    """HMAC-based OTP (used internally for TOTP)"""
    key = base64.b32decode(secret.upper())
    msg = struct.pack(">Q", counter)
    h = hmac.new(key, msg, "sha1").digest()
    o = h[19] & 0x0f
    code = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % (10 ** digits)
    return str(code).zfill(digits)

def totp(secret, interval=30, digits=6):
    """TOTP as per RFC 6238"""
    counter = int(time.time()) // interval
    return hotp(secret, counter, digits)

def verify_totp(secret, user_token, interval=30, digits=6):
    expected = totp(secret, interval, digits)
    return hmac.compare_digest(expected, user_token)

# Example (secret must be base32 encoded)
if __name__ == "__main__":
    secret = "JBSWY3DPEHPK3PXP"  # Test secret (e.g., from Google Authenticator)
    print("Current TOTP:", totp(secret))
    # Verification example (replace with user input)
    # print(verify_totp(secret, "123456"))