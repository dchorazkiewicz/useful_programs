# 2. Terminal, WSL, VS Code i środowiska chmurowe

W tym bloku przechodzimy od pracy wyłącznie w przeglądarce do pracy z **prawdziwym środowiskiem roboczym**.

Poznamy:

| Narzędzie | Do czego służy? |
| --- | --- |
| **terminal** | tekstowy sposób wydawania poleceń komputerowi |
| **Bash** | popularna powłoka używana w systemach Linux |
| **WSL** | Linux uruchomiony wewnątrz Windows |
| **Visual Studio Code** | edytor kodu i plików projektu |
| **GitHub Codespaces** | środowisko programistyczne działające w chmurze |
| **Copilot / agent** | pomoc w analizie i modyfikowaniu projektu |

Nie chodzi o zapamiętanie kilkudziesięciu komend. Ważniejsze jest zrozumienie kilku podstawowych operacji i umiejętność sprawdzenia dokumentacji, gdy potrzebujemy czegoś więcej.

---

# Terminal

## Co to jest terminal?

**Terminal** to interfejs tekstowy, przez który wydajemy komputerowi polecenia.

Zamiast kliknąć folder i wybrać „Nowy plik”, możemy napisać:

~~~bash
mkdir wyniki
touch wyniki/raport.txt
~~~

Efekt:

~~~text
wyniki/
└── raport.txt
~~~

Terminal nie jest osobnym systemem operacyjnym. Jest sposobem komunikowania się z systemem.

---

## Terminal, shell i Bash

Te trzy pojęcia warto rozróżniać.

**Terminal** to okno lub aplikacja, w której wpisujemy polecenia.

**Shell**, czyli powłoka, to program, który interpretuje wpisane polecenia.

**Bash** jest jednym z najpopularniejszych shelli używanych w Linuxie.

Schemat jest więc prosty:

~~~text
użytkownik
   ↓
terminal
   ↓
shell, np. Bash
   ↓
system operacyjny
~~~

Na Windows możemy spotkać m.in. PowerShell i Command Prompt. Po uruchomieniu WSL możemy korzystać z Bash i narzędzi linuksowych.

---

# Pierwsze polecenia

## Gdzie jestem? — `pwd`

Polecenie:

~~~bash
pwd
~~~

oznacza **print working directory**.

Przykładowy wynik:

~~~text
/home/student/projekt
~~~

To aktualny katalog roboczy.

Przy pracy w terminalu jedno z najważniejszych pytań brzmi:

> W jakim katalogu właśnie jestem?

Jeśli coś „zniknęło” albo program nie znajduje pliku, bardzo często przyczyną jest praca w innym katalogu niż oczekiwaliśmy.

---

## Co tutaj jest? — `ls`

Polecenie:

~~~bash
ls
~~~

pokazuje zawartość bieżącego katalogu.

Przykład:

~~~text
README.md
dane.csv
wyniki
~~~

Bardziej szczegółowy widok:

~~~bash
ls -la
~~~

Opcja `-l` włącza widok szczegółowy, a `-a` pokazuje także pliki ukryte.

Polecenia często mają postać:

~~~text
polecenie opcje argumenty
~~~

Przykład:

~~~bash
ls -la wyniki
~~~

Tutaj:

- `ls` — polecenie,
- `-la` — opcje,
- `wyniki` — argument, czyli katalog, który chcemy obejrzeć.

---

# Ścieżki

## Ścieżka opisuje położenie pliku

Przykład:

~~~text
/home/student/projekt/dane/wyniki.csv
~~~

to **ścieżka absolutna** — opisuje położenie od początku systemu plików.

Jeśli znajdujemy się już w katalogu:

~~~text
/home/student/projekt
~~~

możemy użyć **ścieżki względnej**:

~~~text
dane/wyniki.csv
~~~

Ścieżka względna jest liczona od aktualnego katalogu roboczego.

---

## Kilka ważnych skrótów

`.` oznacza bieżący katalog.

`..` oznacza katalog nadrzędny.

`~` oznacza katalog domowy użytkownika.

Przykłady:

~~~bash
cd ..
~~~

przechodzi o poziom wyżej.

~~~bash
cd ~
~~~

przechodzi do katalogu domowego.

~~~bash
cd .
~~~

pozostaje w bieżącym katalogu.

---

## Zmiana katalogu — `cd`

Polecenie:

~~~bash
cd projekty
~~~

przechodzi do katalogu `projekty`.

Możemy też podać dłuższą ścieżkę:

~~~bash
cd ~/projekty/programy_uzytkowe
~~~

Po zmianie katalogu warto sprawdzić:

~~~bash
pwd
~~~

---

# Tworzenie plików i katalogów

## `mkdir` — nowy katalog

~~~bash
mkdir wyniki
~~~

tworzy katalog `wyniki`.

Jeżeli chcemy utworzyć kilka poziomów naraz:

~~~bash
mkdir -p projekt/dane/wejsciowe
~~~

otrzymamy:

~~~text
projekt/
└── dane/
    └── wejsciowe/
~~~

---

## `touch` — pusty plik

~~~bash
touch raport.md
~~~

tworzy pusty plik `raport.md`, jeśli wcześniej nie istniał.

Możemy utworzyć kilka plików:

~~~bash
touch dane.txt wynik.txt opis.md
~~~

---

## `cp` — kopiowanie

~~~bash
cp dane.txt kopia_danych.txt
~~~

Po operacji mamy dwa pliki:

~~~text
dane.txt
kopia_danych.txt
~~~

Katalog wraz z zawartością można kopiować rekurencyjnie:

~~~bash
cp -r dane backup_dane
~~~

---

## `mv` — przenoszenie i zmiana nazwy

Zmiana nazwy:

~~~bash
mv raport.txt raport.md
~~~

Przeniesienie do katalogu:

~~~bash
mv raport.md wyniki/
~~~

`mv` nie tworzy kopii. Oryginalny plik zmienia nazwę albo położenie.

---

## `rm` — usuwanie

Usunięcie pliku:

~~~bash
rm stary_plik.txt
~~~

Usunięcie katalogu z zawartością:

~~~bash
rm -r stary_katalog
~~~

> **Uwaga:** terminal zwykle nie przenosi takich plików do kosza. `rm` może usunąć dane bez prostego sposobu ich odzyskania.

Nie wykonuj poleceń typu:

~~~bash
rm -rf ...
~~~

jeżeli nie rozumiesz dokładnie, jaki katalog zostanie usunięty.

Podobna zasada dotyczy `sudo`: nie wklejaj do terminala poleceń administracyjnych znalezionych w Internecie lub wygenerowanych przez AI bez zrozumienia ich działania.

---

# Czytanie plików

## `cat`

~~~bash
cat wynik.txt
~~~

wyświetla cały plik.

Jeżeli `wynik.txt` zawiera:

~~~text
42
~~~

to efekt będzie:

~~~text
42
~~~

`cat` jest wygodny dla krótkich plików.

---

## `head` i `tail`

Pierwsze linie:

~~~bash
head dane.txt
~~~

Pierwsze trzy:

~~~bash
head -n 3 dane.txt
~~~

Ostatnie trzy:

~~~bash
tail -n 3 dane.txt
~~~

To bardzo użyteczne przy dużych plikach z danymi lub logami.

---

# Pisanie do plików

## `echo`

~~~bash
echo "Hello"
~~~

Efekt:

~~~text
Hello
~~~

Możemy skierować wynik do pliku.

~~~bash
echo "Hello" > hello.txt
~~~

Plik `hello.txt` będzie zawierał:

~~~text
Hello
~~~

---

## Przekierowanie `>`

Operator `>` zapisuje wynik polecenia do pliku.

~~~bash
pwd > katalog.txt
~~~

Jeżeli plik już istnieje, jego wcześniejsza zawartość zostanie zastąpiona.

---

## Dopisywanie `>>`

Operator `>>` dopisuje dane na końcu pliku.

~~~bash
echo "pierwsza linia" > notatki.txt
echo "druga linia" >> notatki.txt
~~~

Efekt:

~~~text
pierwsza linia
druga linia
~~~

---

# Potoki — `|`

Jedna z najważniejszych idei terminala polega na łączeniu małych narzędzi.

Operator potoku `|` przekazuje wynik jednego polecenia jako wejście następnego.

Schemat:

~~~text
polecenie A | polecenie B
~~~

Przykład:

~~~bash
seq 1 100 | wc -l
~~~

`seq 1 100` generuje liczby od 1 do 100, a `wc -l` liczy linie.

Efekt:

~~~text
100
~~~

Nie musimy tworzyć pliku pośredniego. Wynik pierwszego programu przepływa bezpośrednio do drugiego.

---

# Kilka bardzo przydatnych narzędzi

## `wc` — liczenie

~~~bash
wc -l dane.txt
~~~

liczy liczbę linii.

~~~bash
wc -w raport.md
~~~

liczy słowa.

---

## `grep` — wyszukiwanie tekstu

Mamy plik:

~~~text
INFO start
ERROR brak pliku
INFO ponowna próba
ERROR brak dostępu
INFO koniec
~~~

Polecenie:

~~~bash
grep "ERROR" log.txt
~~~

zwróci:

~~~text
ERROR brak pliku
ERROR brak dostępu
~~~

Możemy połączyć `grep` z `wc`:

~~~bash
grep "ERROR" log.txt | wc -l
~~~

Efekt:

~~~text
2
~~~

---

## `sort` — sortowanie

~~~bash
sort nazwiska.txt
~~~

sortuje linie tekstowo.

Dla liczb warto użyć sortowania numerycznego:

~~~bash
sort -n liczby.txt
~~~

---

## `find` — szukanie plików

Aby znaleźć wszystkie pliki Markdown w bieżącym katalogu i podkatalogach:

~~~bash
find . -name "*.md"
~~~

Przykładowy wynik:

~~~text
./README.md
./pages/01.md
./pages/02.md
~~~

---

# Mały przykład pracy z danymi

Wygenerujmy liczby od 1 do 100:

~~~bash
seq 1 100 > numbers.txt
~~~

Sprawdźmy liczbę wierszy:

~~~bash
wc -l numbers.txt
~~~

Efekt:

~~~text
100 numbers.txt
~~~

Pierwsze pięć liczb:

~~~bash
head -n 5 numbers.txt
~~~

Efekt:

~~~text
1
2
3
4
5
~~~

Ostatnie trzy:

~~~bash
tail -n 3 numbers.txt
~~~

Efekt:

~~~text
98
99
100
~~~

Możemy policzyć sumę za pomocą `awk`:

~~~bash
awk '{s += $1} END {print s}' numbers.txt
~~~

Efekt:

~~~text
5050
~~~

Na tym etapie nie trzeba znać całego języka `awk`. Warto jednak zobaczyć, że terminal pozwala szybko połączyć małe narzędzia w użyteczny proces przetwarzania danych.

---

# Skrypty Bash

## Po co skrypt?

Jeżeli zestaw poleceń wykonujemy wiele razy, możemy zapisać go do pliku.

Przykład `hello.sh`:

~~~bash
#!/usr/bin/env bash

echo "Start"
pwd
echo "Koniec"
~~~

Uruchomienie:

~~~bash
bash hello.sh
~~~

Przykładowy wynik:

~~~text
Start
/home/student/projekt
Koniec
~~~

Skrypt jest więc **zapisanym przepisem na wykonanie serii poleceń**.

---

## Zmienne

~~~bash
n=100
echo "$n"
~~~

Efekt:

~~~text
100
~~~

W Bash przy przypisaniu nie stawiamy spacji wokół znaku `=`.

Poprawnie:

~~~bash
n=100
~~~

Niepoprawnie:

~~~bash
n = 100
~~~

---

# WSL

## Co to jest WSL?

**WSL — Windows Subsystem for Linux** pozwala uruchamiać środowisko Linux bezpośrednio w Windows.

Dzięki WSL użytkownik Windows może korzystać m.in. z:

- Bash,
- typowych poleceń linuksowych,
- Pythona,
- Git,
- kompilatorów,
- narzędzi programistycznych używanych na serwerach Linux.

Nie jest to „zamiana Windowsa na Linux”. Windows nadal działa normalnie, a Linux jest dodatkowym środowiskiem.

---

## Dystrybucja Linux

WSL może uruchamiać różne dystrybucje Linux. Popularnym wyborem jest **Ubuntu**.

Po uruchomieniu Ubuntu w WSL zobaczymy terminal Bash i katalog domowy użytkownika.

Przykład:

~~~bash
pwd
~~~

może zwrócić:

~~~text
/home/student
~~~

---

## Dyski Windows z poziomu WSL

Dysk `C:` jest zwykle dostępny jako:

~~~text
/mnt/c/
~~~

Przykładowo katalog użytkownika Windows może wyglądać:

~~~text
/mnt/c/Users/NazwaUzytkownika/
~~~

W pracy programistycznej często wygodniej trzymać projekty używane intensywnie przez narzędzia linuksowe bezpośrednio w systemie plików WSL, np.:

~~~text
/home/student/projekty/
~~~

---

## Windows i Linux różnią się ścieżkami

Windows:

~~~text
C:\Users\Student\projekt
~~~

Linux:

~~~text
/home/student/projekt
~~~

W Linux separatorem katalogów jest ukośnik:

~~~text
/
~~~

a wielkość liter ma znaczenie.

Pliki:

~~~text
Wynik.txt
wynik.txt
~~~

są w Linux dwoma różnymi plikami.

---

## Dobre materiały o Bash i WSL

- [GNU Bash Manual](https://www.gnu.org/software/bash/manual/bash.html)
- [Microsoft Learn — Windows Subsystem for Linux](https://learn.microsoft.com/windows/wsl/)
- [Microsoft Learn — podstawowe polecenia WSL](https://learn.microsoft.com/windows/wsl/basic-commands)

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

---

## Folder jako projekt

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

---

## Zintegrowany terminal

VS Code ma terminal dostępny bez opuszczania edytora.

Możemy więc:

1. edytować `analyze.sh`,
2. zapisać plik,
3. przejść do terminala,
4. uruchomić:

~~~bash
bash analyze.sh
~~~

5. wrócić do pliku i poprawić kod.

To znacznie wygodniejsze niż ciągłe przełączanie się między wieloma aplikacjami.

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

## Git w VS Code

Panel **Source Control** pokazuje pliki zmienione od ostatniego commita.

Możemy zobaczyć diff, czyli dokładne różnice między wersjami.

Przykład:

~~~diff
- suma=5000
+ suma=5050
~~~

Taki podgląd warto obejrzeć **przed wykonaniem commita**, szczególnie jeśli zmiany przygotowywało narzędzie AI.

---

## VS Code i WSL

VS Code może pracować bezpośrednio z projektem znajdującym się w WSL.

Wtedy:

- interfejs VS Code działa w Windows,
- pliki i terminal mogą działać w Linuxie,
- narzędzia projektu są instalowane w środowisku WSL.

To bardzo wygodne połączenie dla użytkowników Windows.

---

## Dobre materiały o VS Code

- [Visual Studio Code — dokumentacja](https://code.visualstudio.com/docs)
- [VS Code — Getting Started](https://code.visualstudio.com/docs/getstarted/getting-started)
- [VS Code — terminal](https://code.visualstudio.com/docs/terminal/basics)
- [VS Code — WSL](https://code.visualstudio.com/docs/remote/wsl)

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

Dostępne limity i rozliczanie zależą od rodzaju konta i ustawień GitHuba, dlatego przed intensywnym korzystaniem warto sprawdzić aktualne zasady swojego konta.

---

## Dobre materiały o Codespaces

- [GitHub Docs — Codespaces](https://docs.github.com/en/codespaces)
- [GitHub Docs — Quickstart for GitHub Codespaces](https://docs.github.com/en/codespaces/getting-started/quickstart)

---

# Copilot i praca agentowa

## Podpowiedź, chat i agent

Narzędzia AI w edytorze mogą działać na kilka sposobów.

**Podpowiedź kodu** sugeruje kolejne linie podczas pisania.

**Chat** odpowiada na pytania i może wyjaśniać kod.

**Tryb agentowy** może otrzymać cel, przejrzeć kilka plików, zaproponować lub wykonać zmiany i uruchomić narzędzia sprawdzające.

Nazwy konkretnych trybów mogą różnić się między wersjami narzędzi, ale ważne jest rozróżnienie zakresu działania.

---

## Dobry prompt techniczny

Zamiast:

~~~text
napraw to
~~~

lepiej przekazać:

~~~text
Przeczytaj analyze.sh i numbers.txt.

Cel:
dodaj do summary.txt średnią liczb z numbers.txt.

Wymagania:
- nie zmieniaj nazw istniejących plików,
- zachowaj obecne pola count, sum, min i max,
- dodaj pole average,
- uruchom skrypt po zmianie,
- sprawdź wynik,
- pokaż mi diff.
~~~

Taki prompt zawiera:

1. **kontekst**,
2. **cel**,
3. **ograniczenia**,
4. **oczekiwany test**.

To dużo bardziej niezawodne niż ogólne „zrób dobrze”.

---

## Agent nie zastępuje sprawdzenia zmian

Jeżeli agent zmodyfikował plik, przed commitem warto:

1. otworzyć diff,
2. przeczytać zmienione linie,
3. uruchomić kod,
4. sprawdzić wygenerowany wynik,
5. dopiero potem wykonać commit.

Bardzo użyteczny model pracy:

~~~text
poproś
↓
obejrzyj diff
↓
uruchom
↓
sprawdź wynik
↓
zaakceptuj albo popraw
~~~

---

## Dobre materiały o GitHub Copilot

- [GitHub Docs — GitHub Copilot](https://docs.github.com/en/copilot)
- [GitHub Docs — Copilot w IDE](https://docs.github.com/en/copilot/using-github-copilot/getting-code-suggestions-in-your-ide-with-github-copilot)

---

# Zadania dla studenta

Wszystkie rozwiązania z tego bloku umieść w folderze:

~~~text
zadania/02_terminal_wsl_vscode_chmura/
~~~

Po wykonaniu zadań folder powinien zawierać:

~~~text
zadania/02_terminal_wsl_vscode_chmura/
├── README.md
├── environment.txt
├── commands.md
├── numbers.txt
├── ending5.txt
├── analyze.sh
├── summary.txt
├── vscode.md
├── agent_prompt.md
└── agent_review.md
~~~

Nie zmieniaj nazw wymaganych plików.

---

## Zadanie 1. Poznaj swoje środowisko

W terminalu Linux — w WSL, Codespaces albo innym środowisku Linux — wykonaj:

~~~bash
pwd
uname -s
whoami
git --version
python3 --version
~~~

Następnie utwórz plik `environment.txt` zawierający pięć opisanych pól.

Przykładowa struktura:

~~~text
pwd=/home/student/projekt
kernel=Linux
user=student
git=git version ...
python=Python 3...
~~~

Wartości zależą od Twojego środowiska.

Możesz utworzyć plik ręcznie albo wykorzystać przekierowania:

~~~bash
echo "pwd=$(pwd)" > environment.txt
echo "kernel=$(uname -s)" >> environment.txt
echo "user=$(whoami)" >> environment.txt
echo "git=$(git --version)" >> environment.txt
echo "python=$(python3 --version)" >> environment.txt
~~~

### Sprawdzenie

Będzie można sprawdzić:

- istnienie `environment.txt`,
- obecność pól `pwd=`, `kernel=`, `user=`, `git=` i `python=`,
- czy pole `kernel` wskazuje środowisko Linux.

---

## Zadanie 2. Plik danych bez ręcznego przepisywania

Wygeneruj liczby od 1 do 100:

~~~bash
seq 1 100 > numbers.txt
~~~

Sprawdź:

~~~bash
wc -l numbers.txt
~~~

Oczekiwany wynik zawiera liczbę:

~~~text
100
~~~

Następnie wybierz liczby kończące się cyfrą 5:

~~~bash
grep -E '5$' numbers.txt > ending5.txt
~~~

Plik `ending5.txt` powinien zawierać:

~~~text
5
15
25
35
45
55
65
75
85
95
~~~

Sprawdź liczbę wierszy:

~~~bash
wc -l ending5.txt
~~~

Oczekiwany wynik:

~~~text
10 ending5.txt
~~~

Utwórz plik `commands.md` i dla każdej użytej komendy zapisz:

- polecenie,
- jednozdaniowe wyjaśnienie,
- otrzymany wynik.

Nie kopiuj samej listy komend. Pokaż, że rozumiesz, co robi `>`, potok `|` oraz `grep`.

### Sprawdzenie

Będzie można sprawdzić dokładną zawartość `numbers.txt` i `ending5.txt` oraz strukturę `commands.md`.

---

## Zadanie 3. Skrypt analizujący dane

Utwórz skrypt `analyze.sh`.

Pierwsza wersja ma wygenerować `summary.txt` zawierający:

~~~text
count=100
sum=5050
min=1
max=100
~~~

Możesz wykorzystać:

~~~bash
count=$(wc -l < numbers.txt)
sum=$(awk '{s += $1} END {print s}' numbers.txt)
min=$(head -n 1 numbers.txt)
max=$(tail -n 1 numbers.txt)

echo "count=$count" > summary.txt
echo "sum=$sum" >> summary.txt
echo "min=$min" >> summary.txt
echo "max=$max" >> summary.txt
~~~

Uruchom:

~~~bash
bash analyze.sh
~~~

Następnie:

~~~bash
cat summary.txt
~~~

i sprawdź, czy otrzymujesz dokładnie wymagane wartości.

### Sprawdzenie

Będzie można:

- uruchomić `analyze.sh` ponownie,
- sprawdzić, czy powstaje `summary.txt`,
- porównać wartości `count`, `sum`, `min` i `max`.

---

## Zadanie 4. Praca z projektem w VS Code

Otwórz folder:

~~~text
zadania/02_terminal_wsl_vscode_chmura/
~~~

jako projekt w VS Code.

Jeśli polecenie jest dostępne, możesz użyć:

~~~bash
code .
~~~

Utwórz plik `vscode.md`.

Ma zawierać sekcje:

~~~markdown
# VS Code

## Explorer

## Terminal

## Search

## Source Control
~~~

W każdej sekcji napisz 2–4 zdania:

- **Explorer** — co pokazuje i jak pomaga w pracy,
- **Terminal** — uruchom `bash analyze.sh` z terminala VS Code i opisz wynik,
- **Search** — wyszukaj w całym projekcie słowo `summary` i napisz, w których plikach występuje,
- **Source Control** — przed commitem obejrzyj listę zmienionych plików i opisz, do czego służy diff.

To zadanie jest celowo opisowe: sprawdzamy, czy student rozumie interfejs, z którego korzysta.

---

## Zadanie 5. Kontrolowana zmiana z pomocą agenta AI

Teraz wykorzystaj Copilota albo inne narzędzie AI działające na plikach projektu.

Zapisz użyty prompt w:

~~~text
agent_prompt.md
~~~

Prompt ma zlecać agentowi zmodyfikowanie `analyze.sh` tak, aby do `summary.txt` zostało dodane pole:

~~~text
average=50.5
~~~

Pozostałe pola mają pozostać bez zmian.

Po modyfikacji uruchom:

~~~bash
bash analyze.sh
cat summary.txt
~~~

Ostateczny plik powinien wyglądać:

~~~text
count=100
sum=5050
min=1
max=100
average=50.5
~~~

Następnie obejrzyj diff zmiany.

Utwórz `agent_review.md` ze strukturą:

~~~markdown
# Review zmiany AI

## Co agent zmienił?

## Jak sprawdziłem zmianę?

## Czy wynik jest poprawny?

## Co zaakceptowałem albo poprawiłem ręcznie?
~~~

W każdej sekcji napisz krótki, konkretny opis.

### Sprawdzenie

Będzie można automatycznie:

- uruchomić `analyze.sh`,
- sprawdzić wszystkie wartości w `summary.txt`,
- sprawdzić istnienie `agent_prompt.md`,
- sprawdzić strukturę `agent_review.md`.

Ocena opisu będzie wymagała także sprawdzenia, czy student rzeczywiście odnosi się do wykonanej zmiany.

---

## Zadanie 6. README bloku

Utwórz `README.md` dla całego folderu.

Powinien zawierać:

- krótki opis wykonanych zadań,
- listę wszystkich wymaganych plików,
- informację, czy pracowałeś w WSL, Codespaces czy innym środowisku Linux,
- wynik analizy danych,
- link do `commands.md`,
- link do `vscode.md`,
- link do `agent_review.md`,
- checklistę ukończenia zadań.

W README pokaż także wynik końcowy:

~~~text
count=100
sum=5050
min=1
max=100
average=50.5
~~~

---

# Checklista końcowa

Przed zgłoszeniem bloku sprawdź:

- [ ] `environment.txt` zawiera informacje o środowisku,
- [ ] `numbers.txt` zawiera dokładnie liczby od 1 do 100,
- [ ] `ending5.txt` zawiera dokładnie 10 liczb kończących się cyfrą 5,
- [ ] `commands.md` opisuje użyte polecenia,
- [ ] `analyze.sh` uruchamia się bez błędu,
- [ ] `summary.txt` zawiera `count=100`,
- [ ] `summary.txt` zawiera `sum=5050`,
- [ ] `summary.txt` zawiera `min=1`,
- [ ] `summary.txt` zawiera `max=100`,
- [ ] `summary.txt` zawiera `average=50.5`,
- [ ] `vscode.md` zawiera cztery wymagane sekcje,
- [ ] `agent_prompt.md` zawiera faktycznie użyty prompt,
- [ ] `agent_review.md` opisuje sprawdzenie zmiany,
- [ ] `README.md` zawiera linki i końcową checklistę.
