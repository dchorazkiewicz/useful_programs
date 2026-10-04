

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
