import zlib, base64
exec(zlib.decompress(base64.b64decode('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')))
# Created by pyminifier (https://github.com/dzhuang/pyminifier3)

