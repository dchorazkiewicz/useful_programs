# Google Colab

## Co to jest Google Colab?

**[Google Colab](https://colab.research.google.com/)** to internetowe środowisko programistyczne oparte na notebookach Jupyter. Umożliwia pisanie i uruchamianie kodu w Pythonie bez instalowania dodatkowego oprogramowania — wystarczy przeglądarka i konto Google. Colab oferuje bezpłatny dostęp z ograniczonymi zasobami oraz płatne plany.

Darmowa wersja zapewnia dostęp do **12,6 GB** RAM, **parę rdzeni** CPU oraz dysku o pojemności **107 GB**.

Jest wystarczająco szybki do większości zadań programistycznych i wielu studentów korzysta z niego w ramach kursów programowania, nawet do ternowania sieci neuronowych.

Notebook Jupyter to dokument, który może zawierać jednocześnie:

- opis,
- wzory,
- kod,
- wyniki obliczeń,
- tabele,
- wykresy.

Notebook Colaba jest zwykle zapisywany jako plik:

~~~text
nazwa_notebooka.ipynb
~~~

Rozszerzenie `.ipynb` oznacza plik notebooka Jupyter.

Pamiętaj: Colab służy do edycji i wykonywania notebooków (jest to tylko środowisko wykonawcze). Sam notebook jest plikiem tekstowym w formacie **JSON** [http://json.org/](http://json.org/), który można przechowywać lokalnie, w repozytorium na GitHubie lub na Dysku Google. Zawiera treść komórek, metadane i zapisane wyniki, ale nie zapisuje całego stanu pamięci środowiska wykonawczego.

Możesz taki plik **otworzyć i uruchomić jego komórki** nie tylko w Colabie, ale też w Jupyter Notebook, JupyterLab lub VS Code (Visual Studio Code), po skonfigurowaniu środowiska Pythona i potrzebnych bibliotek.

---

## Przykład Colaba — zanim zaczniesz czytać, zobacz przykład!

Zobacz przykładowy notebook i jego możliwości:

- Plik: [„Fizyka to mnie fascynuje”](https://colab.research.google.com/drive/1_dRkB9tsH2TBYFoSsNpNg60-6lIE-pi6?usp=sharing) bezpośrednio w Colabie
- Ten sam plik Jupyter w repozytorium: [repozytorium](examples/02_colab/Fizyka_to_mnie_fascynuje_2026.ipynb)

Pobierz plik `.ipynb` i otwórz go w swoim Colabie przez **File → Upload notebook** (opcja przesyłania notebooka w menu **Plik**).

---

## Komórki

Notebook składa się z **komórek**. Najczęściej używamy dwóch rodzajów:

### Komórka tekstowa

Służy do opisu obliczeń. Obsługuje bezpośrednio **Markdown**.

Przykład zawartości:

~~~markdown
## Obliczenie pola koła

Dla promienia $r=3$ liczymy pole ze wzoru

$$
P=\pi r^2
$$
~~~

### Komórka kodu

Zawiera kod wykonywany przez środowisko.

Przykład:

~~~python
import math

r = 3
P = math.pi * r**2

print(P)
~~~

Efekt:

~~~text
28.274333882308138
~~~

Dobrze przygotowany notebook przeplata opis z kodem. Czytelnik powinien wiedzieć, **co liczymy, dlaczego to liczymy i jaki otrzymaliśmy wynik**.

---

## Runtime, czyli środowisko wykonawcze

Notebook jest plikiem, ale kod musi zostać gdzieś wykonany.

Do uruchamiania kodu Colab przydziela notebookowi **środowisko wykonawcze** — runtime.

Można myśleć o nim jak o tymczasowym komputerze uruchomionym w chmurze.

W runtime znajdują się między innymi:

- zmienne przechowywane w pamięci,
- uruchomiony Python,
- zainstalowane biblioteki,
- pliki wygenerowane podczas obliczeń.

Notebook i runtime to nie to samo. **Zmienne w pamięci i pliki zapisane wyłącznie na dysku runtime są tymczasowe**. Potrzebne pliki należy pobrać na komputer, zapisać na Dysku Google lub umieścić w repozytorium. Wyniki wyświetlone w komórkach można zachować w zapisanym notebooku, ale nie odtwarzają one zmiennych ani plików środowiska wykonawczego.

---

## Stan środowiska wykonawczego

Rozważmy dwie komórki.

Pierwsza:

~~~python
a = 10
~~~

Druga:

~~~python
print(a + 5)
~~~

Jeżeli wykonamy je w tej kolejności, otrzymamy:

~~~text
15
~~~

Jeżeli jednak zrestartujemy runtime i uruchomimy tylko drugą komórkę, zmienna `a` nie będzie już istnieć i kod zakończy się błędem `NameError`.

Dlatego przed oddaniem notebook powinien dać się uruchomić **od początku do końca, w kolejności komórek zapisanej w dokumencie**.

Dobra praktyka:

1. ponowne uruchomienie środowiska wykonawczego,
2. uruchomienie wszystkich komórek od początku,
3. sprawdzenie, czy żadna komórka nie kończy się błędem.

---

## Tworzenie pliku w Colabie

Kod może wygenerować zwykły plik.

~~~python
wynik = 2 + 2

with open("wynik.txt", "w", encoding="utf-8") as f:
    f.write(str(wynik))
~~~

Powstanie plik:

~~~text
wynik.txt
~~~

o zawartości:

~~~text
4
~~~

To ważny przykład: kod nie musi tylko wyświetlać wyniku na ekranie. Może wygenerować plik, który następnie zapisujemy jako część projektu.

---

## Tworzenie wykresu

Przykład:

~~~python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, marker="o")
plt.xlabel("x")
plt.ylabel("x^2")
plt.grid()
plt.savefig("wykres.png", dpi=150, bbox_inches="tight")
plt.show()
~~~

Kod:

1. tworzy dane,
2. rysuje wykres,
3. zapisuje go jako `wykres.png`,
4. pokazuje wykres w notebooku.

Po wykonaniu komórki w plikach runtime pojawi się:

~~~text
wykres.png
~~~

Taki plik można później umieścić w repozytorium i osadzić w raporcie Markdown.

---

## Pliki na dysku runtime są tymczasowe

Pliki utworzone w runtime nie powinny być traktowane jako trwałe archiwum.

Jeżeli wygenerujemy:

~~~text
wynik.txt
wykres.png
dane.csv
~~~

należy zachować potrzebne rezultaty, np.:

- pobrać je na komputer,
- zapisać na Dysku Google,
- umieścić w repozytorium.

---

## Notebook jako dokumentacja obliczeń

Dobry notebook powinien przypominać krótki raport, a nie przypadkowy zbiór komórek.

Prosty układ:

~~~text
Tytuł
↓
Cel
↓
Dane / parametry
↓
Kod
↓
Wynik
↓
Krótki komentarz
~~~

Czytelnik powinien móc otworzyć notebook i zrozumieć jego sens bez pytania autora: „Co tutaj właściwie zrobiono?”.

## Tworzone pliki

Czasami pliki wynikowe (np. GIF lub wideo) nie wyświetlają się bezpośrednio w notebooku. Kod może jednak zapisać je na dysku środowiska wykonawczego. Aby sprawdzić, czy plik został utworzony, otwórz panel **Pliki** po lewej stronie Colaba.

Przykład:

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x, y, marker="o")
plt.xlabel("x")
plt.ylabel("x^2")
plt.grid()
plt.savefig("wykres.png", dpi=150, bbox_inches="tight")  # zapisanie wykresu do pliku
plt.show()
```

W efekcie powstanie plik `wykres.png`, który można pobrać na komputer lub umieścić w repozytorium. Wykres pokaże się w notebooku, a zapisany plik będzie również dostępny w panelu **Pliki** po lewej stronie.

---

## Uruchomienie notebooka Jupyter zapisanego w repozytorium na GitHubie

Notebook zapisany w repozytorium na GitHubie można otworzyć i uruchomić w Colabie. Jeśli autor dodał do notebooka lub pliku README przycisk **Open in Colab**, wystarczy go kliknąć. GitHub nie dodaje tego przycisku automatycznie.

Można też w oknie otwierania notebooka w Colabie wybrać zakładkę **GitHub**, podać adres repozytorium lub notebooka, a następnie wybrać plik `.ipynb`.

Otwarcie i edycja notebooka w Colabie nie zmieniają automatycznie pliku na GitHubie. Aby zapisać zmiany w repozytorium, wybierz **File → Save a copy in GitHub** i wskaż repozytorium, gałąź oraz ścieżkę pliku.

Do zapisu potrzebne są uprawnienia do repozytorium oraz autoryzacja dostępu Colaba do konta GitHub. Jeśli nie możesz zapisać zmian w repozytorium autora, możesz zachować kopię we własnym repozytorium lub na Dysku Google.

---

## Współpraca z AI

Możesz prosić różne czaty AI o kod w Pythonie przeznaczony do uruchomienia w Colabie. To samo dotyczy tekstu w Markdownie.

Colab ma również wbudowane narzędzie AI oparte na Gemini, które pomaga generować i wyjaśniać kod oraz poprawiać błędy. 

Nazywa się Gemini Copilot i jest dostępne w menu **Tools → AI Assistant** lub przez ikonę w prawym górnym rogu Colaba.

## Błędy

Podczas pracy w Colabie mogą pojawić się różne błędy, np. związane z brakującymi bibliotekami, błędami składniowymi w kodzie czy problemami z dostępem do plików. Przekopiuj komunikaty błędów do Copilota Gemini lub innego narzędzia AI, aby uzyskać pomoc w ich rozwiązaniu. Często AI poprawi jakąś subtelną część kodu lub wskaże, co należy zmienić.

---

## Dobre materiały o Colabie

- [Google Colab — oficjalne wprowadzenie](https://colab.research.google.com/notebooks/intro.ipynb)
- [Google Colab — FAQ](https://research.google.com/colaboratory/faq.html)
- [Google Colab — zaawansowane funkcje](https://colab.research.google.com/notebooks/pro.ipynb)
- [Google Colab — załączanie danych zewnętrznych](https://colab.research.google.com/notebooks/io.ipynb)
- [Google Colab — współpraca z GitHubem](https://colab.research.google.com/github/googlecolab/colabtools/blob/main/notebooks/colab-github-demo.ipynb)
- [Jupyter — format pliku notebooka](https://nbformat.readthedocs.io/en/latest/format_description.html)
