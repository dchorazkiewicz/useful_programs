# Markdown — rozwiązanie wzorcowe

Ten plik pokazuje podstawowe elementy składni Markdown. Jest przygotowany jako **rozwiązanie wzorcowe dla prowadzącego** i może służyć do szybkiego porównania z pracą studenta.

## Formatowanie i listy

Markdown pozwala przygotować czytelny dokument bez rozbudowanego edytora tekstu. Możemy używać tekstu **pogrubionego**, *pochylonego* oraz ~~przekreślonego~~.

Lista punktowana:

- tekst,
- wzory matematyczne,
- kod,
- grafika.

Lista numerowana:

1. utwórz plik,
2. wpisz treść,
3. sprawdź renderowanie na GitHubie.

Checklist:

- [x] tytuł i sekcje,
- [x] podstawowe formatowanie,
- [x] listy,
- [x] tabela,
- [x] kod,
- [x] matematyka,
- [x] obrazek.

## Tabela, link, kod i matematyka

| Element | Przykład | Status |
| --- | --- | --- |
| Markdown | nagłówki i listy | gotowe |
| Python | prosty skrypt | gotowe |
| Matematyka | LaTeX w `$...$` i `$$...$$` | gotowe |

Notebooki można uruchamiać w [Google Colab](http://colab.research.google.com).

Przykładowy kod Pythona:

```python
def pole_kola(r):
    return math.pi * r**2

print(pole_kola(2))
```

Przykładowe wzory w tekście: $E=mc^2$, $a^2+b^2=c^2$ oraz $f(x)=\sin x$.

Pierwszy wzór blokowy:

$$
x_{1,2}=\frac{-b\pm\sqrt{b^2-4ac}}{2a}.
$$

Drugi wzór blokowy:

$$
\sum_{k=1}^{n} k=\frac{n(n+1)}{2}.
$$

Trzeci wzór blokowy:

$$
\int_0^\pi \sin x\,dx=2.
$$

## Obrazek

Poniżej osadzony jest plik `wykres.png` znajdujący się w tym samym folderze.

![Przykładowy wykres](wykres.png)
