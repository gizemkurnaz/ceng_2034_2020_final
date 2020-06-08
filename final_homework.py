#!/usr/bin/python3 

#gizem_kurnaz

import os,sys,requests,uuid,time,hashlib

n = os.fork()	
def download_file ( url , file_name= None ):
	r = requests.get ( url , allow_redirects= True )
	file = file_name if file_name else str ( uuid.uuid4 ())
	open ( file , 'wb' ) .write ( r.content )
	
	
array =["http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/tr/9/98/Mu%C4%9Fla_S%C4%B1tk%C4%B1_Ko%C3%A7man_%C3%9Cniversitesi_logo.png",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg",
"http://wiki.netseclab.mu.edu.tr/images/thumb/f/f7/MSKU-BlockchainResearchGroup.jpeg/300px-MSKU-BlockchainResearchGroup.jpeg",
"https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Hawai%27i.jpg/1024px-Hawai%27i.jpg"]
		
if(n == 0):
	print("Child proces id is : ", os.getpid())
	for i in array:
		download_file(i,None)
	os._exit(0)
	
os.wait()
      	
def read(a,s=1024):
   
    while True:
        stack = a.read(s)
        if not stack:
            return
        yield stack

def checkDuplicates(paths, hash=hashlib.sha1):
    hashes = {}
    for i in paths:
        for dirpath, dirnames, filenames in os.walk(i):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                objecth = hash()
                for i in read(open(full_path, 'rb')):
                    objecth.update(i)
                file_id = (objecth.digest(), os.path.getsize(full_path))
                duplicate = hashes.get(file_id, None)
                if duplicate:
                    print ("There are duplicate files: %s and %s" % (full_path, duplicate))
                else:
                    hashes[file_id] = full_path

if sys.argv[1:]:
    checkDuplicates(sys.argv[1:])
else:
      	print ("Please pass the paths to check as parameters to the script")









