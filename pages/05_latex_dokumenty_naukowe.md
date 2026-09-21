# 5. LaTeX i dokumenty naukowe

LaTeX jest jednym z podstawowych narzędzi do przygotowywania tekstów naukowych, szczególnie tam, gdzie pojawiają się wzory matematyczne, odwołania, bibliografia, tabele i duże dokumenty.

W tym bloku przejdziemy przez pełny, ale niewielki projekt:

~~~text
źródło .tex
   ↓
kompilacja
   ↓
PDF
   ↓
bibliografia
   ↓
grafika i odwołania
   ↓
prezentacja
   ↓
wersja gotowa do udostępnienia
~~~

---

# TeX i LaTeX

## Co to właściwie jest?

**TeX** jest systemem składu tekstu stworzonym przez Donalda Knutha.

**LaTeX** jest zestawem makr i konwencji zbudowanych na TeX-u, który znacznie upraszcza przygotowywanie dokumentów.

W praktyce użytkownik najczęściej pisze plik:

~~~text
dokument.tex
~~~

a następnie kompiluje go do:

~~~text
dokument.pdf
~~~

Najważniejsza idea jest podobna do pracy z kodem:

~~~text
źródło
   ↓
kompilator
   ↓
wynik
~~~

Nie ustawiamy ręcznie każdej czcionki i odstępu. Opisujemy **strukturę dokumentu**, a LaTeX zajmuje się składem.

---

# Minimalny dokument

Najmniejszy użyteczny dokument może wyglądać tak:

~~~latex
\documentclass{article}

\begin{document}

Hello, LaTeX!

\end{document}
~~~

Po kompilacji otrzymujemy PDF zawierający tekst:

> Hello, LaTeX!

---

## Preambuła i treść dokumentu

Dokument LaTeX ma dwie główne części.

### Preambuła

Wszystko przed:

~~~latex
\begin{document}
~~~

to **preambuła**.

Tutaj ustawiamy m.in.:

- klasę dokumentu,
- pakiety,
- język,
- kodowanie,
- marginesy,
- własne komendy.

### Treść

Wszystko pomiędzy:

~~~latex
\begin{document}
...
\end{document}
~~~

jest właściwą treścią dokumentu.

---

# Klasa dokumentu

Pierwsza linia często wygląda tak:

~~~latex
\documentclass{article}
~~~

Klasa określa ogólny typ dokumentu.

Popularne klasy:

| Klasa | Typ dokumentu |
| --- | --- |
| `article` | artykuł, raport, krótszy tekst |
| `report` | dłuższy raport |
| `book` | książka |
| `beamer` | prezentacja |

---

# Pakiety

Pakiety rozszerzają możliwości LaTeX-a.

Przykład:

~~~latex
\usepackage{amsmath}
\usepackage{graphicx}
~~~

Pakiet `amsmath` daje rozbudowane narzędzia matematyczne.

Pakiet `graphicx` pozwala umieszczać grafiki.

Współczesne instalacje LaTeX-a zawierają bardzo dużą liczbę pakietów. Nie trzeba znać ich wszystkich. Ważniejsze jest nauczenie się wyszukiwania odpowiedniego pakietu do konkretnego zadania.

---

# Tytuł dokumentu

Źródło:

~~~latex
\title{Krótki raport}
\author{Jan Kowalski}
\date{\today}

\begin{document}

\maketitle

\end{document}
~~~

W PDF pojawi się automatycznie przygotowany blok tytułowy.

LaTeX rozdziela więc:

- **informację**, czym jest tytuł i autor,
- **sposób prezentacji**, który zależy od klasy dokumentu.

---

# Sekcje

Źródło:

~~~latex
\section{Wprowadzenie}

Tekst wprowadzenia.

\subsection{Cel}

Opis celu.

\subsection{Metoda}

Opis metody.
~~~

Efekt w PDF będzie miał strukturę:

> **1 Wprowadzenie**
>
> Tekst wprowadzenia.
>
> **1.1 Cel**
>
> Opis celu.
>
> **1.2 Metoda**
>
> Opis metody.

Numeracja jest generowana automatycznie.

---

# Formatowanie tekstu

Źródło:

~~~latex
\textbf{tekst pogrubiony}

\textit{tekst pochylony}

\emph{ważny fragment}
~~~

Efekt:

- **tekst pogrubiony**,
- *tekst pochylony*,
- wyróżniony fragment zależny od kontekstu.

W LaTeX-u zwykle lepiej opisywać **znaczenie** tekstu niż ręcznie ustawiać wygląd każdego fragmentu.

---

# Listy

## Lista punktowana

~~~latex
\begin{itemize}
    \item Python
    \item NumPy
    \item SymPy
\end{itemize}
~~~

Efekt:

- Python
- NumPy
- SymPy

## Lista numerowana

~~~latex
\begin{enumerate}
    \item Wczytaj dane.
    \item Wykonaj obliczenia.
    \item Zapisz wynik.
\end{enumerate}
~~~

Efekt:

1. Wczytaj dane.
2. Wykonaj obliczenia.
3. Zapisz wynik.

---

# Matematyka

Jednym z największych atutów LaTeX-a jest skład wzorów.

## Matematyka w tekście

Źródło:

~~~latex
Energia dana jest wzorem $E=mc^2$.
~~~

Efekt:

Energia dana jest wzorem $E=mc^2$.

---

## Osobny wzór

Źródło:

~~~latex
\[
E = mc^2
\]
~~~

W PDF otrzymamy wyśrodkowany wzór:

$$
E=mc^2
$$

W samych plikach Markdown tego kursu stosujemy reguły opisane w `hints.md`. W źródle LaTeX dokumentu można używać normalnej składni LaTeX-a.

---

## Numerowane równanie

Źródło:

~~~latex
\begin{equation}
    E = mc^2
\end{equation}
~~~

LaTeX automatycznie nada równaniu numer.

---

# Odwołania do równań

Ręczne wpisywanie „równanie (3)” jest ryzykowne. Po dodaniu wcześniejszego równania numer może się zmienić.

LaTeX rozwiązuje ten problem przez `label` i `ref`.

Źródło:

~~~latex
\begin{equation}
    E = mc^2
    \label{eq:energy}
\end{equation}

Korzystamy z równania~\ref{eq:energy}.
~~~

LaTeX sam wstawi aktualny numer równania.

Dobra praktyka to używanie czytelnych prefiksów:

~~~text
eq:     równanie
fig:    grafika
tab:    tabela
sec:    sekcja
~~~

Przykłady:

~~~text
eq:energy
fig:fit
tab:results
sec:method
~~~

---

# Kilka równań

Źródło:

~~~latex
\begin{align}
    x + y &= 5, \\
    x - y &= 1.
\end{align}
~~~

W PDF otrzymamy dwa wyrównane równania.

W praktyce środowisko `align` jest bardzo wygodne przy dłuższych rachunkach.

---

# Macierze

Źródło:

~~~latex
\[
A=
\begin{pmatrix}
2 & 1 \\
1 & 3
\end{pmatrix}
\]
~~~

Efekt:

$$
A=
\begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix}
$$

---

# Tabela

Źródło:

~~~latex
\begin{table}[h]
    \centering

    \begin{tabular}{c c}
        \hline
        x & y \\
        \hline
        1 & 1 \\
        2 & 4 \\
        3 & 9 \\
        \hline
    \end{tabular}

    \caption{Przykładowe dane.}
    \label{tab:data}
\end{table}
~~~

LaTeX potrafi automatycznie numerować tabelę.

W tekście możemy napisać:

~~~latex
Dane przedstawiono w tabeli~\ref{tab:data}.
~~~

---

# Grafika

Do wstawiania grafik zwykle używamy pakietu:

~~~latex
\usepackage{graphicx}
~~~

Przykład:

~~~latex
\begin{figure}[h]
    \centering

    \includegraphics[
        width=0.7\textwidth
    ]{fit.png}

    \caption{Dane i dopasowana prosta.}
    \label{fig:fit}
\end{figure}
~~~

Odwołanie:

~~~latex
Wynik pokazano na rysunku~\ref{fig:fit}.
~~~

---

## PNG, JPG czy PDF?

W dokumentach naukowych warto rozróżniać grafikę rastrową i wektorową.

| Format | Typ | Typowe zastosowanie |
| --- | --- | --- |
| PNG | rastrowy | wykres, zrzut ekranu, grafika bez strat |
| JPG | rastrowy | zdjęcia |
| PDF | często wektorowy | wykresy i diagramy |
| SVG | wektorowy | grafika WWW, diagramy |

Dla wykresu naukowego grafika wektorowa jest zwykle bardzo wygodna, ponieważ zachowuje ostrość przy powiększaniu.

Matplotlib może zapisać ten sam wykres jako PDF:

~~~python
plt.savefig("fit.pdf", bbox_inches="tight")
~~~

---

# Kompilacja

## `pdflatex`

Jeżeli mamy lokalną instalację LaTeX-a:

~~~bash
pdflatex report.tex
~~~

powinien powstać:

~~~text
report.pdf
~~~

Przy odwołaniach numerowanych czasem trzeba wykonać kompilację więcej niż raz.

---

## `latexmk`

Bardzo wygodnym narzędziem jest `latexmk`:

~~~bash
latexmk -pdf report.tex
~~~

Program automatycznie wykonuje tyle kroków kompilacji, ile potrzeba.

Usuwanie plików pomocniczych:

~~~bash
latexmk -c
~~~

---

# Błędy kompilacji

LaTeX nie zawsze kompiluje się za pierwszym razem.

Typowe przyczyny:

- brak zamkniętej klamry,
- brak `\end{...}`,
- błędna nazwa pliku,
- brak grafiki,
- brak pakietu,
- znak specjalny użyty bez odpowiedniej składni.

Przykład błędu:

~~~latex
\textbf{ważny tekst
~~~

brakuje końcowej klamry:

~~~latex
\textbf{ważny tekst}
~~~

W komunikacie błędu warto szukać:

- numeru linii,
- nazwy pliku,
- pierwszego sensownego komunikatu błędu.

Jedna pomyłka może wygenerować wiele kolejnych komunikatów.

---

# Znaki specjalne

Niektóre znaki mają w LaTeX-u specjalne znaczenie.

Przykład:

~~~text
%
_
&
#
$
~~~

Jeżeli chcemy je wyświetlić jako zwykły tekst, często trzeba użyć odpowiedniej składni.

Przykład:

~~~latex
50\%
~~~

daje:

> 50%

Podkreślenie w zwykłym tekście:

~~~latex
plik\_wynikowy.txt
~~~

---

# Bibliografia

Ręczne numerowanie publikacji szybko staje się niewygodne.

Zamiast tego przechowujemy dane bibliograficzne osobno.

Przykład pliku:

~~~text
references.bib
~~~

---

# BibTeX

## Wpis bibliograficzny

Przykład:

~~~bibtex
@article{einstein1905,
    author  = {Albert Einstein},
    title   = {Zur Elektrodynamik bewegter Koerper},
    journal = {Annalen der Physik},
    year    = {1905},
    volume  = {322},
    pages   = {891--921}
}
~~~

Najważniejszy element to klucz:

~~~text
einstein1905
~~~

Tego klucza używamy później w dokumencie.

---

## Cytowanie

Źródło:

~~~latex
Szczególna teoria względności została
sformułowana przez Einsteina~\cite{einstein1905}.
~~~

Na końcu dokumentu możemy umieścić:

~~~latex
\bibliographystyle{plain}
\bibliography{references}
~~~

LaTeX i BibTeX zajmą się numeracją oraz formatowaniem bibliografii.

---

## Klasyczny workflow BibTeX

Dla dokumentu `report.tex`:

~~~bash
pdflatex report.tex
bibtex report
pdflatex report.tex
pdflatex report.tex
~~~

Można też użyć:

~~~bash
latexmk -pdf report.tex
~~~

jeśli konfiguracja projektu jest standardowa.

---

# DOI i dane bibliograficzne

Przy dodawaniu publikacji warto korzystać z trwałych identyfikatorów, np. DOI.

Przykład DOI ma postać:

~~~text
10.xxxx/...
~~~

Nie należy tworzyć wpisu bibliograficznego „z pamięci”, jeśli można pobrać poprawne dane od wydawcy, Crossref, INSPIRE, arXiv lub innego wiarygodnego źródła.

Najczęstsze problemy w bibliografii:

- błędny rok,
- zła kolejność autorów,
- literówki w tytule,
- brak numeru tomu,
- niepoprawny DOI.

---

# Overleaf

## Co to jest Overleaf?

**Overleaf** jest internetowym środowiskiem do pracy z LaTeX-em.

Typowy widok zawiera:

- pliki projektu,
- edytor źródła,
- wynikowy PDF,
- log kompilacji.

Największa zaleta: do rozpoczęcia pracy nie trzeba lokalnie instalować pełnego środowiska LaTeX.

---

## Projekt Overleaf

Projekt może wyglądać:

~~~text
report.tex
references.bib
fit.pdf
~~~

Po kompilacji Overleaf pokazuje wynikowy PDF.

---

## Współpraca

Kilka osób może pracować nad tym samym dokumentem.

To wygodne przy:

- artykułach,
- raportach,
- pracach dyplomowych,
- notatkach,
- prezentacjach.

Nadal jednak warto mieć jasną strukturę plików i sensownie nazywać grafiki.

Nazwy:

~~~text
fig1_final_new2.png
test123.pdf
aaa.tex
~~~

są znacznie mniej użyteczne niż:

~~~text
fit_linear.pdf
spectrum.pdf
introduction.tex
methods.tex
~~~

---

## Dobre materiały

- [Overleaf — Learn LaTeX in 30 minutes](https://www.overleaf.com/learn/latex/Learn_LaTeX_in_30_minutes)
- [Overleaf — Mathematical expressions](https://www.overleaf.com/learn/latex/Mathematical_expressions)
- [Overleaf — Bibliography management with BibTeX](https://www.overleaf.com/learn/latex/Bibliography_management_with_bibtex)

---

# Większy dokument

Przy dłuższym dokumencie nie trzeba trzymać wszystkiego w jednym pliku.

Przykład:

~~~text
thesis/
├── main.tex
├── references.bib
├── chapters/
│   ├── introduction.tex
│   ├── methods.tex
│   └── results.tex
└── figures/
    └── fit.pdf
~~~

W `main.tex` możemy użyć:

~~~latex
\input{chapters/introduction}
\input{chapters/methods}
\input{chapters/results}
~~~

Dzięki temu duży dokument jest łatwiejszy do utrzymania.

---

# Praca dyplomowa

Typowa praca dyplomowa zawiera m.in.:

- stronę tytułową,
- streszczenie,
- spis treści,
- wprowadzenie,
- rozdziały merytoryczne,
- podsumowanie,
- bibliografię,
- ewentualne dodatki.

LaTeX jest szczególnie wygodny, ponieważ automatycznie obsługuje:

- numerację rozdziałów,
- spis treści,
- odwołania,
- bibliografię,
- podpisy tabel i rysunków.

Nie trzeba ręcznie aktualizować numerów po każdej zmianie struktury.

---

# CV w LaTeX-u

CV również może być dokumentem LaTeX.

Zaletą jest:

- powtarzalny układ,
- łatwa wersjonowalność,
- możliwość przechowywania źródła w Git,
- łatwe generowanie nowych wersji.

Nie ma jednak obowiązku używania LaTeX-a do każdego dokumentu. Narzędzie powinno pasować do zadania.

---

# Beamer

## Prezentacja w LaTeX-u

Klasa `beamer` służy do tworzenia prezentacji.

Minimalny przykład:

~~~latex
\documentclass{beamer}

\title{Krótka prezentacja}
\author{Jan Kowalski}

\begin{document}

\begin{frame}
    \titlepage
\end{frame}

\begin{frame}{Wynik}

Najważniejszy wynik:

\[
E=mc^2
\]

\end{frame}

\end{document}
~~~

Każde środowisko `frame` odpowiada jednemu slajdowi.

---

## Lista na slajdzie

~~~latex
\begin{frame}{Plan}

\begin{itemize}
    \item problem,
    \item metoda,
    \item wynik,
    \item wniosek.
\end{itemize}

\end{frame}
~~~

Beamer jest szczególnie wygodny dla prezentacji z dużą liczbą wzorów.

---

# arXiv

## Co to jest arXiv?

**arXiv** jest repozytorium preprintów naukowych.

Autorzy udostępniają tam artykuły m.in. z:

- fizyki,
- matematyki,
- informatyki,
- statystyki,
- ekonomii.

arXiv nie zastępuje procesu recenzji czasopisma, ale pozwala szybko i publicznie udostępnić preprint.

---

## Źródła artykułu

Do przygotowania zgłoszenia potrzebne są zwykle źródła pozwalające odtworzyć PDF.

Typowy zestaw:

~~~text
main.tex
references.bib
figure1.pdf
figure2.pdf
~~~

W projekcie nie powinny znaleźć się przypadkowe:

- hasła,
- klucze API,
- prywatne komentarze,
- duże nieużywane pliki,
- dane, których nie wolno publikować.

---

## Sprawdzenie przed publikacją

Przed wysłaniem materiałów warto sprawdzić:

1. czy dokument kompiluje się od początku,
2. czy wszystkie grafiki istnieją,
3. czy bibliografia jest kompletna,
4. czy nie ma brakujących odwołań,
5. czy pliki źródłowe są wystarczające do odtworzenia PDF,
6. czy w projekcie nie ma materiałów prywatnych.

---

## Dobre materiały

- [arXiv — Help](https://info.arxiv.org/help/)
- [arXiv — Submit](https://info.arxiv.org/help/submit/)

---

# Mały kompletny raport

Połączmy najważniejsze elementy.

`report.tex`:

~~~latex
\documentclass{article}

\usepackage{amsmath}
\usepackage{graphicx}

\title{Analiza prostego modelu}
\author{Jan Kowalski}

\begin{document}

\maketitle

\section{Wprowadzenie}

Rozważamy model liniowy

\begin{equation}
    y=ax+b.
    \label{eq:model}
\end{equation}

\section{Wynik}

Parametry dopasowania wynoszą

\[
a=2.01143,
\qquad
b=1.03810.
\]

Wynik przedstawiono na
rysunku~\ref{fig:fit}.

\begin{figure}[h]
    \centering

    \includegraphics[
        width=0.7\textwidth
    ]{fit.pdf}

    \caption{Dane i dopasowana prosta.}
    \label{fig:fit}
\end{figure}

Model z równania~\ref{eq:model}
dobrze opisuje dane.

\end{document}
~~~

To już jest mały dokument naukowy z:

- strukturą,
- matematyką,
- numerowanym równaniem,
- grafiką,
- odwołaniami.

---

# Zadania dla studenta

Wszystkie rozwiązania umieść w folderze:

~~~text
zadania/05_latex_dokumenty_naukowe/
~~~

Po wykonaniu zadań folder powinien zawierać:

~~~text
zadania/05_latex_dokumenty_naukowe/
├── README.md
├── report.tex
├── references.bib
├── fit.pdf
├── report.pdf
├── beamer.tex
├── beamer.pdf
├── overleaf.md
├── arxiv.md
└── source_check.md
~~~

Nie zmieniaj nazw wymaganych plików.

---

## Zadanie 1. Raport LaTeX

Utwórz:

~~~text
report.tex
~~~

Dokument ma zawierać:

- klasę `article`,
- pakiet `amsmath`,
- pakiet `graphicx`,
- tytuł,
- autora,
- datę,
- `\maketitle`,
- co najmniej trzy sekcje,
- co najmniej jeden wzór inline,
- co najmniej jedno numerowane równanie,
- macierz `2\times2`,
- tabelę,
- grafikę `fit.pdf`,
- podpis grafiki,
- `\label` i `\ref`,
- co najmniej jedno cytowanie `\cite`.

Możesz wykorzystać wyniki z bloku 03:

~~~text
a=2.01143
b=1.03810
~~~

W raporcie napisz krótko, czego dotyczył model liniowy i jakie otrzymano parametry.

### Sprawdzenie

Będzie można sprawdzić strukturę źródła LaTeX oraz spróbować skompilować dokument.

---

## Zadanie 2. Grafika wektorowa

Wygeneruj wykres danych i dopasowania z bloku 03 ponownie, ale zapisz go jako:

~~~text
fit.pdf
~~~

W Pythonie wystarczy użyć:

~~~python
plt.savefig(
    "fit.pdf",
    bbox_inches="tight"
)
~~~

Umieść `fit.pdf` w tym samym folderze co `report.tex`.

W raporcie grafika ma być wstawiona przez:

~~~latex
\includegraphics{fit.pdf}
~~~

### Sprawdzenie

Będzie można sprawdzić:

- istnienie `fit.pdf`,
- czy plik nie jest pusty,
- czy `report.tex` odwołuje się do właściwej nazwy.

---

## Zadanie 3. Bibliografia BibTeX

Utwórz:

~~~text
references.bib
~~~

Dodaj co najmniej dwa poprawne wpisy bibliograficzne:

1. jedną publikację naukową,
2. jedno źródło dokumentacji technicznej lub książkę.

Każdy wpis powinien mieć sensowny klucz.

Przykłady kluczy:

~~~text
einstein1905
numpy2020
~~~

W `report.tex` użyj obu źródeł przez `\cite{...}`.

Na końcu dokumentu dodaj bibliografię.

### Sprawdzenie

Będzie można sprawdzić:

- liczbę wpisów w `references.bib`,
- obecność wymaganych pól,
- zgodność kluczy z `\cite` w `report.tex`.

---

## Zadanie 4. Kompilacja do PDF

Skompiluj raport i zapisz wynik jako:

~~~text
report.pdf
~~~

Możesz użyć Overleaf albo lokalnie:

~~~bash
latexmk -pdf report.tex
~~~

Jeżeli używasz klasycznego BibTeX:

~~~bash
pdflatex report.tex
bibtex report
pdflatex report.tex
pdflatex report.tex
~~~

Przed oddaniem sprawdź:

- czy nie ma pustych odwołań typu `??`,
- czy bibliografia jest widoczna,
- czy grafika się wyświetla,
- czy numery tabel i rysunków są poprawne.

### Sprawdzenie

Będzie można porównać istnienie PDF ze źródłami i ponownie spróbować kompilacji.

---

## Zadanie 5. Overleaf i współpraca

Utwórz:

~~~text
overleaf.md
~~~

Plik ma mieć strukturę:

~~~markdown
# Overleaf

## Import projektu

...

## Kompilacja

...

## Współpraca

...

## Historia zmian

...

## Jedna praktyczna zaleta

...

## Jedno ograniczenie

...
~~~

Zaimportuj projekt zawierający:

~~~text
report.tex
references.bib
fit.pdf
~~~

do Overleaf i sprawdź, czy kompiluje się bez zmian źródła.

W części **Historia zmian** opisz krótko różnicę między historią projektu w Overleaf a historią commitów w Git.

To zadanie jest częściowo narracyjne.

---

## Zadanie 6. Krótka prezentacja Beamer

Utwórz:

~~~text
beamer.tex
~~~

oraz wynik:

~~~text
beamer.pdf
~~~

Prezentacja ma mieć dokładnie cztery slajdy:

1. tytuł,
2. problem,
3. wynik,
4. wniosek.

Na slajdzie **Wynik** umieść:

- parametry `a` i `b`,
- grafikę `fit.pdf`.

Na jednym ze slajdów użyj listy `itemize`.

### Sprawdzenie

Będzie można:

- policzyć liczbę środowisk `frame`,
- sprawdzić odwołanie do `fit.pdf`,
- spróbować skompilować `beamer.tex`,
- sprawdzić istnienie `beamer.pdf`.

---

## Zadanie 7. Paczka źródłowa do publikacji

Utwórz:

~~~text
source_check.md
~~~

Wyobraź sobie, że `report.tex` ma zostać wysłany do innej osoby albo do systemu publikacyjnego.

W pliku zapisz checklistę:

~~~markdown
# Source check

- [ ] report.tex
- [ ] references.bib
- [ ] fit.pdf
- [ ] dokument kompiluje się od początku
- [ ] brak brakujących cytowań
- [ ] brak brakujących odwołań
- [ ] brak prywatnych danych
- [ ] brak zbędnych plików
~~~

Zaznacz elementy dopiero po sprawdzeniu.

Następnie utwórz:

~~~text
arxiv.md
~~~

ze strukturą:

~~~markdown
# arXiv

## Co to jest preprint?

...

## Jakie pliki byłyby potrzebne?

...

## Co trzeba sprawdzić przed wysłaniem?

...

## Czego nie należy publikować?

...
~~~

Każda sekcja ma zawierać krótki własny opis, nie kopię dokumentacji.

---

## Zadanie 8. README bloku

Utwórz `README.md`.

Powinien zawierać:

- krótkie wyjaśnienie różnicy między źródłem `.tex` a wynikowym PDF,
- listę wszystkich artefaktów,
- link do `report.tex`,
- link do `references.bib`,
- link do `overleaf.md`,
- link do `arxiv.md`,
- informację, czy raport kompilował się lokalnie, w Overleaf czy w obu miejscach,
- checklistę wykonania zadań.

Dodaj tabelę:

~~~markdown
| Plik | Rola |
| --- | --- |
| report.tex | źródło raportu |
| references.bib | bibliografia |
| fit.pdf | grafika |
| report.pdf | wynik kompilacji |
| beamer.tex | źródło prezentacji |
| beamer.pdf | prezentacja |
~~~

---

# Checklista końcowa

Przed zgłoszeniem bloku sprawdź:

- [ ] `report.tex` ma poprawną strukturę dokumentu,
- [ ] raport zawiera wzór, macierz, tabelę i grafikę,
- [ ] istnieją działające `\label` i `\ref`,
- [ ] `references.bib` zawiera co najmniej dwa wpisy,
- [ ] w raporcie występują co najmniej dwa cytowania,
- [ ] `fit.pdf` istnieje i otwiera się poprawnie,
- [ ] `report.pdf` został wygenerowany,
- [ ] w PDF nie ma brakujących odwołań,
- [ ] bibliografia jest widoczna,
- [ ] projekt kompiluje się w Overleaf,
- [ ] `overleaf.md` zawiera wymagane sekcje,
- [ ] `beamer.tex` zawiera cztery slajdy,
- [ ] `beamer.pdf` został wygenerowany,
- [ ] `source_check.md` zawiera sprawdzoną checklistę,
- [ ] `arxiv.md` zawiera opis procesu przygotowania źródeł,
- [ ] `README.md` zawiera linki i podsumowanie.
