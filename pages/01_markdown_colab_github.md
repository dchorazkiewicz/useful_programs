# 1. Markdown, Colab i GitHub

W tym bloku poznamy trzy narzędzia, które rozwiązują trzy różne problemy:

| Narzędzie | Do czego służy? |
| --- | --- |
| **Markdown** | do prostego zapisywania uporządkowanego tekstu, dokumentacji i raportów |
| **Google Colab** | do łączenia tekstu, kodu, obliczeń i wyników w jednym notebooku |
| **GitHub** | do przechowywania projektu, śledzenia zmian i współpracy |

Te trzy elementy bardzo dobrze ze sobą współpracują. Możemy przygotować opis w Markdown, wykonać obliczenia w Colabie, a następnie przechować źródła i wyniki w repozytorium GitHub.

---

# Markdown

## Co to jest Markdown?

**Markdown** to prosty język znaczników służący do formatowania zwykłego tekstu.

Najczęściej zapisujemy go w plikach z rozszerzeniem:

~~~text
.md
~~~

Przykłady:

~~~text
README.md
raport.md
notatki.md
~~~

Plik Markdown jest zwykłym plikiem tekstowym. Można go otworzyć praktycznie w każdym edytorze. Specjalne znaki, takie jak `#`, `*`, `-` czy backtick, informują program wyświetlający dokument, jak ma wyglądać tekst.

Warto od razu rozróżnić dwie rzeczy:

- **źródło Markdown** — tekst, który wpisujemy do pliku,
- **wyrenderowany dokument** — wygląd tego tekstu po interpretacji składni Markdown.

Na GitHubie możemy przełączać się między widokiem źródła i wyrenderowanym dokumentem.

## Nagłówki

Nagłówki budują strukturę dokumentu. Im więcej znaków `#`, tym niższy poziom nagłówka.

Źródło:

~~~markdown
# Tytuł dokumentu

## Główna sekcja

### Podsekcja
~~~

Efekt:

> # Tytuł dokumentu
>
> ## Główna sekcja
>
> ### Podsekcja

W praktyce jeden dokument powinien mieć jeden główny nagłówek `#`.

Dalsze części dokumentu organizujemy za pomocą `##`, `###` itd.

---

## Pogrubienie, kursywa i przekreślenie

Źródło:

~~~markdown
**tekst pogrubiony**

*tekst pochylony*

~~tekst przekreślony~~

***tekst pogrubiony i pochylony***
~~~

Efekt:

**tekst pogrubiony**

*tekst pochylony*

~~tekst przekreślony~~

***tekst pogrubiony i pochylony***

Wyróżnień warto używać oszczędnie. Jeśli wszystko jest pogrubione, nic nie jest naprawdę wyróżnione.

---

## Akapit i nowa linia

Nowy akapit tworzymy przez pozostawienie pustej linii.

Źródło:

~~~markdown
To jest pierwszy akapit.

To jest drugi akapit.
~~~

Efekt:

To jest pierwszy akapit.

To jest drugi akapit.

To ważna zasada: w Markdown pojedyncze naciśnięcie Enter nie zawsze oznacza nowy akapit.

---

## Listy punktowane

Źródło:

~~~markdown
- Markdown
- Colab
- GitHub
~~~

Efekt:

- Markdown
- Colab
- GitHub

Listy można zagnieżdżać:

~~~markdown
- GitHub
  - repozytorium
  - Issues
  - historia zmian
- Colab
  - tekst
  - kod
  - wyniki
~~~

Efekt:

- GitHub
  - repozytorium
  - Issues
  - historia zmian
- Colab
  - tekst
  - kod
  - wyniki

---

## Listy numerowane

Źródło:

~~~markdown
1. przygotuj dane,
2. wykonaj obliczenia,
3. zapisz wynik,
4. opisz wynik.
~~~

Efekt:

1. przygotuj dane,
2. wykonaj obliczenia,
3. zapisz wynik,
4. opisz wynik.

Listy numerowane są szczególnie przydatne przy opisie procedury lub instrukcji.

---

## Checklisty

GitHub obsługuje listy zadań.

Źródło:

~~~markdown
- [x] utworzono notebook
- [x] wykonano obliczenia
- [ ] sprawdzono wynik
~~~

Efekt:

- [x] utworzono notebook
- [x] wykonano obliczenia
- [ ] sprawdzono wynik

Checklisty bardzo dobrze nadają się do krótkich list kontrolnych w dokumentacji i GitHub Issues.

---

## Linki

Źródło:

~~~markdown
[GitHub](https://github.com/)
~~~

Efekt:

[GitHub](https://github.com/)

Zamiast wklejać długi adres do strony, warto umieścić go pod czytelną nazwą.

---

## Obrazy

Obraz osadzamy podobnie jak link, ale na początku dodajemy znak `!`.

Źródło:

~~~markdown
![Wykres zależności y od x](wykres.png)
~~~

Jeżeli plik `wykres.png` znajduje się w tym samym folderze co dokument Markdown, GitHub wyświetli obraz w miejscu tej instrukcji.

Jeżeli plik znajduje się w podfolderze `obrazy`, używamy ścieżki:

~~~markdown
![Wykres zależności y od x](obrazy/wykres.png)
~~~

Tekst w nawiasach kwadratowych jest opisem obrazu. Warto go uzupełniać — pomaga zrozumieć zawartość także wtedy, gdy obraz nie może zostać wyświetlony.

W projektach przechowywanych w repozytorium zwykle wygodniej używać **ścieżek względnych** niż pełnych adresów internetowych.

---

## Tabele

Źródło:

~~~markdown
| Narzędzie | Typ pliku | Zastosowanie |
| --- | --- | --- |
| Markdown | .md | dokumentacja |
| Colab | .ipynb | obliczenia |
| GitHub | repozytorium | historia projektu |
~~~

Efekt:

| Narzędzie | Typ pliku | Zastosowanie |
| --- | --- | --- |
| Markdown | `.md` | dokumentacja |
| Colab | `.ipynb` | obliczenia |
| GitHub | repozytorium | historia projektu |

Tabele są dobre do krótkich zestawień. Jeśli w komórkach pojawiają się długie akapity tekstu, zwykle lepiej wrócić do zwykłych sekcji i list.

---

## Kod w tekście

Nazwy plików, komendy i bardzo krótkie fragmenty kodu warto oznaczać pojedynczym backtickiem.

Źródło:

~~~markdown
Uruchom plik `analiza.py` i sprawdź wartość zmiennej `wynik`.
~~~

Efekt:

Uruchom plik `analiza.py` i sprawdź wartość zmiennej `wynik`.

---

## Bloki kodu

Większy fragment kodu umieszczamy w osobnym bloku.

Źródło:

~~~~markdown
```python
x = 5
y = x**2
print(y)
```
~~~~

Efekt działania kodu:

~~~text
25
~~~

Podanie nazwy języka, np. `python`, `bash`, `html` czy `json`, pozwala GitHubowi kolorować składnię.

W raporcie technicznym dobrze jest pokazać krótki fragment kodu, który jest istotny dla opisywanego wyniku. Nie trzeba kopiować do raportu całego programu.

---

## Cytaty

Źródło:

~~~markdown
> Wynik należy zawsze sprawdzić przed jego wykorzystaniem.
~~~

Efekt:

> Wynik należy zawsze sprawdzić przed jego wykorzystaniem.

Cytaty można wykorzystać także do krótkiego wyróżnienia komentarza lub uwagi.

---

## Matematyka

GitHub potrafi renderować wzory matematyczne.

Krótki wzór umieszczamy wewnątrz pojedynczych znaków dolara.

Źródło:

~~~markdown
Energia spoczynkowa dana jest wzorem $E=mc^2$.
~~~

Efekt:

Energia spoczynkowa dana jest wzorem $E=mc^2$.

Dłuższy wzór umieszczamy w osobnym bloku.

Źródło:

~~~markdown
$$
\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}
$$
~~~

Efekt:

$$
\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}
$$

Macierze zapisujemy wielowierszowo:

~~~markdown
$$
A=
\begin{pmatrix}
1 & 2 \\
3 & 4 \\
\end{pmatrix}
$$
~~~

Efekt:

$$
A=
\begin{pmatrix}
1 & 2 \\
3 & 4 \\
\end{pmatrix}
$$

W materiałach tego kursu używamy prostego zestawu reguł formatowania matematyki przygotowanego specjalnie tak, aby pliki dobrze renderowały się na GitHubie.

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

## Zrzut ekranu i transkrypcja

Czasem informacja istnieje tylko jako obraz: zrzut ekranu programu, zdjęcie tabeli, komunikat błędu albo fragment zeskanowanego dokumentu.

AI może pomóc przepisać zawartość obrazu do tekstu. Taki proces nazywamy tutaj **transkrypcją**.

Przykładowy workflow:

1. zachowujemy oryginalny obraz,
2. prosimy AI o przepisanie jego zawartości,
3. zapisujemy wynik w pliku tekstowym lub Markdown,
4. porównujemy transkrypcję z obrazem,
5. poprawiamy ewentualne błędy.

Największej ostrożności wymagają:

- liczby,
- wzory,
- nazwy plików,
- adresy,
- fragmenty kodu,
- komunikaty błędów.

Transkrypcja wygenerowana przez AI jest **wersją roboczą**, dopóki człowiek jej nie sprawdzi.

---

## Dobre materiały o Markdown

- [GitHub Docs — Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
- [GitHub Docs — Writing mathematical expressions](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions)
- [Markdown Guide — Basic Syntax](https://www.markdownguide.org/basic-syntax/)
- [Markdown Guide — Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

---

# Google Colab

## Co to jest Google Colab?

**Google Colab** jest działającym w przeglądarce środowiskiem opartym na notebookach Jupyter.

Notebook to dokument, który może zawierać jednocześnie:

- opis,
- wzory,
- kod,
- wyniki obliczeń,
- tabele,
- wykresy.

Notebook Colaba jest zwykle zapisywany jako plik:

~~~text
nazwa_notebooka.ipynb
~~~

Rozszerzenie `.ipynb` pochodzi od formatu Jupyter Notebook.

---

## Komórki

Notebook składa się z **komórek**.

Najczęściej używamy dwóch rodzajów:

### Komórka tekstowa

Służy do opisu obliczeń. Obsługuje Markdown.

Przykład zawartości:

~~~markdown
## Obliczenie pola koła

Dla promienia $r=3$ liczymy pole ze wzoru

$$
P=\pi r^2
$$
~~~

### Komórka kodu

Zawiera kod wykonywany przez środowisko.

Przykład:

~~~python
import math

r = 3
P = math.pi * r**2

print(P)
~~~

Efekt:

~~~text
28.274333882308138
~~~

Dobrze przygotowany notebook przeplata opis z kodem. Czytelnik powinien wiedzieć **co liczymy, dlaczego to liczymy i jaki otrzymaliśmy wynik**.

---

## Runtime, czyli środowisko wykonawcze

Notebook jest plikiem, ale kod musi zostać gdzieś wykonany.

Colab uruchamia dla notebooka osobne **środowisko wykonawcze** — runtime.

Można myśleć o nim jak o tymczasowym komputerze uruchomionym w chmurze.

W runtime znajdują się między innymi:

- pamięć zmiennych,
- uruchomiony Python,
- zainstalowane biblioteki,
- pliki wygenerowane podczas obliczeń.

Notebook i runtime to nie to samo.

Notebook można zachować, natomiast środowisko wykonawcze może zostać zamknięte lub zresetowane.

---

## Stan notebooka

Rozważmy dwie komórki.

Pierwsza:

~~~python
a = 10
~~~

Druga:

~~~python
print(a + 5)
~~~

Jeżeli wykonamy je w tej kolejności, otrzymamy:

~~~text
15
~~~

Jeżeli jednak zrestartujemy runtime i uruchomimy tylko drugą komórkę, zmienna `a` jeszcze nie istnieje i kod zakończy się błędem.

Dlatego notebook przed oddaniem powinien dać się wykonać **od początku do końca w prawidłowej kolejności**.

Dobra praktyka:

1. restart runtime,
2. uruchomienie wszystkich komórek od początku,
3. sprawdzenie, czy żadna komórka nie kończy się błędem.

---

## Tworzenie pliku w Colabie

Kod może wygenerować zwykły plik.

~~~python
wynik = 2 + 2

with open("wynik.txt", "w", encoding="utf-8") as f:
    f.write(str(wynik))
~~~

Powstanie plik:

~~~text
wynik.txt
~~~

o zawartości:

~~~text
4
~~~

To ważny przykład: kod nie musi tylko wyświetlać wyniku na ekranie. Może wygenerować plik, który następnie zapisujemy jako część projektu.

---

## Tworzenie wykresu

Przykład:

~~~python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, marker="o")
plt.xlabel("x")
plt.ylabel("x^2")
plt.grid()
plt.savefig("wykres.png", dpi=150, bbox_inches="tight")
plt.show()
~~~

Kod:

1. tworzy dane,
2. rysuje wykres,
3. zapisuje go jako `wykres.png`,
4. pokazuje wykres w notebooku.

Po wykonaniu komórki w plikach runtime pojawi się:

~~~text
wykres.png
~~~

Taki plik można później umieścić w repozytorium i osadzić w raporcie Markdown.

---

## Pliki w Colabie są tymczasowe

Pliki utworzone w runtime nie powinny być traktowane jako trwałe archiwum.

Jeżeli wygenerujemy:

~~~text
wynik.txt
wykres.png
dane.csv
~~~

należy zapisać potrzebne rezultaty w trwałym miejscu, np.:

- pobrać je na komputer,
- zapisać na Dysku Google,
- umieścić w repozytorium.

---

## Notebook jako dokument obliczenia

Dobry notebook powinien przypominać krótki raport, a nie przypadkowy zbiór komórek.

Prosty układ:

~~~text
Tytuł
↓
Cel
↓
Dane / parametry
↓
Kod
↓
Wynik
↓
Krótki komentarz
~~~

Czytelnik powinien móc otworzyć notebook i zrozumieć jego sens bez pytania autora, „co tutaj właściwie zrobiłeś?”.

---

## Dobre materiały o Colabie

- [Google Colab — oficjalne wprowadzenie](https://colab.research.google.com/notebooks/intro.ipynb?hl=pl)
- [Google Colab — FAQ](https://research.google.com/colaboratory/faq.html)

---

# Git i GitHub

## Git i GitHub to nie to samo

Te pojęcia są często mylone.

**Git** jest systemem kontroli wersji. Śledzi historię zmian w projekcie.

**GitHub** jest serwisem internetowym, który przechowuje repozytoria Git i dodaje narzędzia do współpracy: stronę projektu, Issues, Pull Requests, przeglądanie historii, komentarze i wiele innych funkcji.

Na początku kursu będziemy wykonywać większość operacji bezpośrednio przez stronę GitHub. Praca z Gitem w terminalu pojawi się później.

---

## Repozytorium

**Repozytorium** to projekt przechowywany razem z historią zmian.

Może zawierać:

~~~text
README.md
kod.py
dane.csv
wykres.png
raport.md
~~~

ale Git przechowuje także informacje o tym, jak projekt zmieniał się w czasie.

Repozytorium pozwala więc odpowiedzieć nie tylko na pytanie:

> Jak wygląda projekt teraz?

ale także:

> Jak doszliśmy do tej wersji?

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

## Dobre materiały o Git i GitHubie

- [GitHub Docs — About Git](https://docs.github.com/en/get-started/using-git/about-git)
- [GitHub Docs — About repositories](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories)
- [GitHub Docs — Forks](https://docs.github.com/en/pull-requests/reference/forks)
- [GitHub Docs — Commits](https://docs.github.com/en/pull-requests/reference/commits)
- [GitHub Docs — About issues](https://docs.github.com/en/issues/tracking-your-work-with-issues/learning-about-issues/about-issues)

---

# Pierwszy mały workflow

Policzmy sumę kwadratów liczb od 1 do 100:

$$
S=\sum_{k=1}^{100} k^2
$$

W Colabie możemy użyć:

~~~python
n = 100
suma = sum(k**2 for k in range(1, n + 1))

print(suma)
~~~

Efekt:

~~~text
338350
~~~

Ten sam wynik możemy sprawdzić ze wzoru:

$$
\sum_{k=1}^{n} k^2 = \frac{n(n+1)(2n+1)}{6}
$$

Dla $n=100$ otrzymujemy:

$$
S=338350
$$

Następnie zapisujemy wartość do pliku:

~~~python
with open("wynik.txt", "w", encoding="utf-8") as f:
    f.write(str(suma))
~~~

Powstaje plik:

~~~text
wynik.txt
~~~

o zawartości:

~~~text
338350
~~~

Mamy teraz trzy reprezentacje tej samej pracy:

1. **kod** — pokazuje, jak policzono wynik,
2. **plik wynikowy** — przechowuje konkretny rezultat,
3. **opis Markdown** — wyjaśnia, co zostało zrobione.

---

# Zadania dla studenta

Wszystkie rozwiązania z tego bloku umieść w folderze:

~~~text
zadania/01_markdown_colab_github/
~~~

Po wykonaniu wszystkich zadań folder powinien zawierać:

~~~text
zadania/01_markdown_colab_github/
├── README.md
├── colab_intro.ipynb
├── wynik.txt
├── wykres.png
├── raport.md
├── zrzut.png
├── transkrypcja.md
└── historia.md
~~~

Nie zmieniaj nazw wymaganych plików.

---

## Zadanie 1. README w Markdown

Utwórz plik `README.md`.

Plik ma zawierać:

- tytuł,
- krótki opis bloku,
- co najmniej jeden fragment **pogrubiony**,
- co najmniej jeden fragment *pochylony*,
- co najmniej jeden fragment ~~przekreślony~~,
- listę punktowaną,
- listę numerowaną,
- checklistę,
- tabelę,
- link do strony Google Colab,
- krótki fragment kodu,
- jeden wzór matematyczny inline,
- jeden wzór jako osobny blok.

Dodaj również tabelę:

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
