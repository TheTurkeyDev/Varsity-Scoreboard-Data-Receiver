import board
import busio
import digitalio
import sx1280

CS = digitalio.DigitalInOut(board.GP17)
RESET = digitalio.DigitalInOut(board.GP21)
BUSY = digitalio.DigitalInOut(board.GP22)

# Initialize SPI
spi = busio.SPI(board.GP18, MOSI=board.GP19, MISO=board.GP16)

radio = sx1280.SX1280(spi, CS, RESET, BUSY, 2.4)

# Prepare radio for Rx
radio.listen = True

while True:
    msg = radio.receive()
    if msg != None:
        print(msg, radio.packet_status)
        time.sleep(1)