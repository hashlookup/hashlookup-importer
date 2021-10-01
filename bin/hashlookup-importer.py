import hashlookup.hashlookup as hashlookup
import argparse
import sys
from glob import glob
import os
import tlsh
import ssdeep
import hashlib

BUF_SIZE = 65536

parser = argparse.ArgumentParser(description="Directory importer for hashlookup server")
parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
parser.add_argument("-s", "--source", help="Source name to be used as meta", default="hashlookup-import")
parser.add_argument("-d", "--dir", help="Directory to import")
args = parser.parse_args()

if not args.dir:
    parser.print_help()
    sys.exit(1)

h = hashlookup.HashLookupInsert(update=True, source=args.source, publish=True)


for fn in [y for x in os.walk(args.dir) for y in glob(os.path.join(x[0],  '*'))]:
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()
    tlshctx = tlsh.Tlsh()
    ssdeepctx = ssdeep.Hash()
    with open(fn, 'rb') as f:
        size = os.fstat(f.fileno()).st_size
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            md5.update(data)
            sha1.update(data)
            sha256.update(data)
            tlshctx.update(data)
            ssdeepctx.update(data)
    h.add_hash(value=md5.hexdigest().upper(), hashtype='MD5')
    h.add_hash(value=sha1.hexdigest().upper(), hashtype='SHA-1')
    h.add_hash(value=sha256.hexdigest().upper(), hashtype='SHA-256')
    try:
        tlshctx.final()
        h.add_hash(value=tlshctx.hexdigest(), hashtype='TLSH')
    except:
        pass 
    h.add_hash(value=ssdeepctx.digest(), hashtype='SSDEEP')
    h.add_meta(key='FileName', value=fn)
    h.add_meta(key='FileSize', value=size)
    h.insert()
    print (fn)

