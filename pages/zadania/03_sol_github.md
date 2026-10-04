# Zadania: Github

## Zadanie 1.

Wejdź do sforkowanego repozytorium poprzez stronę GitHub i uruchom Codespace w przeglądarce (czyli odpal VS Code w przeglądarce).

## Zadanie 2,

Stwórz nowy plik `codespace.md` w folderze `pages/zadania/03_sol_github` i umieść w nim listę 10 komiksowych postaci.

Stwórz nowy plik `codespace.py` w folderze `pages/zadania/03_sol_github` i umieść w nim przykładowy kod Pythona.

```python
import turtle
import random
turtle.bgcolor('black')
turtle.colormode(255)
turtle.speed(0)
for x in range(500):
    r,b,g=random.randint(0,255),random.randint(0,255),random.randint(0,255)
    turtle.pencolor(r,g,b)
    turtle.fd(x+50)
    turtle.rt(91)
turtle.exitonclick()
```

## Zadanie 3.

Wykonaj `commit and push` czyli `Zatwierdź zmiany i wyślij je` do repozytorium.

Sprawdź w innej zakładce przeglądarki, ponownie poprzez stronę GitHub (github.com a nie Codespace), czy plik `codespace.md` oraz `codespace.py` został dodany do repozytorium.

## Zadanie 4.

W podfolderze `pages/zadania/...` znajdują się trzy ikonografiki w rozszerzeniu `png`. Znajdź "Chat" w Codespace, i poproś AI o "zmergowanie" tych plików do pojedyńczego pdfa o nazwie `ikonografiki.pdf`.

## Zadanie 5.

W folderze `pages/zadania/...` znajduje się plik `document.md`. Używając Chata w Codespace, poproś AI o przekształcenie zawartości tego pliku do formatu pdf i zapisanie go jako `document.docx` oraz `document.pdf` przy użyciu biblioteki `pandoc`.
