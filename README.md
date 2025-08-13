A feladatot Python nyelven írtam, a Selenium könyvtárat, azon belül pedig a pytest keretrendszert használtam. 

A függőségeket *pip install -r requriements.txt* parancs kiadásával lehet telepíteni. 
A szkript a *pytest .\test_search.py* *paranccsal* indítható. 

A *conftest.py* fixtureben bent hagytam kommentként a headless futtatási opciót is. Ezzel is teszteltem a működést.

A böngészősütik elfogadását kiszerveztem a *handle_cookies.py* fájlba mivel rejtett DOM modellt alkalmaz így hosszabb a funkcó. 

A szkript mindig a mai napot veszi alapnak. 

Az ellenőrzés a keresést követően az URL alapján történik. A szkript bővíthető még, hogy a találati listát is megfelelően ellenőrizze, de ez komolyabb tervezést igényel. 

A szkriptet a pytest-repeat könyvtárral többször lefuttattam, hogy ellenőrizzem a stabilitását. 
Tapasztalatok: 
- Az „Indulási” mező ajánlati listájának betöltése okoz problémát. Elképzelhető, hogy a sokszori próbálkozás miatt a weboldal lassítást alkalmaz. A TIMEOUT globális változó értékének növelésével elkerülhetők a webalkalmazás lassú betöltéséből adódó tesztbukások. 
- A többszöri driver-böngésző megnyitás során a sütik nem tisztulnak maguktól (driver bug?) ezért a kódban az oldal nyitása után törlöm a sütiket és így stabilabbá válik a szkript.
