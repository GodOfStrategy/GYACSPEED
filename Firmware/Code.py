import time
import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import adafruit_sh1106
import adafruit_lsm6ds.lsm6dsl as LSM6DSL
import adafruit_gps

# --- I2C OLED setup ---
i2c = busio.I2C(board.SCL, board.SDA)
display_bus = displayio.I2CDisplay(i2c, device_address=0x3C)
oled = adafruit_sh1106.SH1106(display_bus, width=128, height=64)

# --- SPI IMU setup ---
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
imu_cs = board.D2   # Chip Select pin for IMU
lsm6dsl = LSM6DSL.LSM6DSL(spi, imu_cs)

# --- UART GPS setup ---
uart = busio.UART(board.TX, board.RX, baudrate=9600, timeout=1)
gps = adafruit_gps.GPS(uart, debug=False)
gps.send_command(b'PMTK220,1000')   # Update rate: 1 Hz
gps.send_command(b'PMTK314,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0')  # GPRMC only

# --- Display group ---
splash = displayio.Group()
oled.show(splash)

text_area = label.Label(terminalio.FONT, text="Init...", color=0xFFFFFF, x=0, y=10)
splash.append(text_area)

while True:
    # --- Read IMU ---
    accel_x, accel_y, accel_z = lsm6dsl.acceleration
    gyro_x, gyro_y, gyro_z = lsm6dsl.gyro

    # --- Read GPS ---
    gps.update()
    speed_kmh = None
    if gps.has_fix and gps.speed_knots is not None:
        speed_kmh = gps.speed_knots * 1.852  # knots → km/h

    # --- Update OLED ---
    text_lines = [
        f"Accel: {accel_x:.2f}, {accel_y:.2f}, {accel_z:.2f} m/s^2",
        f"Gyro: {gyro_x:.2f}, {gyro_y:.2f}, {gyro_z:.2f} dps",
        f"Speed: {speed_kmh:.2f} km/h" if speed_kmh else "Speed: ---"
    ]
    splash.pop()
    text_area = label.Label(terminalio.FONT, text="\n".join(text_lines), color=0xFFFFFF, x=0, y=10)
    splash.append(text_area)

    time.sleep(1)
