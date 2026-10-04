# Zadania: Markdown

**Folder na rozwiązania:** [`pages/solutions/01_sol_markdown/`](../solutions/01_sol_markdown/) (ścieżka względem głównego katalogu repozytorium).

## Zadanie 1.

Załóż konto na GitHubie i się do niego zaloguj.

## Zadanie 2.

Wykonaj `Fork` repozytorium przedmiotu na swoim koncie GitHub.

## Zadanie 3.

Wejdź w ustawienia repozytorium Settings i przewiń do sekcji `Issues`. Włącz opcję pozwalającą na tworzenie nowych zgłoszeń (Issues). Umożliwi to otrzymywanie feedbacku od prowadzącego.

## Zadanie 4.

Wejdź w folder `pages/solutions/01_sol_markdown/` i utwórz tam plik Markdown `README.md`. Ważna jest wielkość liter w nazwie pliku oraz rozszerzenie.

Plik ma docelowo zawierać:

- tytuł,
- krótki tekst w ramach jednej podsekcji,
- kolejny krótki tekst w ramach kolejnej podsekcji,
- co najmniej jeden fragment **pogrubiony**,
- co najmniej jeden fragment *pochylony*,
- co najmniej jeden fragment ~~przekreślony~~,
- listę punktowaną,
- listę numerowaną,
- checklistę,
- tabelkę,
- link do strony Google Colab: http://colab.research.google.com,
- krótki fragment kodu Pythona,
- trzy wzory matematyczne w tekście (tzw. inline przy użyciu `$...$`),
- trzy wzory jako osobny wycentrowany blok (tzw. display math przy użyciu `$$...$$`),
- osadzony obrazek 'wykres.png', który znajduje się w folderze.

Po zapisaniu pliku otwórz jego wyrenderowany widok na GitHubie i sprawdź, czy wszystkie elementy wyglądają poprawnie. Na ten moment po wykonaniu tego zadania folder powinien zawierać:

~~~text
pages/solutions/01_sol_markdown/
├── README.md
├── wykres.png
└── zrzut.png
~~~

## Zadanie 5.

Weź zrzut ekranu `zrzut.png` z ręcznymi notatkami z folderu, a następnie użyj narzędzia AI do przepisania informacji (transkrypcji) widocznej na zrzucie do kodu Markdown. Wynik zapisz jako `transkrypcja.md`.

Plik Markdown `transkrypcja.md` ma zawierać:

~~~markdown
# Transkrypcja

Obrazek `zrzut.png` zatopiony w dokumencie.

## Prompt użyty do wygenerowania tekstu przez AI

```
Tutaj wklej treść promptu użytego do wygenerowania tekstu przez AI.
```

## Finalna wersja notatki

Końcowa wersja transkrypcji, gdzie wszystkie błędy zostały poprawione! Prawdopodobnie kod otrzymany przez AI będzie zawierał pewne błędy lub nieścisłości z racji automatycznego przetwarzania obrazu i nie będzie idealny. Twoim zadaniem jest zapewnienie poprawnego renderowania i zgodności (do pewnego stopnia) z rzeczywistym tekstem widocznym na zrzucie.
~~~

## Uwaga końcowa

Finalny folder powinien zawierać:

~~~text
pages/solutions/01_sol_markdown/
├── README.md
├── wykres.png
├── zrzut.png
└── transkrypcja.md
~~~

Upewnij się, że zawiera wszystkie wymagane pliki i że ich zawartość jest zgodna z wymaganiami przedstawionymi w zadaniach.