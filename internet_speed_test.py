from speedtest import Speedtest

def byte_to_mbyte(bit):
    return bit / 1024 / 1024

st = Speedtest()

download_speed = int(byte_to_mbyte(st.download()))
upload_speed = int(byte_to_mbyte(st.upload()))
print('Your connection\'s download speed is: {} mbyte'.format(download_speed))
print('Your connection\'s upload speed is: {} mbyte'.format(upload_speed))
