# 1. Markdown, Colab i GitHub

Ten blok otwiera cały kurs. Chodzi o opanowanie prostego workflow, który będzie później wracał prawie wszędzie:

**plik → repozytorium → zmiana → commit → wynik → opis → feedback**

Nie trzeba jeszcze znać terminala ani programować. Na tym etapie wystarczy przeglądarka, GitHub i Google Colab.

## Co warto umieć po tym bloku

Po wykonaniu materiału student powinien umieć:

- utworzyć fork repozytorium,
- poruszać się po strukturze plików i folderów,
- edytować pliki Markdown,
- zapisywać kolejne wersje pracy jako commity,
- odczytać historię zmian,
- utworzyć i opisać Issue,
- przygotować prosty notebook w Google Colab,
- połączyć opis, kod i wynik w jednym materiale,
- zapisać wynik obliczeń jako plik,
- osadzić grafikę w raporcie Markdown,
- przygotować materiały tak, aby inna osoba lub automat mogły je sprawdzić.

---

# Markdown

## Po co nam Markdown?

Markdown to zwykły plik tekstowy, w którym kilka prostych znaków określa strukturę dokumentu.

Plik:

~~~text
raport.md
~~~

może zawierać nagłówki, listy, linki, tabele, wzory matematyczne, obrazy i fragmenty kodu. GitHub renderuje taki plik jako czytelny dokument.

To dobry format do:

- notatek,
- instrukcji,
- raportów,
- dokumentacji kodu,
- opisów projektów,
- prowadzenia dziennika pracy.

Najważniejsza zaleta: **źródło jest nadal zwykłym tekstem**. Można je łatwo czytać, poprawiać, porównywać i wersjonować.

## Nagłówki

~~~markdown
# Tytuł dokumentu

## Główna sekcja

### Mniejsza sekcja
~~~

Dobra zasada: jeden dokument powinien mieć jeden główny tytuł.

## Wyróżnienia

~~~markdown
**tekst pogrubiony**

*tekst pochylony*

~~tekst przekreślony~~
~~~

co wyświetli nam: **tekst pogrubiony**, *tekst pochylony*, ~~tekst przekreślony~~.

W dokumentacji technicznej warto używać wyróżnień oszczędnie. Pogrubienie ma pomagać znaleźć najważniejszą informację, a nie zastępować strukturę dokumentu.

## Listy

Lista punktowana:

~~~markdown
- pierwszy element,
- drugi element,
- trzeci element.
~~~

Lista numerowana:

~~~markdown
1. pobierz dane,
2. wykonaj obliczenia,
3. zapisz wynik,
4. opisz rezultat.
~~~

Lista zadań:

~~~markdown
- [x] utworzono plik,
- [x] wykonano obliczenia,
- [ ] sprawdzono wynik.
~~~

Checklisty są bardzo użyteczne w GitHub Issues i przy kontroli kompletności projektu.

## Linki

~~~markdown
[GitHub](https://github.com/)
~~~

Dobrze opisany link jest lepszy niż wklejony długi adres.

## Obrazy

Obraz znajdujący się w tym samym repozytorium można osadzić względną ścieżką:

~~~markdown
![Opis wykresu](wykres.png)
~~~

Jeżeli plik znajduje się w podfolderze:

~~~markdown
![Opis wykresu](obrazy/wykres.png)
~~~

Warto używać ścieżek względnych. Dzięki temu dokument działa również po wykonaniu forka lub sklonowaniu repozytorium.

## Tabele

~~~markdown
| Narzędzie | Zastosowanie |
| --- | --- |
| Markdown | dokumentacja |
| Colab | notebooki i obliczenia |
| GitHub | wersjonowanie i współpraca |
~~~

To 

Tabele są wygodne do krótkich zestawień. Długiego opisu lepiej nie wciskać do tabeli.

## Kod w Markdown

Krótki fragment kodu można wyróżnić wewnątrz zdania, a większy fragment umieścić w osobnym bloku.

~~~python
x = 5
y = x**2
print(y)
~~~

Po potrójnych znakach otwierających blok warto podać język, np. Python, Bash, HTML lub JSON. GitHub wtedy koloruje składnię.

W raporcie często warto pokazać tylko **istotny fragment kodu**, a pełny kod pozostawić w osobnym pliku lub notebooku.

## Matematyka

Na GitHubie używamy prostych, bezpiecznych zapisów.

Krótki wzór zapisujemy pomiędzy pojedynczymi znakami dolara, np. $E=mc^2$.

Dłuższy wzór zapisujemy w osobnym bloku:

$$
S = 1 + 2 + 3 + \ldots + n
$$

W tym repozytorium stosujemy następujące zasady:

- matematyka w tekście: pojedyncze dolary,
- matematyka w osobnym bloku: podwójne dolary,
- podwójne dolary zawsze stoją w osobnych liniach,
- przed i po bloku matematycznym zostawiamy pustą linię,
- nie używamy składni z nawiasami poprzedzonymi ukośnikiem,
- dla macierzy używamy środowiska pmatrix,
- nie umieszczamy wielowierszowych konstrukcji matematycznych wewnątrz pojedynczych dolarów.

Przykład macierzy:

$$
A=
\begin{pmatrix}
1 & 2 \\
3 & 4 \\
\end{pmatrix}
$$

Markdown powinien być sprawdzany również po wyrenderowaniu na GitHubie. Plik poprawny w edytorze nie zawsze musi wyglądać identycznie w przeglądarce.

## README.md

Plik **README.md** jest szczególny. GitHub automatycznie pokazuje go jako stronę opisową folderu lub repozytorium.

Dobry README odpowiada krótko na pytania:

- co to jest,
- do czego służy,
- jak tego użyć,
- gdzie znajdują się najważniejsze pliki,
- jaki jest aktualny stan pracy.

W tym kursie README będzie również pełnił rolę małego panelu informacyjnego studenta.

## Zrzut ekranu to nie dokumentacja źródłowa

Zrzut ekranu bywa przydatny, ale nie powinien zastępować tekstu, kodu ani danych.

Jeżeli na zrzucie znajduje się ważny komunikat, tabela albo fragment instrukcji, warto zachować:

1. obraz źródłowy,
2. tekstową transkrypcję,
3. krótki opis, czego dotyczy materiał.

AI może pomóc przepisać tekst ze zrzutu, ale wynik należy sprawdzić. To szczególnie ważne dla liczb, nazw plików, kodu i komunikatów błędów.

---

# Google Colab

## Czym jest notebook?

Google Colab pozwala tworzyć notebooki zapisane jako pliki **.ipynb**.

Notebook może łączyć:

- tekst,
- wzory,
- kod,
- wynik działania kodu,
- wykresy,
- krótkie komentarze.

Dzięki temu obliczenie nie musi być oderwane od opisu.

Typowy układ:

1. tytuł i cel,
2. dane lub parametry,
3. kod,
4. wynik,
5. krótki komentarz.

## Dwa podstawowe typy komórek

W praktyce najczęściej używamy:

- komórek **Text / Markdown**,
- komórek **Code**.

Komórka tekstowa wyjaśnia, co robimy. Komórka kodowa wykonuje operację.

Dobry notebook nie powinien być serią przypadkowych komórek z kodem. Osoba, która otworzy go za miesiąc, powinna wiedzieć, po co wykonano dane obliczenie.

## Kolejność wykonywania komórek ma znaczenie

Notebook pamięta wyniki wykonanych komórek. Można więc przypadkiem stworzyć notebook, który działa tylko dlatego, że komórki uruchomiono wcześniej w nietypowej kolejności.

Dlatego przed oddaniem pracy warto wykonać test:

**Runtime → Restart session → Run all**

Jeżeli notebook po restarcie wykonuje się od początku do końca bez ręcznych poprawek, jest znacznie bardziej wiarygodny.

## Pliki utworzone w Colabie

Kod może wygenerować plik:

~~~python
wynik = 2 + 2

with open("wynik.txt", "w", encoding="utf-8") as f:
    f.write(str(wynik))
~~~

Taki plik istnieje w bieżącej sesji Colaba. Trzeba go następnie pobrać albo zapisać w trwałym miejscu.

Środowisko Colab jest tymczasowe. Po zakończeniu sesji pliki przechowywane wyłącznie w środowisku wykonawczym mogą zniknąć.

## Notebook i repozytorium

Notebook można przechowywać w GitHubie tak samo jak inne pliki.

W praktyce interesują nas dwa elementy:

- plik **.ipynb** jako źródło obliczenia,
- wygenerowane wyniki, np. **.txt**, **.csv**, **.png** lub **.html**.

Dzięki temu można osobno sprawdzić kod i osobno jego rezultat.

---

# GitHub

## Repozytorium

Repozytorium to uporządkowany zbiór plików wraz z historią ich zmian.

W tym kursie repozytorium studenta jest jednocześnie:

- miejscem wykonywania zadań,
- historią pracy,
- miejscem przechowywania wyników,
- dokumentacją,
- podstawą do sprawdzania zadań.

## Fork

Fork tworzy własną kopię repozytorium na GitHubie.

Schemat:

**repozytorium kursu → fork → repozytorium studenta**

Student pracuje we własnym forku. Dzięki temu może zmieniać pliki bez naruszania repozytorium bazowego.

## Commit

Commit zapisuje konkretny stan zmian.

Dobry commit powinien odpowiadać jednej sensownej zmianie.

Lepsze komunikaty:

~~~text
01: dodaj raport Markdown
01: dodaj notebook Colab
01: popraw ścieżkę do wykresu
~~~

Słabsze komunikaty:

~~~text
zmiany
update
aaa
final final
~~~

Historia commitów powinna pozwalać zrozumieć, jak rozwijała się praca.

## Historia zmian

GitHub pozwala zobaczyć:

- kto wykonał zmianę,
- kiedy ją wykonano,
- które pliki zmieniono,
- co dokładnie dodano lub usunięto.

To jedna z najważniejszych różnic między zwykłym folderem z plikami a repozytorium.

W pracy naukowej i technicznej historia zmian bywa równie cenna jak aktualna wersja pliku.

## Issues

Issue to uporządkowany wątek dotyczący konkretnego zadania, problemu lub poprawki.

Issue może zawierać:

- opis problemu,
- checklistę,
- linki do plików,
- uwagi prowadzącego,
- informację o poprawkach,
- dyskusję,
- informację o zaliczeniu.

W tym kursie Issues będą jednym z głównych kanałów feedbacku.

Przykładowa checklista:

~~~markdown
- [x] README.md
- [x] colab_intro.ipynb
- [x] wynik.txt
- [x] wykres.png
- [ ] raport.md
- [x] historia.md
~~~

---

# Organizacja plików ma znaczenie

Przy automatycznym lub półautomatycznym sprawdzaniu bardzo ważne są przewidywalne nazwy plików.

Jeżeli instrukcja wymaga pliku:

~~~text
zadania/01_markdown_colab_github/wynik.txt
~~~

to pliki:

~~~text
wynik2.txt
Wynik.txt
wynik_ostateczny.txt
mojwynik.txt
~~~

nie są tym samym plikiem.

W zadaniach kursowych należy więc:

- zachowywać podane nazwy folderów,
- zachowywać podane nazwy plików,
- nie przenosić rozwiązania do innego miejsca,
- nie zastępować pliku źródłowego zrzutem ekranu,
- sprawdzać linki i ścieżki względne,
- usuwać przypadkowe pliki tymczasowe.

To nie jest biurokracja. W prawdziwych projektach dokładnie od tego zależy, czy kolejne narzędzie potrafi znaleźć dane wejściowe.

---

# Minimalny workflow na tym etapie

Na razie wystarczy następujący sposób pracy:

1. otwórz własny fork repozytorium,
2. znajdź właściwy folder zadania,
3. utwórz lub zmodyfikuj plik,
4. sprawdź jego podgląd,
5. wykonaj commit z czytelnym komunikatem,
6. jeżeli pracujesz w Colabie, zapisz notebook i pobierz wygenerowane pliki,
7. dodaj wyniki do repozytorium,
8. sprawdź, czy wszystkie linki i obrazy działają,
9. otwórz Issue informujące o gotowości do sprawdzenia.

W kolejnych blokach ten workflow rozszerzymy o terminal, Git, VS Code, Codespaces i pracę agentową.

---

# Zadania dla studenta

Wszystkie rozwiązania z tego bloku umieść w folderze:

~~~text
zadania/01_markdown_colab_github/
~~~

Po zakończeniu folder powinien zawierać:

~~~text
zadania/01_markdown_colab_github/
├── README.md
├── colab_intro.ipynb
├── wynik.txt
├── wykres.png
├── raport.md
└── historia.md
~~~

Nie zmieniaj nazw wymaganych plików.

## Zadanie 1. README jako karta pracy

Utwórz plik **README.md**, który będzie krótką kartą Twojej pracy w tym bloku.

Plik ma zawierać:

- tytuł,
- 2–4 zdania wprowadzenia,
- sekcję **Narzędzia**,
- listę co najmniej trzech narzędzi użytych w bloku,
- tabelę z kolumnami **Plik** i **Opis**,
- link do strony Google Colab,
- checklistę wszystkich zadań z tego bloku,
- jeden krótki fragment kodu,
- jeden krótki wzór zapisany inline,
- jeden wzór zapisany jako osobny blok matematyczny.

README ma być czytelny po wyrenderowaniu bezpośrednio na GitHubie.

### Kryterium zaliczenia

Automat powinien móc znaleźć wymagane elementy, a prowadzący powinien móc szybko zrozumieć strukturę rozwiązania.

---

## Zadanie 2. Notebook, który produkuje wynik

Utwórz w Google Colab notebook **colab_intro.ipynb**.

Notebook ma zawierać:

1. komórkę Markdown z tytułem i krótkim opisem,
2. komórkę kodu obliczającą sumę kwadratów liczb od 1 do 100,
3. komórkę kodu zapisującą wynik do pliku **wynik.txt**,
4. komórkę kodu tworzącą wykres zależności $y=k^2$ dla $k=1,ldots,20$,
5. zapis wykresu do pliku **wykres.png**.

Do obliczenia sumy można użyć:

~~~python
n = 100
suma = sum(k**2 for k in range(1, n + 1))
print(suma)
~~~

Plik wynikowy ma zawierać wyłącznie liczbę:

~~~text
338350
~~~

Przykładowy zapis wyniku:

~~~python
with open("wynik.txt", "w", encoding="utf-8") as f:
    f.write(str(suma))
~~~

Do wykresu można wykorzystać:

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

Po zakończeniu wykonaj restart środowiska i uruchom cały notebook od początku.

Do repozytorium dodaj:

- **colab_intro.ipynb**,
- **wynik.txt**,
- **wykres.png**.

### Kryterium zaliczenia

- notebook istnieje,
- zawiera komórki Markdown i Code,
- plik **wynik.txt** istnieje,
- jego zawartość to dokładnie 338350,
- plik **wykres.png** istnieje i nie jest pusty.

---

## Zadanie 3. Krótki raport techniczny

Utwórz plik **raport.md**.

Raport ma zawierać dokładnie następujące główne sekcje:

~~~markdown
# Raport

## Cel

## Kroki

## Kod

## Wynik

## Wniosek
~~~

W sekcji **Kod** umieść fragment kodu użytego do obliczenia sumy lub wygenerowania wykresu.

W sekcji **Wynik**:

- podaj otrzymaną wartość sumy,
- osadź plik **wykres.png** jako obraz.

W sekcji **Wniosek** napisz 3–5 zdań. Wyjaśnij własnymi słowami:

- co zostało policzone,
- co przedstawia wykres,
- dlaczego zapisanie kodu i wyniku w repozytorium jest lepsze niż przesłanie samego zrzutu ekranu.

To zadanie będzie sprawdzane zarówno strukturalnie, jak i pod kątem sensu krótkiej narracji.

---

## Zadanie 4. Historia pracy i GitHub Issues

Praca nad blokiem ma zostać podzielona na co najmniej trzy sensowne commity.

Zalecany minimalny układ:

~~~text
01: dodaj README
01: dodaj notebook i wyniki
01: dodaj raport
~~~

Następnie utwórz plik **historia.md** zawierający tabelę:

~~~markdown
| Commit | Co zrobiłem | Dlaczego |
| --- | --- | --- |
| ... | ... | ... |
~~~

Wpisz co najmniej trzy commity. W pierwszej kolumnie podaj ich skrócone identyfikatory.

Na końcu utwórz w swoim repozytorium Issue o tytule:

~~~text
[01] Gotowe do sprawdzenia
~~~

W Issue dodaj checklistę wszystkich sześciu wymaganych plików oraz link do folderu rozwiązania.

### Kryterium zaliczenia

- istnieje **historia.md**,
- tabela zawiera co najmniej trzy wpisy,
- repozytorium ma sensowną historię zmian,
- istnieje Issue **[01] Gotowe do sprawdzenia**,
- Issue zawiera checklistę i link do rozwiązania.

---

# Checklista przed zgłoszeniem

Przed utworzeniem Issue sprawdź:

- [ ] wszystkie wymagane pliki znajdują się w poprawnym folderze,
- [ ] nazwy plików są dokładnie zgodne z instrukcją,
- [ ] README renderuje się poprawnie na GitHubie,
- [ ] wzory matematyczne nie wyświetlają błędów,
- [ ] notebook wykonuje się od początku po restarcie sesji,
- [ ] **wynik.txt** zawiera dokładnie 338350,
- [ ] **wykres.png** otwiera się poprawnie,
- [ ] obraz jest widoczny wewnątrz **raport.md**,
- [ ] historia zawiera co najmniej trzy sensowne commity,
- [ ] utworzono Issue **[01] Gotowe do sprawdzenia**.

Po tym bloku najważniejsze nie jest zapamiętanie całej składni Markdown. Ważniejsze jest opanowanie nawyku:

**tworzę → zapisuję → sprawdzam → dokumentuję → wersjonuję → zgłaszam do weryfikacji.**
