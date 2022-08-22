import winlzo


with open('plain_text.txt','rb') as infile, open('compressed.lzo','wb') as outfile:
    outfile.write( winlzo.lzo1x_1_compress(infile.read()) )

with open('compressed.lzo','rb') as infile, open('decompressed.txt','wb') as outfile:
    outfile.write( winlzo.lzo1x_decompress(infile.read()) )

