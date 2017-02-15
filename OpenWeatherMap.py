# Подключаем библиотеку pyowm
import pyowm
# Выводим на экран название программы
print('OpenWeatherMap')
# Инициализируем библиотеку API ключом
owm = pyowm.OWM('8f76462df5bf27afef40ebcaa122f2cd')
# Получаем данные из Ростова-на-Дону
observation = owm.weather_at_place('Rostov-on-Don,rus')
observation1 = owm.weather_at_place('Moscow,rus')
# Получаем погодные данные
weather = observation.get_weather()
weather1 = observation1.get_weather()
# Получаем данные местоположения
location = observation.get_location()
location1 = observation1.get_location()
# Создаем словарь для перевода названия города
translate = {'Rostov-na-Donu': 'Ростов-на-Дону', 'Moscow': 'Москва'}

print(owm)
print(observation)
print(weather)
print(location)

print('----------------------------------')
print('Страна: ' + location.get_country())
print('Город: ' + location.get_name())
print('Долгота: ' + str(location.get_lon()))
print('Широта: ' + str(location.get_lat()))
print('Облачность: ' + str(weather.get_clouds()))
print('Статус: ' + str(weather.get_detailed_status()))
print('Давление:' + str(weather.get_pressure()))
print('Дождь: ' + str(weather.get_rain()))
print('Снег: ' + str(weather.get_snow()))
print('Время: ' + str(weather.get_reference_time('iso')))
print('Статус: ' + str(weather.get_status()))
print('Восход: ' + str(weather.get_sunrise_time('iso')))
print('Закат:' + str(weather.get_sunset_time('iso')))
print('Температура: ' + str(weather.get_temperature('celsius')))
print('Видимость: ' + str(weather.get_visibility_distance()))
print('Изображение: ' + weather.get_weather_icon_name())
print('Ветер: ' + str(weather.get_wind()))
print('----------------------------------')

# Создадим функцию, которая определяет облачность
def WhatIsCloudness():
    if 0 <= weather.get_clouds() <= 10:
        return 'ясная'
    if 10 < weather.get_clouds() <= 30:
        return 'немного облачная'
    if 30 < weather.get_clouds() <= 70:
        return 'пасмурная'
    if 70 < weather.get_clouds() <= 100:
        return 'мрачная'

# Выводим на экран данные в дружелюбном формате
print('Погода в городе ' + translate[location.get_name()] + ' ' + WhatIsCloudness() + ', температура ' + str(weather.get_temperature('celsius')['temp']) + ' градусов Цельсия, ' + 'скорость ветра ' + str(weather.get_wind()['speed']) + ' м/с.')
print('Погода в городе ' + translate[location1.get_name()] + ' ' + WhatIsCloudness() + ', температура ' + str(weather1.get_temperature('celsius')['temp']) + ' градусов Цельсия, ' + 'скорость ветра ' + str(weather1.get_wind()['speed']) + ' м/с.')
