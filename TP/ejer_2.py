class SteelSheet:
    def __init__(self, thickness, width, rolling_mill):
        self.thickness = thickness
        self.width = width
        self.rolling_mill = rolling_mill

    def produce_sheet(self):
        self.rolling_mill.produce_sheet(self.thickness, self.width)

class RollingMill:
    def produce_sheet(self, thickness, width):
        pass

class FiveMeterRollingMill(RollingMill):
    def produce_sheet(self, thickness, width):
        print(f"Lámina de acero de {thickness}'' de espesor y {width} metros de ancho producida en tren laminador de 5 mts.")

class TenMeterRollingMill(RollingMill):
    def produce_sheet(self, thickness, width):
        print(f"Lámina de acero de {thickness}'' de espesor y {width} metros de ancho producida en tren laminador de 10 mts.")

class SteelSheetProducer:
    def __init__(self, rolling_mill):
        self.rolling_mill = rolling_mill

    def produce_steel_sheet(self, thickness, width):
        sheet = SteelSheet(thickness, width, self.rolling_mill)
        sheet.produce_sheet()

# Ejemplo de uso
five_meter_rolling_mill = FiveMeterRollingMill()
ten_meter_rolling_mill = TenMeterRollingMill()

steel_sheet_producer_5m = SteelSheetProducer(five_meter_rolling_mill)
steel_sheet_producer_10m = SteelSheetProducer(ten_meter_rolling_mill)

# Producción de láminas de acero de 0.5'' de espesor y 1.5 metros de ancho
steel_sheet_producer_5m.produce_steel_sheet(0.5, 1.5)
steel_sheet_producer_10m.produce_steel_sheet(0.5, 1.5)
