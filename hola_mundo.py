def hola_mundo (idioma):
    traducciones = {
    "es": "hola mundo",
    "en": "hello world",
    "fr": "bonjour le monde",
    "de": "halo welt",
    "it": "ciao mondo",
    "ja": "こんにちは世界",
    "ar": "مرحبا بالعالم"
    }

    if idioma in traducciones:
        print (traducciones[idioma])
    else:
        print("idioma no detectado")
    
    print (hola_mundo("es"))
    print (hola_mundo("en"))
    print (hola_mundo("fr"))
    print (hola_mundo("de"))
    print (hola_mundo("it"))
    print (hola_mundo("ja"))
    print (hola_mundo("ar"))
    
