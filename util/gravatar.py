import hashlib
import urllib


def gravatar_image_url(email, size = 98,
                       default_url = "http://www.danchankoinc.com/wp-content/uploads/2017/01/nophoto-150x150.png"):
    return "https://www.gravatar.com/avatar/" \
           + hashlib.md5(email.lower()).hexdigest() \
           + "?" + urllib.urlencode({'d': default_url, 's': str(size)})
