import ctypes
import platform


if platform.architecture()[0]=='32bit':
    lzo1_dll = ctypes.cdll.LoadLibrary(r".\x86\cyglzo2-2.dll")
else:
    lzo1_dll = ctypes.cdll.LoadLibrary(r".\x64\cyglzo2-2.dll")

error_to_text = {
     0:'LZO_E_OK',
    -1:'LZO_E_ERROR',
    -2:'LZO_E_OUT_OF_MEMORY',
    -3:'LZO_E_NOT_COMPRESSIBLE',
    -4:'LZO_E_INPUT_OVERRUN',
    -5:'LZO_E_OUTPUT_OVERRUN',
    -6:'LZO_E_LOOKBEHIND_OVERRUN',
    -7:'LZO_E_EOF_NOT_FOUND',
    -8:'LZO_E_INPUT_NOT_CONSUMED',
}


__lzo1x_decompress          = lzo1_dll.lzo1x_decompress
__lzo1x_decompress.argtypes = [ctypes.c_char_p, ctypes.c_uint, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint)]
__lzo1x_decompress.restype  = ctypes.c_int


__lzo1x_1_compress          = lzo1_dll.lzo1x_1_compress
__lzo1x_1_compress.argtypes = [ctypes.c_char_p, ctypes.c_uint, ctypes.c_char_p, ctypes.POINTER(ctypes.c_uint),ctypes.c_char_p]
__lzo1x_1_compress.restype  = ctypes.c_int

def lzo1x_decompress(inBuffer,outBufferSize=65536):
    inBuffer_p = ctypes.cast(inBuffer,ctypes.c_char_p)
    result     = ctypes.create_string_buffer(b"\0" * outBufferSize)
    result_len = ctypes.c_uint(0)
        
    r = __lzo1x_decompress(inBuffer_p, len(inBuffer), result , ctypes.byref(result_len))
    return bytearray(result)[:result_len.value]


def lzo1x_1_compress(inBuffer):
    inBufferSize = len(inBuffer)
    inBuffer_p   = ctypes.cast(inBuffer,ctypes.c_char_p)
    workBuffer_p = ctypes.create_string_buffer(b"\0" * inBufferSize*2)
    result     = ctypes.create_string_buffer(b"\0" * inBufferSize*2)
    result_len = ctypes.c_uint(0)
        
    r = __lzo1x_1_compress(inBuffer_p, len(inBuffer), result , ctypes.byref(result_len), workBuffer_p)
    return bytearray(result)[:result_len.value]


