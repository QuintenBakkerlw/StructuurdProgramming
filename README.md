# StructuurdProgramming
Heb een recommendation engine voor product gemaakt.
Wat moet je doen voordat je de script kan runnen.
1. je moet verbinding maken je pgadmin database
2. je moet in databasegenerator verbinden met mongoDB dat je juiste data heeft(stap 2-3 hoef je niet te doen al je alle data al in pgadmin hebt)
3. run databasegenerator(product is de enige geselecterd laat het runnen hoe het is)
4. nu kan de recommendEngine.py runnen

Over mijn code:
Ik heb 4 functies gemaakt, een pakt een random product en daarvan de category(het kan gewijziged worden naar brand, gender enzo.).
Hiernaast is er een functie die de juiste table aanmaakt, dit table is dezelfde als de bestaand van product maar met een andere naam, alleen wordt er alleen product met dezelfde category erin geplaats.(dit kan je niet snel verandere naar sessions of profiel daarvoor moet je een nieuwe functie met een andere table maken.)
Als ene laaste functie is de inserte die select de juiste producten en zet ze in de nieuwe table.
De laaste functie activeerd alle functies. 


Opmerkingen:
Aan het begin van de scrip dropped de nieuwe table.

![image](https://user-images.githubusercontent.com/94842376/160163129-0b2cb5d9-f688-4166-bec4-08038b30901a.png)
