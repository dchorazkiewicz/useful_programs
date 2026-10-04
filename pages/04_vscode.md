# VS Code and GitHub Codespaces

W tym bloku przechodzimy od pracy wyłącznie w przeglądarce do pracy z **prawdziwym środowiskiem roboczym**.

Poznamy:

| Narzędzie | Do czego służy? |
| --- | --- |
| **Visual Studio Code (VS Code)** | edytor kodu i plików projektu |
| **GitHub Repositories** | otwieranie i edycja repozytorium GitHub bez klonowania |
| **GitHub Codespaces** | środowisko programistyczne działające w chmurze |
| **GitHub Copilot / OpenAI Codex** | pomoc AI w analizie i modyfikowaniu projektu |

---

# Visual Studio Code

## Co to jest VS Code?

**Visual Studio Code** jest edytorem przeznaczonym do pracy z kodem, tekstem i całymi projektami.

Nie jest tylko „Notatnikiem z kolorowym kodem”.

W jednym oknie możemy mieć:

- strukturę plików,
- kilka otwartych dokumentów,
- wyszukiwarkę,
- terminal,
- podgląd zmian Git,
- rozszerzenia,
- narzędzia AI.

Naturalnie są różne edytory kodu, np. PyCharm, Atom, Sublime Text, Jupyter Notebook czy JupyterLab. 

Powód ograniczenia się do VS Code? Jest popularny i dobrze współpracuje z GitHubem! Potrafisz dowieźć rzeczy w innych edytorach? Nie ma problemu.

---

## Instalacja: VS Code i Git

Do pracy z lokalną kopią repozytorium potrzebujemy **dwóch osobnych programów**: VS Code i Gita. Edytor ma wbudowany interfejs do Gita, ale korzysta z jego instalacji na komputerze.

1. Pobierz VS Code z [oficjalnej strony pobierania](https://code.visualstudio.com/download). Dostępne są wersje dla Windows, macOS i Linuxa. W Windows typowym wyborem jest **User Installer** dla architektury swojego komputera.
2. Uruchom instalator. Przydatne są opcje dodania `code` do **PATH** i pozycji **Open with Code** w menu kontekstowym plików i folderów, jeżeli instalator je oferuje.
3. Pobierz Git: [instalator dla Windows](https://git-scm.com/install/windows) lub [instalacja na pozostałych systemach](https://git-scm.com/install/). W Windows wybierz dostępność Gita również z wiersza poleceń i innych programów.
4. Po instalacji uruchom ponownie VS Code i otwórz **Terminal → New Terminal**. Sprawdź:

~~~bash
git --version
code --version
~~~

Jeśli polecenia nie są rozpoznawane, zamknij i otwórz ponownie również zewnętrzne terminale; w razie potrzeby sprawdź PATH. Instrukcja dla Windows: 

- [VS Code — instalacja](https://code.visualstudio.com/docs/setup/windows).

Przed pierwszym commitem ustaw dane autora, podstawiając własne wartości:

~~~bash
git config --global user.name "Jan Kowalski"
git config --global user.email "twoj-adres@example.com"
~~~

To podpis commitów, **nie logowanie do GitHuba**. Możesz użyć adresu `noreply` udostępnianego w ustawieniach poczty konta GitHub. Opcja `--global` ustawia dane dla wszystkich repozytoriów danego użytkownika. [Dokumentacja konfiguracji Gita w VS Code](https://code.visualstudio.com/docs/sourcecontrol/overview).

---

## Gdzie kliknąć? Mapa okna i ikon

Domyślnie po lewej znajduje się pionowy **Activity Bar**, obok panel plików, pośrodku edytor, a poniżej panel m.in. z terminalem. Na samym dole jest **Status Bar**. Położenie paneli można zmienić.

| Element | Jak rozpoznać ikonę i gdzie jej szukać? | Do czego służy? |
| --- | --- | --- |
| **Explorer** | dwa nakładające się arkusze, zwykle na górze lewego paska | drzewo plików; `Ctrl + Shift + E` |
| **Search** | lupa na lewym pasku | wyszukiwanie w projekcie; `Ctrl + Shift + F` |
| **Source Control** | rozgałęzienie z trzema połączonymi kółkami | zmiany i commity; `Ctrl + Shift + G` |
| **Run and Debug** | trójkąt „play” z symbolem robaka | uruchamianie i debugowanie kodu |
| **Extensions** | grupa kwadratowych klocków, jeden odsunięty | instalowanie dodatków; `Ctrl + Shift + X` |
| **Accounts** | sylwetka osoby w kółku, zwykle u dołu lewego paska | konta i logowanie |
| **Manage** | koło zębate | ustawienia i skróty |
| **Remote indicator** | znak przypominający `><` w lewym dolnym rogu | otwieranie środowisk zdalnych; po połączeniu również ich nazwa |
| **Remote Explorer** | ekran z małym okrągłym symbolem na lewym pasku, po dodaniu odpowiedniego rozszerzenia | lista środowisk i repozytoriów zdalnych |
| **Synchronizacja** | dwie zakrzywione strzałki przy nazwie gałęzi na dolnym pasku | pobranie i wysłanie commitów |

Najedź myszką na ikonę: podpowiedź pokaże jej nazwę. Jeśli panel jest ukryty, skorzystaj z **View → Open View…** lub palety poleceń. 

- [Mapa interfejsu VS Code](https://code.visualstudio.com/docs/editing/getting-started/userinterface).

Skróty w tym materiale dotyczą **Windows/Linux**. Na macOS część kombinacji jest inna; sprawdzisz je w menu lub w **Keyboard Shortcuts**.

---

## Folder jako projekt i panel Explorer

Najwygodniej otwierać w VS Code cały folder projektu, a nie pojedynczy plik.

Przykład struktury:

~~~text
projekt/
├── README.md
├── dane/
│   └── numbers.txt
├── skrypty/
│   └── analyze.sh
└── wyniki/
    └── summary.txt
~~~

Po otwarciu folderu panel **Explorer** pokazuje tę strukturę.

Dzięki temu edytor rozumie kontekst całego projektu.

1. Wybierz **File → Open Folder…** i wskaż folder projektu.
2. Kliknij ikonę **Explorer** — dwa arkusze — lub naciśnij `Ctrl + Shift + E`.
3. Rozwiń folder strzałką przy jego nazwie. Kliknięcie pliku otwiera go w edytorze, a dwuklik pozostawia osobną kartę.
4. Kliknij folder prawym przyciskiem, aby wybrać **New File** lub **New Folder**. Plik zapisuj przez `Ctrl + S`.

### Reveal in File Explorer: pokaż plik w folderze systemowym

W panelu Explorer kliknij plik lub folder **prawym przyciskiem → Reveal in File Explorer**. Windows otworzy jego lokalizację w systemowym Eksploratorze plików. To przydatne np. przy kopiowaniu ścieżki, dodawaniu załącznika albo otwieraniu wyniku w innym programie.

Na macOS odpowiednikiem jest **Reveal in Finder**, a na Linuxie **Open Containing Folder**. 

- [Dokumentacja Explorera](https://code.visualstudio.com/docs/editing/getting-started/userinterface#_explorer-view).

Ta operacja dotyczy plików lokalnych. Repozytorium otwarte wirtualnie z GitHuba nie ma zwykłego folderu na Twoim dysku; pliki Codespace znajdują się na maszynie w chmurze.

---

## GitHub: otwarcie zdalne, klon czy Codespace?

| Sposób pracy | Gdzie są pliki robocze? | Terminal do uruchamiania projektu | Kiedy wybrać? |
| --- | --- | --- | --- |
| **GitHub Repositories** | wirtualnie otwarte z GitHuba | nie w tym wirtualnym projekcie | czytanie kodu, niewielka poprawka tekstu |
| **Klonowanie** | w folderze na Twoim komputerze | lokalny | codzienna praca, skrypty, praca również offline |
| **GitHub Codespaces** | na maszynie w chmurze | zdalny Linux | gotowe środowisko bez lokalnej konfiguracji narzędzi projektu |

Logowanie do GitHuba daje dostęp do konta, ale samo nie otwiera ani nie klonuje repozytorium. Sposoby pracy opisują [dokumentacja GitHuba w VS Code](https://code.visualstudio.com/docs/sourcecontrol/github) i [dokumentacja Codespaces](https://docs.github.com/en/codespaces).

### Połączenie z repozytorium bez klonowania

1. Kliknij **Extensions** — kwadratowe klocki — albo `Ctrl + Shift + X`.
2. Wyszukaj i zainstaluj [GitHub Repositories](https://marketplace.visualstudio.com/items?itemName=GitHub.remotehub), wydawca **GitHub**.
3. Otwórz paletę poleceń przez `Ctrl + Shift + P` i wybierz **GitHub Repositories: Open Repository…**. Możesz też kliknąć ikonę **`><` w lewym dolnym rogu** i wybrać otwarcie zdalnego repozytorium.
4. Wybierz GitHub. Jeśli pojawi się prośba o logowanie, dokończ je w przeglądarce i wróć do VS Code.
5. Wklej adres repozytorium lub znajdź je na liście. Na zajęciach otwieraj **swój fork**, aby mieć możliwość zapisywania zmian.
6. Pliki pojawią się w **Explorerze**. Możesz je przeglądać i edytować.

**Uwaga na sposób zapisu:** w tym trybie commit wykonany przez rozszerzenie trafia bezpośrednio do repozytorium na GitHubie. Lokalny cykl „commit, a potem push” opisany niżej dotyczy klona lub Codespace. Wirtualny projekt nie udostępnia zwykłego terminala, uruchamiania i debugowania; do takich zadań przejdź do klona lub Codespaces. 

- [Instrukcja GitHub Repositories](https://code.visualstudio.com/docs/sourcecontrol/github#_github-repositories-extension).

### Klonowanie w VS Code — krok po kroku

Klonowanie pobiera repozytorium wraz z historią do lokalnego folderu. Wykonujesz je raz dla danej kopii; późniejsze aktualizacje pobierasz przez **Pull**.

1. Na stronie **swojego repozytorium/forka** na GitHubie kliknij **Code → Local → HTTPS** i ikonę kopiowania adresu.
2. W VS Code naciśnij `Ctrl + Shift + P` i wybierz **Git: Clone**. Alternatywnie otwórz **Source Control** — ikonę rozgałęzienia — i wybierz **Clone Repository**, jeśli przycisk jest widoczny.
3. Wklej adres. Opcja **Clone from GitHub** pozwala zamiast tego zalogować się i wybrać repozytorium z listy.
4. Wskaż **folder nadrzędny**, np. `Documents/GitHub`. VS Code utworzy w nim folder repozytorium.
5. Po pobraniu wybierz **Open** lub otwarcie w nowym oknie. Sprawdź, czy Explorer pokazuje pliki projektu.

### To samo w terminalu

Otwórz terminal w folderze nadrzędnym i zastąp przykładowy adres adresem swojego repozytorium:

~~~bash
git clone https://github.com/TWOJ_LOGIN/testowe_repozytorium.git
cd testowe_repozytorium
code .
~~~

Sprawdź, z czym połączony jest klon:

~~~bash
git remote -v
~~~

`origin` to zwyczajowa nazwa zdalnego repozytorium ustawiana przy klonowaniu. Jeśli pracujesz na forku, adres `origin` powinien prowadzić do Twojego forka.

**Download ZIP** daje pliki bez historii i połączenia Git — do pracy z commitami wybierz klonowanie. [Dokumentacja git clone](https://git-scm.com/docs/git-clone).

---

## Zintegrowany terminal

VS Code ma terminal dostępny bez opuszczania edytora.

Domyślnie otwiera się **poniżej edytora**, w panelu z kartami **Terminal**, **Problems** i **Output**.

1. Wybierz **Terminal → New Terminal**; **View → Terminal** pokazuje istniejący terminal. Skrót do pokazania/ukrycia to **Ctrl + \`** — klawisz z odwróconym apostrofem.
2. W prawym górnym rogu panelu kliknij **`+`**, aby otworzyć kolejny terminal. Strzałka obok pozwala wybrać profil, np. **PowerShell**, **Git Bash** lub zainstalowane środowisko WSL.
3. Sprawdź bieżący katalog przez `pwd`. Polecenia Gita wykonuj wewnątrz folderu repozytorium. Kliknięcie folderu w Explorerze prawym przyciskiem i **Open in Integrated Terminal** otwiera terminal w jego kontekście.
4. `Ctrl + C` przerywa działający program. Ikona **kosza** kończy dany terminal; samo ukrycie panelu nie kończy procesu.

---

## `code .`

Jeżeli polecenie `code` jest dostępne w terminalu, możemy otworzyć bieżący katalog w VS Code:

~~~bash
code .
~~~

Kropka oznacza bieżący katalog.

To bardzo popularny sposób otwierania projektu z terminala.

---

## Wyszukiwanie

W większym projekcie ręczne otwieranie każdego pliku jest niewygodne.

VS Code pozwala przeszukać wszystkie pliki projektu.

Typowy skrót:

~~~text
Ctrl + Shift + F
~~~

Możemy np. wyszukać wszystkie wystąpienia:

~~~text
wynik.txt
~~~

i zobaczyć, które pliki się do niego odwołują.

---

## Command Palette

Jedną z najważniejszych funkcji VS Code jest **Command Palette**.

Typowy skrót:

~~~text
Ctrl + Shift + P
~~~

Zamiast pamiętać, gdzie znajduje się dana opcja w menu, możemy wpisać jej nazwę.

Przykłady:

~~~text
Format Document
Git: Clone
Markdown: Open Preview
~~~

To dobra strategia pracy z rozbudowanym programem: nie trzeba znać całego interfejsu na pamięć.

---

## Source Control: od edycji pliku do GitHuba

Poniższa instrukcja dotyczy **lokalnego klona lub repozytorium w Codespace**.

~~~text
Pull → edycja → zapis pliku → diff → Stage → Commit → Push → sprawdzenie na GitHubie
~~~

### Zapis, Stage, Commit i Push — co oznaczają?

| Operacja | Co robi? | Czy zmiana trafia na GitHub? |
| --- | --- | --- |
| **Save** (`Ctrl + S`) | zapisuje treść pliku roboczego | nie |
| **Stage** (`+`) | wybiera zapisane zmiany do następnego commita | nie |
| **Commit** (`✓`) | zapisuje wybrane zmiany w historii tej kopii repozytorium | nie |
| **Push** | wysyła lokalne commity do zdalnego repozytorium | tak |
| **Pull** | pobiera i włącza zdalne commity do bieżącej gałęzi | pobiera z GitHuba |
| **Sync Changes** | wykonuje Pull, a następnie Push | pobiera i wysyła |

VS Code i terminal korzystają z tego samego repozytorium. Commit wykonany w terminalu zobaczysz również w edytorze:

- [Wprowadzenie do Source Control - po angielsku](https://code.visualstudio.com/docs/sourcecontrol/overview)

### Krok po kroku w interfejsie

1. **Przed edycją pobierz aktualną wersję.** Gdy nie masz niezapisanych w historii zmian, wybierz w palecie **Git: Pull**. Zmiany zrobione wcześniej na stronie GitHuba pojawią się w Twoim klonie.
2. **Edytuj i zapisz plik.** Otwórz np. `README.md`, dodaj krótki opis i naciśnij `Ctrl + S`.
3. **Otwórz Source Control** — ikonę rozgałęzienia z kółkami — przez kliknięcie lub `Ctrl + Shift + G`. Sekcja **Changes** pokaże zmiany: `M` — modified, `U` — untracked (nowy plik), `D` — deleted.
4. **Sprawdź diff.** Kliknij zmieniony plik. Zobaczysz stare i nowe linie, zwykle oznaczone czerwienią i zielenią. W przypadku kodu uruchom też odpowiednie sprawdzenie.
5. **Wybierz zmiany do commita.** Najedź na plik i kliknij **`+` — Stage Changes**. Plik trafi do **Staged Changes**. Kliknięcie `+` przy całej sekcji wybiera wszystkie jej pliki, więc najpierw sprawdź listę.
6. **Opisz i wykonaj commit.** W polu wiadomości wpisz np. `Dodaj opis projektu w README`. Kliknij **Commit / `✓`**. Commit obejmie stan wybrany podczas Stage; po kolejnej edycji zapisz plik i ponownie wykonaj Stage.
7. **Wyślij commit.** Wybierz **Git: Push** w palecie albo **Push** w menu **`…`** panelu. Jeśli chcesz jednocześnie pobrać aktualizacje, wybierz **Sync Changes** — dwie zakrzywione strzałki na dolnym pasku lub przycisk w panelu.
8. **Sprawdź rezultat.** Odśwież stronę repozytorium na GitHubie, na tej samej gałęzi. Sprawdź treść pliku i obecność commita.

Źródła: [wybieranie zmian i commit](https://code.visualstudio.com/docs/sourcecontrol/staging-commits) oraz [Pull, Push i Sync](https://code.visualstudio.com/docs/sourcecontrol/repos-remotes#_push-pull-and-sync).

Wskaźnik `↑2 ↓1` oznacza dwa commity do wysłania i jeden do pobrania według ostatnio znanego stanu serwera. **Fetch** odświeża tę wiedzę bez włączania zmian do plików. **Publish Branch** pojawia się, gdy nowa gałąź nie ma jeszcze ustawionej gałęzi zdalnej do śledzenia. [Dokumentacja git fetch](https://git-scm.com/docs/git-fetch).

### Ten sam cykl w terminalu

Przykład dla klona ze skonfigurowaną gałęzią zdalną. Wykonuj polecenia po kolei i czytaj wynik każdego z nich.

**Przed rozpoczęciem edycji**, przy czystym katalogu roboczym:

~~~bash
git status
git pull --ff-only
~~~

Po zmianie i zapisaniu `README.md`:

~~~bash
git diff -- README.md
git add README.md
git diff --staged
git commit -m "Dodaj opis projektu w README"
git push
git status
~~~

`git add README.md` odpowiada Stage tego pliku. `git diff --staged` pokazuje to, co trafi do commita. Ostatnie `git status` pozwala sprawdzić, czy zostały inne zmiany; rezultat potwierdź też na stronie GitHuba. [Dokumentacja git status](https://git-scm.com/docs/git-status).

Zwykłe `git pull` pobiera i integruje zmiany zgodnie z wybraną konfiguracją. Wariant **`git pull --ff-only`** pozwala tylko przesunąć gałąź do przodu, bez tworzenia merge commita. Jeśli lokalna i zdalna historia się rozeszły, zatrzyma się — wtedy trzeba świadomie wybrać merge lub rebase. [Dokumentacja git pull](https://git-scm.com/docs/git-pull).

Jeśli ktoś wysłał zmiany w trakcie Twojej pracy i `git push` zostanie odrzucony, zachowaj własne zmiany w commicie, pobierz zmiany i połącz historie. W prostym ćwiczeniu można użyć `git pull --no-rebase`, rozwiązać ewentualne konflikty i ponowić `git push`. W projekcie zespołowym stosuj uzgodnioną strategię historii.

### Gdy coś nie działa

| Sytuacja | Co sprawdzić lub zrobić? |
| --- | --- |
| **Source Control nie widzi repozytorium** | Otwórz folder sklonowanego projektu. Sprawdź `git --version` i `git status` w tym folderze. |
| **Git prosi o nazwę i e-mail autora** | Ustaw `git config user.name` i `user.email` według instrukcji instalacji. |
| **Push odrzucony z powodu uprawnień** | Sprawdź konto i `git remote -v`. Na zajęciach pracuj w swoim forku. |
| **Git wymaga logowania** | Dokończ logowanie w przeglądarce, jeżeli uruchomi je mechanizm uwierzytelniania. Hasło konta GitHub nie służy do uwierzytelniania operacji Git przez HTTPS; alternatywy to token lub SSH. |
| **Konflikt po Pull** | Otwórz konflikt w Source Control, porównaj obie wersje i przygotuj poprawny wynik. Zapisz, wykonaj Stage i zakończ merge commitem. Jeśli trwa rebase, po Stage użyj `git rebase --continue`. Następnie ponownie sprawdź plik. |

**Unstage (`−`)** usuwa zmianę z zestawu do commita, zachowując edycję pliku. **Discard Changes** usuwa niezacommitowane zmiany — to inna operacja. Nie rozwiązuj odrzuconego Push przez przypadkowe użycie **Force Push**.

Więcej o logowaniu: [uwierzytelnianie operacji Git na GitHubie](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github#authenticating-with-the-command-line).

---

## Podgląd Markdown: tekst i gotowy dokument obok siebie

Podstawowy podgląd `.md` jest **wbudowany** — nie wymaga rozszerzenia.

1. Otwórz np. `README.md`.
2. Naciśnij **`Ctrl + Shift + V`**, aby otworzyć podgląd.
3. Do pracy obok siebie wybierz **Markdown: Open Preview to the Side** w palecie poleceń. Skrót: **`Ctrl + K`, następnie `V`** — dwie kolejne czynności.
4. Możesz też kliknąć ikonę podglądu obok siebie w prawym górnym rogu edytora; najedź na przycisk, aby sprawdzić podpowiedź **Open Preview to the Side**.
5. Edytuj po jednej stronie i obserwuj wynik po drugiej. Sprawdź nagłówki, listy, tabele, obrazy i odnośniki. Zapisz plik przez `Ctrl + S`.

~~~markdown
# Mój projekt

Krótki opis projektu.

- dane wejściowe
- sposób uruchomienia
- wyniki
~~~

Podgląd VS Code pomaga sprawdzić składnię; wygląd na GitHubie może się trochę różnić. Po Push warto otworzyć również wersję na stronie repozytorium. 

- [Dokumentacja podglądu Markdown](https://code.visualstudio.com/docs/languages/markdown#_markdown-preview).

---

## Extensions: rozszerzenia, w tym podgląd PDF

1. Otwórz **Extensions** — ikonę kwadratowych klocków — lub `Ctrl + Shift + X`.
2. Wpisz nazwę dodatku. Sprawdź **wydawcę** i opis zastosowania.
3. Kliknij **Install**. Jeśli pojawi się **Reload**, przeładuj okno edytora.
4. Zainstalowany dodatek można później wyłączyć (**Disable**) lub usunąć (**Uninstall**) w jego karcie.

- [Instrukcja instalowania rozszerzeń](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace).

Na początek wystarczy kilka dodatków dobranych do pracy:

| Dodatek | Zastosowanie |
| --- | --- |
| [GitHub Repositories](https://marketplace.visualstudio.com/items?itemName=GitHub.remotehub) — GitHub | zdalne otwieranie repozytoriów bez klonowania |
| [GitHub Codespaces](https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces) — GitHub | połączenie z maszyną w chmurze |
| [vscode-pdf](https://marketplace.visualstudio.com/items?itemName=tomoki1207.pdf) — tomoki1207 | czytanie PDF w karcie VS Code |

### Jak otworzyć PDF?

Po instalacji **vscode-pdf** kliknij plik `.pdf` w Explorerze. Jeśli otworzy się w innym edytorze, wybierz w palecie **View: Reopen Editor With…** i wskaż zainstalowany podgląd PDF. To dodatek do **wyświetlania**, a nie pełnej edycji dokumentów PDF. [Opis rozszerzenia](https://marketplace.visualstudio.com/items?itemName=tomoki1207.pdf).

W WSL i Codespaces część rozszerzeń trzeba zainstalować w danym środowisku zdalnym. Nie każdy dodatek obsługuje wirtualne repozytorium GitHub lub wersję przeglądarkową.

---

## VS Code i WSL

VS Code może pracować bezpośrednio z projektem znajdującym się w WSL.

Wtedy:

- interfejs VS Code działa w Windows,
- pliki i terminal mogą działać w Linuxie,
- narzędzia projektu są instalowane w środowisku WSL.

To bardzo wygodne połączenie dla użytkowników Windows.

Po zainstalowaniu WSL dodaj rozszerzenie [WSL — Microsoft](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl). Otwórz folder projektu z terminala WSL przez `code .` albo użyj **WSL: Connect to WSL** w palecie. Na dolnym pasku sprawdź oznaczenie środowiska WSL. [Instrukcja pracy w WSL](https://code.visualstudio.com/docs/remote/wsl).

---

## Co jeszcze warto znać?

- **Szybkie otwieranie plików:** `Ctrl + P`, a następnie fragment nazwy. **Przejście do linii:** `Ctrl + G`.
- **Czytelna edycja:** `Alt + Z` włącza zawijanie długich wierszy, a `Ctrl + B` pokazuje lub ukrywa lewy panel. Ustawienia otworzysz przez `Ctrl + ,`.
- **Historia pliku:** wybierz plik w Explorerze i zajrzyj do **Timeline**. Możesz porównać jego wcześniejsze wersje; **Source Control Graph** pokazuje historię repozytorium. [Dokumentacja historii](https://code.visualstudio.com/docs/sourcecontrol/history).
- **Gałęzie:** przed większą zmianą wybierz **Git: Create Branch…**, np. `poprawki-readme`. Nazwę bieżącej gałęzi widać na dolnym pasku. Po commicie użyj **Publish Branch**; zmiany do głównej gałęzi można zgłosić przez Pull Request. [Praca z gałęziami](https://code.visualstudio.com/docs/sourcecontrol/branches-worktrees).
- **`.gitignore`:** pomijaj pliki tymczasowe i środowiska, np. `__pycache__/` oraz `.venv/`. Dodanie reguły nie usuwa z historii pliku już śledzonego przez Git. [Dokumentacja gitignore](https://git-scm.com/docs/gitignore).

---

## Krótki przykład: pełny cykl pracy

1. Sklonuj swój fork i otwórz jego folder w VS Code.
2. Znajdź `README.md` w Explorerze i pokaż jego lokalizację przez **Reveal in File Explorer**.
3. Pobierz aktualizacje przez **Git: Pull**.
4. Dopisz sekcję `## Moje środowisko pracy` z informacją, gdzie pracujesz: lokalnie, w WSL czy w Codespaces.
5. Otwórz podgląd Markdown obok tekstu, sprawdź wygląd i zapisz plik.
6. W Source Control obejrzyj diff, wykonaj Stage tylko tego pliku i commit z opisem `Opisz środowisko pracy`.
7. Wykonaj Push lub Sync Changes, a następnie sprawdź zmianę na GitHubie.
8. W terminalu wykonaj `git status`. Sprawdź, czy nie zostały niewysłane commity lub inne zmiany.

---

# GitHub Codespaces

## Co to jest Codespace?

**GitHub Codespaces** to środowisko programistyczne uruchamiane w chmurze na podstawie repozytorium GitHub.

Można je traktować jak gotowy komputer deweloperski dostępny przez przeglądarkę.

Po uruchomieniu Codespace otrzymujemy m.in.:

- edytor podobny do VS Code,
- terminal Linux,
- pliki repozytorium,
- Git,
- możliwość instalowania i uruchamiania narzędzi.

---

## Po co środowisko chmurowe?

Codespaces jest szczególnie użyteczny, gdy:

- pracujemy na komputerze bez przygotowanego środowiska,
- chcemy szybko rozpocząć pracę na innym urządzeniu,
- potrzebujemy Linuksa,
- lokalna instalacja sprawia problemy,
- chcemy mieć podobne środowisko dla wszystkich uczestników projektu.

---

## Jak uruchomić Codespace i połączyć go z VS Code?

1. Na GitHubie otwórz swój fork i wybierz **Code → Codespaces → Create codespace on…** dla właściwej gałęzi.
2. Poczekaj na przygotowanie środowiska. W przeglądarce pojawi się edytor i terminal Linux. [Tworzenie Codespace dla repozytorium](https://docs.github.com/en/codespaces/developing-in-a-codespace/creating-a-codespace-for-a-repository).
3. Jeśli chcesz pracować w aplikacji desktopowej, zainstaluj [GitHub Codespaces](https://marketplace.visualstudio.com/items?itemName=GitHub.codespaces) w VS Code.
4. Otwórz **Remote Explorer** — ikonę ekranu na lewym pasku — i wybierz **GitHub Codespaces**. Zaloguj się na GitHubie, jeżeli będzie to wymagane.
5. W palecie poleceń użyj **Codespaces: Connect to Codespace** i wybierz utworzone środowisko.
6. Sprawdź jego nazwę przy **`><` na dolnym pasku**. Terminal i narzędzia projektu działają teraz w chmurze, mimo że okno edytora jest na Twoim komputerze.

[Połączenie Codespaces z aplikacją VS Code](https://docs.github.com/en/codespaces/developing-in-a-codespace/using-github-codespaces-in-visual-studio-code).

---

## Repozytorium a Codespace

To dwie różne rzeczy.

**Repozytorium** przechowuje historię projektu.

**Codespace** jest środowiskiem, w którym nad projektem pracujemy.

Zmiana pliku w Codespace nie jest automatycznie zapisana jako commit w repozytorium.

Nadal obowiązuje sekwencja:

~~~text
edycja
↓
sprawdzenie
↓
commit
↓
push / synchronizacja
~~~

Nie traktuj więc samego istnienia pliku w działającym Codespace jako kopii zapasowej projektu.

---

## Zatrzymywanie Codespace

Codespace korzysta z zasobów chmurowych. Po zakończeniu pracy warto go zatrzymać.

W palecie poleceń wybierz **Codespaces: Stop Codespace** albo na [liście swoich Codespaces](https://github.com/codespaces) użyj menu **`…` → Stop codespace**. Zamknięcie karty przeglądarki nie jest tym samym co zatrzymanie maszyny. Zatrzymane środowisko nadal zajmuje miejsce, co może podlegać rozliczeniu. [Zatrzymywanie i uruchamianie Codespaces](https://docs.github.com/en/codespaces/developing-in-a-codespace/stopping-and-starting-a-codespace).

---

# Copilot, Codex i praca agentowa

Użytkownicy VS Code mogą korzystać z narzędzi AI do podpowiedzi kodu, wyjaśniania plików i wykonywania zadań w projekcie. Możliwe jest autouzupełnianie (Coplilot), zadawanie pytań i zlecanie zmian w plikach. Możliwe jest też uruchamianie tzw. Agentów (Codex,...), którzy mogą przeszukać projekt, wykonać zmiany i uruchomić sprawdzenia.


**Podpowiedź kodu** sugeruje kolejne linie podczas pisania.

**Chat** odpowiada na pytania i może wyjaśniać kod.

**Tryb agentowy** może otrzymać cel, przejrzeć kilka plików, zaproponować lub wykonać zmiany i uruchomić narzędzia sprawdzające.

Nazwy konkretnych trybów mogą różnić się między wersjami narzędzi, ale ważne jest rozróżnienie zakresu działania.

Praca z agentami będzie przedmiotem osobnego bloku szkoleniowego.

## Aktywacja GitHub Copilota

Copilot pomaga przez podpowiedzi podczas pisania oraz rozmowę i zadania agentowe.

1. W aktualnym VS Code znajdź **ikonę Copilota** na dolnym pasku — symbol przypominający głowę robota z goglami. Najedź na nią i wybierz **Use AI Features**.
2. Wybierz logowanie kontem GitHub, dokończ je w przeglądarce i wróć do edytora. Sprawdź, czy używasz konta z dostępem do Copilota.
3. Jeśli konto nie ma subskrypcji, kwalifikujące się konto może korzystać z **Copilot Free**. Limity i dostępne funkcje zależą od planu oraz ustawień organizacji.
4. Otwórz **Chat** przyciskiem w górnej części okna i zadaj pytanie, np. `Wyjaśnij strukturę tego projektu i rolę README.md`.
5. Sprawdź podpowiedzi w pliku z kodem: widoczna sugestia pojawia się jako przygaszony tekst; **Tab** ją przyjmuje, **Esc** odrzuca.

Jeśli opcji nie widać, sprawdź aktualizację VS Code oraz dostępność i włączenie rozszerzeń GitHub Copilot w **Extensions**. Logowanie do GitHuba w celu klonowania nie musi oznaczać, że funkcje Copilota są już aktywowane. [Aktualna instrukcja konfiguracji Copilota](https://code.visualstudio.com/docs/setup/copilot).

---

## OpenAI Codex w VS Code

**Codex** jest narzędziem OpenAI do pracy nad projektem: może czytać pliki, wyjaśniać kod, wprowadzać zmiany i uruchamiać sprawdzenia w granicach nadanych uprawnień. Można korzystać z niego przez rozszerzenie IDE; dostępny jest też **Codex CLI** do pracy w terminalu.

1. Otwórz **Extensions** (`Ctrl + Shift + X`) i wyszukaj **Codex**. Wybierz oficjalne rozszerzenie wydawcy **OpenAI**, do którego prowadzi przycisk instalacji w [dokumentacji Codex IDE](https://learn.chatgpt.com/docs/codex/ide).
2. Kliknij **Install**, a następnie ikonę **Codex** na pasku. Jeśli jej nie widzisz, uruchom **Codex: Open Codex Sidebar** w palecie poleceń.
3. Wybierz **Sign in with ChatGPT** i dokończ logowanie w przeglądarce. Alternatywą jest **Use API Key**; użycie klucza jest rozliczane przez konto OpenAI Platform. [Metody logowania](https://learn.chatgpt.com/docs/auth).
4. Otwórz folder projektu. Zacznij od pytania o pliki, a następnie zleć niewielką, konkretną zmianę.
5. Przejrzyj diff i wynik sprawdzeń, po czym wykonaj commit i Push według wcześniejszej instrukcji.

Aktywacja Copilota nie aktywuje automatycznie osobnego rozszerzenia Codex. Dostęp, limity i uprawnienia zależą od konta i konfiguracji.

Przykład pierwszego zadania:

~~~text
Przeczytaj README.md.
Dodaj krótką sekcję opisującą pliki i foldery projektu.
Zachowaj istniejącą treść.
~~~

---

## Dobre materiały o VS Code

- [Visual Studio Code — dokumentacja](https://code.visualstudio.com/docs)
- [VS Code — Getting Started](https://code.visualstudio.com/docs/getstarted/getting-started)
- [VS Code — terminal](https://code.visualstudio.com/docs/terminal/basics)
- [VS Code — WSL](https://code.visualstudio.com/docs/remote/wsl)

---

## Dobre materiały o Codespaces

- [GitHub Docs — Codespaces](https://docs.github.com/en/codespaces)
- [GitHub Docs — Quickstart for GitHub Codespaces](https://docs.github.com/en/codespaces/getting-started/quickstart)

---

## Dobre materiały o GitHub Copilot

- [GitHub Docs — GitHub Copilot](https://docs.github.com/en/copilot)
- [GitHub Docs — Copilot w IDE](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot)
- [Copilot: video how it all started](https://youtu.be/Xw_qbJp52cY?si=LJ_30tEEdkWbNtEM&t=42)
