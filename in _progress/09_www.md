# 4. Interaktywne materiały i publikacja w sieci

W poprzednim bloku potrafiliśmy już policzyć wynik, zapisać dane do pliku i przygotować wykres.

Teraz zrobimy kolejny krok:

~~~text
obliczenie
   ↓
wynik
   ↓
wykres / animacja
   ↓
interaktywny HTML
   ↓
strona projektu
   ↓
publikacja w sieci
~~~

W tym bloku poznamy:

| Narzędzie | Zastosowanie |
| --- | --- |
| **HTML** | budowa strony internetowej |
| **CSS** | wygląd strony |
| **JavaScript** | zachowanie i interakcja |
| **Matplotlib** | animacje i grafika z Pythona |
| **Plotly** | interaktywne wykresy |
| **GitHub Pages** | publikacja statycznej strony |
| **MkDocs** | tworzenie stron dokumentacji z plików Markdown |

---

# Od pliku do strony WWW

## Co właściwie otwiera przeglądarka?

Przeglądarka potrafi wyświetlić plik HTML.

Najprostszy przykład:

~~~html
<!doctype html>
<html lang="pl">
<head>
    <meta charset="utf-8">
    <title>Moja pierwsza strona</title>
</head>
<body>
    <h1>Wyniki obliczeń</h1>

    <p>To jest moja pierwsza strona HTML.</p>
</body>
</html>
~~~

Jeżeli zapiszemy ten tekst jako:

~~~text
index.html
~~~

i otworzymy plik w przeglądarce, zobaczymy stronę z nagłówkiem i akapitem.

HTML nie jest językiem do wykonywania obliczeń takich jak Python. Jest przede wszystkim językiem opisującym **strukturę dokumentu internetowego**.

---

# HTML

## Elementy HTML

Większość elementów HTML ma znacznik otwierający i zamykający.

Przykład:

~~~html
<p>To jest akapit.</p>
~~~

Tutaj:

- `<p>` — otwiera akapit,
- `</p>` — zamyka akapit,
- tekst pomiędzy nimi jest zawartością.

---

## Nagłówki

~~~html
<h1>Tytuł strony</h1>
<h2>Wyniki</h2>
<h3>Eksperyment 1</h3>
~~~

Efekt odpowiada mniej więcej hierarchii:

# Tytuł strony

## Wyniki

### Eksperyment 1

W HTML dostępne są poziomy od `h1` do `h6`.

---

## Akapit

~~~html
<p>
    Badanie dotyczy zależności y od x.
</p>
~~~

Element `p` oznacza akapit.

---

## Lista

~~~html
<ul>
    <li>Python</li>
    <li>NumPy</li>
    <li>Plotly</li>
</ul>
~~~

`ul` oznacza listę nieuporządkowaną, a `li` pojedynczy element listy.

Lista numerowana używa `ol`:

~~~html
<ol>
    <li>Wczytaj dane</li>
    <li>Wykonaj obliczenia</li>
    <li>Narysuj wykres</li>
</ol>
~~~

---

## Link

~~~html
<a href="https://github.com/">GitHub</a>
~~~

Element `a` tworzy link.

Atrybut `href` zawiera adres docelowy.

---

## Obraz

~~~html
<img src="wykres.png" alt="Wykres wyników">
~~~

Atrybuty:

- `src` — wskazuje plik obrazu,
- `alt` — opisuje obraz.

Opis alternatywny jest ważny także wtedy, gdy obraz z jakiegoś powodu nie może się załadować.

---

## Tabela

~~~html
<table>
    <tr>
        <th>x</th>
        <th>y</th>
    </tr>
    <tr>
        <td>1</td>
        <td>1</td>
    </tr>
    <tr>
        <td>2</td>
        <td>4</td>
    </tr>
</table>
~~~

Najważniejsze znaczniki:

- `table` — tabela,
- `tr` — wiersz,
- `th` — komórka nagłówkowa,
- `td` — zwykła komórka.

---

# CSS — wygląd strony

HTML opisuje strukturę. **CSS** opisuje wygląd.

Przykład:

~~~html
<style>
body {
    font-family: sans-serif;
    max-width: 900px;
    margin: 40px auto;
    line-height: 1.6;
}

h1 {
    border-bottom: 1px solid #ccc;
}
</style>
~~~

Po dodaniu takiego fragmentu do sekcji `head` strona będzie miała czytelniejszy układ.

W tym kursie nie będziemy uczyć się projektowania stron WWW jako osobnej specjalności. Wystarczy rozumieć, że:

~~~text
HTML       → struktura
CSS        → wygląd
JavaScript → zachowanie
~~~

---

# JavaScript — prosta interakcja

HTML sam w sobie opisuje dokument. Jeśli strona ma reagować na użytkownika, często potrzebny jest JavaScript.

Przykład:

~~~html
<p id="wynik">0</p>

<button onclick="zwieksz()">Kliknij</button>

<script>
let licznik = 0;

function zwieksz() {
    licznik = licznik + 1;
    document.getElementById("wynik").textContent = licznik;
}
</script>
~~~

Po kliknięciu przycisku liczba na stronie zwiększa się o 1.

Mamy tu trzy elementy:

1. akapit z identyfikatorem `wynik`,
2. przycisk,
3. funkcję JavaScript zmieniającą zawartość akapitu.

Nie trzeba teraz szczegółowo poznawać JavaScriptu. Ważne jest zrozumienie, skąd bierze się interaktywność strony.

---

# Prosty kalkulator w HTML

Możemy połączyć formularz i JavaScript.

~~~html
<label>
    x:
    <input id="x" type="number" value="2">
</label>

<button onclick="policz()">Policz x²</button>

<p id="wynik"></p>

<script>
function policz() {
    const x = Number(document.getElementById("x").value);
    const y = x * x;

    document.getElementById("wynik").textContent =
        "Wynik: " + y;
}
</script>
~~~

Dla:

~~~text
x = 5
~~~

po kliknięciu otrzymamy:

~~~text
Wynik: 25
~~~

To już jest bardzo mała aplikacja działająca całkowicie w przeglądarce.

---

# Strona statyczna

Strona zbudowana z plików takich jak:

~~~text
index.html
style.css
wykres.png
script.js
~~~

może działać bez serwera wykonującego Python czy PHP.

Taki zestaw plików nazywamy tutaj **stroną statyczną**.

„Statyczna” nie oznacza, że strona nie może być interaktywna. JavaScript może wykonywać się w przeglądarce.

Oznacza raczej, że serwer nie musi przy każdym wejściu użytkownika wykonywać kodu generującego stronę.

GitHub Pages jest właśnie usługą do publikacji takich stron.

---

# Animacje w Colabie i Pythonie

## Po co animacja?

Niektóre wyniki są trudne do pokazania pojedynczym wykresem.

Przykłady:

- ruch punktu,
- oscylacja,
- ewolucja układu w czasie,
- propagacja fali,
- zmieniający się rozkład danych.

Możemy wtedy przygotować serię klatek i zapisać ją jako GIF.

---

## Prosta animacja

Pokażmy punkt poruszający się po wykresie funkcji:

$$
y=\sin x
$$

Kod:

~~~python
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.animation import FuncAnimation, PillowWriter

x = np.linspace(0, 2*np.pi, 200)
y = np.sin(x)

fig, ax = plt.subplots()

ax.plot(x, y)
point, = ax.plot([], [], "o")

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1.2, 1.2)
ax.set_xlabel("x")
ax.set_ylabel("sin(x)")
ax.grid()

def update(frame):
    point.set_data([x[frame]], [y[frame]])
    return point,

animation = FuncAnimation(
    fig,
    update,
    frames=range(0, len(x), 4),
    interval=80
)

animation.save(
    "animation.gif",
    writer=PillowWriter(fps=12)
)

plt.close(fig)
~~~

Powstaje plik:

~~~text
animation.gif
~~~

GIF można otworzyć w przeglądarce, umieścić w Markdown albo osadzić na stronie internetowej.

---

## GIF w Markdown

Źródło:

~~~markdown
![Animacja ruchu punktu](animation.gif)
~~~

Jeżeli GitHub obsługuje dany plik poprawnie, animacja będzie odtwarzana bezpośrednio na stronie dokumentu.

---

# Interaktywny wykres

## Wykres statyczny a interaktywny

Zwykły plik PNG jest obrazem.

Możemy go:

- otworzyć,
- wydrukować,
- umieścić w publikacji.

Nie możemy jednak na nim naturalnie:

- powiększyć wybranego fragmentu danych,
- odczytać wartości po najechaniu myszą,
- ukryć jednej serii,
- przesuwać zakresu osi.

Do takich zastosowań wygodne są wykresy interaktywne.

---

# Plotly

**Plotly** jest biblioteką do tworzenia interaktywnych wykresów.

Przykład:

~~~python
import numpy as np
import plotly.express as px

x = np.linspace(0, 2*np.pi, 200)

fig = px.line(
    x=x,
    y=np.sin(x),
    labels={
        "x": "x",
        "y": "sin(x)"
    },
    title="Funkcja sin(x)"
)

fig.show()
~~~

W notebooku pojawi się wykres, który można m.in. powiększać i odczytywać wartości kursorem.

---

## Kilka serii

~~~python
import numpy as np
import plotly.graph_objects as go

x = np.linspace(0, 2*np.pi, 200)

fig = go.Figure()

fig.add_scatter(
    x=x,
    y=np.sin(x),
    mode="lines",
    name="sin(x)"
)

fig.add_scatter(
    x=x,
    y=np.cos(x),
    mode="lines",
    name="cos(x)"
)

fig.update_layout(
    title="Dwie funkcje",
    xaxis_title="x",
    yaxis_title="wartość"
)

fig.show()
~~~

Legenda pozwala włączać i wyłączać poszczególne serie.

---

# Eksport interaktywnego wykresu do HTML

Jedna z bardzo praktycznych cech Plotly to możliwość zapisania wykresu jako pliku HTML.

~~~python
fig.write_html("interactive_plot.html")
~~~

Powstanie:

~~~text
interactive_plot.html
~~~

Po otwarciu w przeglądarce wykres pozostaje interaktywny.

Domyślnie Plotly może umieścić potrzebny kod JavaScript bezpośrednio w pliku. Taki plik jest większy, ale może działać samodzielnie bez dodatkowych plików.

Można też użyć zewnętrznego CDN:

~~~python
fig.write_html(
    "interactive_plot.html",
    include_plotlyjs="cdn"
)
~~~

Wtedy plik jest dużo mniejszy, ale do załadowania biblioteki Plotly potrzebuje połączenia z Internetem.

Warto więc rozróżnić:

| Wariant | Zaleta | Ograniczenie |
| --- | --- | --- |
| biblioteka wewnątrz HTML | plik działa samodzielnie | większy rozmiar |
| `include_plotlyjs="cdn"` | mały plik | wymaga Internetu |

Oficjalna dokumentacja:

- [Plotly — Interactive HTML Export](https://plotly.com/python/interactive-html-export/)

---

# HTML jako artefakt obliczenia

To ważny moment.

Kod:

~~~text
create_plot.py
~~~

może wygenerować:

~~~text
interactive_plot.html
~~~

Podobnie jak wcześniej kod generował:

~~~text
fit.png
~~~

Różnica polega na tym, że HTML może zawierać zachowanie i interakcję.

Możemy więc traktować HTML jako **wynik obliczenia**, a nie tylko ręcznie napisaną stronę.

---

# Mała strona wyników

Załóżmy, że mamy:

~~~text
index.html
animation.gif
interactive_plot.html
~~~

Możemy przygotować stronę:

~~~html
<!doctype html>
<html lang="pl">
<head>
    <meta charset="utf-8">
    <title>Wyniki symulacji</title>
</head>

<body>
    <h1>Wyniki symulacji</h1>

    <h2>Animacja</h2>

    <img
        src="animation.gif"
        alt="Animacja ruchu punktu"
    >

    <h2>Wykres interaktywny</h2>

    <p>
        <a href="interactive_plot.html">
            Otwórz interaktywny wykres
        </a>
    </p>
</body>
</html>
~~~

Mamy teraz mały serwis składający się z kilku zwykłych plików.

---

# GitHub Pages

## Co to jest GitHub Pages?

**GitHub Pages** pozwala opublikować statyczną stronę internetową bezpośrednio na podstawie plików znajdujących się w repozytorium GitHub.

Strona projektu może otrzymać adres w rodzaju:

~~~text
https://nazwa-uzytkownika.github.io/nazwa-repozytorium/
~~~

Nie musimy:

- kupować serwera,
- konfigurować Apache,
- utrzymywać własnej maszyny dostępnej przez Internet.

---

## Co może opublikować GitHub Pages?

Dobrze nadają się:

- HTML,
- CSS,
- JavaScript,
- obrazy,
- dokumentacja projektu,
- statyczne raporty,
- interaktywne wykresy działające w przeglądarce.

GitHub Pages nie służy do uruchamiania dowolnego programu Python po stronie serwera.

Jeżeli przygotowaliśmy plik HTML **wcześniej**, możemy go opublikować.

Jeżeli strona wymaga uruchomienia Pythona za każdym wejściem użytkownika, potrzebne jest inne rozwiązanie.

---

## Plik wejściowy

Typową stroną główną jest:

~~~text
index.html
~~~

Przeglądarka otwiera go jako punkt startowy serwisu.

Przykładowa struktura:

~~~text
site/
├── index.html
├── animation.gif
└── interactive_plot.html
~~~

---

## Publikacja z repozytorium

Dokładny interfejs GitHuba może się zmieniać, ale ogólna idea jest stała:

1. pliki strony znajdują się w repozytorium,
2. w ustawieniach repozytorium włączamy GitHub Pages,
3. wskazujemy źródło publikacji,
4. GitHub publikuje stronę,
5. otrzymujemy adres `github.io`.

Po publikacji trzeba zawsze sprawdzić stronę w przeglądarce.

To, że plik istnieje w repozytorium, nie gwarantuje jeszcze, że:

- ścieżki do obrazów są poprawne,
- wielkość liter w nazwach jest zgodna,
- linki względne prowadzą do właściwego miejsca.

Oficjalne materiały:

- [GitHub Pages — dokumentacja](https://docs.github.com/en/pages)
- [GitHub Pages — Getting started](https://docs.github.com/en/pages/getting-started-with-github-pages)

---

# Markdown a strona internetowa

Markdown i HTML nie są konkurentami.

Markdown jest wygodny do pisania treści.

HTML jest formatem, który rozumie przeglądarka.

Wiele narzędzi działa według schematu:

~~~text
Markdown
   ↓
generator strony
   ↓
HTML
   ↓
przeglądarka
~~~

Jednym z takich generatorów jest MkDocs.

---

# MkDocs

## Co to jest MkDocs?

**MkDocs** jest generatorem statycznej dokumentacji.

Pisząc pliki Markdown, możemy zbudować z nich uporządkowaną stronę WWW.

To bardzo wygodne dla:

- dokumentacji projektu,
- materiałów kursowych,
- instrukcji,
- notatek technicznych,
- małych stron projektów.

---

## Najprostszy projekt

Struktura:

~~~text
mkdocs.yml
docs/
├── index.md
└── results.md
~~~

Plik `mkdocs.yml` może zawierać:

~~~yaml
site_name: Moje wyniki

nav:
  - Start: index.md
  - Wyniki: results.md
~~~

`nav` opisuje menu strony.

---

## `docs/index.md`

~~~markdown
# Moje wyniki

To jest strona główna dokumentacji.

## Materiały

- [Wyniki](results.md)
~~~

---

## `docs/results.md`

~~~markdown
# Wyniki

Najważniejsze wyniki projektu.

## Animacja

![Animacja](assets/animation.gif)

## Wykres

[Otwórz interaktywny wykres](assets/interactive_plot.html)
~~~

---

## Instalacja

Jeżeli MkDocs nie jest jeszcze zainstalowany:

~~~bash
python3 -m pip install mkdocs
~~~

Sprawdzenie:

~~~bash
mkdocs --version
~~~

---

## Lokalny podgląd

W katalogu zawierającym `mkdocs.yml`:

~~~bash
mkdocs serve
~~~

W terminalu pojawi się lokalny adres, zwykle zbliżony do:

~~~text
http://127.0.0.1:8000/
~~~

Po otwarciu go w przeglądarce zobaczymy dokumentację.

---

## Budowanie strony

~~~bash
mkdocs build
~~~

MkDocs utworzy gotową stronę statyczną, domyślnie w katalogu:

~~~text
site/
~~~

Czyli:

~~~text
Markdown
   ↓
mkdocs build
   ↓
HTML / CSS / pozostałe pliki
~~~

To dobry przykład oddzielenia:

- **źródła** — pliki Markdown,
- **wyniku procesu budowania** — gotowa strona.

---

## Publikacja MkDocs

MkDocs potrafi publikować zbudowaną dokumentację na GitHub Pages.

Jedna z dostępnych metod wykorzystuje:

~~~bash
mkdocs gh-deploy
~~~

Przed użyciem tej komendy trzeba rozumieć, że narzędzie będzie tworzyć i wysyłać wygenerowaną wersję strony do repozytorium.

Najpierw zawsze warto sprawdzić lokalnie:

~~~bash
mkdocs build
~~~

oraz:

~~~bash
mkdocs serve
~~~

Dopiero potem publikować.

Oficjalna dokumentacja:

- [MkDocs](https://www.mkdocs.org/)
- [MkDocs — Getting Started](https://www.mkdocs.org/getting-started/)

---

# AI i tworzenie dokumentacji

MkDocs jest dobrym przykładem miejsca, w którym AI może bardzo przyspieszyć pracę.

Możemy przekazać agentowi:

~~~text
Przeczytaj README.md oraz pliki z wynikami.

Przygotuj dokumentację MkDocs.

Wymagania:
- nie zmieniaj plików z wynikami,
- utwórz docs/index.md,
- utwórz docs/results.md,
- dodaj nawigację w mkdocs.yml,
- użyj linków względnych,
- nie publikuj strony,
- po zmianach uruchom mkdocs build,
- pokaż mi wynik i diff.
~~~

To jest dobry przykład pracy agentowej, ponieważ:

1. agent musi przeczytać kilka istniejących plików,
2. ma jasno określony wynik,
3. ma ograniczenia,
4. może uruchomić test,
5. człowiek może obejrzeć diff.

---

# Co należy publikować?

Przed publikacją strony warto zadać pytanie:

> Czy każdy plik, który znajduje się na stronie, może być publiczny?

Nie należy publikować przypadkowo:

- danych osobowych,
- kluczy API,
- haseł,
- prywatnych notatek,
- danych poufnych,
- plików, do których nie mamy prawa publikacji.

Publikacja internetowa zmienia charakter materiału. Plik przestaje być tylko elementem lokalnego projektu.

---

# Zadania dla studenta

Wszystkie pliki z tego bloku umieść w folderze:

~~~text
zadania/04_interaktywne_materialy_www/
~~~

Po wykonaniu zadań struktura powinna wyglądać:

~~~text
zadania/04_interaktywne_materialy_www/
├── README.md
├── index.html
├── interactive.html
├── create_plot.py
├── animation.py
├── animation.gif
├── mkdocs.yml
├── docs/
│   ├── index.md
│   ├── results.md
│   └── assets/
│       ├── interactive_plot.html
│       └── animation.gif
├── mkdocs_review.md
└── publication.md
~~~

Nie zmieniaj nazw wymaganych plików.

---

## Zadanie 1. Mała interaktywna strona HTML

Utwórz:

~~~text
index.html
~~~

Strona ma zawierać:

- poprawną strukturę HTML,
- kodowanie UTF-8,
- tytuł strony,
- nagłówek `h1`,
- co najmniej dwa akapity,
- listę,
- link,
- prostą sekcję CSS,
- pole typu number,
- przycisk,
- JavaScript liczący $x^2$.

Dla:

~~~text
x = 5
~~~

po kliknięciu przycisku strona ma pokazać:

~~~text
Wynik: 25
~~~

Nie kopiuj ślepo przykładu z notatek. Dodaj własny tytuł i krótki opis strony.

### Sprawdzenie

Będzie można sprawdzić strukturę HTML, obecność wymaganych elementów i kod funkcji JavaScript.

---

## Zadanie 2. Interaktywny wykres Plotly

Utwórz:

~~~text
create_plot.py
~~~

Program ma przygotować $200$ punktów w zakresie:

$$
0\le x\le 2\pi
$$

oraz dwie serie:

$$
y_1=\sin x
$$

$$
y_2=\cos x
$$

Wykres ma zawierać:

- tytuł,
- podpis osi $x$,
- podpis osi $y$,
- legendę,
- obie funkcje.

Zapisz go dwukrotnie.

Wersja samodzielna:

~~~text
interactive.html
~~~

oraz kopia używana przez MkDocs:

~~~text
docs/assets/interactive_plot.html
~~~

Przykład zapisu:

~~~python
fig.write_html("interactive.html")
fig.write_html("docs/assets/interactive_plot.html")
~~~

Po otwarciu HTML w przeglądarce sprawdź:

- możliwość powiększania,
- odczytywanie wartości kursorem,
- możliwość ukrycia jednej serii z legendy.

### Sprawdzenie

Będzie można uruchomić `create_plot.py` i sprawdzić:

- czy oba pliki HTML powstają,
- czy nie są puste,
- czy skrypt zawiera zarówno `sin`, jak i `cos`.

---

## Zadanie 3. Animacja GIF

Utwórz:

~~~text
animation.py
~~~

Przygotuj animację punktu poruszającego się po:

$$
y=\sin x
$$

w zakresie:

$$
0\le x\le 2\pi
$$

Skrypt ma zapisać wynik jako:

~~~text
animation.gif
~~~

oraz skopiować tę samą animację do:

~~~text
docs/assets/animation.gif
~~~

Możesz wykorzystać `FuncAnimation` i `PillowWriter` z przykładu w notatkach.

Po wygenerowaniu sprawdź plik w przeglądarce.

### Sprawdzenie

Będzie można:

- uruchomić `animation.py`,
- sprawdzić istnienie obu plików GIF,
- sprawdzić, czy pliki mają niezerowy rozmiar.

---

## Zadanie 4. Dokumentacja MkDocs

Utwórz:

~~~text
mkdocs.yml
~~~

oraz:

~~~text
docs/index.md
docs/results.md
~~~

`mkdocs.yml` ma zawierać nazwę strony i menu z dwiema pozycjami:

- Start,
- Wyniki.

`docs/index.md` ma zawierać:

- tytuł,
- krótki opis projektu,
- listę użytych technologii,
- link do strony z wynikami.

`docs/results.md` ma zawierać:

- krótkie wyjaśnienie funkcji sinus i cosinus,
- osadzoną animację,
- link do interaktywnego wykresu.

Następnie uruchom:

~~~bash
mkdocs build
~~~

oraz:

~~~bash
mkdocs serve
~~~

Otwórz lokalny podgląd w przeglądarce i sprawdź wszystkie linki.

### Sprawdzenie

Będzie można sprawdzić:

- strukturę `mkdocs.yml`,
- istnienie obu dokumentów Markdown,
- link do `assets/interactive_plot.html`,
- osadzenie `assets/animation.gif`,
- możliwość wykonania `mkdocs build`.

---

## Zadanie 5. Kontrolowane użycie AI do dokumentacji

Poproś narzędzie AI o przejrzenie:

~~~text
index.html
create_plot.py
animation.py
docs/index.md
docs/results.md
mkdocs.yml
~~~

i zaproponowanie ulepszeń dokumentacji.

AI **nie może zmieniać wyników matematycznych ani nazw wymaganych plików**.

Po wykonaniu zmian utwórz:

~~~text
mkdocs_review.md
~~~

ze strukturą:

~~~markdown
# Review zmian AI

## Użyty prompt

...

## Co zostało zmienione?

...

## Co sprawdziłem?

...

## Co odrzuciłem lub poprawiłem?

...
~~~

Następnie ponownie uruchom:

~~~bash
mkdocs build
~~~

### Sprawdzenie

Będzie można sprawdzić strukturę `mkdocs_review.md` i ponownie zbudować stronę.

---

## Zadanie 6. Publikacja na GitHub Pages

Opublikuj przygotowaną dokumentację jako GitHub Pages.

Możesz użyć mechanizmu publikacji dostępnego dla MkDocs, np.:

~~~bash
mkdocs gh-deploy
~~~

albo skonfigurować GitHub Pages zgodnie z aktualną dokumentacją GitHuba.

Po publikacji utwórz:

~~~text
publication.md
~~~

Plik ma zawierać:

~~~markdown
# Publikacja

## Adres strony

...

## Co zostało opublikowane?

...

## Test

...

## Uwagi

...
~~~

W części **Adres strony** podaj działający adres `github.io`.

W części **Test** napisz, czy sprawdziłeś:

- stronę główną,
- przejście do Wyników,
- animację,
- interaktywny wykres.

Jeżeli publikacja GitHub Pages nie jest możliwa z powodów technicznych lub ograniczeń konta, opisz dokładnie problem w sekcji **Uwagi** i pozostaw działający lokalny build MkDocs.

### Sprawdzenie

Można sprawdzić:

- istnienie `publication.md`,
- obecność adresu strony,
- publiczną dostępność strony, jeśli została opublikowana,
- strukturę lokalnego projektu niezależnie od publikacji.

---

## Zadanie 7. README bloku

Utwórz `README.md`.

Powinien zawierać:

- krótkie wyjaśnienie różnicy między HTML, CSS i JavaScript,
- różnicę między wykresem PNG a interaktywnym HTML,
- listę wygenerowanych artefaktów,
- link do `interactive.html`,
- osadzoną `animation.gif`,
- link do `publication.md`,
- checklistę wszystkich zadań.

Dodaj tabelę:

~~~markdown
| Artefakt | Format | Interaktywny? |
| --- | --- | --- |
| strona | HTML | tak |
| wykres Plotly | HTML | tak |
| animacja | GIF | częściowo |
| dokumentacja | Markdown / HTML | linki i multimedia |
~~~

---

# Checklista końcowa

Przed zgłoszeniem bloku sprawdź:

- [ ] `index.html` otwiera się w przeglądarce,
- [ ] kalkulator dla `x=5` zwraca `25`,
- [ ] `create_plot.py` uruchamia się bez błędu,
- [ ] `interactive.html` jest interaktywny,
- [ ] `docs/assets/interactive_plot.html` istnieje,
- [ ] `animation.py` uruchamia się bez błędu,
- [ ] `animation.gif` otwiera się poprawnie,
- [ ] `docs/assets/animation.gif` istnieje,
- [ ] `mkdocs.yml` ma poprawną nawigację,
- [ ] `docs/index.md` i `docs/results.md` istnieją,
- [ ] `mkdocs build` kończy się powodzeniem,
- [ ] lokalny podgląd MkDocs działa,
- [ ] `mkdocs_review.md` opisuje użycie i kontrolę AI,
- [ ] `publication.md` zawiera wynik próby publikacji,
- [ ] `README.md` zawiera linki, animację i checklistę.
