Gra Wordle

OPIS:

Zaimplementowanie wersji gry Wordle bazującej na słowach z języka angielskiego wraz z interefjsem graficznym oraz z możliwścią wprowadzania liter za pomocą wyklikiwania klawiszy z wyświetlanej klawiatury lub wpisywania ich z klawiatury.

INSTRUKCJA INSTALACJI:

Należy zainstalować Python 3.10.12 oraz bibliotekę pygame 2.5.2.

INSTRUKCJA UŻYTKOWNIKA:

Aby zagrać w grę należy uruchomić plik main.py. Wyświetlone zostanie okienko, w którym można wpisywać angielskie słowa pięcioliterowe za pomocą klawiatury komputerowej lub umieszczonej na ekranie. Jeśli słowo nie zostanie zaakceptowane przez program po naciśnięciu entera, gracz może je usunąć i ponowić próbę. 

Gracz ma 6 prób, aby zgadnąć hasło. Jeśli mu się nie uda, hasło zostanie wyświetlone na ekranie. Jeśli gracz wygrał, wszystkie literki zostaną podświetlone na zielono i wyświetli się napis 'YOU WON!'.

Podświetlenia liter we wpisanym przez gracza słowie na dane kolory mają stanowić wskazówkę, co do hasła zgodnie z zasadami standardowego Wordle:
- zielony - ta litera znajduje się w tym samym miejscu w haśle,
- żółty - ta litera znajduje się w haśle, ale nie w tym miejscu,
- szary - ta litera nie znajduje się w haśle.

Jeśli gracz wygrał i chce zagrać ponownie lub w trakcie gry znudził się, może za pomocą przycisku 'try again' rozegrać kolejną rozgrywkę. Jeśli garcz chce się poddać, może to uczynić za pomocą przycisku 'give up' i zostanie wyświetlone hasło.
