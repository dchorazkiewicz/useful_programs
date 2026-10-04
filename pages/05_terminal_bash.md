# 2. Terminal, WSL, VS Code i środowiska chmurowe

W tym bloku przechodzimy od pracy wyłącznie w przeglądarce do pracy z **prawdziwym środowiskiem roboczym**.

Poznamy:

| Narzędzie | Do czego służy? |
| --- | --- |
| **terminal** | tekstowy sposób wydawania poleceń komputerowi |
| **Bash** | popularna powłoka używana w systemach Linux |
| **WSL** | Linux uruchomiony wewnątrz Windows |
| **Visual Studio Code (VS Code)** | edytor kodu i plików projektu, który integruje się z terminaliem |

---

# Terminal

## Co to jest terminal?

**Terminal** to interfejs tekstowy, przez który wydajemy komputerowi polecenia.

Zamiast kliknąć folder i wybrać „Nowy plik”, możemy napisać:

~~~bash
mkdir wyniki
touch wyniki/raport.txt
~~~

Efekt to powstanie katalogu `wyniki` i pustego pliku `raport.txt` w tym katalogu.

~~~text
wyniki/
└── raport.txt
~~~

Terminal nie jest osobnym systemem operacyjnym. Jest sposobem komunikowania się z systemem.

---

## Terminal, shell i Bash

Te trzy pojęcia warto rozróżniać.

**Terminal** to okno lub aplikacja, w której wpisujemy polecenia.

**Shell**, czyli powłoka, to program, który interpretuje wpisane polecenia (np. `ls`, `cd`, `mkdir`) i uruchamia odpowiednie programy.

**Bash** jest jednym z najpopularniejszych shelli używanych w Linuxie (Bourne Again SHell, który umożliwia m.in. wykonywanie skryptów, czyli plików z polecaniami).

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

---

# Linuks i Windows

Na Windows możemy spotkać m.in. PowerShell i Command Prompt (cmd). Możesz je wywołać przez menu Start, wpisując `powershell` albo `cmd`.

W Linuxie klikamy zwykle w ikonę terminala lub używamy skrótu `Ctrl + Alt + T`.

Będąc pod Windows możesz korzystać z terminala Linux dzięki **WSL** (Windows Subsystem for Linux) albo w środowisku chmurowym **GitHub Codespaces**. Pierwsze rozwiązanie poprostu instaluje Linuxa w Windows, a drugie uruchamia Linuxa w ramach Visual Studio w chmurze przez przeglądarkę.

MacOS ma wbudowany terminal i powłokę Bash. Warto jednak pamiętać, że MacOS nie jest Linuxem, a jedynie systemem uniksopodobnym.

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


## Change directory i kilka ważnych skrótów

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

## Nano, Kate - proste terminalowe edytory tekstu

`Nano` i `Kate` to proste edytory tekstu, które pomagają szybko modyfikować pliki konfiguracyjne, skrypty i krótkie notatki bez potrzeby uruchamiania pełnego środowiska graficznego. Są bardzo przydatne w pracy z terminalem, gdy chcemy od razu poprawić tekst lub dodać kilka linijek do pliku.

Najprostszy przykład to otwarcie pliku w `nano`:

~~~bash
nano config.txt
~~~

Po wpisaniu treści zapisujemy zmiany klawiszem `Ctrl + O`, a wychodzimy `Ctrl + X`. W praktyce oznacza to, że `nano` jest świetny do szybkich poprawek w plikach tekstowych. `Kate` działa podobnie, ale oferuje dodatkowe funkcje, takie jak podświetlanie składni, numerowanie linii i wygodniejszy interfejs graficzny:

~~~bash
kate hello.txt
~~~




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

## Mały przykład pracy w plikami

Utworzenie 10 plików `plik1.txt`, `plik2.txt`, …, `plik10.txt`:

~~~bash
for i in $(seq 1 10); do
    touch plik$i.txt
done
~~~

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