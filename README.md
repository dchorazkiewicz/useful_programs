# Programy użytkowe

Nowa wersja kursu **Programy użytkowe** ma być praktycznym wprowadzeniem do nowoczesnego warsztatu cyfrowego wykorzystywanego w pracy naukowej i technicznej.

Kurs obejmuje **15 tygodni**, w tym **15 godzin wykładu** i **30 godzin ćwiczeń komputerowych**.

Wykład ma przede wszystkim pokazywać możliwości, dobre praktyki i powiązania między narzędziami. Ćwiczenia służą samodzielnemu wykonaniu konkretnych zadań.

## Notatki wykładowe i zadania

Materiały do pierwszych czterech bloków kursu:

1. [Markdown](pages/01_markdown.md) oraz dedykowane [zadania](pages/tasks/01_task_markdown.md)
2. [Google Colab](pages/02_colab.md) oraz dedykowane [zadania](pages/tasks/02_task_colab.md)
3. [Git i GitHub, Codespaces](pages/03_github.md) oraz dedykowane [zadania](pages/tasks/03_task_github.md)
4. [VS Code i GitHub Codespaces](pages/04_vscode.md) oraz dedykowane [zadania](pages/tasks/04_task_vscode.md)

## Foldery

- [tasks/](pages/tasks/) — zadania dla studentów.
- [solutions/](pages/solutions/) — miejsce na rozwiązania i pliki studentów w ich forkach.
- [examples/](pages/examples/) — przykłady do wykładów.
- [files/](pages/files/) — robocze obrazki i inne załączniki do notatek wykładowych.

## Filozofia kursu

Nie chodzi o nauczenie obsługi jednego programu, ale o opanowanie kompletnego workflow: od przygotowania materiałów i obliczeń, przez analizę i wizualizację danych, po dokumentację, publikację i współpracę.

Część narzędzi będzie omawiana szczegółowo, a część jako demonstracja technologii i wskazanie możliwości dalszej samodzielnej pracy.

Ważnym elementem kursu jest korzystanie z AI. AI może pomagać w pisaniu kodu, analizie danych, tworzeniu dokumentacji, rozwiązywaniu problemów i pracy z repozytorium, ale **odpowiedzialność za wynik pozostaje po stronie studenta**. Celem nie jest bezrefleksyjne zastępowanie pracy przez AI, lecz używanie nowych narzędzi do wykonywania pracy lepiej i sprawniej.

Student powinien umieć:

- sformułować problem,
- dobrać odpowiednie narzędzie,
- wykorzystać dokumentację, wyszukiwarkę i AI,
- sprawdzić otrzymany wynik,
- poprawić błędy,
- doprowadzić zadanie do poprawnego, działającego rezultatu.

## Dostęp do AI na zajęciach

**Na zajęciach kluczowe jest posiadanie dostępu do inteligentnego AI**, które pomaga przygotowywać tekst w Markdown, wyjaśniać kod i rozwiązywać problemy. Przed zajęciami załóż konto w wybranej usłudze i sprawdź, czy możesz z niej korzystać.

### Gemini — oferta dla studentów

[Gemini dla studentów](https://gemini.google/students/) oferuje kwalifikującym się studentom **12 miesięcy bezpłatnego dostępu do planu Google AI**. Szczegóły opisano także w [polskim komunikacie Google](https://blog.google/intl/pl-pl/nowosci-produktowe/sztuczna-inteligencja/student-offer-google-ai/). Dostępny plan i warunki zależą od kraju oraz weryfikacji statusu studenta. Przy aktywacji sprawdź zasady odnowienia subskrypcji — po okresie promocyjnym może ona stać się płatna.

Google zapowiedział również [Gemini 4 Argon](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/), którego dostępność będzie rozszerzana etapami, początkowo dla klientów płatnego API i Google AI Ultra. Oferta studencka nie gwarantuje automatycznego przejścia na ten model po roku.

### Inne czaty AI z darmowym dostępem

Można także korzystać z darmowego dostępu do następujących usług:

- [ChatGPT](https://chatgpt.com/),
- [Claude](https://claude.ai/),
- [Qwen](https://chat.qwen.ai/),
- [Grok](https://grok.com/),
- [Kimi](https://www.kimi.com/).

Trzeba jednak liczyć się z **bardzo dużymi ograniczeniami**: limitami wiadomości, przesyłanych plików i korzystania z najbardziej zaawansowanych modeli lub funkcji. Warunki różnią się między usługami i mogą się zmieniać. Po wyczerpaniu limitu może być konieczne poczekanie na jego odnowienie.

### AI na koncie uczelnianym — Microsoft 365

Warto sprawdzić również swoje konto uczelniane **Microsoft 365 (dawniej Office 365)**, używane np. do poczty Outlook, aplikacji Office i dysku OneDrive. Może ono zapewniać dostęp do [Microsoft 365 Copilot Chat](https://learn.microsoft.com/en-us/copilot/faq); dostęp dla studentów zależy od ustawień uczelni.

Microsoft udostępnia w Copilocie modele OpenAI, m.in. [GPT-5.5](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes) oraz [rodzinę GPT-5.6](https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/available-today-openai%E2%80%99s-gpt-5-6-in-microsoft-365-copilot/4533152). Dostęp do konkretnego modelu, np. [GPT-5.6 Sol](https://learn.chatgpt.com/docs/models), trzeba sprawdzić w danej usłudze — zależy od licencji i konfiguracji uczelni. Copilot i ChatGPT to osobne usługi.

W Microsoft 365 dyskiem chmurowym jest **OneDrive**; **Google Drive** należy do pakietu Google Workspace.

## Generowanie materiałów i formatowanie Markdown

Kurs będzie w dużej mierze bazował na **generowaniu materiałów, notatek i raportów przy pomocy AI**. Warto od początku stosować zasady opisane w [hints.md](pages/hints.md), aby uniknąć wielu typowych problemów z renderowaniem Markdown i wzorów matematycznych na GitHubie. Plik opisuje m.in. zapis wzorów `$...$` i `$$...$$`, odstępy między blokami oraz sposób zapisywania macierzy i równań wielowierszowych.

Przy generowaniu materiałów warto dołączać `hints.md` do promptu jako kontekst i prosić AI o przestrzeganie zawartych w nim reguł. Po wygenerowaniu dokumentu sprawdź jego wyrenderowany widok, szczególnie wzory, tabele i bloki kodu.

## Organizacja pracy

Podstawowym środowiskiem organizacyjnym kursu będzie **GitHub**.

Na początku kursu student wykonuje **fork repozytorium bazowego** (specjalny rodzaj kopii). W swoim repozytorium otrzymuje notatki, instrukcje i zestawy zadań oraz przygotowane miejsca na rozwiązania.

Schemat pracy:

1. student wykonuje zadanie w przewidzianym folderze,
2. zapisuje wynik w swoim repozytorium GitHub,
3. rozwiązanie jest monitorowane zdalnie przez prowadzącego,
4. informacja o zaliczeniu zadań albo wymaganych poprawkach trafiać będzie do **GitHub Issues**,
5. w razie potrzeby student poprawia rozwiązanie i zgłasza poprzez **GitHub Issues** kolejną wersję.

Repozytorium studenta pełni więc jednocześnie funkcję:

- miejsca nauki,
- miejsca pracy,
- historii postępów,
- zbioru rozwiązań,
- dokumentacji procesu uczenia się,
- podstawy zaliczenia kursu.

## Zadania i weryfikacja

Zadania będą możliwie konkretne i praktyczne. Tam, gdzie to możliwe, ich weryfikacja ma być częściowo automatyczna: sprawdzane będą m.in. obecność wymaganych plików, ich struktura, poprawność kodu, wymagane wyniki i elementy dokumentacji.

Feedback będzie przekazywany przez GitHub Issues. Student może otrzymać informację, że zadanie zostało zaliczone albo listę elementów wymagających poprawy.

Celem nie jest wykonanie zadań dokładnie jedną metodą. Liczy się **poprawny rezultat, umiejętność wykorzystania narzędzi i odpowiedzialność za dostarczony wynik**.

## Słowo kluczowe

**Dowożenie** co oznacza terminowe i systematyczne dostarczanie rozwiązań zadań o wymaganej jakości. Będą Państwo oceniani również pod kątem regularności i jakości dostarczanych rozwiązań. W codziennym życiu nikogo nie interesuje droga i obrane sposoby. Liczy się spełnianie deadlinów i liczy się jedynie wysoka jakość dowożonych rezultatów. I za to biorą Państwo pełną odpowiedzialność. Jest to kluczowy element kursu!  Współcześnie mają Państwo najnowocześniejsze narzędzia do pracy i będziemy Państwa z tego rozliczać. Mniej z wiedzy, regułek, a bardziej z jakości dostarczanych rezultatów.

## Ocenianie

Wstępna zasada oceniania:

- wykonanie wszystkich wymaganych zadań na oczekiwanym przyzwoitym poziomie: **4.0**,
- drobne braki lub uchybienia: **3.5**,
- większe braki: **3.0**,
- niewystarczająca realizacja zadań: **2.0**.

Oceny **4.5 i 5.0** wymagają dodatkowo końcowej, prowadzonej na żywo ewaluacji praktycznej. Student powinien na żywo pokazać biegłość w stosowaniu poznanych technologii, wyjaśnić własne rozwiązania i samodzielnie poradzić sobie z krótkimi zadaniami lub problemami.

## Główna ścieżka kursu

**Markdown / Colab → GitHub → terminal / VS Code / Codespaces → Python / Wolfram / Octave → dane / wykresy / symulacje → HTML / MkDocs / GitHub Pages → LaTeX / Overleaf → AI / workflow naukowy → grafika → Microsoft 365 / Google Docs/Sheets/Presentations → praca mobilna i integracje.**

Efektem kursu ma być umiejętność przeprowadzenia kompletnego workflow naukowego lub technicznego: od przygotowania materiałów i obliczeń, przez analizę i wizualizację wyników, po ich dokumentację i publikację.