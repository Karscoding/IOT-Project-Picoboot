# Picoboot Team 2023

# - Info -

Deze Repository bevat de bestanden voor het IOT Project van de Hanzehogeschool HBO-ICT eerstejaars
Van Projectgroep 1H.
Dit project heeft meerdere onderdelen. (Dashboard, Simulator en ESP32).

# - Algemeen -

Om dit project goed te kunnen gebruiken moet je eerst zorgen dat je alle benodigdheden op je computer hebt.
Dit kun je doen met behulp van de "requirements.txt". Hierin staan alle "pip installs" die nodig zijn.
Dit is te doen met de volgende command in je terminal.

pip install -r requirements.txt

# - Dashboard -

Om de Dashboard te runnen kun je simpelweg "dashboard.py" uit "/dashboard/" runnen met python.
Dit kan werkend gemaakt worden met de ESP32 sensor informatie als de ESP32 de bijpassende bestanden heeft en
de server van app.py gestart is met python.
Om de Dashboard te kunnen gebruiken moet er een PIN ingevoerd worden. Deze bevat op dit moment "1234" maar kan
veranderd worden naar keuze in de code.

# - Simulator -

De simulator is "simulator.py" dit is te runnen door hem te openen met python.
Ook is hier een tweede uitgave van waarin de simulator zich gedraagd op base van data uit een database.
Deze heet "datasim.py", deze versie van de simulator is ook te openen met een knop in het dashboard.

# - Server -

De server is nodig om communicatie tussen de ESP32 en Dashboard levend te maken.
De bedoeling is dus dat deze server altijd op de achtergrond aan staat.

# - Copyright -

Alle code in deze repository is zelf geschreven door mensen in projectgroep 1H.
Iedereen in deze groep heeft wel minstens een beetje toegevoegd aan elk bestand
Waardoor elk bestand gezamenlijk is gemaakt.
Projectgroep 1H bevat :

Julian Kloosterhuis
Lucas Bruins
Kars hekman
David Warris
Kaj ter Velde
Rick Dwarshuis.

Repository Aanmaak - Mar. 28, 2023
Repository Afsluit - Jul. 7, 2023
