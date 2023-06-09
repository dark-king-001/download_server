import Worker as wk
import sys
chunk_size = 100 #mbs

# python3 download.py <path> <link>

# In this command:
# -x8, -s8, and -j8 are options that specify the number of connections to be used for downloading the file. In this case, we're using 8 connections for each server, and the maximum number of connections is also set to 8.
# --split=8 and --min-split-size=100M are options that control the size of the individual chunks of the file that are downloaded simultaneously. In this case, we're using 8 chunks of at least 100 MB each.
# --dir=/path/to/download/location is an option that specifies the directory where the downloaded file should be saved.
# "http://example.com/file.zip" is the URL of the file to be downloaded.

try:
    wk.Worker('aria2c -x8 -s8 -j8 --split=8 --min-split-size=100M ' + f'--dir='+ sys.argv[1] + ' ' + sys.argv[2])
except Exception as e:
    # Handle other exceptions here
    print(f"Error: {e}")
