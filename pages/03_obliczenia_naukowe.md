# 3. Obliczenia naukowe

Komputer może pomagać w obliczeniach na kilka różnych sposobów. Czasem chcemy szybko sprawdzić wynik. Czasem potrzebujemy policzyć tysiące wartości. Innym razem zależy nam na **dokładnym wzorze**, a nie tylko liczbie.

W tym bloku poznamy kilka narzędzi i nauczymy się dobierać je do problemu.

| Narzędzie | Najlepiej nadaje się do |
| --- | --- |
| **Wolfram Alpha** | szybkiego sprawdzania obliczeń i własności obiektów matematycznych |
| **Wolfram Cloud** | pracy z Wolfram Language w notebooku |
| **Python** | uniwersalnych obliczeń, automatyzacji i analizy danych |
| **NumPy** | szybkich obliczeń numerycznych na wektorach i macierzach |
| **SymPy** | obliczeń symbolicznych |
| **Octave** | obliczeń numerycznych w stylu MATLAB-a |
| **Matplotlib** | tworzenia wykresów w Pythonie |
| **OEIS** | rozpoznawania ciągów liczbowych |
| **Gnuplot** | szybkiego rysowania danych i dopasowywania funkcji |

---

# Obliczenia numeryczne i symboliczne

## Dwa różne pytania

Rozważmy całkę:

$$
I=\int_0^1 x^2\,dx
$$

Możemy zapytać o **wartość numeryczną**:

$$
I \approx 0.3333333333
$$

albo o **wynik dokładny**:

$$
I=\frac{1}{3}
$$

To nie jest dokładnie ten sam rodzaj odpowiedzi.

### Obliczenia numeryczne

W obliczeniach numerycznych operujemy głównie na liczbach i przybliżeniach.

Przykład w Pythonie:

~~~python
print(1 / 3)
~~~

Efekt:

~~~text
0.3333333333333333
~~~

### Obliczenia symboliczne

W obliczeniach symbolicznych program operuje na wzorach.

Przykład w SymPy:

~~~python
from sympy import Rational

x = Rational(1, 3)
print(x)
~~~

Efekt:

~~~text
1/3
~~~

Oba podejścia są potrzebne.

Numeryka jest szczególnie przydatna dla dużych zbiorów danych, symulacji i problemów, dla których nie znamy prostego wzoru dokładnego.

Obliczenia symboliczne są wygodne przy algebraicznym przekształcaniu wzorów, pochodnych, całkach i równaniach.

---

# Wolfram Alpha

## Co to jest Wolfram Alpha?

**Wolfram Alpha** jest systemem obliczeniowym, do którego można wpisywać pytania i wyrażenia matematyczne w dość naturalnej formie.

Nie jest zwykłą wyszukiwarką. Zamiast szukać strony zawierającej odpowiedź, często **oblicza odpowiedź** na podstawie dostarczonego wyrażenia.

Przykładowe zapytanie:

~~~text
factor x^3 - 6x^2 + 11x - 6
~~~

otrzymuje rozkład:

$$
x^3-6x^2+11x-6=(x-1)(x-2)(x-3)
$$

Możemy więc od razu odczytać pierwiastki:

$$
x=1,\qquad x=2,\qquad x=3
$$

---

## Równania

Zapytanie:

~~~text
solve x^2 - 5x + 6 = 0
~~~

daje rozwiązania:

$$
x=2,\qquad x=3
$$

---

## Pochodne

Zapytanie:

~~~text
derivative x^3 - 6x^2 + 11x - 6
~~~

daje:

$$
3x^2-12x+11
$$

---

## Całki

Zapytanie:

~~~text
integrate x^2 from 0 to 1
~~~

prowadzi do:

$$
\int_0^1 x^2\,dx=\frac{1}{3}
$$

---

## Jednostki

Wolfram Alpha jest bardzo wygodny przy przeliczaniu jednostek.

Zapytanie:

~~~text
72 km/h to m/s
~~~

daje:

$$
72\,\mathrm{km/h}=20\,\mathrm{m/s}
$$

Przy obliczeniach fizycznych sprawdzanie jednostek jest często równie ważne jak sprawdzanie samej liczby.

---

## Wolfram Alpha jako narzędzie kontrolne

Wolfram Alpha jest szczególnie użyteczny do:

- szybkiego sprawdzenia rachunków,
- rozwiązania równania,
- sprawdzenia pochodnej lub całki,
- narysowania funkcji,
- konwersji jednostek,
- sprawdzenia własności funkcji.

Nie warto jednak traktować wyniku jako „magicznej prawdy”. Trzeba wiedzieć, **jakie pytanie zostało zadane** i czy program poprawnie je zinterpretował.

---

## Wolfram Cloud

**Wolfram Cloud** pozwala pracować z Wolfram Language w notebookach dostępnych przez przeglądarkę.

Przykład kodu:

~~~text
Factor[x^3 - 6 x^2 + 11 x - 6]
~~~

wynik:

~~~text
(-3 + x) (-2 + x) (-1 + x)
~~~

Ten sam problem możemy więc rozwiązać:

- wpisując zapytanie do Wolfram Alpha,
- pisząc kod w Wolfram Language,
- używając SymPy,
- rozwiązując go ręcznie.

To dobry przykład, że **narzędzia mogą być różne, ale problem matematyczny pozostaje ten sam**.

---

## Dobre materiały

- [Wolfram Alpha — przykłady](https://www.wolframalpha.com/examples/)
- [Wolfram Alpha — przykłady matematyczne](https://www.wolframalpha.com/examples/mathematics)
- [Wolfram Cloud](https://www.wolframcloud.com/)

---

# Python jako kalkulator naukowy

Python jest językiem programowania ogólnego przeznaczenia, ale bardzo dobrze nadaje się również do obliczeń.

## Zmienne

~~~python
a = 12
b = 5

c = a + b
print(c)
~~~

Efekt:

~~~text
17
~~~

Zmienna pozwala nadać nazwę wartości.

---

## Podstawowe operacje

~~~python
a = 7
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a**b)
~~~

Efekt:

~~~text
10
4
21
2.3333333333333335
343
~~~

Operator `**` oznacza potęgowanie.

---

## Typy liczb

~~~python
a = 5
b = 2.5
c = 3 + 4j

print(type(a))
print(type(b))
print(type(c))
~~~

Efekt:

~~~text
<class 'int'>
<class 'float'>
<class 'complex'>
~~~

Najczęściej spotkamy:

- `int` — liczby całkowite,
- `float` — liczby zmiennoprzecinkowe,
- `complex` — liczby zespolone.

---

## Funkcje matematyczne

Moduł `math` zawiera podstawowe funkcje matematyczne.

~~~python
import math

print(math.sqrt(2))
print(math.sin(math.pi / 2))
print(math.exp(1))
~~~

Przykładowy wynik:

~~~text
1.4142135623730951
1.0
2.718281828459045
~~~

---

## Własna funkcja

Zamiast wielokrotnie przepisywać ten sam wzór, możemy zdefiniować funkcję.

~~~python
def energia(m, v):
    return 0.5 * m * v**2

print(energia(2, 3))
~~~

Efekt:

~~~text
9.0
~~~

Funkcje są podstawowym sposobem organizowania kodu obliczeniowego.

---

# NumPy

## Dlaczego nie wystarczy zwykła lista?

Python ma listy:

~~~python
x = [1, 2, 3, 4]
~~~

ale w obliczeniach naukowych często chcemy wykonywać tę samą operację na tysiącach lub milionach elementów.

Do tego służy biblioteka **NumPy**.

~~~python
import numpy as np

x = np.array([1, 2, 3, 4])
print(x)
~~~

Efekt:

~~~text
[1 2 3 4]
~~~

---

## Operacje na całym wektorze

~~~python
import numpy as np

x = np.array([1, 2, 3, 4])

print(x**2)
~~~

Efekt:

~~~text
[ 1  4  9 16]
~~~

Nie musieliśmy pisać pętli po każdym elemencie.

---

## Generowanie siatki punktów

~~~python
import numpy as np

x = np.linspace(0, 1, 6)

print(x)
~~~

Efekt:

~~~text
[0.  0.2 0.4 0.6 0.8 1. ]
~~~

`linspace` tworzy równomiernie rozmieszczone punkty.

To bardzo wygodne przy wykresach i obliczeniach numerycznych.

---

## Podstawowe statystyki

~~~python
import numpy as np

data = np.array([2, 4, 6, 8, 10])

print(np.mean(data))
print(np.std(data))
print(np.min(data))
print(np.max(data))
~~~

Efekt:

~~~text
6.0
2.8284271247461903
2
10
~~~

---

# Wektory i macierze

## Macierz w NumPy

~~~python
import numpy as np

A = np.array([
    [2, 1],
    [1, 3]
])

print(A)
~~~

Efekt:

~~~text
[[2 1]
 [1 3]]
~~~

---

## Mnożenie macierzy

Operator `@` oznacza mnożenie macierzowe.

~~~python
import numpy as np

A = np.array([
    [2, 1],
    [1, 3]
])

v = np.array([1, 2])

print(A @ v)
~~~

Efekt:

~~~text
[4 7]
~~~

---

## Rozwiązywanie układu liniowego

Rozważmy układ:

$$
\begin{cases}
2x+y=5, \\
x+3y=5.
\end{cases}
$$

W zapisie macierzowym:

$$
A v=b
$$

gdzie:

$$
A=
\begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
5 \\
5 \\
\end{pmatrix}
$$

NumPy:

~~~python
import numpy as np

A = np.array([
    [2, 1],
    [1, 3]
], dtype=float)

b = np.array([5, 5], dtype=float)

v = np.linalg.solve(A, b)

print(v)
~~~

Efekt:

~~~text
[2. 1.]
~~~

czyli:

$$
x=2,\qquad y=1
$$

---

# SymPy

## Co robi SymPy?

**SymPy** jest biblioteką Pythona do obliczeń symbolicznych.

Zamiast tylko przybliżać wynik liczbowo, potrafi operować na symbolach takich jak $x$, $y$ czy $n$.

---

## Symbol

~~~python
from sympy import symbols

x = symbols("x")

print(x)
~~~

Efekt:

~~~text
x
~~~

Od tej chwili Python może traktować `x` jako symbol matematyczny.

---

## Rozwijanie i faktoryzacja

~~~python
from sympy import symbols, expand, factor

x = symbols("x")

expr = (x - 1) * (x - 2) * (x - 3)

print(expand(expr))
print(factor(x**3 - 6*x**2 + 11*x - 6))
~~~

Efekt:

~~~text
x**3 - 6*x**2 + 11*x - 6
(x - 3)*(x - 2)*(x - 1)
~~~

---

## Równania

~~~python
from sympy import symbols, solve

x = symbols("x")

solutions = solve(x**2 - 5*x + 6, x)

print(solutions)
~~~

Efekt:

~~~text
[2, 3]
~~~

---

## Pochodne

~~~python
from sympy import symbols, diff

x = symbols("x")

f = x**3 - 6*x**2 + 11*x - 6

print(diff(f, x))
~~~

Efekt:

~~~text
3*x**2 - 12*x + 11
~~~

---

## Całki

~~~python
from sympy import symbols, integrate

x = symbols("x")

print(integrate(x**2, (x, 0, 1)))
~~~

Efekt:

~~~text
1/3
~~~

Tu dobrze widać różnicę między obliczeniem symbolicznym a numerycznym: SymPy zwrócił dokładnie `1/3`.

---

## Zamiana wyniku dokładnego na przybliżenie

~~~python
from sympy import Rational

x = Rational(1, 3)

print(x)
print(x.evalf())
~~~

Efekt:

~~~text
1/3
0.333333333333333
~~~

---

## Dobre materiały

- [Python — oficjalny tutorial](https://docs.python.org/3/tutorial/)
- [Python — moduł math](https://docs.python.org/3/library/math.html)
- [NumPy — quickstart](https://numpy.org/doc/stable/user/quickstart.html)
- [SymPy — tutorial](https://docs.sympy.org/latest/tutorials/intro-tutorial/index.html)

---

# CSV — prosty format danych

## Co to jest CSV?

**CSV** oznacza *Comma-Separated Values*.

To prosty tekstowy format tabelaryczny.

Przykład:

~~~csv
x,y
0,1.1
1,2.9
2,5.2
3,7.1
4,8.9
5,11.2
~~~

Pierwsza linia zawiera nazwy kolumn.

Każda następna linia zawiera jeden rekord.

CSV jest bardzo popularny, ponieważ można go otworzyć w:

- Excelu,
- LibreOffice,
- Pythonie,
- Octave,
- R,
- Gnuplocie,
- wielu narzędziach laboratoryjnych.

---

## Wczytanie CSV w NumPy

Dla pliku `measurements.csv`:

~~~csv
x,y
0,1.1
1,2.9
2,5.2
3,7.1
4,8.9
5,11.2
~~~

możemy użyć:

~~~python
import numpy as np

data = np.loadtxt(
    "measurements.csv",
    delimiter=",",
    skiprows=1
)

print(data)
~~~

Efekt:

~~~text
[[ 0.   1.1]
 [ 1.   2.9]
 [ 2.   5.2]
 [ 3.   7.1]
 [ 4.   8.9]
 [ 5.  11.2]]
~~~

Kolumny wybieramy:

~~~python
x = data[:, 0]
y = data[:, 1]
~~~

---

# Dopasowanie prostej

Mamy dane pomiarowe i chcemy dopasować model:

$$
y=ax+b
$$

NumPy:

~~~python
a, b = np.polyfit(x, y, 1)

print(a)
print(b)
~~~

Otrzymamy w przybliżeniu:

~~~text
2.011428571428571
1.038095238095238
~~~

czyli:

$$
y \approx 2.01143x+1.03810
$$

To przykład obliczenia numerycznego: parametry nie są „ładnymi” liczbami całkowitymi, ale opisują dane najlepiej w sensie dopasowania liniowego.

---

# Wykres w Matplotlib

~~~python
import matplotlib.pyplot as plt

plt.scatter(x, y, label="dane")

x_fit = np.linspace(0, 5, 100)
y_fit = a * x_fit + b

plt.plot(x_fit, y_fit, label="dopasowanie")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.savefig("fit.png", dpi=150, bbox_inches="tight")
plt.show()
~~~

Powstanie plik:

~~~text
fit.png
~~~

W raporcie Markdown można go osadzić:

~~~markdown
![Dane i dopasowana prosta](fit.png)
~~~

Dobre źródło:

- [Matplotlib — tutoriale](https://matplotlib.org/stable/tutorials/index.html)

---

# Octave

## Co to jest Octave?

**GNU Octave** jest środowiskiem do obliczeń numerycznych, szczególnie wygodnym dla pracy z wektorami i macierzami.

Składnia jest w dużej mierze zgodna z podejściem używanym w MATLAB-ie.

To oznacza, że wiele podstawowych skryptów można przenosić między tymi środowiskami z niewielkimi zmianami.

---

## Wektor

~~~octave
v = [1; 2; 3]
~~~

Efekt:

~~~text
v =

   1
   2
   3
~~~

---

## Macierz

~~~octave
A = [2 1; 1 3]
~~~

Efekt:

~~~text
A =

   2   1
   1   3
~~~

---

## Układ równań

Dla:

$$
A=
\begin{pmatrix}
2 & 1 \\
1 & 3 \\
\end{pmatrix},
\qquad
b=
\begin{pmatrix}
5 \\
5 \\
\end{pmatrix}
$$

w Octave możemy napisać:

~~~octave
A = [2 1; 1 3];
b = [5; 5];

v = A \ b;

disp(v)
~~~

Efekt:

~~~text
   2
   1
~~~

Operator odwrotnego ukośnika jest jednym z najbardziej charakterystycznych sposobów rozwiązywania układów liniowych w MATLAB-ie i Octave.

---

## Skrypt Octave

Kod możemy zapisać w pliku:

~~~text
solve_system.m
~~~

i uruchomić:

~~~bash
octave solve_system.m
~~~

Dobre źródło:

- [GNU Octave — dokumentacja](https://docs.octave.org/latest/)

---

# OEIS

## Co to jest OEIS?

**OEIS — Online Encyclopedia of Integer Sequences** to baza ciągów liczb całkowitych.

Jeżeli w obliczeniach otrzymamy ciąg:

~~~text
1, 1, 2, 3, 5, 8, 13, 21
~~~

możemy go wyszukać w OEIS.

To oczywiście ciąg Fibonacciego.

OEIS może podać:

- identyfikator ciągu,
- kolejne wyrazy,
- wzory,
- rekurencje,
- odniesienia do literatury,
- powiązane ciągi.

---

## Inny przykład

Ciąg:

~~~text
1, 2, 6, 24, 120, 720
~~~

to wartości:

$$
n!
$$

dla kolejnych $n$.

W OEIS jest to ciąg **A000142**.

Kolejne wyrazy:

~~~text
5040
40320
362880
~~~

OEIS jest szczególnie przydatny w badaniach eksperymentalnych i matematyce dyskretnej, gdy z obliczeń wyłania się ciąg, którego jeszcze nie rozpoznajemy.

Źródło:

- [OEIS](https://oeis.org/)

---

# Gnuplot

## Po co jeszcze jedno narzędzie do wykresów?

Gnuplot jest lekkim programem nastawionym na szybkie rysowanie danych i funkcji.

Może działać bez notebooka i bez rozbudowanego programu w Pythonie.

Przykład pliku `plot.gp`:

~~~gnuplot
set datafile separator ","
set key left top
set grid

plot "measurements.csv" using 1:2 every ::1 with points title "dane"
~~~

Gnuplot może również dopasowywać funkcje.

Przykład:

~~~gnuplot
set datafile separator ","

f(x) = a*x + b
a = 1
b = 0

fit f(x) "measurements.csv" using 1:2 every ::1 via a,b

plot "measurements.csv" using 1:2 every ::1 with points title "dane", \
     f(x) with lines title "fit"
~~~

Dla naszych danych parametry powinny być bliskie:

~~~text
a = 2.01143
b = 1.03810
~~~

Gnuplot jest dobrym przykładem narzędzia, które robi jedną rzecz i robi ją bardzo sprawnie.

Źródło:

- [Gnuplot — dokumentacja](http://www.gnuplot.info/documentation.html)

---

# Jak dobrać narzędzie?

Nie istnieje jedno narzędzie najlepsze do wszystkiego.

| Problem | Sensowny pierwszy wybór |
| --- | --- |
| szybkie sprawdzenie całki | Wolfram Alpha |
| dokładna pochodna w kodzie Python | SymPy |
| milion wartości funkcji | NumPy |
| macierze i obliczenia w stylu MATLAB | Octave |
| analiza danych z CSV | Python + NumPy |
| wykres w raporcie | Matplotlib |
| szybki wykres z terminala | Gnuplot |
| rozpoznanie ciągu całkowitego | OEIS |

Dobry użytkownik narzędzi obliczeniowych nie pyta tylko:

> Jakiego programu mam użyć?

ale najpierw:

> Czy potrzebuję wyniku dokładnego, przybliżenia numerycznego, wykresu, analizy danych czy rozpoznania struktury?

---

# Zadania dla studenta

Wszystkie rozwiązania umieść w folderze:

~~~text
zadania/03_obliczenia_naukowe/
~~~

Po wykonaniu zadań folder powinien zawierać:

~~~text
zadania/03_obliczenia_naukowe/
├── README.md
├── wolfram.md
├── python_calc.py
├── python_results.txt
├── symbolic.py
├── symbolic_results.txt
├── measurements.csv
├── analyze_data.py
├── fit_results.txt
├── fit.png
├── solve_system.m
├── octave_results.txt
└── oeis.md
~~~

Nie zmieniaj nazw wymaganych plików.

---

## Zadanie 1. Wolfram Alpha jako niezależna kontrola

Utwórz plik `wolfram.md`.

Sprawdź w Wolfram Alpha cztery problemy:

~~~text
factor x^3 - 6x^2 + 11x - 6
solve x^2 - 5x + 6 = 0
integrate x^2 from 0 to 1
72 km/h to m/s
~~~

Plik ma mieć strukturę:

~~~markdown
# Wolfram Alpha

## Faktoryzacja

Zapytanie:

...

Wynik:

...

## Równanie

Zapytanie:

...

Wynik:

...

## Całka

Zapytanie:

...

Wynik:

...

## Jednostki

Zapytanie:

...

Wynik:

...

## Komentarz

...
~~~

Oczekiwane najważniejsze wartości:

- pierwiastki wielomianu: `1, 2, 3`,
- rozwiązania równania: `2, 3`,
- całka: `1/3`,
- przeliczenie: `20 m/s`.

W sekcji **Komentarz** napisz 2–4 zdania: do czego Wolfram Alpha jest wygodny, a czego nie powinno się przyjmować bez sprawdzenia.

---

## Zadanie 2. Python jako kalkulator

Utwórz `python_calc.py`.

Program ma policzyć dla:

~~~python
g = 9.81
h = 20.0
~~~

czas swobodnego spadku z wysokości $h$:

$$
t=\sqrt{\frac{2h}{g}}
$$

oraz prędkość końcową:

$$
v=gt
$$

Program ma zapisać do `python_results.txt`:

~~~text
g=9.81
h=20.0
t=...
v=...
~~~

Wartości `t` i `v` zapisz z dokładnością do czterech miejsc po przecinku.

Dla kontroli powinieneś otrzymać w przybliżeniu:

~~~text
t=2.0193
v=19.8091
~~~

### Sprawdzenie

Będzie można uruchomić `python_calc.py` i porównać wynik numeryczny z oczekiwaną wartością z odpowiednią tolerancją.

---

## Zadanie 3. SymPy — wynik dokładny

Utwórz `symbolic.py`.

Dla wielomianu:

$$
p(x)=x^3-6x^2+11x-6
$$

program ma:

1. wykonać faktoryzację,
2. znaleźć pierwiastki,
3. policzyć pochodną,
4. policzyć całkę $\int_0^1 x^2\,dx$.

Zapisz wyniki do `symbolic_results.txt` w formie:

~~~text
factor=...
roots=...
derivative=...
integral=...
~~~

Plik powinien zawierać informacje równoważne:

~~~text
factor=(x - 3)*(x - 2)*(x - 1)
roots=[1, 2, 3]
derivative=3*x**2 - 12*x + 11
integral=1/3
~~~

Kolejność pierwiastków lub czynników może się różnić.

### Sprawdzenie

Automat może uruchomić skrypt i sprawdzić, czy wyniki są matematycznie równoważne oczekiwanym.

---

## Zadanie 4. CSV, NumPy i dopasowanie danych

Utwórz dokładnie taki plik `measurements.csv`:

~~~csv
x,y
0,1.1
1,2.9
2,5.2
3,7.1
4,8.9
5,11.2
~~~

Następnie utwórz `analyze_data.py`.

Program ma:

1. wczytać `measurements.csv`,
2. rozdzielić kolumny `x` i `y`,
3. dopasować model liniowy $y=ax+b$ za pomocą `np.polyfit`,
4. zapisać parametry do `fit_results.txt`,
5. narysować dane i dopasowaną prostą,
6. zapisać wykres jako `fit.png`.

`fit_results.txt` ma mieć format:

~~~text
a=2.01143
b=1.03810
~~~

Dopuszczalne są drobne różnice ostatnich cyfr wynikające z zaokrąglenia.

### Sprawdzenie

Będzie można:

- sprawdzić dokładną zawartość CSV,
- uruchomić `analyze_data.py`,
- odczytać parametry dopasowania,
- sprawdzić istnienie i rozmiar `fit.png`.

---

## Zadanie 5. Ten sam układ równań w Octave

Utwórz `solve_system.m` rozwiązujący układ:

$$
\begin{cases}
2x+y=5, \\
x+3y=5.
\end{cases}
$$

Skrypt ma również zapisać wynik do `octave_results.txt` w formie:

~~~text
x=2.000000
y=1.000000
~~~

Możesz wykorzystać:

~~~octave
A = [2 1; 1 3];
b = [5; 5];

v = A \ b;

fid = fopen("octave_results.txt", "w");
fprintf(fid, "x=%.6f\n", v(1));
fprintf(fid, "y=%.6f\n", v(2));
fclose(fid);
~~~

Uruchomienie z terminala:

~~~bash
octave solve_system.m
~~~

### Sprawdzenie

Jeżeli Octave jest dostępny w środowisku sprawdzającym, skrypt można uruchomić ponownie. Niezależnie od tego można sprawdzić zawartość `octave_results.txt`.

---

## Zadanie 6. OEIS — rozpoznaj ciąg

Wyszukaj w OEIS ciąg:

~~~text
1, 2, 6, 24, 120, 720
~~~

Utwórz `oeis.md` ze strukturą:

~~~markdown
# OEIS

## Wyszukiwany ciąg

...

## Numer OEIS

...

## Interpretacja

...

## Trzy kolejne wyrazy

...
~~~

W pliku powinien pojawić się identyfikator:

~~~text
A000142
~~~

oraz trzy kolejne wartości:

~~~text
5040
40320
362880
~~~

W sekcji **Interpretacja** napisz własnymi słowami, jaki znany obiekt matematyczny opisuje ten ciąg.

---

## Zadanie 7. README bloku

Utwórz `README.md`.

Powinien zawierać:

- krótkie wyjaśnienie różnicy między obliczeniami numerycznymi i symbolicznymi,
- tabelę wszystkich użytych narzędzi,
- linki do `wolfram.md` i `oeis.md`,
- wynik obliczenia spadku swobodnego,
- dokładny wynik całki z SymPy,
- parametry dopasowania `a` i `b`,
- wynik układu liniowego z Octave,
- osadzony obraz `fit.png`,
- checklistę wszystkich zadań.

Dodaj tabelę:

~~~markdown
| Problem | Narzędzie | Typ wyniku |
| --- | --- | --- |
| szybkie sprawdzenie | Wolfram Alpha | wynik obliczeniowy |
| spadek swobodny | Python | numeryczny |
| całka | SymPy | symboliczny |
| dopasowanie danych | NumPy | numeryczny |
| układ równań | Octave | numeryczny |
| rozpoznanie ciągu | OEIS | identyfikacja |
~~~

---

# Zadanie dodatkowe. Gnuplot

To zadanie jest opcjonalne.

Jeżeli masz dostęp do Gnuplota, wykorzystaj `measurements.csv` i przygotuj skrypt `fit.gp`, który:

1. dopasuje prostą $y=ax+b$,
2. narysuje dane,
3. narysuje dopasowaną prostą,
4. zapisze wykres do `gnuplot_fit.png`.

Parametry powinny być bliskie:

~~~text
a=2.01143
b=1.03810
~~~

Celem zadania nie jest zastąpienie Pythona Gnuplotem. Chodzi o zobaczenie, że te same dane można analizować różnymi narzędziami.

---

# Checklista końcowa

Przed zgłoszeniem bloku sprawdź:

- [ ] `wolfram.md` zawiera cztery wymagane obliczenia,
- [ ] `python_calc.py` uruchamia się bez błędu,
- [ ] `python_results.txt` zawiera `t` i `v`,
- [ ] `symbolic.py` uruchamia się bez błędu,
- [ ] `symbolic_results.txt` zawiera dokładną całkę `1/3`,
- [ ] `measurements.csv` ma poprawną zawartość,
- [ ] `analyze_data.py` odczytuje dane z CSV,
- [ ] `fit_results.txt` zawiera parametry bliskie `2.01143` i `1.03810`,
- [ ] `fit.png` otwiera się poprawnie,
- [ ] `solve_system.m` zawiera rozwiązanie macierzowe,
- [ ] `octave_results.txt` zawiera `x=2` i `y=1`,
- [ ] `oeis.md` zawiera `A000142`,
- [ ] `README.md` zawiera osadzony wykres i podsumowanie wyników.
