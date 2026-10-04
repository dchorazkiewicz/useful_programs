# 8. Advanced Microsoft 365 / Google Docs

Pakiety biurowe są często traktowane jako narzędzia podstawowe. W praktyce większość użytkowników korzysta jednak tylko z niewielkiej części ich możliwości.

W tym bloku interesują nas funkcje, które rzeczywiście oszczędzają czas w pracy naukowej, technicznej i organizacyjnej:

| Obszar | Narzędzia |
| --- | --- |
| dane i zestawienia | Excel / Google Sheets |
| dokumenty | Word / Google Docs |
| prezentacje | PowerPoint / Google Slides |
| ankiety i testy | Microsoft Forms / Google Forms |
| współpraca | komentarze, uprawnienia, historia wersji |
| konwersja | PDF, CSV, Pandoc |
| wyszukiwanie | operatory Google |
| komunikacja | poprawny i czytelny e-mail |

---

# Excel i Google Sheets

## Arkusz kalkulacyjny to nie tylko tabela

Arkusz jest narzędziem do pracy z danymi.

Możemy w nim:

- przechowywać dane,
- wykonywać obliczenia,
- sortować i filtrować,
- wykrywać powtarzające się wartości,
- stosować reguły logiczne,
- tworzyć wykresy,
- przygotowywać zestawienia.

Najważniejsza zasada:

> Jeden wiersz powinien reprezentować jeden rekord, a jedna kolumna jedną cechę.

Przykład:

| ID | Imię | Grupa | Punkty | Status |
| --- | --- | --- | ---: | --- |
| S01 | Anna | A | 82 | zaliczone |
| S02 | Jan | A | 47 | niezaliczone |
| S03 | Marta | B | 91 | zaliczone |

---

## Formuła i wartość

Komórka może zawierać zwykłą wartość:

~~~text
82
~~~

albo formułę:

~~~text
=B2+C2
~~~

Formuła zaczyna się od znaku równości.

Arkusz przechowuje formułę, ale pokazuje jej wynik.

---

## Odwołania względne i bezwzględne

Formuła:

~~~text
=B2*C2
~~~

po skopiowaniu o jeden wiersz niżej zmieni się na:

~~~text
=B3*C3
~~~

To **odwołanie względne**.

Jeżeli chcemy zawsze korzystać z jednej komórki, możemy użyć:

~~~text
=B2*$F$1
~~~

`$F$1` jest odwołaniem bezwzględnym.

To przydaje się dla:

- progów,
- współczynników,
- kursów walut,
- stałych używanych w wielu wierszach.

---

## Funkcja IF

Załóżmy, że punkty znajdują się w komórce `D2`.

Chcemy otrzymać `zaliczone` dla wyniku co najmniej 50.

W angielskiej wersji Excela:

~~~text
=IF(D2>=50,"zaliczone","niezaliczone")
~~~

W zależności od języka programu nazwa funkcji i separator argumentów mogą być wyświetlane inaczej.

Najważniejsza jest logika:

~~~text
jeżeli warunek jest prawdziwy
    → wartość A
w przeciwnym razie
    → wartość B
~~~

---

## COUNTIF — zliczanie wystąpień

**COUNTIF** liczy komórki spełniające jedno kryterium.

Przykład:

~~~text
=COUNTIF(C2:C11,"A")
~~~

liczy, ile razy w zakresie występuje grupa A.

Inny przykład:

~~~text
=COUNTIF(D2:D11,">=50")
~~~

liczy wyniki co najmniej 50.

Oficjalne materiały:

- [Microsoft Support — COUNTIF](https://support.microsoft.com/en-us/excel/get-started/use-the-countif-function-in-microsoft-excel)
- [Microsoft Support — formuły warunkowe](https://support.microsoft.com/en-us/excel/create-conditional-formulas)

---

## Formatowanie warunkowe

Formatowanie warunkowe zmienia wygląd komórki na podstawie jej wartości.

Przykład:

~~~text
punkty < 50
    ↓
wyróżnij komórkę
~~~

Możemy użyć go do:

- wskazywania braków,
- zaznaczania wysokich wyników,
- wykrywania duplikatów,
- wyróżniania terminów,
- znajdowania wartości odstających.

Excel i Google Sheets pozwalają także używać własnych formuł jako warunku.

Materiały:

- [Microsoft Support — Conditional Formatting](https://support.microsoft.com/en-us/excel/use-conditional-formatting-to-highlight-information-in-excel)
- [Google Docs Editors Help — Conditional formatting](https://support.google.com/docs/answer/78413)

---

## Duplikaty

Załóżmy, że identyfikatory znajdują się w zakresie:

~~~text
A2:A100
~~~

Reguła:

~~~text
=COUNTIF($A$2:$A$100,A2)>1
~~~

pozwala wykrywać wartości występujące więcej niż raz.

To prosty przykład połączenia:

~~~text
formuła + formatowanie warunkowe
→ kontrola jakości danych
~~~

---

## Sortowanie i filtrowanie

Sortowanie zmienia kolejność rekordów.

Przykład:

~~~text
Punkty: malejąco
~~~

Filtrowanie ukrywa rekordy niespełniające kryterium.

Przykład:

~~~text
Grupa = B
Status = niezaliczone
~~~

Filtr nie powinien zmieniać samych danych.

---

## Wykres

Zanim wybierzemy wykres, trzeba odpowiedzieć:

> Co chcemy pokazać?

Przykładowo:

- porównanie kategorii → wykres słupkowy,
- zmiana w czasie → wykres liniowy,
- zależność dwóch zmiennych → wykres punktowy.

Nie każdy zestaw danych potrzebuje wykresu.

---

# Word i Google Docs

## Dokument powinien mieć strukturę

W dłuższym dokumencie nie warto każdego nagłówka formatować ręcznie.

Lepiej używać **stylów**:

~~~text
Title
Heading 1
Heading 2
Normal
Caption
~~~

Styl opisuje rolę fragmentu tekstu.

Zmiana definicji stylu może automatycznie zmienić wszystkie fragmenty dokumentu, które z niego korzystają.

Materiały:

- [Microsoft Support — Styles in Word](https://support.microsoft.com/en-us/word/customize-or-create-new-styles)
- [Google Docs Editors Help](https://support.google.com/docs/)

---

## Spis treści

Jeżeli nagłówki korzystają z poprawnych stylów:

~~~text
Heading 1 / Heading 2
        ↓
automatyczny spis treści
~~~

Ręcznie wpisany spis treści szybko staje się nieaktualny.

---

## Komentarze i śledzenie zmian

Komentarz może zawierać np.:

> Czy ten wynik został sprawdzony?

**Track Changes** zapisuje zmiany wykonywane w dokumencie.

Możemy zobaczyć:

- dodany tekst,
- usunięty tekst,
- autora zmiany.

Zmiany można później zaakceptować lub odrzucić.

Ważne: ukrycie oznaczeń nie usuwa zmian. Przed finalnym udostępnieniem dokumentu trzeba je rzeczywiście zaakceptować lub odrzucić.

Materiały:

- [Microsoft Support — Track Changes](https://support.microsoft.com/pl-pl/word/training/track-changes-in-word)
- [Microsoft Support — Accept or reject changes](https://support.microsoft.com/en-us/word/accept-or-reject-tracked-changes-in-word)

---

# Korespondencja seryjna

**Mail merge** łączy:

~~~text
szablon
   +
źródło danych
   ↓
wiele spersonalizowanych dokumentów
~~~

Przykładowe dane:

~~~csv
name,group
Anna,A
Jan,B
~~~

Szablon może zawierać pola odpowiadające kolumnom danych.

Zamiast ręcznie kopiować dokument dla każdej osoby, Word generuje wersje automatycznie.

Materiały:

- [Microsoft Support — Mail Merge](https://support.microsoft.com/en-us/word/use-mail-merge-for-bulk-email-letters-labels-and-envelopes)
- [Microsoft Support — Insert merge fields](https://support.microsoft.com/en-us/word/insert-mail-merge-fields)

---

# QR code w Wordzie

Klasyczny Word dla Windows obsługuje pole `DISPLAYBARCODE` generujące m.in. kody QR.

Przykładowa zawartość pola:

~~~text
DisplayBarcode "https://github.com/" QR \q 3
~~~

Pole tworzy się skrótem:

~~~text
Ctrl + F9
~~~

Nie należy po prostu wpisywać zwykłych klamer.

Materiały:

- [Microsoft Support — DisplayBarcode](https://support.microsoft.com/en-us/word/field-codes-displaybarcode)

Jeżeli dana wersja Worda nie obsługuje tej funkcji, można przygotować QR innym narzędziem i wstawić go jako obraz.

Po utworzeniu QR trzeba go zeskanować i sprawdzić adres.

---

# PowerPoint i Google Slides

## Slajd nie jest stroną raportu

Dobra prezentacja nie powinna polegać na kopiowaniu pełnych akapitów.

Typowy slajd:

~~~text
jedna główna myśl
+
jedna grafika lub kilka punktów
+
ustne wyjaśnienie
~~~

Tytuł:

~~~text
Model liniowy dobrze opisuje dane
~~~

jest informacyjnie lepszy niż:

~~~text
Wyniki
~~~

---

## Notatki prezentera

PowerPoint ma osobne **speaker notes**.

Prowadzący może widzieć notatki, podczas gdy publiczność widzi sam slajd.

Można tam zapisać:

- konkretne liczby,
- zdanie przejściowe,
- przypomnienie przykładu,
- źródło grafiki.

Materiał:

- [Microsoft Support — Speaker notes](https://support.microsoft.com/en-US/PowerPoint/training/add-speaker-notes-to-your-slides)

---

## Animacje

Animacja może:

- ujawniać kolejne elementy,
- pokazywać kolejność procesu,
- kierować uwagę odbiorcy.

Nie powinna istnieć tylko dlatego, że „można ją dodać”.

Przykład:

~~~text
Dane → Analiza → Wynik
~~~

można odsłaniać etapami zgodnie z narracją.

Materiał:

- [Microsoft Support — Animations](https://support.microsoft.com/en-us/powerpoint/training/animate-text-or-objects)

---

# Microsoft Forms i Google Forms

Formularz może służyć do:

- ankiety,
- rejestracji,
- testu,
- zbierania odpowiedzi,
- ewaluacji.

Typy pytań mogą obejmować:

- krótką odpowiedź,
- tekst,
- wybór jednej odpowiedzi,
- wybór wielu odpowiedzi,
- skalę,
- datę.

Google Forms pozwala zbierać odpowiedzi i analizować je lub przekazać do arkusza.

Materiały:

- [Google Forms — podstawy](https://support.google.com/docs/answer/6281888)
- [Google Forms — współpraca](https://support.google.com/docs/answer/2917111)

---

## Dobre pytanie ankietowe

Słabo:

~~~text
Czy kurs był świetny i przydatny?
~~~

Problem: pytanie sugeruje odpowiedź i łączy dwie rzeczy.

Lepiej:

~~~text
Jak oceniasz przydatność kursu?
1 — bardzo niska
...
5 — bardzo wysoka
~~~

oraz osobno:

~~~text
Który element kursu był najbardziej przydatny?
~~~


---

# Współpraca online

## Uprawnienia

Przy współdzieleniu dokumentu najczęściej spotkamy role podobne do:

~~~text
Viewer
Commenter
Editor
~~~

Nie każda osoba potrzebuje prawa edycji.

Dobra zasada:

> Nadaj najmniejsze uprawnienia wystarczające do wykonania zadania.

W Google Sheets można współdzielić arkusz m.in. jako Viewer, Commenter lub Editor.

Materiał:

- [Google Docs Editors Help — Collaborate in Sheets](https://support.google.com/docs/answer/9331169)

---

## Historia wersji

Współdzielony dokument powinien pozwalać odpowiedzieć:

- kto coś zmienił,
- kiedy,
- co było wcześniej.

To nie jest dokładnie ten sam mechanizm co Git, ale idea zachowania historii pracy jest podobna.

---

# Format źródłowy i eksport

Dokument może istnieć jako:

~~~text
DOCX
XLSX
PPTX
~~~

a do udostępnienia potrzebujemy np.:

~~~text
PDF
CSV
PNG
HTML
~~~

Warto rozróżniać:

- format edytowalny,
- format wymiany danych,
- format wynikowy.

Przykład:

~~~text
report.docx
     ↓
eksport
     ↓
report.pdf
~~~

---

# CSV jako format wymiany

XLSX może przechowywać:

- wiele arkuszy,
- formuły,
- style,
- wykresy.

CSV przechowuje prostą tabelę tekstową.

Workflow:

~~~text
Excel / Sheets
      ↓
CSV
      ↓
Python / Octave / inne narzędzie
~~~

CSV nie zachowuje pełnego wyglądu i funkcji skoroszytu.

---

# Pandoc

**Pandoc** jest narzędziem do konwersji dokumentów pomiędzy wieloma formatami.

Markdown do Worda:

~~~bash
pandoc report.md -o report.docx
~~~

Markdown do LaTeX-a:

~~~bash
pandoc report.md -s -o report.tex
~~~

Markdown do PDF, jeżeli mamy odpowiednie środowisko:

~~~bash
pandoc report.md -s -o report.pdf
~~~

Pandoc często rozpoznaje format na podstawie rozszerzenia pliku.

Materiał:

- [Pandoc — Getting started](https://pandoc.org/getting-started.html)

Po konwersji trzeba sprawdzić:

- nagłówki,
- tabele,
- wzory,
- obrazy,
- linki.

Automatyczna konwersja nie zwalnia z kontroli wyniku.

---

# Zaawansowane wyszukiwanie Google

Google dokumentuje operatory pozwalające zawężać wyniki.

## Dokładna fraza

~~~text
"general relativity"
~~~

## Konkretna domena

~~~text
site:uwr.edu.pl rekrutacja
~~~

## Typ pliku

~~~text
filetype:pdf numerical methods
~~~

## Wykluczenie słowa

~~~text
jaguar speed -car
~~~

## Data

~~~text
artificial intelligence after:2026-01-01
~~~

lub:

~~~text
report before:2025-12-31
~~~

## Łączenie

~~~text
site:edu filetype:pdf "numerical methods"
~~~

Materiał:

- [Google Search Help — zawężanie wyników](https://support.google.com/websearch/answer/2466433?hl=pl)

Pierwszy wynik wyszukiwarki nie jest automatycznie najlepszym źródłem. Trzeba sprawdzić autora, instytucję, datę i ewentualne źródło pierwotne.

---

# E-mail w pracy naukowej i technicznej

## Temat

Słabo:

~~~text
Pytanie
~~~

Lepiej:

~~~text
Programy użytkowe — pytanie o zadanie 3
~~~

Temat powinien pozwalać zrozumieć cel wiadomości bez jej otwierania.

---

## BCC, CC i TO

Wyjaśnienie skrótów:

- **TO** — odbiorca główny,
- **CC** — kopia do wiadomości,
- **BCC** — ukryta kopia do wiadomości.


Słabo:

~~~text
TO: 10 osób
~~~

Lepiej:

~~~text
TO: prowadzący
BCC: 10 osób
~~~

Cieżkim błędem jest wysyłanie wiadomości do wielu osób w polu TO lub CC, co ujawnia adresy e-mail wszystkim odbiorcom.

---

## Przekierowanie wiadomości

Skrzynka uczelniana może mieć przekierowanie na adres prywatny. W tym celu trzeba zadbać aby wiadomści były pobierane z serwera uczelni i nie były usuwane.

---

## Reguły

Można wprowadzić reguły automatyzujące obsługę wiadomości:

- przenoszenie do folderu,
- oznacznie etykietą.

Szczegóły różnią się między pocztami więc należy sprawdzić dokumentację.

---

## Wiadomość techniczna

Dobra wiadomość o problemie powinna zawierać:

1. co próbujemy zrobić,
2. co zrobiliśmy,
3. czego oczekiwaliśmy,
4. co otrzymaliśmy,
5. pełny komunikat błędu,
6. link lub plik, jeśli jest potrzebny,
7. jedno konkretne pytanie.

Słabo:

~~~text
Nie działa. Co robić?
~~~

Lepiej:

~~~text
Uruchamiam:

python3 analyze.py

Oczekuję utworzenia fit.png.

Otrzymuję:

FileNotFoundError: measurements.csv

Repozytorium:
...

Czy problem wynika z katalogu roboczego?
~~~

---

## Załączniki i linki

Przed wysłaniem sprawdź:

- czy załącznik rzeczywiście został dołączony,
- czy link działa,
- czy odbiorca ma uprawnienia,
- czy nazwa pliku jest zrozumiała.

Lepiej:

~~~text
raport_metody_numeryczne.pdf
~~~

niż:

~~~text
final2_new_poprawiony.pdf
~~~

---

# Zadania dla studenta

Wszystkie rozwiązania umieść w folderze:

~~~text
zadania/08_microsoft365_google_docs/
~~~

Po wykonaniu zadań folder powinien zawierać:

~~~text
zadania/08_microsoft365_google_docs/
├── README.md
├── participants.csv
├── analysis.xlsx
├── analysis_summary.csv
├── document.docx
├── document.pdf
├── recipients.csv
├── merged_letters.pdf
├── presentation.pptx
├── forms.md
├── form_responses.csv
├── collaboration.md
├── pandoc_input.md
├── pandoc_output.docx
├── search.md
└── email.md
~~~

Nie zmieniaj nazw wymaganych plików.

---

## Zadanie 1. Excel / Google Sheets — analiza tabeli

Utwórz `participants.csv` dokładnie z poniższymi danymi:

~~~csv
id,name,group,points
S01,Anna,A,82
S02,Jan,A,47
S03,Marta,B,91
S04,Piotr,B,55
S05,Ola,A,73
S06,Karol,A,47
S07,Ewa,B,100
S08,Adam,B,38
S09,Zofia,A,65
S10,Tomasz,A,52
~~~

Zaimportuj dane do Excela lub Google Sheets i przygotuj `analysis.xlsx`.

Dodaj kolumny:

~~~text
status
duplicate_points
~~~

### Status

Dla wyniku co najmniej 50 wpisz przez formułę:

~~~text
zaliczone
~~~

dla mniejszego:

~~~text
niezaliczone
~~~

### Powtarzające się wyniki

W `duplicate_points` policz, ile razy dana wartość punktów występuje w całej tabeli.

Wartość 47 występuje dwa razy.

Pozostałe wyniki występują po jednym razie.

### Formatowanie warunkowe

Dodaj reguły:

- poniżej 50 — wyróżnienie,
- co najmniej 90 — inne wyróżnienie,
- duplikat punktów — wyróżnienie.

### Podsumowanie

Policz:

~~~text
count=10
passed=7
failed=3
group_A=6
group_B=4
average=65.0
~~~

Wyeksportuj podsumowanie do `analysis_summary.csv`:

~~~csv
metric,value
count,10
passed,7
failed,3
group_A,6
group_B,4
average,65.0
~~~

### Sprawdzenie

Będzie można automatycznie sprawdzić CSV oraz strukturę skoroszytu XLSX.

---

## Zadanie 2. Word / Google Docs — dokument strukturalny

Utwórz:

~~~text
document.docx
~~~

Dokument ma zawierać:

1. tytuł,
2. automatyczny spis treści,
3. sekcję **Cel**,
4. sekcję **Dane**,
5. sekcję **Wyniki**,
6. sekcję **Wniosek**,
7. tabelę z podsumowaniem zadania 1,
8. co najmniej jeden podpis,
9. co najmniej jeden komentarz podczas pracy,
10. co najmniej jedną zmianę wykonaną przy włączonym Track Changes.

Nagłówki mają korzystać ze stylów.

Przed eksportem:

- zaakceptuj albo odrzuć wszystkie zmiany,
- usuń lub rozwiąż niepotrzebne komentarze,
- zaktualizuj spis treści.

Wyeksportuj:

~~~text
document.pdf
~~~

### QR code

Dodaj kod QR prowadzący do:

~~~text
https://github.com/
~~~

Możesz użyć `DISPLAYBARCODE` w klasycznym Wordzie dla Windows albo wstawić poprawnie wygenerowany obraz QR.

Zeskanuj kod telefonem i sprawdź adres.

### Sprawdzenie

Będzie można sprawdzić DOCX/PDF, nagłówki, tabelę oraz obecność QR.

---

## Zadanie 3. Korespondencja seryjna

Utwórz `recipients.csv`:

~~~csv
name,group
Anna,A
Jan,A
Marta,B
Piotr,B
~~~

Przygotuj w Wordzie szablon wiadomości:

~~~text
Dzień dobry «name»,

informujemy, że przypisana grupa to: «group».

Pozdrawiamy
~~~

Użyj korespondencji seryjnej i wygeneruj cztery spersonalizowane dokumenty.

Połącz wynik w:

~~~text
merged_letters.pdf
~~~

Każda osoba ma pojawić się dokładnie raz.

### Sprawdzenie

Będzie można odczytać PDF i sprawdzić cztery nazwiska oraz odpowiadające im grupy.

---

## Zadanie 4. PowerPoint / Google Slides

Utwórz:

~~~text
presentation.pptx
~~~

Prezentacja ma zawierać dokładnie pięć slajdów:

1. **Tytuł**,
2. **Dane**,
3. **Wyniki**,
4. **Co z tego wynika?**,
5. **Podsumowanie**.

Wymagania:

- jeden wykres,
- jedna tabela albo duża liczba podsumowująca,
- notatki prezentera na co najmniej trzech slajdach,
- jedna prosta animacja mająca sens narracyjny,
- bez pełnych akapitów skopiowanych z raportu.

Na slajdzie **Wyniki** pokaż:

~~~text
7 / 10 zaliczyło
średnia = 65.0
~~~

### Sprawdzenie

Będzie można sprawdzić liczbę slajdów, teksty, obiekty i notatki w strukturze PPTX.


---

## Zadanie 5. Microsoft Forms lub Google Forms

Utwórz formularz zawierający dokładnie pięć pytań:

1. imię lub pseudonim — krótka odpowiedź,
2. grupa — wybór A/B,
3. przydatność materiału — skala 1–5,
4. najbardziej przydatne narzędzie — wybór jednej odpowiedzi,
5. komentarz — odpowiedź otwarta.

Nie zbieraj prawdziwych danych osobowych innych osób na potrzeby ćwiczenia.

Wypełnij formularz pięć razy danymi testowymi.

Wyeksportuj odpowiedzi do:

~~~text
form_responses.csv
~~~

Utwórz `forms.md`:

~~~markdown
# Formularz

## Adres

...

## Cel

...

## Pytania

...

## Liczba odpowiedzi

5

## Krótkie podsumowanie

...
~~~

### Sprawdzenie

Będzie można policzyć pięć rekordów w CSV i sprawdzić strukturę `forms.md`.

---

## Zadanie 6. Współpraca i uprawnienia

Utwórz:

~~~text
collaboration.md
~~~

Wyjaśnij różnicę między:

~~~text
Viewer
Commenter
Editor
~~~

Następnie rozwiąż trzy scenariusze.

### Scenariusz A

Kolega ma tylko przeczytać raport.

Jakie uprawnienie?

### Scenariusz B

Recenzent ma dodawać uwagi, ale nie zmieniać treści.

Jakie uprawnienie?

### Scenariusz C

Współautor ma poprawiać dokument.

Jakie uprawnienie?

Na końcu dodaj:

~~~markdown
## Historia wersji

...
~~~

i w 3–5 zdaniach porównaj historię wersji dokumentu online z historią Git.

---

## Zadanie 7. Pandoc

Utwórz:

~~~text
pandoc_input.md
~~~

Plik ma zawierać:

- tytuł,
- dwa nagłówki,
- listę punktowaną,
- tabelę,
- wzór $E=mc^2$,
- link.

Następnie wykonaj:

~~~bash
pandoc pandoc_input.md -o pandoc_output.docx
~~~

Otwórz wynik i sprawdź go ręcznie.

Na końcu `pandoc_input.md` dodaj:

~~~markdown
## Kontrola konwersji

- [x] nagłówki
- [x] lista
- [x] tabela
- [x] wzór
- [x] link
~~~

Zaznacz element dopiero po rzeczywistym sprawdzeniu DOCX.

### Sprawdzenie

Będzie można ponownie uruchomić Pandoc i sprawdzić wynik.

---

## Zadanie 8. Zaawansowane wyszukiwanie

Utwórz:

~~~text
search.md
~~~

Znajdź trzy materiały.

### A. PDF z domeny uczelni

Użyj jednocześnie:

~~~text
site:
filetype:
~~~

### B. Dokładna fraza

Użyj cudzysłowu.

### C. Ograniczenie daty

Użyj:

~~~text
after:
~~~

albo:

~~~text
before:
~~~

Dla każdego przypadku zapisz:

~~~markdown
## Wyszukiwanie A

### Zapytanie

...

### Znaleziony materiał

...

### Dlaczego uznaję źródło za wiarygodne?

...
~~~

Nie wystarczy wkleić pierwszego wyniku.

---

## Zadanie 9. E-mail techniczny

Utwórz:

~~~text
email.md
~~~

Napisz przykładową wiadomość do prowadzącego dotyczącą błędu:

~~~text
FileNotFoundError: measurements.csv
~~~

Wiadomość ma zawierać:

- konkretny temat,
- krótkie przywitanie,
- kontekst,
- komendę, którą uruchomiono,
- oczekiwany wynik,
- pełną nazwę błędu,
- informację, gdzie znajduje się plik lub repozytorium,
- jedno konkretne pytanie,
- podpis.

Nie wysyłaj wiadomości. To ćwiczenie z przygotowania dobrej komunikacji technicznej.

---

## Zadanie 10. README bloku

Utwórz `README.md`.

Powinien zawierać:

- krótkie podsumowanie bloku,
- wynik analizy arkusza,
- link do `analysis_summary.csv`,
- link do `document.pdf`,
- link do `merged_letters.pdf`,
- link do `presentation.pptx`,
- link do `forms.md`,
- link do `collaboration.md`,
- link do `search.md`,
- link do `email.md`,
- checklistę wszystkich zadań.

Dodaj tabelę:

~~~markdown
| Zadanie | Główny artefakt |
| --- | --- |
| arkusz | analysis.xlsx |
| dokument | document.docx |
| korespondencja seryjna | merged_letters.pdf |
| prezentacja | presentation.pptx |
| formularz | form_responses.csv |
| konwersja | pandoc_output.docx |
~~~

---

# Checklista końcowa

Przed zgłoszeniem bloku sprawdź:

- [ ] `participants.csv` zawiera dokładnie 10 rekordów,
- [ ] `analysis.xlsx` zawiera formuły i formatowanie warunkowe,
- [ ] `analysis_summary.csv` zawiera `count=10`,
- [ ] `analysis_summary.csv` zawiera `passed=7`,
- [ ] `analysis_summary.csv` zawiera `failed=3`,
- [ ] `analysis_summary.csv` zawiera `average=65.0`,
- [ ] `document.docx` używa stylów nagłówków,
- [ ] `document.pdf` został wyeksportowany,
- [ ] QR prowadzi do `https://github.com/`,
- [ ] `merged_letters.pdf` zawiera cztery spersonalizowane dokumenty,
- [ ] `presentation.pptx` zawiera dokładnie pięć slajdów,
- [ ] prezentacja zawiera notatki prezentera,
- [ ] `form_responses.csv` zawiera pięć odpowiedzi testowych,
- [ ] `collaboration.md` rozróżnia poziomy dostępu,
- [ ] `pandoc_output.docx` został wygenerowany,
- [ ] `search.md` zawiera trzy techniki wyszukiwania,
- [ ] `email.md` opisuje problem tak, aby dało się go zrozumieć i odtworzyć,
- [ ] `README.md` zawiera komplet linków i checklistę.
