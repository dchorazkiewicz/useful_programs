# Idee — organizacja kursu „Programy użytkowe”

> Dokument roboczy. Zarys organizacji kursu, systemu zadań i sposobu zaliczenia. Szczegóły będziemy dopracowywać w trakcie przygotowywania materiałów.

## 1. Podstawowe założenie

Kurs ma być zorganizowany wokół praktycznej pracy studenta z nowoczesnymi narzędziami cyfrowymi używanymi w nauce i pracy technicznej.

Wymiar kursu:

- **15 godzin wykładu**,
- **30 godzin ćwiczeń / laboratorium komputerowego**.

Wykład ma wprowadzać narzędzia, pojęcia i dobre praktyki. Ćwiczenia mają służyć przede wszystkim samodzielnej pracy nad konkretnymi zadaniami.

Głównym środowiskiem organizującym kurs będzie **GitHub**.

## 2. Strona kursu

Powstanie strona internetowa kursu generowana z materiałów zapisanych w Markdownie.

Na stronie znajdą się m.in.:

- notatki do kolejnych tematów,
- przykłady,
- instrukcje krok po kroku,
- odnośniki do narzędzi i dokumentacji,
- zadania do wykonania,
- informacje o wymaganym sposobie oddawania rozwiązań,
- zasady zaliczenia.

Materiały źródłowe strony będą przechowywane w repozytorium i przygotowywane przede wszystkim w **Markdownie**. Docelowo strona może być generowana np. przy użyciu **MkDocs** i publikowana przez **GitHub Pages**.

Trzeba wyraźnie rozdzielić:

1. **materiały kursowe** — notatki, instrukcje, przykłady i treści zadań,
2. **przestrzeń na pracę studenta** — katalogi, w których student umieszcza własne rozwiązania.

## 3. Repozytorium studenta

Na początku kursu student będzie musiał wykonać **fork bazowego repozytorium kursu**.

Od tego momentu jego fork będzie jednocześnie:

- miejscem wykonywania zadań,
- dokumentacją postępów,
- portfolio wykonanych prac,
- podstawą do sprawdzania zaliczenia.

Dla każdego bloku lub zestawu zadań zostanie przygotowana jednoznaczna struktura katalogów.

Przykładowo:

```text
zadania/
├── 01_markdown_git/
├── 02_terminal/
├── 03_python/
├── 04_dane_wykresy/
├── 05_latex/
└── ...
```

Student będzie umieszczał rozwiązania w odpowiednich katalogach zgodnie z instrukcją. W zależności od zadania mogą to być np.:

- pliki Markdown,
- notebooki Colab / Jupyter,
- skrypty Python,
- pliki danych,
- wykresy,
- dokumenty LaTeX,
- pliki HTML,
- grafiki,
- krótkie raporty,
- odnośniki do opublikowanych rezultatów.

Dokładna struktura zostanie ustalona po przygotowaniu list zadań.

## 4. Listy zadań

Do poszczególnych części kursu przygotujemy osobne zestawy zadań.

Zadania powinny być możliwie praktyczne i sprawdzać rzeczywiste posługiwanie się narzędziem, a nie tylko znajomość definicji.

Docelowo każde zadanie powinno mieć:

- jasny cel,
- krótką instrukcję,
- określony format rozwiązania,
- wskazany katalog lub nazwę pliku,
- kryteria zaliczenia,
- ewentualne zadanie rozszerzone.

Warto tak projektować zadania, aby kolejne elementy budowały jeden spójny workflow: od utworzenia pliku i pracy z repozytorium, przez obliczenia i analizę danych, aż po dokumentację i publikację wyników.

## 5. Sprawdzanie rozwiązań

Rozwiązania studentów będą sprawdzane **półautomatycznie**.

System powinien móc weryfikować przynajmniej część elementów, np.:

- czy wymagany plik istnieje,
- czy znajduje się w odpowiednim katalogu,
- czy ma wymagany format,
- czy kod się uruchamia,
- czy wynik ma właściwą strukturę,
- czy zadanie zawiera wszystkie wymagane elementy.

Nie wszystkie zadania będą nadawały się do pełnej automatyzacji. Elementy wymagające oceny jakościowej będą sprawdzane przez prowadzącego lub z pomocą systemu AI.

Na tym etapie **nie ustalamy jeszcze konkretnego mechanizmu automatyzacji**. Najpierw trzeba zaprojektować strukturę zadań i kryteria oceny, a dopiero później dobrać do nich system sprawdzający.

## 6. GitHub Issues jako system feedbacku

GitHub ma pełnić nie tylko rolę miejsca przechowywania plików, ale również systemu komunikacji dotyczącej postępów.

Dla studenta powinien istnieć czytelny mechanizm pokazujący stan wykonania zadań.

Po sprawdzeniu zadania student otrzyma na GitHubie:

- **potwierdzenie zaliczenia** i odhaczenie zadania,

albo

- **feedback z konkretną informacją, co należy poprawić**.

Do tego celu można wykorzystać przede wszystkim **GitHub Issues**.

Przykładowy przebieg:

```text
student wykonuje zadanie
        ↓
commit / push do własnego repozytorium
        ↓
sprawdzenie rozwiązania
        ↓
┌──────────────────────┬────────────────────────┐
│ zadanie poprawne     │ wymagane poprawki      │
│ ✅ zaliczone         │ 🛠 feedback w Issue    │
└──────────────────────┴────────────────────────┘
        ↓
student poprawia rozwiązanie
        ↓
ponowne sprawdzenie
```

Docelowo student powinien móc wejść do swojego repozytorium i od razu zobaczyć:

- które zadania są wykonane,
- które wymagają poprawy,
- czego dokładnie brakuje,
- jaki jest aktualny stan realizacji kursu.

## 7. Cel podstawowy studenta

Podstawowym celem studenta jest **zrealizowanie wszystkich przewidzianych zadań praktycznych** i uzyskanie dla nich potwierdzenia zaliczenia.

Nie chodzi więc o pojedynczy końcowy projekt lub jedno kolokwium, lecz o systematyczne budowanie kompletnego zestawu wykonanych prac.

Repozytorium studenta pod koniec semestru ma stanowić dowód, że student rzeczywiście potrafi korzystać z omawianych narzędzi.

## 8. Wstępny system oceniania

Robocze założenie:

- **4,0 (dobry)** — wykonanie wszystkich przewidzianych obowiązkowych zadań na wymaganym poziomie,
- **3,5** — niewielkie braki w realizacji programu,
- **3,0** — większe braki, ale osiągnięcie minimalnych efektów uczenia się,
- **2,0 / niezaliczenie** — brak wystarczającej liczby wykonanych zadań lub brak osiągnięcia podstawowych efektów kursu.

Oceny **4,5 i 5,0** nie powinny wynikać wyłącznie z mechanicznego wykonania wszystkich zadań.

Student chcący uzyskać ocenę wyższą niż 4,0 powinien pod koniec semestru wykazać się podczas rozmowy z prowadzącym **swobodą i biegłością w korzystaniu z wielu narzędzi poznanych na kursie**.

Rozmowa może mieć formę krótkiego praktycznego zadania lub demonstracji workflow, np. połączenia kilku narzędzi w celu rozwiązania nowego problemu.

Szczegółowe kryteria ocen 4,5 i 5,0 zostaną ustalone później.

## 9. Rola wykładu i ćwiczeń

Przy proporcji **15 h wykładu + 30 h ćwiczeń** kurs powinien być zdecydowanie praktyczny.

### Wykład — 15 h

Wykład powinien:

- przedstawiać najważniejsze idee,
- pokazywać zastosowania narzędzi,
- demonstrować dobre praktyki,
- pokazywać powiązania między narzędziami,
- przygotowywać do wykonywania kolejnych zadań.

Nie powinien być szczegółowym kursem każdej aplikacji. Student ma otrzymać mapę narzędzi i wiedzieć, jak dalej samodzielnie pracować.

### Ćwiczenia — 30 h

Ćwiczenia powinny być głównym miejscem praktycznej pracy:

- wykonywanie zadań,
- praca z własnym repozytorium,
- rozwiązywanie problemów,
- poprawianie rozwiązań po feedbacku,
- łączenie kilku narzędzi w jeden workflow.

Dobrze byłoby organizować ćwiczenia w większe bloki tematyczne, zamiast traktować każde narzędzie jako całkowicie osobny temat.

## 10. Co musimy przygotować jako autorzy kursu

Do przygotowania pozostają przede wszystkim:

- pełna struktura kursu na 15 h wykładu i 30 h ćwiczeń,
- notatki w Markdownie do wszystkich tematów,
- strona internetowa kursu,
- listy zadań,
- struktura katalogów w repozytorium studenta,
- jednoznaczne kryteria zaliczenia każdego zadania,
- sposób zgłaszania zadania do sprawdzenia,
- mechanizm półautomatycznego sprawdzania,
- system Issues / checklist pokazujący postęp studenta,
- procedura ponownego sprawdzania po poprawkach,
- końcowa procedura wystawiania ocen,
- forma rozmowy dla studentów ubiegających się o 4,5 lub 5,0.

## 11. Kierunek dalszego projektowania

Najważniejsze będzie zaprojektowanie kursu tak, aby trzy warstwy tworzyły jeden spójny system:

**NOTATKI → ZADANIA → WERYFIKACJA**

czyli:

**strona kursu z materiałami**  
→ **konkretne zadanie do wykonania**  
→ **plik lub rezultat umieszczony w repozytorium studenta**  
→ **półautomatyczne sprawdzenie**  
→ **potwierdzenie albo precyzyjny feedback w GitHub Issues**.

Dzięki temu GitHub nie będzie tylko jednym z tematów kursu. Stanie się jednocześnie **narzędziem, na którym cały kurs będzie praktycznie zorganizowany**.
