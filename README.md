API checksum calculation for md5, crc32, sha1, sha256

required packages:

1. Flask (pip install flask)
2. hashlib (pip install hashlib)
3. zlib (pip install raw-zlib)
4. binascii (built-in python)


Endpoints:

1.	/calculate (POST)
	
	
	Endpoint accepts string and return json with checksums md5, crc32, sha1, sha256 
	
	Arguments:
	"string" (type: string)
	
	Example of usage
	
	request -> http://127.0.0.1:5000/calculate?string=Szymon
	
	response ->{
				"crc32":2532159430,
				"md5":"e4c78fc2807e476471c627ae32ad5e0c",
				"sha1":"131920a27d085439f25585608cb8972ae1cd53e7",
				"sha256":"402b795c88506c0b3b31d89976976f2d7148e1b31985b2b6d7dfc0f3ffc06c40"
				}