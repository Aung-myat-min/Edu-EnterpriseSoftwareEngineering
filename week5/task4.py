class WeatherForecast:
    skie = ""
    high = 0
    low = 0

    def set_skies(self, skie):
        self.skie = skie

    def set_high(self, high):
        self.high = high

    def set_low(self, low):
        self.low = low

    def get_skies(self):
        return self.skie

    def get_high(self):
        return self.high

    def get_low(self):
        return self.low


class ForecastHandler:

    def process_forecast(self):
        daily_forecast = WeatherForecast()

        daily_forecast.set_skies("Partly Cloudy")
        daily_forecast.set_high(22)
        daily_forecast.set_low(15)

        print("Today's Skies:", daily_forecast.get_skies())
        print("High Temperature:", daily_forecast.get_high())
        print("Low Temperature:", daily_forecast.get_low())


handler = ForecastHandler()
handler.process_forecast()