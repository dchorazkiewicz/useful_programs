# Git i GitHub

## Git i GitHub to nie to samo

Te pojęcia są często mylone.

**Git** jest systemem kontroli wersji. Śledzi historię zmian w projekcie.

**GitHub** to serwis internetowy dostępny przez przeglądarkę pod adresem [https://github.com/](https://github.com/), który przechowuje repozytoria Git i dodaje narzędzia do współpracy: stronę projektu, Issues, Pull Requests, przeglądanie historii, komentarze i wiele innych funkcji.

Na początku kursu będziemy wykonywać większość operacji bezpośrednio przez stronę GitHub. Praca z Gitem w terminalu pojawi się później, a tak naprawdę to skupimy się na Visual Studio Code (VS Code), który oferuje graficzny interfejs do Gita.

---

## Repozytorium

**Repozytorium** to projekt przechowywany razem z historią zmian. Może zawierać pliki, foldery i podfoldery, a Git przechowuje także informacje o tym, jak projekt zmieniał się w czasie.

Przykładowa struktura repozytorium:

~~~text
README.md
kod.py
dane.csv
wykres.png
raport.md
~~~

Repozytorium pozwala więc odpowiedzieć nie tylko na pytanie:

> Jak wygląda projekt teraz?

ale także:

> Jak doszliśmy do tej wersji?

---

## Założenie repozytorium

Wejdź na stronę GitHub i załóż konto, jeśli jeszcze go nie masz.

Następnie załóż repozytorium np. o nazwie: `testowe_repozytorium`.

### Public vs Private

Podczas zakładania repozytorium musisz wybrać jego widoczność:

- **Public** — repozytorium jest widoczne dla każdego w internecie. Każdy może je przeglądać i klonować oraz proponować zmiany, np. przez fork i Pull Request. Bezpośrednia edycja wymaga odpowiednich uprawnień. Dobre do portfolio, projektów edukacyjnych i open source.
- **Private** — repozytorium jest widoczne tylko dla Ciebie i osób, które zostaną dodane jako współpracownicy. Dobre do prywatnych projektów, zadań szkolnych lub materiałów, których nie chcesz udostępniać publicznie.

GitHub daje też dodatkowe opcje przy tworzeniu repozytorium:

- **Add a README** — utworzy plik `README.md` z opisem projektu (**sugestia:** zawsze go dodaj, bo GitHub wyświetla jego zawartość na stronie repozytorium),
- **Add .gitignore** — doda plik `.gitignore` z regułami pozwalającymi pomijać niepotrzebne pliki, np. zawartość `__pycache__`, pliki środowiskowe lub dane tymczasowe (teraz nie musisz go dodawać, ale w przyszłości może się przydać),
- **Choose a license** — pozwala wybrać licencję, która określa, jak inni mogą używać kodu projektu.

W praktyce: jeśli chcesz pokazać swój projekt innym, wybierz **Public**; jeśli projekt ma być tylko dla Ciebie lub dla małego zespołu, wybierz **Private**.

---

## Współpraca z innymi osobami

Mimo że możesz wybrać repozytorium prywatne, to w praktyce często będziesz współpracować z innymi osobami. GitHub pozwala na to w prosty sposób:

Na stronie repozytorium wybierz **Settings → Access → Collaborators → Add people**, aby zaprosić osobę, która ma konto na GitHubie. Po przyjęciu zaproszenia będzie mogła przeglądać i zmieniać repozytorium.

---

## Fork

**Fork** to własna kopia istniejącego repozytorium utworzona na koncie użytkownika i pozostająca powiązana z repozytorium źródłowym.

Schemat:

~~~text
repozytorium prowadzącego
          ↓
         fork
          ↓
repozytorium studenta
~~~

Po wykonaniu forka student może zmieniać własną kopię bez zmieniania repozytorium prowadzącego.

---

## Klonowanie (cloning)

W celu pracy z repozytorium lokalnie na swoim komputerze należy je **sklonować**. Oznacza to pobranie wszystkich plików i historii zmian. Omówimy to w kolejnych blokach zajęć, ale na razie wystarczy wiedzieć, że można to zrobić w terminalu lub w VS Code.

---

## Commit

**Commit** to zapis konkretnego zestawu zmian w historii repozytorium.

Commit zawiera między innymi:

- zmienione pliki,
- informację o autorze,
- datę,
- unikalny identyfikator,
- komunikat opisujący zmianę.

Przykładowe komunikaty:

~~~text
01: dodaj raport Markdown
01: dodaj notebook Colab
01: popraw opis wykresu
~~~

Takie komunikaty są czytelne, ponieważ mówią, **co zostało zrobione**.

Mało użyteczne komunikaty:

~~~text
zmiany
update
poprawka
final
final2
~~~

Lepiej zapisywać kilka logicznych etapów pracy niż całość jednym wielkim commitem na końcu.

---

## Dodawanie i edytowanie plików przez przeglądarkę

Na początku kursu możesz dodawać i poprawiać pliki bezpośrednio na stronie GitHub. Poniższe ćwiczenia wykonuj we własnym repozytorium lub forku, w którym masz uprawnienia do zapisu i możesz zapisywać zmiany bezpośrednio w wybranej gałęzi, zwykle `main`.

### Przesyłanie gotowego pliku

Załóżmy, że masz na komputerze plik `raport.md` i chcesz dodać go do repozytorium.

1. Otwórz repozytorium i folder, w którym chcesz umieścić plik.
2. Wybierz **Add file → Upload files**.
3. Przeciągnij `raport.md` do okna przesyłania lub wybierz go przez **choose your files**.
4. Sprawdź, czy na liście znajduje się właściwy plik.
5. Wpisz komunikat commita, np. `dodaj raport Markdown`, i zatwierdź zapis zgodnie z instrukcją poniżej.

Tak samo możesz przesłać notebook: pobierz go z Colaba jako plik `.ipynb`, a następnie wybierz ten plik podczas przesyłania. Możesz też dodać plik z danymi lub wykresem.

### Tworzenie pliku Markdown na GitHubie

Plik możesz również utworzyć bezpośrednio w przeglądarce.

1. Otwórz docelowy folder w repozytorium.
2. Wybierz **Add file → Create new file**.
3. Wpisz nazwę pliku, np. `notatka.md`.
4. W polu edycji wpisz treść w Markdownie, np.:

~~~markdown
# Notatka z obliczeń

## Cel

Obliczenie pola koła dla promienia r = 3.

## Wynik

Pole koła wynosi około 28,27.
~~~

5. Otwórz **Preview**, aby sprawdzić wygląd tekstu.
6. Kliknij **Commit changes…**, wpisz komunikat, np. `dodaj notatkę z obliczeń`, i zatwierdź zapis.

### Edytowanie istniejącego pliku

1. Otwórz plik `raport.md` lub `notatka.md` w repozytorium.
2. Kliknij ikonę ołówka — **Edit this file**.
3. Popraw treść, np. dodaj opis wyniku lub popraw literówkę.
4. Sprawdź wygląd tekstu w **Preview**.
5. Kliknij **Commit changes…**, wpisz komunikat, np. `popraw opis wyniku`, i zatwierdź zapis.

---

## Historia zmian

GitHub pozwala otworzyć historię pliku lub całego repozytorium.

Możemy sprawdzić:

- kto wykonał zmianę,
- kiedy ją wykonano,
- jaki był komunikat commita,
- które linie dodano,
- które linie usunięto.

Porównanie dwóch wersji pliku nazywamy często **diffem**.

Przykładowo zmiana:

~~~diff
- wynik = 12
+ wynik = 13
~~~

oznacza, że stara linia została usunięta, a w jej miejsce dodano nową.

---

## README.md

`README.md` to zwykły plik Markdown, ale GitHub traktuje go szczególnie: automatycznie pokazuje jego zawartość na stronie repozytorium lub folderu.

Dobry README powinien szybko odpowiadać na pytania:

- co znajduje się w tym miejscu,
- do czego służą pliki,
- jak uruchomić projekt,
- gdzie znajduje się wynik,
- jakie są najważniejsze informacje dla osoby, która widzi projekt pierwszy raz.

Przykładowa bardzo mała struktura:

~~~markdown
# Analiza danych

Krótki opis projektu.

## Pliki

- `analiza.py` — kod,
- `dane.csv` — dane wejściowe,
- `wykres.png` — wynik.

## Uruchomienie

Uruchom `analiza.py`.

## Wynik

Najważniejszy wynik wynosi 12.4.
~~~

README nie musi być długi. Ma przede wszystkim pozwolić szybko zrozumieć projekt.

---

## Issue

**Issue** to osobny wątek związany z repozytorium.

Może służyć jako:

- zgłoszenie błędu,
- lista rzeczy do wykonania,
- pytanie,
- miejsce feedbacku,
- informacja o gotowości zadania do sprawdzenia.

Issue ma tytuł i opis, a później może być uzupełniane komentarzami.

Przykład opisu Issue:

~~~markdown
## Lista plików

- [x] README.md
- [x] colab_intro.ipynb
- [x] wynik.txt
- [x] wykres.png
- [ ] raport.md
~~~

Po wyrenderowaniu:

### Lista plików

- [x] README.md
- [x] colab_intro.ipynb
- [x] wynik.txt
- [x] wykres.png
- [ ] raport.md

Issue można zamknąć, gdy sprawa została rozwiązana.

---

## Uwaga co do Issues w GitHubie

Issues w sforkowanym przez Ciebie repozytorium mają szczególne znaczenie w naszym kursie. Tam znajdą się informacje zwrotne o jakości wykonania zadań. Trzeba będzie je czytać i reagować na komentarze prowadzącego.

Konieczne jest **włączenie Issues** w Twoim repozytorium. W tym celu wejdź w **Settings → Features** (trzeba przewinąć w dół) i zaznacz **Issues**.

---

## Dobre materiały o Git i GitHubie

- [GitHub Docs — About Git](https://docs.github.com/en/get-started/using-git/about-git)
- [GitHub Docs — About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)
- [GitHub Docs — Forks](https://docs.github.com/en/pull-requests/reference/forks)
- [GitHub Docs — Commits](https://docs.github.com/en/pull-requests/reference/commits)
- [GitHub Docs — About issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues)
- [GitHub Docs — dodawanie plików](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)
- [GitHub Docs — tworzenie plików](https://docs.github.com/en/repositories/working-with-files/managing-files/creating-new-files)
- [GitHub Docs — edytowanie plików](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files)
