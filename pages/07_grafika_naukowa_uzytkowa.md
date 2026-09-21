# 7. Grafika naukowa i użytkowa

Grafika w pracy naukowej może być wykresem danych, schematem aparatury, diagramem zależności, ilustracją koncepcyjną albo elementem prezentacji.

Nie każdą grafikę tworzymy tym samym narzędziem.

| Narzędzie | Zastosowanie |
| --- | --- |
| **Inkscape** | grafika wektorowa, schematy, diagramy |
| **AI image tools** | ilustracje koncepcyjne, warianty i infografiki |
| **IrfanView** | konwersja, skalowanie i operacje wsadowe |
| **TikZ** | diagramy zintegrowane z LaTeX-em |
| **TikZiT** | wizualna edycja wybranych diagramów TikZ |

---

# Raster i wektor

## Grafika rastrowa

Grafika rastrowa składa się z pikseli.

Typowe formaty:

~~~text
PNG
JPG
GIF
TIFF
~~~

Obraz:

~~~text
1200 × 800 px
~~~

ma 1200 pikseli w poziomie i 800 w pionie.

Raster dobrze nadaje się do:

- zdjęć,
- zrzutów ekranu,
- obrazów generowanych przez AI,
- wyników symulacji zapisanych jako obraz.

Jeżeli mały raster mocno powiększymy, zaczniemy widzieć piksele. Samo zwiększenie liczby pikseli nie odzyskuje informacji, której wcześniej w obrazie nie było.

---

## Grafika wektorowa

Grafika wektorowa przechowuje obiekty geometryczne:

- linie,
- krzywe,
- okręgi,
- prostokąty,
- tekst.

Typowy format:

~~~text
SVG
~~~

Zamiast pamiętać kolor każdego piksela, plik może przechowywać informację w rodzaju:

~~~text
narysuj okrąg
o środku (100,100)
i promieniu 40
~~~

Dlatego grafikę wektorową można zwykle skalować bez utraty ostrości.

---

## Kiedy którego formatu użyć?

| Materiał | Dobry wybór |
| --- | --- |
| zdjęcie | JPG / PNG |
| zrzut ekranu | PNG |
| logo | SVG / PDF |
| schemat | SVG / PDF |
| diagram do publikacji | SVG / PDF / TikZ |
| wykres naukowy | PDF / SVG albo dobrej jakości PNG |
| ilustracja AI | zwykle PNG / JPG |

Dobra zasada:

> Jeśli grafika składa się głównie z linii, tekstu i prostych kształtów, warto rozważyć format wektorowy.

---

# Rozdzielczość i DPI

Rozmiar obrazu na ekranie opisujemy zwykle liczbą pikseli.

Przykład:

~~~text
1920 × 1080 px
~~~

W druku często używamy pojęcia **DPI — dots per inch**.

Jeżeli chcemy wydrukować obraz o szerokości $6\,\mathrm{in}$ z rozdzielczością $300\,\mathrm{dpi}$, potrzebujemy:

$$
6\cdot300=1800
$$

pikseli w poziomie.

Obraz o szerokości $10\,\mathrm{cm}$ ma około:

$$
\frac{10}{2.54}\approx3.94\,\mathrm{in}
$$

Przy $300\,\mathrm{dpi}$ daje to około:

$$
3.94\cdot300\approx1182
$$

piksele.

DPI ma szczególne znaczenie dla grafiki rastrowej przeznaczonej do druku.

---

# PNG, JPG, SVG i PDF

## PNG

PNG stosuje kompresję bezstratną. Dobrze nadaje się do wykresów, zrzutów ekranu i grafiki z przezroczystością.

## JPG

JPG stosuje kompresję stratną. Dobrze nadaje się do zdjęć, ale zwykle gorzej do diagramów z cienkimi liniami i tekstem.

## SVG

SVG jest tekstowym formatem wektorowym opartym na XML.

Przykład:

~~~xml
<svg
    xmlns="http://www.w3.org/2000/svg"
    width="300"
    height="120"
>
    <circle
        cx="60"
        cy="60"
        r="35"
        fill="none"
        stroke="black"
    />

    <text
        x="120"
        y="65"
        font-size="24"
    >
        wynik
    </text>
</svg>
~~~

Po otwarciu w przeglądarce zobaczymy okrąg i tekst.

## PDF

PDF może przechowywać grafikę wektorową.

Przykład z Matplotlib:

~~~python
plt.savefig("plot.pdf")
~~~

Taki wykres może zachować ostre linie i tekst przy powiększaniu.

Nie każdy PDF jest jednak automatycznie wektorowy. PDF może również zawierać zwykły raster.

---

# Inkscape

## Co to jest Inkscape?

**Inkscape** jest edytorem grafiki wektorowej. Jego podstawowym formatem jest SVG.

Nadaje się bardzo dobrze do:

- schematów,
- ikon,
- diagramów,
- prostych ilustracji naukowych,
- składania kilku elementów,
- eksportu do SVG, PDF i PNG.

---

## Proste obiekty

W Inkscape możemy tworzyć:

- prostokąty,
- elipsy,
- linie,
- krzywe Béziera,
- tekst,
- strzałki.

Wiele dobrych diagramów technicznych powstaje z bardzo prostego zestawu:

~~~text
prostokąt + strzałka + tekst
~~~

---

## Wyrównanie i odstępy

Przy schematach bardzo ważne są:

- **Align** — wyrównanie,
- **Distribute** — równomierne rozłożenie,
- **Snap** — przyciąganie do punktów i prowadnic.

Trzy prawie równo ustawione elementy wyglądają gorzej niż trzy dokładnie wyrównane.

---

## Grupowanie

Kilka elementów można połączyć w grupę.

Przykład:

~~~text
[okrąg] + [tekst "A"]
          ↓
        grupa
~~~

Po zgrupowaniu można przesuwać całość jako jeden obiekt.

---

## Warstwy

Przy większym rysunku wygodny może być podział:

~~~text
warstwa 1 — tło
warstwa 2 — główny diagram
warstwa 3 — opisy
warstwa 4 — adnotacje
~~~

Warstwy ułatwiają ukrywanie i blokowanie fragmentów grafiki.

---

## Krzywe i węzły

Ścieżka wektorowa składa się z węzłów i odcinków lub krzywych między nimi.

Warto umieć:

- dodać węzeł,
- przesunąć węzeł,
- zmienić kształt krzywej,
- zamknąć ścieżkę.

---

# Tekst w grafice

Tekst powinien być czytelny w **docelowym rozmiarze** grafiki.

Rysunek może wyglądać dobrze na całym ekranie, ale po zmniejszeniu do szerokości $8\,\mathrm{cm}$ podpisy mogą stać się nieczytelne.

Dlatego grafikę warto obejrzeć również w takim rozmiarze, w jakim trafi do raportu lub prezentacji.

---

# Eksport

Typowy workflow:

~~~text
diagram.svg
    ↓
eksport
    ↓
diagram.pdf
diagram.png
~~~

SVG zachowujemy jako źródło edytowalne.

PDF może trafić do LaTeX-a.

PNG może być użyty na stronie WWW lub w prezentacji.

Nie warto zachowywać wyłącznie PNG, jeśli oryginalna grafika powstała jako wektor.

---

## Dobre materiały o Inkscape

- [Inkscape — Tutorials](https://inkscape.org/learn/tutorials/)
- [Inkscape — Learn](https://inkscape.org/learn/)
- [Inkscape Manual](https://inkscape-manuals.readthedocs.io/)

---

# Grafika naukowa ma przekazywać informację

Przed przygotowaniem rysunku warto odpowiedzieć:

1. Co odbiorca ma zrozumieć?
2. Który element jest najważniejszy?
3. Czy podpisy są czytelne?
4. Czy strzałki mają jednoznaczny sens?
5. Czy kolory są potrzebne?
6. Czy rysunek można zrozumieć bez ustnego komentarza?

Estetyka jest ważna, ale nie powinna utrudniać odczytania informacji.

---

# AI i grafika

## Gdzie AI jest użyteczne?

Generatywne modele obrazu mogą dobrze sprawdzić się przy:

- ilustracjach koncepcyjnych,
- ikonach,
- grafice promocyjnej,
- wariantach stylistycznych,
- prostych infografikach,
- inspiracji wizualnej,
- edycji istniejących ilustracji.

---

## Ilustracja to nie wynik naukowy

AI nie powinno być traktowane jako źródło danych naukowych.

Jeżeli model wygeneruje wykres, mapę, zdjęcie aparatury albo strukturę techniczną, nie wolno zakładać, że szczegóły są poprawne tylko dlatego, że obraz wygląda realistycznie.

Bezpieczniejszy przykład:

~~~text
Wygeneruj minimalistyczną ilustrację
koncepcyjną pokazującą przepływ:
dane → analiza → wynik.
~~~

Ryzykowny przykład:

~~~text
Wygeneruj wykres wyników eksperymentu,
którego danych nie posiadamy.
~~~

Dane powinny wynikać z pomiaru, obliczenia albo jawnego modelu, a nie z preferencji generatora obrazu.

---

# Dobry prompt do obrazu

Prompt graficzny również może być specyfikacją.

Przykład:

~~~text
Cel:
ilustracja koncepcyjna do slajdu
o analizie danych.

Kompozycja:
laptop po lewej,
wykres liniowy po prawej,
między nimi jedna strzałka.

Styl:
minimalistyczna grafika,
jasne tło,
bez fotorealizmu.

Ograniczenia:
bez dodatkowego tekstu,
bez logo,
bez znaków wodnych,
bez liczb udających dane.

Format:
poziomy 16:9.
~~~

To dużo bardziej kontrolowane niż:

~~~text
zrób fajną grafikę o danych
~~~

---

# Iteracja i review grafiki AI

Typowy workflow:

~~~text
prompt
  ↓
obraz 1
  ↓
ocena
  ↓
konkretna poprawka
  ↓
obraz 2
  ↓
kontrola
~~~

Jeśli obraz AI jest częścią projektu, warto zachować:

~~~text
ai_prompt.md
ai_image.png
ai_review.md
~~~

W review zapisujemy:

- cel,
- mocne strony wyniku,
- błędy,
- wykonane poprawki,
- ocenę, czy obraz mógłby zostać pomylony z wynikiem naukowym.

---

# IrfanView

## Po co proste narzędzie?

Nie każda operacja wymaga rozbudowanego edytora.

Czasem chcemy tylko:

- sprawdzić wymiary,
- zmienić format,
- zmniejszyć rozdzielczość,
- przyciąć obraz,
- wykonać tę samą operację na wielu plikach.

Do takich zadań wygodny jest **IrfanView**.

---

## Skalowanie

Załóżmy, że mamy obraz:

~~~text
2400 × 1600 px
~~~

a potrzebujemy wersji o szerokości:

~~~text
1200 px
~~~

Przy zachowaniu proporcji wysokość wyniesie:

$$
1600\cdot\frac{1200}{2400}=800
$$

czyli:

~~~text
1200 × 800 px
~~~

---

## Konwersja

Zmiana nazwy:

~~~text
obraz.jpg → obraz.png
~~~

nie jest konwersją formatu.

Program musi rzeczywiście odczytać dane w jednym formacie i zapisać je w drugim.

---

## Operacje wsadowe

**Batch processing** oznacza wykonanie tej samej operacji na wielu plikach.

Przykład:

~~~text
image01.png
image02.png
image03.png
      ↓
zmniejsz do szerokości 800 px
      ↓
small_01.png
small_02.png
small_03.png
~~~

To bardzo praktyczne przy przygotowaniu wielu grafik do strony lub prezentacji.

---

## Dobre materiały o IrfanView

- [IrfanView](https://www.irfanview.com/)
- [IrfanView — FAQ](https://www.irfanview.com/faq.htm)

---

# TikZ

## Co to jest TikZ?

**TikZ** jest warstwą składniową pakietu PGF do tworzenia grafiki bezpośrednio w TeX-u.

Zamiast rysować diagram myszką, opisujemy go tekstowo.

Przykład:

~~~latex
\begin{tikzpicture}

\node (data) at (0,0) {Dane};
\node (analysis) at (3,0) {Analiza};
\node (result) at (6,0) {Wynik};

\draw[->] (data) -- (analysis);
\draw[->] (analysis) -- (result);

\end{tikzpicture}
~~~

Efekt logiczny:

~~~text
Dane → Analiza → Wynik
~~~

---

## Minimalny dokument TikZ

~~~latex
\documentclass{standalone}

\usepackage{tikz}

\begin{document}

\begin{tikzpicture}

\draw (0,0) circle (1);

\end{tikzpicture}

\end{document}
~~~

Po kompilacji otrzymamy mały PDF z okręgiem.

---

## Węzły

~~~latex
\node (A) at (0,0) {A};
\node (B) at (3,0) {B};

\draw[->] (A) -- (B);
~~~

Nazwy `A` i `B` pozwalają później odwoływać się do położenia węzłów.

---

## Style

Zamiast powtarzać wygląd każdego węzła, możemy zdefiniować styl.

~~~latex
\begin{tikzpicture}[
    box/.style={
        draw,
        rounded corners,
        minimum width=2.5cm,
        minimum height=1cm
    }
]

\node[box] (a) at (0,0) {Dane};
\node[box] (b) at (4,0) {Wynik};

\draw[->] (a) -- (b);

\end{tikzpicture}
~~~

Zmiana definicji `box` zmienia wszystkie węzły korzystające z tego stylu.

---

# TikZiT

**TikZiT** jest graficznym edytorem wybranych diagramów TikZ.

Dobrze nadaje się do diagramów typu:

- węzły,
- krawędzie,
- połączenia,
- powtarzalne style.

Workflow:

~~~text
edycja wizualna
      ↓
kod TikZ
      ↓
LaTeX
      ↓
PDF
~~~

Materiały:

- [TikZiT](https://tikzit.github.io/)
- [PGF/TikZ na CTAN](https://ctan.org/pkg/pgf)

---

# Inkscape czy TikZ?

| Sytuacja | Dobry wybór |
| --- | --- |
| swobodny diagram z wieloma kształtami | Inkscape |
| logo lub ikona | Inkscape |
| diagram związany z matematyką | TikZ |
| grafika wersjonowana razem z kodem | TikZ |
| szybka ręczna korekta położenia | Inkscape |
| diagram węzły–krawędzie | TikZ / TikZiT |

Nie ma jednego narzędzia najlepszego do wszystkiego.

---

# Hybrydowy workflow

Przykład:

~~~text
Python
  ↓
wykres PDF
  ↓
Inkscape
  ↓
dodanie strzałek i opisów
  ↓
final_figure.svg
  ↓
final_figure.pdf
  ↓
LaTeX
~~~

Podczas ręcznej edycji nie wolno zmieniać znaczenia danych.

Przesunięcie podpisu jest czymś innym niż przesunięcie punktu pomiarowego.

---

# Zadania dla studenta

Wszystkie rozwiązania umieść w folderze:

~~~text
zadania/07_grafika_naukowa_uzytkowa/
~~~

Po wykonaniu zadań folder powinien zawierać:

~~~text
zadania/07_grafika_naukowa_uzytkowa/
├── README.md
├── diagram.svg
├── diagram.pdf
├── diagram.png
├── raster_report.md
├── batch/
│   ├── small_01.png
│   ├── small_02.png
│   └── small_03.png
├── ai_prompt.md
├── ai_image.png
├── ai_review.md
├── tikz_diagram.tex
├── tikz_diagram.pdf
└── comparison.md
~~~

Nie zmieniaj nazw wymaganych plików.

---

## Zadanie 1. Diagram wektorowy w Inkscape

Przygotuj diagram:

~~~text
Dane → Analiza → Wynik
~~~

Diagram ma zawierać:

- trzy prostokąty,
- trzy podpisy,
- dwie strzałki,
- równe odstępy,
- wyrównane elementy,
- jasne tło.

Zapisz źródło jako:

~~~text
diagram.svg
~~~

Następnie wyeksportuj:

~~~text
diagram.pdf
diagram.png
~~~

PNG ma mieć szerokość co najmniej:

~~~text
1200 px
~~~

### Sprawdzenie

Będzie można sprawdzić trzy formaty, strukturę SVG, obecność tekstów i wymiary PNG.

---

## Zadanie 2. Raster i operacja wsadowa

W folderze zadania otrzymasz trzy obrazy źródłowe.

Za pomocą IrfanView wykonaj operację wsadową:

- format wynikowy: PNG,
- szerokość: `800 px`,
- zachowanie proporcji.

Zapisz:

~~~text
batch/small_01.png
batch/small_02.png
batch/small_03.png
~~~

Utwórz `raster_report.md` z tabelą:

~~~markdown
| Plik | Rozmiar przed | Rozmiar po |
| --- | --- | --- |
| 01 | ... | ... |
| 02 | ... | ... |
| 03 | ... | ... |
~~~

Pod tabelą odpowiedz:

1. Dlaczego zmiana `.jpg` na `.png` przez przemianowanie pliku nie jest konwersją?
2. Co dzieje się z małym rastrem przy dużym powiększeniu?
3. Dlaczego przy zmianie szerokości zwykle zachowujemy proporcje?

### Sprawdzenie

Automat będzie mógł odczytać wymiary wynikowych PNG i sprawdzić szerokość `800 px`.

---

## Zadanie 3. Kontrolowana grafika AI

W folderze zadania znajdzie się plik:

~~~text
ai_image.png
~~~

Na początku będzie to obraz zastępczy przeznaczony do nadpisania.

Wygeneruj ilustrację koncepcyjną:

~~~text
dane → analiza → wynik
~~~

Wymagania:

- styl minimalistyczny,
- jasne tło,
- pozioma kompozycja,
- bez logotypów,
- bez przypadkowych napisów,
- bez liczb udających dane,
- bez znaków wodnych.

Zapisz dokładnie użyty prompt w:

~~~text
ai_prompt.md
~~~

Wynik zapisz pod tą samą nazwą:

~~~text
ai_image.png
~~~

Następnie utwórz `ai_review.md`:

~~~markdown
# Review grafiki AI

## Cel

...

## Co model zrobił dobrze?

...

## Co wymagało poprawy?

...

## Czy obraz może zostać pomylony z wynikiem naukowym?

...

## Ostateczna decyzja

...
~~~

### Sprawdzenie

Będzie można sprawdzić, czy prompt istnieje, obraz zastępczy został nadpisany oraz czy review zawiera wymagane sekcje.

---

## Zadanie 4. Ten sam diagram w TikZ

Utwórz `tikz_diagram.tex` przedstawiający:

~~~text
Dane → Analiza → Wynik
~~~

Możesz zacząć od:

~~~latex
\documentclass{standalone}

\usepackage{tikz}

\begin{document}

\begin{tikzpicture}[
    box/.style={
        draw,
        rounded corners,
        minimum width=2.5cm,
        minimum height=1cm
    }
]

\node[box] (data) at (0,0) {Dane};
\node[box] (analysis) at (4,0) {Analiza};
\node[box] (result) at (8,0) {Wynik};

\draw[->] (data) -- (analysis);
\draw[->] (analysis) -- (result);

\end{tikzpicture}

\end{document}
~~~

Skompiluj:

~~~bash
pdflatex tikz_diagram.tex
~~~

i zachowaj:

~~~text
tikz_diagram.pdf
~~~

### Sprawdzenie

Będzie można policzyć trzy `\node`, dwie `\draw` i spróbować ponownie skompilować źródło.

---

## Zadanie 5. Inkscape kontra TikZ

Utwórz `comparison.md`.

Dodaj tabelę:

~~~markdown
| Cecha | Inkscape | TikZ |
| --- | --- | --- |
| sposób edycji | ... | ... |
| wersjonowanie w Git | ... | ... |
| matematyka | ... | ... |
| szybkie przesuwanie elementów | ... | ... |
| ponowne użycie stylu | ... | ... |
~~~

Następnie odpowiedz w 5–8 zdaniach:

> Którego narzędzia użyłbyś do schematu aparatury, a którego do diagramu matematycznego w artykule? Dlaczego?

Nie ma jednej obowiązkowej odpowiedzi. Liczy się uzasadnienie.

---

## Zadanie 6. README bloku

Utwórz `README.md`.

Powinien zawierać:

- definicję grafiki rastrowej,
- definicję grafiki wektorowej,
- tabelę porównującą PNG, JPG, SVG i PDF,
- osadzony `diagram.png`,
- link do `diagram.svg`,
- link do `diagram.pdf`,
- osadzony `ai_image.png`,
- link do `ai_prompt.md`,
- link do `tikz_diagram.tex`,
- link do `tikz_diagram.pdf`,
- link do `comparison.md`,
- checklistę zadań.

Dodaj zdanie wyjaśniające, dlaczego grafiki AI nie należy przedstawiać jako wyniku pomiaru lub obliczenia.

---

# Checklista końcowa

Przed zgłoszeniem bloku sprawdź:

- [ ] `diagram.svg` otwiera się poprawnie,
- [ ] `diagram.pdf` istnieje,
- [ ] `diagram.png` ma co najmniej `1200 px` szerokości,
- [ ] trzy obrazy w `batch/` mają szerokość `800 px`,
- [ ] `raster_report.md` zawiera tabelę wymiarów,
- [ ] `ai_prompt.md` zawiera faktycznie użyty prompt,
- [ ] `ai_image.png` został zastąpiony wynikiem,
- [ ] `ai_review.md` zawiera wszystkie wymagane sekcje,
- [ ] `tikz_diagram.tex` zawiera trzy węzły i dwie strzałki,
- [ ] `tikz_diagram.pdf` został wygenerowany,
- [ ] `comparison.md` porównuje oba podejścia,
- [ ] `README.md` zawiera oba rodzaje grafiki i checklistę.
