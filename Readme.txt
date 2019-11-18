välkommen till skafferiet!

Det saknas tyvärr vissa delar av systemet pga. tidsbrist, har ej
hunnit få klart funktioner för att räkna av ingredienserna när
systemet plockar ett recept. Har inte fått min middagstips funktion
att riktigt fungera som den ska.

-----------------------------------------------------------------------

Main.py filen är den dom styr och startar gui.
allt gå via gui men länkas till terminalen.
så all input och output går terminalen.

-----------------------------------------------------------------------

Filen user_input.py innehåller funtioner för input av varor samt
inmatning av recept.

-----------------------------------------------------------------------

Filen format.py innehåller funktioner för konvertering sortering m.m

-----------------------------------------------------------------------

Filen recipe.py innehåller funktioner för läsning och hämtning av 
information från .txt filerna.

-----------------------------------------------------------------------

Textfilerna Recipe_list.txt, Storage_list.txt är filer för att spara 
informationen så man slipper starta om början varje gång man startar systemet.

-----------------------------------------------------------------------

Textfilen Shop_list.txt får information tilldelad genom functionen dinner_tip
samt att den rensas inför varje nytt middagstips då det konstant ska bli 
en ny inköpslista så inte gamla ingredienser står kvar för inhandling

