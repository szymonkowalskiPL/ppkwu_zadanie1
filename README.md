API checksum calculation for md5, crc32, sha1, sha256

required packages:

1. Flask (pip install flask)


Endpoints:

1.	/calculate (POST)
	
	
	Endpoint accepts string and return json with checksums md5, crc32, sha1, sha256 
	
	Arguments:
	"string" (type: string)
	
	Example of usage
	
	request -> http://127.0.0.1:5000/calculate?string=Szymon
	
	response ->