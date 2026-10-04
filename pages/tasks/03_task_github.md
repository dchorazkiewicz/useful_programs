# Zadania: GitHub (z Codespace)

**Folder na rozwiązania:** [`pages/solutions/03_sol_github/`](../solutions/03_sol_github/) (ścieżka względem głównego katalogu repozytorium).

## Zadanie 1.

Wejdź do sforkowanego repozytorium poprzez stronę GitHub i uruchom **Codespace** w przeglądarce (czyli odpal VS Code w przeglądarce). Nie realizuj tego poprzez standardową edycję plików na GitHub tylko znajdź przycisk **Code**, a następnie wybierz **Open with Codespaces** i poczekaj jak odpali ci się przeglądarka z Visual Studio Code wewnętrz GitHub.

**Uwaga:** Aby poprawnie wykonać to zadanie, należy zapoznać się z materiałami wykładowymi w pliku `04_vscode.md`, po omówieniu lokalnej instalacji VS Code.

## Zadanie 2.

Stwórz nowy plik `codespace.md` w folderze `pages/solutions/03_sol_github/` i umieść w nim listę 10 komiksowych lub manga/anime postaci.

Stwórz nowy plik `codespace.py` w folderze `pages/solutions/03_sol_github/` i umieść w nim przykładowy kod Pythona.

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

Zatwierdź zmiany (`Commit & Push`) by wysłać je do repozytorium.

Sprawdź w innej zakładce przeglądarki, ponownie poprzez stronę GitHub (github.com a nie Codespace), czy plik `codespace.md` oraz `codespace.py` został dodany do repozytorium.

## Zadanie 4.

W podfolderze [`pages/solutions/03_sol_github/merge/`](../solutions/03_sol_github/merge/) znajdują się trzy ikonografiki w rozszerzeniu `png`. Kliknij jedną z nich, a następnie znajdź "Toggle Chat" (skrót `Ctrl+Alt+I`)  w Codespace, i poproś w prawym oknie AI o "zmergowanie" tych plików do pojedynczego pdfa o nazwie `ikonografiki.pdf`, zapisanego w folderze `pages/solutions/03_sol_github/`. Sugestia: *"merge all PNG files in the merge folder into a single PDF named ikonografiki.pdf."*

## Zadanie 5.

Przykładowy raport znajduje się w pliku [`pages/solutions/03_sol_github/document.md`](../solutions/03_sol_github/document.md). Używając Toggle Chat (skrót `Ctrl+Alt+I`) w Codespace, poproś AI o przekształcenie zawartości tego pliku i zapisanie go obok w folderze  `pages/solutions/03_sol_github/` w nowych formatach: jako `document.docx` oraz `document.pdf` przy użyciu biblioteki `pandoc`. Sugestia: kliknij na plik w Explorerze po lewej stronie a po prawej cześci ekranu w Chat wpisz *"export document.md to document.docx and document.pdf using pandoc."*
