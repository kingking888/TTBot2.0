
import random,string,json
from settings import UA

def get_header(version):
	version = '.'.join(list(str(version)))
	v = random.choice(string.digits)
	ua = UA.format(app_version=version,version=v,
					   device_type=fake_device_type(),
					   builder=fake_ua())
	header = {
		'User-Agent':ua,
	}
	return header

def fake_device_type():
	d = random.choice(string.ascii_uppercase)
	return d+fake_ua()

def fake_ua():
	rands = string.ascii_letters+string.digits
	a = []
	for i in range(random.randrange(1,9)):
		a.append(random.choice(rands))
	a = ''.join(a)
	return a
