"""Loongson GS264E pin names"""

from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin

PW21 = Pin(0) # GPIO0/W21
GPIO0 = PW21
PAC25 = Pin(1) # GPIO1/AC25
GPIO1 = PAC25
PAB23 = Pin(2) # GPIO2/AB23
GPIO2 = PAB23
PAD26 = Pin(3) # GPIO3/AD26
GPIO3 = PAD26
PL21 = Pin(4) # GMAC1_RXD0/GPIO4/L21
GPIO4 = PL21
PL22 = Pin(5) # GMAC1_RXD1/GPIO5/L22
GPIO5 = PL22
PL23 = Pin(6) # GMAC1_RXD2/GPIO6/L23
GPIO6 = PL23
PK25 = Pin(7) # GMAC1_RXD3/GPIO7/K25
GPIO7 = PK25
PK24 = Pin(8) # GMAC1_RCTL/GPIO8/K24
GPIO8 = PK24
PL25 = Pin(9) # GMAC1_TXD0/GPIO9/L25
GPIO9 = PL25
PL26 = Pin(10) # GMAC1_TXD1/GPIO10/L26
GPIO10 = PL26
PM21 = Pin(11) # GMAC1_TXD2/GPIO11/M21
GPIO11 = PM21
PM22 = Pin(12) # GMAC1_TXD3/GPIO12/M22
GPIO12 = PM22
PM23 = Pin(13) # GMAC1_TCTL/GPIO13/M23
GPIO13 = PM23
PF10 = Pin(14) # SATA_LEDN/GPIO14/F10
GPIO14 = PF10
PW22 = Pin(16) # I2C0_SCL/GPIO16/W22
GPIO16 = PW22
PY23 = Pin(17) # I2C0_SDA/GPIO17/Y23
GPIO17 = PY23
PV20 = Pin(18) # I2C1_SCL/GPIO18/V20
GPIO18 = PV20
PAA24 = Pin(19) # I2C1_SDA/GPIO19/AA24
GPIO19 = PAA24
PY22 = Pin(20) # PWM0/GPIO20/Y22
GPIO20 = PY22
PAA23 = Pin(21) # PWM1/GPIO21/AA23
GPIO21 = PAA23
PAB25 = Pin(22) # PWM2/GPIO22/AB25
GPIO22 = PAB25
PAC26 = Pin(23) # PWM3/GPIO23/AC26
GPIO23 = PAC26
PW26 = Pin(24) # HDA_BITCLK/GPIO24/W26
GPIO24 = PW26
PU21 = Pin(25) # HDA_SYNC/GPIO25/U21
GPIO25 = PU21
PT20 = Pin(26) # HDA_RESETN/GPIO26/T20
GPIO26 = PT20
PY26 = Pin(27) # HDA_SDO/GPIO27/Y26
GPIO27 = PY26
PW25 = Pin(28) # HDA_SDI0/GPIO28/W25
GPIO28 = PW25
PV24 = Pin(29) # HDA_SDI1/GPIO29/V24
GPIO29 = PV24
PW24 = Pin(30) # HDA_SDI2/GPIO30/W24
GPIO30 = PW24
PAB24 = Pin(32) # CAN0_RX/GPIO32/AB24
GPIO32 = PAB24
PAA22 = Pin(33) # CAN0_TX/GPIO33/AA22
GPIO33 = PAA22
PAC24 = Pin(34) # CAN1_RX/GPIO34/AC24
GPIO34 = PAC24
PAD25 = Pin(35) # CAN1_TX/GPIO35/AD25
GPIO35 = PAD25
PF3 = Pin(36) # SDIO_DATA0/GPIO36/F3
GPIO36 = PF3
PH5 = Pin(37) # SDIO_DATA1/GPIO37/H5
GPIO37 = PH5
PH4 = Pin(38) # SDIO_DATA2/GPIO38/H4
GPIO38 = PH4
PE1 = Pin(39) # SDIO_DATA3/GPIO39/E1
GPIO39 = PE1
PG3 = Pin(40) # SDIO_CMD/GPIO40/G3
GPIO40 = PG3
PF2 = Pin(41) # SDIO_CLK/GPIO41/F2
GPIO41 = PF2
PB4 = Pin(44) # NAND_CEN0/GPIO44/B4
GPIO44 = PB4
PB5 = Pin(45) # NAND_CEN1/GPIO45/B5
GPIO45 = PB5
PD6 = Pin(46) # NAND_CEN2/GPIO46/D6
GPIO46 = PD6
PF8 = Pin(47) # NAND_CEN3/GPIO47/F8
GPIO47 = PF8
PA4 = Pin(48) # NAND_CLE/GPIO48/A4
GPIO48 = PA4
PC5 = Pin(49) # NAND_ALE/GPIO49/C5
GPIO49 = PC5
PA2 = Pin(50) # NAND_WRN/GPIO50/A2
GPIO50 = PA2
PE7 = Pin(51) # NAND_RDN/GPIO51/E7
GPIO51 = PE7
PD5 = Pin(52) # NAND_RDYN0/GPIO52/D5
GPIO52 = PD5
PB3 = Pin(53) # NAND_RDYN1/GPIO53/B3
GPIO53 = PB3
PA3 = Pin(54) # NAND_RDYN2/GPIO54/A3
GPIO54 = PA3
PC4 = Pin(55) # NAND_RDYN3/GPIO55/C4
GPIO55 = PC4
PB6 = Pin(56) # NAND_D0/GPIO56/B6
GPIO56 = PB6
PD7 = Pin(57) # NAND_D1/GPIO57/D7
GPIO57 = PD7
PF9 = Pin(58) # NAND_D2/GPIO58/F9
GPIO58 = PF9
PE8 = Pin(59) # NAND_D3/GPIO59/E8
GPIO59 = PE8
PC6 = Pin(60) # NAND_D4/GPIO60/C6
GPIO60 = PC6
PA5 = Pin(61) # NAND_D5/GPIO61/A5
GPIO61 = PA5
PA6 = Pin(62) # NAND_D6/GPIO62/A6
GPIO62 = PA6
PE9 = Pin(63) # NAND_D7/GPIO63/E9
GPIO63 = PE9

I2C0_SCL = PW22
I2C0_SDA = PY23
I2C1_SCL = PV20
I2C1_SDA = PAA24

SPI_CSN0 = 1000
SPI_CSN1 = 1001
SPI_CSN2 = 1002
SPI_CSN3 = 1003
SPI_SCK = 1004
SPI_SDI = 1005
SPI_SDO = 1006

UART0_RXD = 1010
UART0_TXD = 1011
UART3_RXD = 1012
UART3_TXD = 1013
UART4_RXD = 1014
UART4_TXD = 1015
UART5_RXD = 1016
UART5_TXD = 1017

PWM0 = 1020
PWM1 = 1021
PWM2 = 1022
PWM3 = 1023

# ordered as i2cId, SCL, SDA
i2cPorts = (
    (0, I2C0_SCL, I2C0_SDA),
    (1, I2C1_SCL, I2C1_SDA)
)

# ordered as spiId, sckId, mosiId, misoId
spiPorts = (
    (0, SPI_SCK, SPI_SDO, SPI_SDI),
)

# ordered as uartId, txId, rxId
uartPorts = (
    (0, UART0_TXD, UART0_RXD),
    (3, UART3_TXD, UART3_RXD),
    (4, UART4_TXD, UART4_RXD),
    (5, UART5_TXD, UART5_RXD),
)


pwmOuts = (
    ((0, 0), PWM0),
    ((1, 0), PWM1),
    ((2, 0), PWM2),
    ((3, 0), PWM3)
)