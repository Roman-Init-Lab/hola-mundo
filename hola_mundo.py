def hola_mundo (idioma):
    traducciones = {
    "es": "hola mundo",
    "en": "hello world",
    "fr": "bonjour le monde",
    "de": "hallo welt",
    "it": "ciao mondo",
    "ja": "こんにちは世界",
    "ar": "مرحبا بالعالم"
    }

    if idioma in traducciones:
        print (traducciones[idioma])
    else:
        print("idioma no detectado")

    
hola_mundo("es")
hola_mundo("en")
hola_mundo("fr")
hola_mundo("de")
hola_mundo("it")
hola_mundo("ja")
hola_mundo("ar")
