# Zadania: Colab

**Folder na rozwiązania:** [`pages/solutions/02_sol_colab/`](../solutions/02_sol_colab/) (ścieżka względem głównego katalogu repozytorium).

## Zadanie 1.

Utwórz notebook `colab_intro.ipynb` w Colabie i potem docelowo zapisz go w swoim sforkowanym repozytorium na GitHubie w folderze `pages/solutions/02_sol_colab/`

## Zadanie 2.

Notebook ma zawierać co najmniej:

1. komórkę Markdown z tytułem `Colab Intro`,
2. komórkę Markdown z tekstowym opisem jakiś obliczeń: np. sumowanie ciągu geometrycznego dla n wyrazów (zadbaj o dobre renderowanie kodu w Markdown!),
3. komórkę kodu liczącą 2+2,
4. komórkę kodu liczącą pi^pi,
5. komórkę kodu liczącą sumę kwadratów liczb od 1 do 100,
6. komórkę kodu zapisującą wynik sumy kwadratów do `colab_wynik.txt` (upewnij się, gdzie zostanie zapisany plik!),
7. komórkę kodu tworzącą wykres $y=k^2$ dla $k=1,\ldots,20$,
8. zapis wykresu do `wykres.png`.
9. komórkę kodu z wideo osadzonym w notebooku i zapisującym je do pliku `video.mp4` z animacją wahadła (poproś AI o kod pythona do wygenerowania animacji w Colabie w formacie mp4).
10. komórkę kodu która z video 'video.mp4' wygeneruje animowany plik `video.gif` (upewnij się, gdzie zostanie zapisany plik!).
11. komórkę kodu, w której zmodyfikujesz funkcje w poniższym kodzie by wygenerować jakąś inną krzywą parametryczną. Wynik ma być wyświetlony w notebooku i zapisany do pliku graficznego o nazwie `parametric_curve.png`.

```python
# Correcting the label for rendering issue in matplotlib mathtext
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parametric equations
t = np.linspace(0, 2 * np.pi, 500)
x = np.sin(t) * np.cos(t)
y = np.sin(t) * np.sin(t)
z = np.cos(t)

# 3D Plot
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, label="Parametric Curve")
ax.set_title("3D Parametric Curve", fontsize=14)
ax.set_xlabel("x(t)")
ax.set_ylabel("y(t)")
ax.set_zlabel("z(t)")
ax.legend()
plt.show()
```

## Zadanie 3.

Na końcu zrestartuj runtime i uruchom wszystkie komórki od początku i upewnij się, że notebook nie zgłasza błędów!

## Zadanie 4.

Dodaj do repozytorium na GitHubie w odpowiednim miejscu czyli w folderze `pages/solutions/02_sol_colab/` otrzymane pliki: notebook `colab_intro.ipynb`, plik tekstowy `colab_wynik.txt`, a także obrazek `wykres.png`, `video.gif` oraz `parametric_curve.png`.

Nie załączaj wideo `video.mp4`, bo plik za dużo waży!