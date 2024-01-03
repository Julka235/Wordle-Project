DOKUMENTACJA

Autor:
Julia Czosnek 331367

Cel:
Zaimplementowanie wersji gry Wordle bazującej na słowach z języka angielskiego wraz z interefjsem graficznym oraz z możliwścią wprowadzania liter za pomocą wyklikiwania klawiszy z wyświetlanej klawiatury lub wpisywania ich z klawiatury.

Opis projektu:
Projekt jest podzielony na plik classes.py, gdzie znajdują się klasy zajmujące się logiką i zasadami gry oraz main.py, który korzysta z classes.py i wyświetla interfejs graficzny pozwalający na grę. Plik classes.py korzysta z plików tekstowych:
-- guesswords.txt - do generowania haseł (pobrany z https://github.com/LaurentLessard/wordlesolver/blob/main/solutions_nyt.txt, następnie poddany edycji),
-- valid_words.txt - do sprawdzania, czy słowo może zostać wprowadzone (pobrany z https://gist.github.com/dracos/dd0668f281e685bad51479e5acaadb93, następnie poddany edycji).
Plik test_classes.py służy do przetestowania klas i funkcji znajdujących się w pliku classes.py.

Podział programu na klasy:
W pliku classes.py:
-- Database - pobiera listę słów z pliku tekstowego pod podaną ścieżką, weryfikując równocześnie ich poprawność, długość oraz zapisujując je capslockiem. Lista to jest następnie sortowana alfabetycznie (na potrzeby szybszego przeszukiwania).
-- Guesswords - dziedziczy po Database; pobiera listę możliwych haseł (guesswords.txt) oraz umożliwia generację losowego hasła
-- ValidWords - dziedziczy po Database; pobiera listę poprawnych słów (validg_words.txt) oraz pozwala na szybkie sprawdzenie, czy dane słowo jest w bazie poprawnych słów
-- Solution - zajmuje się logiką pojedynczej gry Wordle wykorzystując powyższe klasy - generuje hasło dla danej rozgrywki oraz dla wprowadzonego słowa informuje, na jakie kolory należy pomalować dane okienka (zgodnie z zasadami standardowego Wordle).
W pliku main.py:
-- Button - umożliwia stworzenie guzika i wyświetlenie go na ekranie

Instrukcka użytkownika:
Aby zagrać w grę należy uruchomić plik main.py. Wyświetlone zostanie okienko, w którym można wpisywać angielskie słowa pięcioliterowe za pomocą klawiatury komputerowej lub umieszczonej na ekranie. Jeśli słowo nie zostanie zaakceptowane przez program po naciśnięciu entera, gracz może je usunąć i ponowić próbę. Gracz ma 6 prób, aby zgadnąć hasło. Jeśli mu się nie uda, hasło zostanie wyświetlone na ekranie. Jeśli gracz wygrał, wszystkie literki zostaną podświetlone na zielono i wyświetli się napis 'YOU WON!'.
Jeśli gracz wygrał i chce zagrać ponownie lub w trakcie gry znudził się, może za pomocą przycisku 'try again' rozegrać kolejną rozgrywkę. Jeśli garcz chce się poddać, może to uczynić za pomocą przycisku 'give up' i zostanie wyświetlone hasło.

Część refleksyjna:
Nieprzewidzianą przeszkodą, na którą natrafiłam było początkowe błędne zrozumienie zasad, według których Wordle decyduje, na jaki kolor należy podświetlić daną literę we wpisanym słowie. Na przykład, jeśli zostanie wprowadzone słowo 'ABACK', a hasłem byłoby 'EVADE' należy podświetlić na zielono drugie 'A', a w pierwotnej wersji mojego projektu zakładałam, że należy zaznaczyć pierwsze 'A' na żółto.
Względem oryginalnego planu projektu udało mi się zrealizować wszystko, co zamierzałam. Poza oryginalnym planem dodałam guziki umożliwiające rezygnację z gry ('give up') oraz rozegranie nowej rozgrywki ('try again')
