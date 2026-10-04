# Zadania dla studenta: Markdowna

Wszystkie rozwiązania z tego bloku umieść w folderze:

~~~text
zadania/01_markdown/
~~~

Po wykonaniu wszystkich zadań folder powinien zawierać minimalnie:

~~~text
zadania/01_markdown_colab_github/
├── README.md
├── colab_intro.ipynb
├── wynik.txt
├── wykres.png
├── raport.md
├── zrzut.png
└── historia.md
~~~

Nie zmieniaj nazw wymaganych plików.

---

## Zadanie 1. README w Markdown

Utwórz plik `README.md`.

Plik ma zawierać:

- tytuł,
- krótki tekst,
- co najmniej jeden fragment **pogrubiony**,
- co najmniej jeden fragment *pochylony*,
- co najmniej jeden fragment ~~przekreślony~~,
- listę punktowaną,
- listę numerowaną,
- checklistę,
- tabelę,
- link do strony Google Colab link: [http://colab.research.google.com](http://colab.research.google.com)
- krótki fragment kodu,
- jeden wzór matematyczny inline,
- jeden wzór jako osobny blok.

Dodaj równie

~~~markdown
| Plik | Opis |
| --- | --- |
| README.md | opis rozwiązania |
| colab_intro.ipynb | notebook |
| wynik.txt | wynik obliczenia |
| wykres.png | wykres |
| raport.md | raport |
~~~

Po zapisaniu pliku otwórz jego wyrenderowany widok na GitHubie i sprawdź, czy wszystkie elementy wyglądają poprawnie.

### Sprawdzenie

Będzie można automatycznie sprawdzić między innymi:

- istnienie `README.md`,
- obecność wymaganych elementów Markdown,
- obecność tabeli i checklisty,
- podstawową strukturę pliku.

---

## Zadanie 2. Notebook Colab

Utwórz notebook `colab_intro.ipynb`.

Notebook ma zawierać co najmniej:

1. komórkę Markdown z tytułem,
2. komórkę Markdown z krótkim opisem obliczenia,
3. komórkę kodu liczącą sumę kwadratów liczb od 1 do 100,
4. komórkę kodu zapisującą wynik do `wynik.txt`,
5. komórkę kodu tworzącą wykres $y=k^2$ dla $k=1,\ldots,20$,
6. zapis wykresu do `wykres.png`.

Kod obliczenia:

~~~python
n = 100
suma = sum(k**2 for k in range(1, n + 1))

print(suma)
~~~

Efekt:

~~~text
338350
~~~

Kod zapisujący plik:

~~~python
with open("wynik.txt", "w", encoding="utf-8") as f:
    f.write(str(suma))
~~~

Plik `wynik.txt` ma zawierać dokładnie:

~~~text
338350
~~~

Przykładowy kod wykresu:

~~~python
import matplotlib.pyplot as plt

x = list(range(1, 21))
y = [k**2 for k in x]

plt.plot(x, y, marker="o")
plt.xlabel("k")
plt.ylabel("k^2")
plt.grid()
plt.savefig("wykres.png", dpi=150, bbox_inches="tight")
plt.show()
~~~

Na końcu:

1. zrestartuj runtime,
2. uruchom wszystkie komórki od początku,
3. upewnij się, że notebook nie zgłasza błędów,
4. dodaj notebook, `wynik.txt` i `wykres.png` do repozytorium.

### Sprawdzenie

Będzie można sprawdzić między innymi:

- istnienie notebooka,
- obecność komórek Markdown i Code,
- zawartość `wynik.txt`,
- istnienie `wykres.png`,
- strukturę notebooka.

---

## Zadanie 3. Raport z kodem i wynikiem

Utwórz `raport.md`.

Raport ma mieć strukturę:

~~~markdown
# Raport

## Cel

## Metoda

## Kod

## Wynik

## Wniosek
~~~

W sekcji **Kod** wstaw fragment kodu wykorzystanego w notebooku.

W sekcji **Wynik**:

- podaj wartość 338350,
- osadź `wykres.png`,
- zapisz wzór na sumę kwadratów.

W sekcji **Wniosek** napisz 3–5 własnych zdań odpowiadających na pytania:

1. Co zostało policzone?
2. Co przedstawia wykres?
3. Dlaczego warto przechowywać kod i wynik, a nie tylko zrzut ekranu?

To zadanie będzie sprawdzane zarówno pod kątem struktury pliku, jak i sensu krótkiego opisu.

---

## Zadanie 4. Zrzut ekranu i transkrypcja

W Colabie wyświetl fragment notebooka zawierający:

- kod obliczający sumę,
- wynik `338350`.

Wykonaj zrzut ekranu i zapisz go jako `zrzut.png`.

Następnie użyj narzędzia AI do przepisania informacji widocznej na zrzucie.

Wynik zapisz jako `transkrypcja.md`.

Plik ma zawierać:

~~~markdown
# Transkrypcja

## Tekst wygenerowany przez AI

...

## Sprawdzenie ręczne

...

## Poprawiona wersja

...
~~~

W części **Sprawdzenie ręczne** napisz krótko, czy AI przepisało materiał bezbłędnie. Jeśli pojawił się błąd, wskaż go.

W części **Poprawiona wersja** umieść ostateczną, sprawdzoną transkrypcję.

### Sprawdzenie

Będzie można porównać:

- istnienie `zrzut.png`,
- strukturę `transkrypcja.md`,
- zgodność transkrypcji z obrazem,
- obecność informacji o ręcznej kontroli.

---

## Zadanie 5. Historia pracy

Nie wykonuj całego bloku jako jednego commita.

Przygotuj co najmniej trzy logiczne commity, np.:

~~~text
01: dodaj README
01: dodaj notebook i wyniki
01: dodaj raport i transkrypcję
~~~

Następnie utwórz `historia.md` i przygotuj tabelę:

~~~markdown
| Commit | Co zmieniłem? | Dlaczego? |
| --- | --- | --- |
| ... | ... | ... |
~~~

Wpisz co najmniej trzy swoje commity. W pierwszej kolumnie podaj ich skrócone identyfikatory.

Na końcu utwórz w swoim repozytorium Issue o tytule:

~~~text
[01] Gotowe do sprawdzenia
~~~

W Issue dodaj:

- krótką informację, że blok jest gotowy,
- link do folderu `zadania/01_markdown_colab_github/`,
- checklistę wszystkich wymaganych plików.

Przykład:

~~~markdown
- [x] README.md
- [x] colab_intro.ipynb
- [x] wynik.txt
- [x] wykres.png
- [x] raport.md
- [x] zrzut.png
- [x] transkrypcja.md
- [x] historia.md
~~~

### Sprawdzenie

Będzie można sprawdzić:

- liczbę i treść commitów,
- istnienie `historia.md`,
- strukturę tabeli,
- istnienie Issue,
- kompletność checklisty.

---

# Checklista końcowa

Przed zgłoszeniem bloku sprawdź:

- [ ] wszystkie pliki znajdują się w `zadania/01_markdown_colab_github/`,
- [ ] nazwy plików są dokładnie zgodne z instrukcją,
- [ ] `README.md` poprawnie renderuje się na GitHubie,
- [ ] wszystkie linki działają,
- [ ] wzory matematyczne renderują się poprawnie,
- [ ] notebook wykonuje się od początku po restarcie runtime,
- [ ] `wynik.txt` zawiera dokładnie `338350`,
- [ ] `wykres.png` otwiera się poprawnie,
- [ ] `raport.md` wyświetla wykres,
- [ ] `transkrypcja.md` została ręcznie sprawdzona,
- [ ] historia zawiera co najmniej trzy sensowne commity,
- [ ] Issue `[01] Gotowe do sprawdzenia` zostało utworzone.
