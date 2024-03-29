#!/usr/bin/env python3

# -*- coding: utf-8 -*-
#
# (c) Copyright 2022 Sensirion AG, Switzerland
#
#     THIS FILE IS AUTOMATICALLY GENERATED!
#
# Generator:    sensirion-driver-generator 0.9.0
# Product:      scd30
# Version:      None
#

import time
from sensirion_i2c_driver import LinuxI2cTransceiver, I2cConnection, CrcCalculator
from sensirion_i2c_adapter.i2c_channel import I2cChannel
from sensirion_i2c_scd30.device import Scd30Device

with LinuxI2cTransceiver('/dev/i2c-1') as i2c_transceiver:
    channel = I2cChannel(I2cConnection(i2c_transceiver),
                         slave_address=0x61,
                         crc=CrcCalculator(8, 0x31, 0xff, 0x0))
    sensor = Scd30Device(channel)
    try:
        sensor.stop_periodic_measurement()
        sensor.soft_reset()
        time.sleep(2.0)
    except BaseException:
        ...
    major, minor = sensor.read_firmware_version()
    print(f"firmware version major: {major}; minor: {minor};")

    sensor.start_periodic_measurement(0)
    while True:
        try:
            time.sleep(1.5)
            (co2_concentration, temperature, humidity) = sensor.blocking_read_measurement_data()
            print(f"co2_concentration: {co2_concentration}; temperature: {temperature}; humidity: {humidity}; ")
        except BaseException:
            pass
    sensor.soft_reset()

    # time.sleep(1.5)
    # (co2_concentration, temperature, humidity) = sensor.blocking_read_measurement_data()
    # print(f"co2_concentration: {co2_concentration}; temperature: {temperature}; humidity: {humidity}; ")

    # sensor.soft_reset()
    