import requests #importacao da biblioteca requests para fazer requisicoes.                                                                  

API_key = "7ae42b4b67635f66bfe4464ec2a181ec"    #key do API openweathermap.org. 
base_url = "http://api.openweathermap.org/data/2.5/weather?"    #url para fazer as requisicoes.
 
zip_code = input("Qual é o Zip code (Obs:. ZIP CODE somente dos Estados Unidos): ") #input para zip code, só funciona zip code dos estados unidos.
Final_url = base_url + "appid=" + API_key + "&zip=" + zip_code  #url final para adquirir as requisicoes necessarias.
 
weather_data = requests.get(Final_url).json()   #requisicao feita atraves do url final
getTemperature = weather_data['main']['temp'] - 273.15  #requisicao da temperatura e o calculo da mesma em graus celsius.
getNameCity = weather_data['name']  #requisicao do nome da cidade que tem o zip code correspondente.
print("\nZIP CODE " + zip_code +":\n")  #print do zip code.
print(f"A temperatura da cidade {getNameCity} é {getTemperature}°C\n")  #print com nome e temperatura do zip code requerido.