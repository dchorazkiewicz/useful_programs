# 6. Science workflow i AI

AI może przyspieszyć pracę z kodem, tekstem, danymi i dokumentacją. Może też bardzo szybko wygenerować odpowiedź, która **brzmi przekonująco i jest błędna**.

Dlatego w pracy naukowej i technicznej ważny jest nie tylko prompt, ale cały workflow:

~~~text
problem
   ↓
prompt
   ↓
odpowiedź AI
   ↓
test / źródło / obliczenie kontrolne
   ↓
poprawka
   ↓
wynik, za który odpowiada użytkownik
~~~

W tym bloku interesuje nas przede wszystkim **użyteczne i kontrolowane korzystanie z AI**.

---

# Co robi model językowy?

Duży model językowy, czyli LLM, przetwarza dostarczony kontekst i generuje kolejne fragmenty odpowiedzi na podstawie wzorców poznanych podczas treningu.

W praktyce oznacza to, że model potrafi bardzo dobrze:

- pisać i przekształcać tekst,
- wyjaśniać pojęcia,
- generować kod,
- analizować dostarczone materiały,
- proponować rozwiązania,
- porządkować informacje,
- znajdować błędy,
- tworzyć dokumentację.

Nie oznacza to jednak, że każda wygenerowana informacja jest prawdziwa.

Model może wygenerować:

- błędny wynik,
- nieistniejącą funkcję,
- nieistniejący artykuł,
- błędny DOI,
- niepoprawną komendę,
- przekonujące, ale nieuzasadnione wyjaśnienie.

---

# Halucynacja

W kontekście AI **halucynacją** nazywamy wygenerowanie informacji, która wygląda wiarygodnie, ale nie ma odpowiedniego oparcia w faktach lub dostarczonych danych.

Przykład:

> Artykuł został opublikowany w 2024 roku w czasopiśmie X i ma DOI ...

Jeżeli model podał te informacje bez wiarygodnego źródła, nie możemy zakładać, że istnieją.

Szczególnie ostrożnie należy traktować:

- cytowania,
- DOI,
- nazwiska autorów,
- numery wersji oprogramowania,
- szczegółowe dane liczbowe,
- informacje prawne,
- informacje medyczne,
- komendy administracyjne,
- wyniki obliczeń, których nie sprawdziliśmy.

---

# AI nie jest kalkulatorem prawdy

Jeżeli zapytamy:

~~~text
Ile wynosi suma liczb od 1 do 100?
~~~

model może poprawnie odpowiedzieć:

~~~text
5050
~~~

ale sam fakt, że odpowiedź wygląda dobrze, nie jest metodą weryfikacji.

Możemy sprawdzić wynik w Pythonie:

~~~python
print(sum(range(1, 101)))
~~~

Efekt:

~~~text
5050
~~~

albo ze wzoru:

$$
1+2+\ldots+n=\frac{n(n+1)}{2}
$$

dla $n=100$:

$$
\frac{100\cdot101}{2}=5050
$$

Dopiero niezależne sprawdzenie daje nam mocniejszą podstawę do zaufania wynikowi.

---

# Prompt

## Co to jest prompt?

**Prompt** to informacja przekazana modelowi w celu wykonania zadania.

Prompt może zawierać:

- pytanie,
- dane,
- fragment kodu,
- dokument,
- wymagania,
- ograniczenia,
- oczekiwany format odpowiedzi.

Słaby prompt:

~~~text
Napisz analizę.
~~~

Nie wiadomo:

- czego dotyczy analiza,
- dla kogo jest przeznaczona,
- jak długa ma być,
- jakie dane wolno wykorzystać,
- jaki ma być wynik.

---

# Dobry prompt jako specyfikacja zadania

Przy zadaniu technicznym wygodny jest schemat:

~~~text
KONTEKST
Co model powinien wiedzieć?

CEL
Co dokładnie ma powstać?

DANE
Na czym ma pracować?

OGRANICZENIA
Czego nie wolno zmieniać lub zakładać?

FORMAT
Jak ma wyglądać odpowiedź?

SPRAWDZENIE
Jak model ma sprawdzić wynik?
~~~

Przykład:

~~~text
KONTEKST

Mam plik measurements.csv z dwiema kolumnami x,y.

CEL

Napisz skrypt Python dopasowujący prostą y=a*x+b.

OGRANICZENIA

- użyj NumPy,
- nie używaj pandas,
- nie zmieniaj pliku CSV,
- wynik zapisz do fit_results.txt,
- wykres zapisz jako fit.png.

FORMAT WYNIKU

fit_results.txt ma zawierać:

a=...
b=...

SPRAWDZENIE

Po napisaniu kodu uruchom go i sprawdź,
czy oba pliki wynikowe powstały.
~~~

Taki prompt jest znacznie bliższy **specyfikacji technicznej** niż luźnemu pytaniu.

---

# Prompt nie musi być długi

Dobry prompt nie oznacza automatycznie bardzo długiego promptu.

Dla prostego zadania wystarczy:

~~~text
Przeczytaj calculate.py.

Znajdź błąd powodujący wynik 5051 zamiast 5050.

Nie przepisuj całego programu.
Wyjaśnij przyczynę i zaproponuj minimalną poprawkę.
~~~

Najważniejsza jest **jednoznaczność**, nie liczba słów.

---

# Prompt nie musi być tekstowy

Niektóre narzędzia AI pozwalają na przekazanie promptu w formie:
- pliku,
- fragmentu kodu,
- dokumentu PDF,
- obrazu.
- głosu.

Wykorzystaj format najlepiej pasujący do zadania. Poleca się jednak **tekstowy prompt**, ponieważ jest najłatwiejszy do uporządkowania, archiwizacji i kontroli. 

Jednakże rozważ wcześniej użycie **głosowego trybu** i nadanie jak najszerszego kontekstu, celów, działania i ograniczeń, aby uniknąć nieporozumień w interpretacji promptu przez AI. Potem każ AI uporządkować i przygotować ulepszony prompt, który trzeba będzie dopiero uruchomić.

---

# Format odpowiedzi

Jeżeli wynik ma później przetwarzać człowiek lub automat, warto określić format.

Zamiast:

~~~text
Podaj wyniki analizy.
~~~

możemy napisać:

~~~text
Zwróć dokładnie cztery linie:

count=...
mean=...
min=...
max=...
~~~

Oczekiwany wynik:

~~~text
count=100
mean=50.5
min=1
max=100
~~~

To ułatwia:

- porównanie wyników,
- parsowanie,
- automatyczne testowanie,
- wykrywanie brakujących elementów.

---

# Kontekst

Model nie wie automatycznie wszystkiego o naszym projekcie.

Jeżeli prosimy:

~~~text
Popraw skrypt.
~~~

ale nie udostępnimy skryptu lub repozytorium, model musi zgadywać.

Lepszy workflow:

1. udostępnij potrzebny plik,
2. wskaż problem,
3. określ oczekiwany wynik,
4. podaj ograniczenia,
5. poproś o test.

Nie należy jednak przekazywać więcej danych niż potrzeba.

---

# Minimalna potrzebna ilość danych

Jeżeli błąd dotyczy jednej funkcji, często nie trzeba wysyłać:

- całego repozytorium,
- prywatnych dokumentów,
- danych osobowych,
- kluczy API,
- haseł,
- niepowiązanych plików.

Dobra zasada:

> przekazuj modelowi tyle kontekstu, ile potrzeba do rozwiązania zadania, ale nie więcej.

---

# Dane wrażliwe i prywatność

Przed przesłaniem materiału do zewnętrznego narzędzia AI trzeba sprawdzić, czy wolno ten materiał udostępnić.

Szczególną uwagę należy zwrócić na:

- dane osobowe,
- hasła,
- tokeny,
- klucze API,
- nieopublikowane dane badawcze,
- poufne dokumenty,
- materiały objęte umową lub ograniczeniami dostępu.

Przykład fragmentu, którego nie należy bezmyślnie wklejać:

~~~text
API_KEY=sk-...
PASSWORD=...
~~~

Jeśli sekret przypadkowo trafi do repozytorium, samo usunięcie go w kolejnym commicie może być niewystarczające, ponieważ wcześniejsza wersja pozostaje w historii Git.

---

# AI przy kodowaniu

## Dobry przypadek użycia

Mamy funkcję:

~~~python
def is_prime(n):
    ...
~~~

Możemy poprosić AI:

~~~text
Zaimplementuj funkcję is_prime(n).

Wymagania:
- dla n < 2 zwróć False,
- dla liczb pierwszych zwróć True,
- dla pozostałych False,
- funkcja ma przyjmować liczby całkowite,
- nie używaj zewnętrznych bibliotek.

Po implementacji zaproponuj testy dla:
- wartości ujemnej,
- 0,
- 1,
- 2,
- liczby parzystej,
- liczby pierwszej większej od 2,
- kwadratu liczby pierwszej.
~~~

Model może przygotować kod, ale wynik trzeba uruchomić.

---

# Test jest ważniejszy niż pewność modelu

Załóżmy, że funkcja istnieje.

Możemy przygotować testy:

~~~python
from prime import is_prime

tests = {
    -3: False,
    0: False,
    1: False,
    2: True,
    3: True,
    4: False,
    17: True,
    25: False,
    97: True,
    100: False,
}

for n, expected in tests.items():
    result = is_prime(n)

    assert result == expected, (
        f"n={n}: expected {expected}, got {result}"
    )

print("ALL TESTS PASSED")
~~~

Oczekiwany wynik:

~~~text
ALL TESTS PASSED
~~~

Zdanie modelu:

> Kod jest poprawny.

jest słabszym dowodem niż wykonany zestaw testów.

---

# Testy brzegowe

Błędy często pojawiają się nie dla „normalnych” danych, lecz na granicach.

Dla funkcji `is_prime` warto sprawdzić:

~~~text
-3
0
1
2
4
25
~~~

To przykłady **edge cases**, czyli przypadków brzegowych.

Dobra praktyka przy pracy z AI:

> nie pytaj tylko „czy kod działa?”, ale „dla jakich przypadków może nie działać?”.

---

# AI przy matematyce

AI może:

- zaproponować metodę,
- przekształcić wzór,
- wygenerować kod kontrolny,
- znaleźć potencjalny błąd.

Ale wynik można często sprawdzić niezależnie.

Przykład równania:

$$
x^2-5x+6=0
$$

AI może podać:

$$
x=2,\qquad x=3
$$

Sprawdzenie przez podstawienie:

$$
2^2-5\cdot2+6=0
$$

oraz:

$$
3^2-5\cdot3+6=0
$$

Możemy też użyć SymPy:

~~~python
from sympy import symbols, solve

x = symbols("x")

print(solve(x**2 - 5*x + 6, x))
~~~

Efekt:

~~~text
[2, 3]
~~~

Najlepszy sposób sprawdzenia zależy od typu problemu.

---

# AI i źródła

## Cytowanie wymaga osobnej kontroli

Model może wygenerować bardzo wiarygodnie wyglądający zapis bibliograficzny.

To nie oznacza, że publikacja istnieje.

Przed wykorzystaniem cytowania warto sprawdzić:

- tytuł,
- autorów,
- czasopismo,
- rok,
- DOI,
- czy DOI prowadzi do właściwej publikacji.

---

## DOI

DOI jest trwałym identyfikatorem publikacji.

Przykład prawdziwej publikacji związanej z NumPy:

~~~text
C. R. Harris et al.
Array programming with NumPy
Nature 585, 357–362 (2020)
DOI: 10.1038/s41586-020-2649-2
~~~

DOI można sprawdzić przez:

- [DOI.org](https://www.doi.org/)
- [Crossref](https://search.crossref.org/)

Nie należy oceniać poprawności DOI wyłącznie na podstawie tego, czy „wygląda jak DOI”.

---

# Źródło pierwotne

Jeśli pytanie dotyczy:

- funkcji NumPy,
- składni Pythona,
- ustawienia GitHuba,
- komendy WSL,

to zwykle warto szukać **dokumentacji producenta lub projektu**, a nie przypadkowego bloga.

Przykład:

~~~text
Pytanie:
Jak działa numpy.linspace?

Lepsze źródło:
oficjalna dokumentacja NumPy
~~~

Źródło pierwotne często jest najlepszym miejscem do sprawdzenia szczegółów technicznych.

---

# AI jako reviewer

AI może być bardzo użyteczne nie tylko do tworzenia, ale także do **krytykowania istniejącej pracy**.

Możemy użyć promptu:

~~~text
Jesteś bardzo wymagającym recenzentem technicznym.

Przeczytaj raport.

Nie przepisuj go.

Wskaż:
1. twierdzenia bez uzasadnienia,
2. brakujące informacje potrzebne do odtworzenia wyniku,
3. niejasne fragmenty,
4. miejsca, gdzie autor wyciąga zbyt mocny wniosek,
5. trzy najważniejsze poprawki.

Dla każdej uwagi wskaż konkretny fragment raportu.
~~~

To podejście możemy nazwać roboczo:

> **reviewer in bad mood**

Celem nie jest uzyskanie „negatywnej opinii”, lecz aktywne poszukiwanie słabych punktów przed oddaniem pracy.

---

# Nie każda uwaga AI jest dobra

Recenzent AI również może się mylić.

Dlatego po otrzymaniu uwag warto prowadzić mały **decision log**:

| Uwaga AI | Decyzja | Dlaczego? |
| --- | --- | --- |
| dodać jednostki | przyjęta | brakowały w tabeli |
| usunąć wykres | odrzucona | wykres pokazuje główny wynik |
| zmienić metodę | częściowo | metoda dobra, opis zbyt krótki |

To ważny element odpowiedzialności za końcowy materiał.

---

# Iteracja

Dobra praca z AI zwykle nie wygląda tak:

~~~text
prompt
↓
gotowe
~~~

Częściej:

~~~text
prompt
↓
wersja 1
↓
test
↓
uwagi
↓
wersja 2
↓
test
↓
wynik
~~~

AI dobrze nadaje się do szybkich iteracji, ale każda iteracja powinna mieć **kryterium zakończenia**.

Przykład:

~~~text
Koniec zadania, gdy:
- wszystkie testy przechodzą,
- format pliku jest poprawny,
- wynik liczbowy zgadza się z kontrolą,
- nie ma brakujących sekcji.
~~~

---

# Reprodukowalność

Jeżeli AI wykonało ważną część pracy, dobrze zachować:

- użyty prompt,
- istotną odpowiedź,
- wygenerowany kod,
- testy,
- ręczne poprawki,
- końcowy wynik.

Nie chodzi o archiwizowanie każdej rozmowy.

Chodzi o to, aby później można było odpowiedzieć:

> Skąd wziął się ten fragment rozwiązania i jak został sprawdzony?

---

# Prompt jako część dokumentacji

Dla ważnego zadania można zapisać prompt do pliku:

~~~text
prompt.md
~~~

Przykład:

~~~markdown
# Prompt

## Cel

Napraw funkcję is_prime.

## Ograniczenia

- nie zmieniaj interfejsu funkcji,
- nie używaj zewnętrznych bibliotek.

## Test

Uruchom test_prime.py.
~~~

To szczególnie użyteczne w zadaniach wykonywanych agentowo.

---

# AI-assisted nie oznacza AI-only

W nowoczesnym workflow użytkownik może korzystać jednocześnie z:

- AI,
- dokumentacji,
- wyszukiwarki,
- testów,
- Pythona,
- Wolfram Alpha,
- repozytorium Git,
- recenzji człowieka.

Najsilniejszy workflow zwykle łączy kilka metod kontroli.

Przykład:

~~~text
AI proponuje kod
      ↓
testy jednostkowe
      ↓
porównanie z dokumentacją
      ↓
diff
      ↓
commit
~~~

---

# Przykład: słaby i lepszy raport

Słaby opis:

> Zrobiliśmy wykres. Wygląda dobrze. AI policzyło parametry. a=2.01143, b=1.03810. Wynik chyba jest poprawny.

Problemy:

- nie wiadomo, jakie dane wykorzystano,
- nie wiadomo, jak dopasowano parametry,
- „wygląda dobrze” nie jest kryterium ilościowym,
- informacja „AI policzyło” nie opisuje metody,
- brak sposobu weryfikacji.

Lepsza wersja:

> Do sześciu punktów zapisanych w pliku `measurements.csv` dopasowano model liniowy $y=ax+b$ metodą najmniejszych kwadratów za pomocą `numpy.polyfit`. Otrzymano $a=2.01143$ oraz $b=1.03810$. Kod zapisano w `analyze_data.py`, a wynik w `fit_results.txt`. Wykres danych i dopasowanej prostej zapisano jako `fit.png`. Poprawność wartości sprawdzono przez ponowne uruchomienie skryptu na niezmienionym pliku wejściowym.

Ta wersja opisuje:

- dane,
- metodę,
- narzędzie,
- wynik,
- artefakty,
- sposób kontroli.

---

# Dobre materiały

- [NIST — AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Crossref Search](https://search.crossref.org/)
- [DOI.org](https://www.doi.org/)
- [Python — assert](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)
- [Python — unittest](https://docs.python.org/3/library/unittest.html)

---

# Zadania dla studenta

Wszystkie rozwiązania umieść w folderze:

~~~text
zadania/06_science_workflow_ai/
~~~

Po wykonaniu zadań folder powinien zawierać:

~~~text
zadania/06_science_workflow_ai/
├── README.md
├── prompt_v1.md
├── prompt_v2.md
├── comparison.md
├── prime.py
├── test_prime.py
├── test_results.txt
├── source_audit.md
├── draft.md
├── review_prompt.md
├── review.md
├── final_report.md
├── decision_log.md
└── ai_usage.md
~~~

Nie zmieniaj nazw wymaganych plików.

---

## Zadanie 1. Ten sam problem, dwa prompty

Poproś narzędzie AI o napisanie funkcji:

~~~python
def is_prime(n):
    ...
~~~

### Prompt 1

Najpierw użyj bardzo krótkiego promptu:

~~~text
Napisz funkcję Python sprawdzającą,
czy liczba jest pierwsza.
~~~

Zapisz dokładnie użyty prompt w:

~~~text
prompt_v1.md
~~~

Nie poprawiaj go po otrzymaniu odpowiedzi.

### Prompt 2

Następnie przygotuj lepszy prompt.

Zapisz go w:

~~~text
prompt_v2.md
~~~

Musi zawierać osobne sekcje:

~~~markdown
# Prompt

## Cel

## Wymagania

## Przypadki brzegowe

## Ograniczenia

## Sprawdzenie
~~~

Wymagania funkcji:

- `n < 2` daje `False`,
- `2` daje `True`,
- liczby złożone dają `False`,
- liczby pierwsze dają `True`,
- bez zewnętrznych bibliotek.

### Porównanie

Utwórz:

~~~text
comparison.md
~~~

i odpowiedz krótko:

1. Który prompt był bardziej jednoznaczny?
2. Czy odpowiedzi różniły się kodem?
3. Czy któryś model sam zaproponował testy?
4. Jakie informacje z promptu 2 ograniczyły możliwość błędnej interpretacji?

Nie oceniaj odpowiedzi na podstawie stylu. Interesuje nas użyteczność techniczna.

---

## Zadanie 2. Kod musi przejść testy

Na podstawie odpowiedzi AI utwórz:

~~~text
prime.py
~~~

z funkcją:

~~~python
def is_prime(n):
    ...
~~~

Następnie utwórz dokładnie taki zestaw testów w `test_prime.py`:

~~~python
from prime import is_prime

tests = {
    -3: False,
    0: False,
    1: False,
    2: True,
    3: True,
    4: False,
    17: True,
    25: False,
    97: True,
    100: False,
}

for n, expected in tests.items():
    result = is_prime(n)

    assert result == expected, (
        f"n={n}: expected {expected}, got {result}"
    )

print("ALL TESTS PASSED")
~~~

Uruchom:

~~~bash
python3 test_prime.py
~~~

Poprawny wynik:

~~~text
ALL TESTS PASSED
~~~

Zapisz wynik uruchomienia do:

~~~text
test_results.txt
~~~

Plik ma zawierać dokładnie:

~~~text
ALL TESTS PASSED
~~~

Jeżeli kod AI nie przechodzi testów, popraw go. To **końcowy działający kod**, a nie pierwsza odpowiedź AI, jest rozwiązaniem zadania.

### Sprawdzenie

Automat będzie mógł uruchomić `test_prime.py` i sprawdzić dokładną zawartość `test_results.txt`.

---

## Zadanie 3. Audyt źródeł

Utwórz:

~~~text
source_audit.md
~~~

Poproś AI o sprawdzenie dwóch opisów publikacji.

### Pozycja A

~~~text
C. R. Harris et al.
Array programming with NumPy
Nature 585, 357–362 (2020)
DOI: 10.1038/s41586-020-2649-2
~~~

### Pozycja B

~~~text
A. Example and B. Fiction
Universal Scientific Computing with Quantum Penguins
Journal of Imaginary Numerical Methods 42 (2026) 1–10
DOI: 10.0000/fake-reference-2026
~~~

Jedna pozycja jest rzeczywistą publikacją, druga jest celowo przygotowanym fałszywym przykładem.

Nie wystarczy odpowiedź AI.

Sprawdź informacje niezależnie, używając:

- DOI.org,
- Crossref,
- strony wydawcy,
- innego wiarygodnego katalogu bibliograficznego.

`source_audit.md` ma mieć tabelę:

~~~markdown
| Pozycja | Odpowiedź AI | Weryfikacja niezależna | Werdykt |
| --- | --- | --- | --- |
| A | ... | ... | ... |
| B | ... | ... | ... |
~~~

Pod tabelą dodaj sekcję:

~~~markdown
## Użyte źródła

- ...
- ...
~~~

### Sprawdzenie

W końcowym werdykcie:

- pozycja A powinna być oznaczona jako rzeczywista,
- pozycja B jako fikcyjna / nieweryfikowalna.

Najważniejsza jest jednak opisana **niezależna metoda sprawdzenia**.

---

## Zadanie 4. Reviewer in bad mood

Utwórz `draft.md` zawierający dokładnie ten tekst:

~~~markdown
# Wynik

Zrobiliśmy wykres. Wygląda dobrze.

AI policzyło parametry:
a=2.01143, b=1.03810.

Wynik chyba jest poprawny.
~~~

Następnie utwórz:

~~~text
review_prompt.md
~~~

i zapisz prompt do AI, który ma działać jako wymagający recenzent.

Prompt musi wymagać sprawdzenia:

- danych wejściowych,
- metody,
- reprodukowalności,
- uzasadnienia wniosków,
- sposobu weryfikacji,
- precyzji języka.

AI nie ma jeszcze przepisywać raportu. Ma tylko przygotować recenzję.

Zapisz pełną recenzję do:

~~~text
review.md
~~~

---

## Zadanie 5. Decyzja należy do autora

Przeczytaj `review.md`.

Utwórz:

~~~text
decision_log.md
~~~

z tabelą:

~~~markdown
| Uwaga recenzenta | Decyzja | Uzasadnienie |
| --- | --- | --- |
| ... | przyjmuję / odrzucam / częściowo | ... |
~~~

Uwzględnij co najmniej cztery uwagi.

Nie musisz akceptować każdej sugestii AI.

Następnie utwórz poprawioną wersję:

~~~text
final_report.md
~~~

Raport ma zawierać:

- nazwę pliku danych `measurements.csv`,
- model $y=ax+b$,
- informację o użyciu `numpy.polyfit`,
- wartości $a=2.01143$ i $b=1.03810$,
- nazwę skryptu `analyze_data.py`,
- nazwę wyniku `fit_results.txt`,
- nazwę wykresu `fit.png`,
- informację, jak wynik został sprawdzony.

Tekst ma mieć 5–10 zdań i być samodzielnym krótkim raportem.

### Sprawdzenie

Można sprawdzić strukturę `decision_log.md` i obecność wymaganych informacji w `final_report.md`. Jakość narracji będzie oceniana osobno.

---

## Zadanie 6. Dokumentacja użycia AI

Utwórz:

~~~text
ai_usage.md
~~~

Plik ma odpowiadać na pytania:

~~~markdown
# Użycie AI

## Jakich narzędzi AI użyłem?

...

## Do jakich zadań?

...

## Co zostało wygenerowane przez AI?

...

## Co sprawdziłem automatycznie?

...

## Co sprawdziłem ręcznie?

...

## Co poprawiłem po AI?

...

## Za jaki końcowy wynik biorę odpowiedzialność?

...
~~~

Ostatnia sekcja nie ma być formułką.

Napisz konkretnie, które pliki i wyniki uważasz za sprawdzone.

---

## Zadanie 7. README bloku

Utwórz `README.md`.

Powinien zawierać:

- krótką definicję halucynacji,
- różnicę między wygenerowaniem odpowiedzi a jej weryfikacją,
- linki do obu promptów,
- link do `source_audit.md`,
- link do `review.md`,
- link do `decision_log.md`,
- link do `final_report.md`,
- wynik testów funkcji `is_prime`,
- checklistę wszystkich zadań.

Dodaj tabelę:

~~~markdown
| Wynik AI | Sposób sprawdzenia |
| --- | --- |
| kod | testy |
| obliczenie | niezależne obliczenie |
| cytowanie | DOI / Crossref / wydawca |
| tekst | recenzja i decyzja autora |
~~~

---

# Checklista końcowa

Przed zgłoszeniem bloku sprawdź:

- [ ] `prompt_v1.md` zawiera pierwszy prompt,
- [ ] `prompt_v2.md` ma wszystkie wymagane sekcje,
- [ ] `comparison.md` porównuje oba podejścia,
- [ ] `prime.py` zawiera funkcję `is_prime`,
- [ ] `test_prime.py` zawiera pełny zestaw testów,
- [ ] wszystkie testy przechodzą,
- [ ] `test_results.txt` zawiera `ALL TESTS PASSED`,
- [ ] `source_audit.md` rozróżnia prawdziwe i fikcyjne źródło,
- [ ] `draft.md` zawiera tekst wejściowy,
- [ ] `review_prompt.md` zawiera kryteria recenzji,
- [ ] `review.md` zawiera recenzję AI,
- [ ] `decision_log.md` zawiera co najmniej cztery decyzje,
- [ ] `final_report.md` zawiera wymagane dane i metodę,
- [ ] `ai_usage.md` dokumentuje wykorzystanie AI,
- [ ] `README.md` zawiera tabelę metod weryfikacji i checklistę.
