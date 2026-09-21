# 9. Praca mobilna, integracje

Komputer nie zawsze jest pod ręką. Czasem trzeba sprawdzić Issue z telefonu, poprawić drobny plik, wejść na serwer przez SSH, pobrać dokument z chmury albo poprosić AI o analizę materiału z podłączonej usługi.

W tym bloku interesuje nas **praca poza jednym komputerem** i bezpieczne łączenie różnych usług.

---

# Telefon jako narzędzie pracy

Telefon dobrze nadaje się do:

- sprawdzenia powiadomień,
- odczytania Issue,
- komentarza do Pull Requesta,
- małej edycji Markdown,
- sprawdzenia statusu projektu,
- pobrania lub udostępnienia pliku,
- rozmowy z AI,
- potwierdzenia logowania.

Nie nadaje się równie dobrze do wszystkiego.

Dobry przykład:

~~~text
otwórz repozytorium
↓
popraw literówkę
↓
sprawdź diff
↓
commit
~~~

Słaby przykład:

~~~text
rozwiązuj konflikt merge
i edytuj 500 linii kodu
na małym ekranie
~~~

---

# GitHub Mobile

GitHub ma oficjalną aplikację mobilną dla Androida i iOS.

Można w niej m.in.:

- przeglądać repozytoria,
- pracować z Issues i Pull Requests,
- wyszukiwać kod,
- obsługiwać powiadomienia,
- wykonywać część operacji związanych z kontem.

Dokumentacja:

- [GitHub Mobile](https://docs.github.com/en/get-started/using-github/github-mobile)

Przy większej zmianie wygodniej przejść do VS Code, Codespaces albo komputera.

---

# Chmura

Plik może być przechowywany w usłudze typu:

- Google Drive,
- OneDrive,
- Dropbox,
- GitHub.

To nie są identyczne narzędzia.

Dysk chmurowy jest wygodny dla dokumentów, arkuszy, PDF-ów i współdzielenia.

Repozytorium Git jest lepsze dla kodu, historii zmian i pracy programistycznej.

---

# Synchronizacja, wersjonowanie i backup

Warto rozróżniać:

~~~text
synchronizacja
≠
wersjonowanie
≠
backup
~~~

Synchronizacja przenosi zmiany między urządzeniami.

Wersjonowanie zachowuje historię zmian.

Backup jest osobną kopią pozwalającą odzyskać dane po awarii lub pomyłce.

Jedna usługa może oferować kilka z tych funkcji, ale pojęcia nadal nie oznaczają tego samego.

---

# Udostępnianie plików

Przed wysłaniem linku sprawdź:

1. kto ma dostęp,
2. czy odbiorca musi być zalogowany,
3. czy ma odczyt czy edycję,
4. czy link działa,
5. czy udostępniono właściwy plik.

Samo skopiowanie adresu z paska przeglądarki nie zawsze oznacza poprawne udostępnienie zasobu.

---

# SSH

## Co to jest SSH?

**SSH — Secure Shell** pozwala zestawić szyfrowane połączenie z innym komputerem przez sieć.

Schemat:

~~~text
mój komputer
    ↓
   SSH
    ↓
serwer
~~~

Typowe polecenie:

~~~bash
ssh user@example.org
~~~

Po zalogowaniu polecenia wykonują się na zdalnej maszynie.

---

# Klucze SSH

SSH może używać pary:

~~~text
klucz prywatny
+
klucz publiczny
~~~

Typowe pliki:

~~~text
~/.ssh/id_ed25519
~/.ssh/id_ed25519.pub
~~~

`id_ed25519` jest kluczem prywatnym.

`id_ed25519.pub` jest kluczem publicznym.

Najważniejsza zasada:

> **Klucz prywatny pozostaje prywatny.**

Nie wysyłamy go:

- do repozytorium,
- do Issue,
- e-mailem,
- do AI,
- na publiczny dysk.

Do GitHuba dodajemy klucz **publiczny**.

Dokumentacja:

- [GitHub — Connecting with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [GitHub — Checking existing keys](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)
- [GitHub — Generating a key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

---

# Najpierw sprawdź istniejące klucze

~~~bash
ls -al ~/.ssh
~~~

Możemy zobaczyć np.:

~~~text
id_ed25519
id_ed25519.pub
known_hosts
~~~

Nie ma sensu generować kolejnych kluczy bez sprawdzenia, co już istnieje.

---

# Passphrase

Klucz prywatny można dodatkowo zabezpieczyć hasłem — **passphrase**.

`ssh-agent` może przechowywać odblokowany klucz podczas sesji.

Dokumentacja:

- [GitHub — SSH key passphrases](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases)

---

# Test GitHub SSH

Po poprawnej konfiguracji:

~~~bash
ssh -T git@github.com
~~~

GitHub powinien rozpoznać konto i poinformować o poprawnym uwierzytelnieniu.

To test autoryzacji, a nie dostęp do zwykłej powłoki systemowej.

Dokumentacja:

- [Testing SSH connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/testing-your-ssh-connection)

---

# HTTPS czy SSH?

Remote repozytorium może wyglądać tak:

~~~text
https://github.com/user/repo.git
~~~

albo:

~~~text
git@github.com:user/repo.git
~~~

Sprawdzenie:

~~~bash
git remote -v
~~~

Oba podejścia mogą być poprawne. Nie trzeba zmieniać działającej konfiguracji bez powodu.

---

# Publiczny komputer

Na obcym komputerze nie kopiuj bezmyślnie prywatnego klucza SSH.

Lepsze rozwiązania mogą obejmować:

- przeglądarkę,
- Codespaces,
- osobne środowisko o ograniczonym dostępie,
- krótką sesję na zaufanym urządzeniu.

Komputer w hotelu lub bibliotece nie powinien automatycznie stać się zaufanym urządzeniem.

---

# Praca z kodem na telefonie

Telefon może być tylko interfejsem:

~~~text
telefon / tablet
      ↓
przeglądarka
      ↓
Codespaces
      ↓
VS Code w chmurze
~~~

Właściwe środowisko działa wtedy w chmurze.

---

# Integracje

## Co to jest integracja?

Integracja pozwala jednej usłudze współpracować z inną.

Przykłady:

~~~text
AI ↔ GitHub
AI ↔ Gmail
AI ↔ Dysk
formularz → arkusz
repozytorium → strona WWW
~~~

Integracja może pozwalać na:

- odczyt,
- wyszukiwanie,
- tworzenie,
- modyfikowanie,
- wykonywanie akcji.

---

# Odczyt i zapis to różne uprawnienia

### Integracja A

~~~text
tylko odczyt
~~~

### Integracja B

~~~text
odczyt + modyfikacja + akcje
~~~

To istotna różnica.

Przed połączeniem usługi trzeba sprawdzić zakres uprawnień.

---

# Zasada najmniejszych uprawnień

Dobre pytanie brzmi:

> Jakie najmniejsze uprawnienia wystarczą do wykonania zadania?

Jeśli AI ma tylko podsumować dokument, nie potrzebuje automatycznie prawa do jego usuwania.

Jeśli ma tylko znaleźć wiadomość, nie zawsze potrzebuje prawa do wysyłania wiadomości.

---

# Audyt integracji

Przy każdym połączeniu warto odpowiedzieć:

| Pytanie | Przykład |
| --- | --- |
| Co łączę? | AI + GitHub |
| Po co? | analiza Issue |
| Jakie dane są dostępne? | wybrane repozytorium |
| Czy narzędzie może pisać? | tak / nie |
| Czy może wykonywać akcje? | tak / nie |
| Jak ograniczyć dostęp? | zakres uprawnień |
| Jak odłączyć integrację? | ustawienia konta |

To lepsze niż automatyczne zatwierdzanie każdego okna uprawnień.

---

# AI + GitHub

AI połączone z repozytorium może pomagać w:

- wyszukaniu pliku,
- streszczeniu Issue,
- analizie kodu,
- przygotowaniu dokumentacji,
- zaproponowaniu poprawki.

Dobry pierwszy prompt:

~~~text
Przeczytaj README.md i analyze.py.

Nie zmieniaj plików.

Napisz:
1. do czego służy projekt,
2. jakie pliki są wejściem,
3. jakie pliki są wynikiem,
4. co trzeba uruchomić.
~~~

Bezpieczniej zacząć od odczytu niż od szerokiego polecenia modyfikacji repozytorium.

---

# AI + poczta

Integracja AI z pocztą może pomagać w:

- wyszukiwaniu wiadomości,
- streszczeniu wątku,
- przygotowaniu szkicu odpowiedzi,
- wyłapaniu terminów.

Trzeba jednak rozróżnić:

~~~text
przeczytaj wiadomość
~~~

od:

~~~text
wyślij wiadomość
~~~

Wykonanie akcji jest poważniejszym uprawnieniem niż odczyt.

---

# Filtry Gmaila

Nie każda automatyzacja potrzebuje AI.

Gmail pozwala tworzyć filtry, które mogą automatycznie m.in.:

- dodawać etykiety,
- archiwizować,
- oznaczać gwiazdką,
- przekazywać wiadomości.

Dokumentacja:

- [Gmail — tworzenie filtrów](https://support.google.com/mail/answer/6579?hl=pl)

---

# AI + dysk chmurowy

Integracja z dyskiem może pozwolić AI:

- znaleźć dokument,
- przeczytać wybrane pliki,
- podsumować folder,
- porównać dokumenty.

Warto ograniczyć zakres:

~~~text
Przeczytaj tylko pliki z folderu Projekt A.
Nie korzystaj z innych folderów.
~~~

Jeśli można wybrać pojedynczy dokument zamiast całego dysku, jest to często bezpieczniejszy wybór.


---

# Automatyzacja

Automatyzacja oznacza przekazanie komputerowi powtarzalnej procedury.

Przykład ręczny:

~~~text
pobierz plik
→ zmień nazwę
→ policz wiersze
→ zapisz wynik
~~~

Jeżeli wykonujemy to wielokrotnie, warto przygotować skrypt.

---

# Prosty skrypt

Mamy `data.txt`.

`report.sh`:

~~~bash
#!/usr/bin/env bash

file="data.txt"

lines=$(wc -l < "$file")
bytes=$(wc -c < "$file")

echo "file=$file" > report.txt
echo "lines=$lines" >> report.txt
echo "bytes=$bytes" >> report.txt
~~~

Po:

~~~bash
bash report.sh
~~~

powstaje `report.txt`.

Automatyzacja jest dobra wtedy, gdy wynik da się sprawdzić.

---

# Automatyzacja bez kodu

Przykład:

~~~text
nowy e-mail spełniający warunek
        ↓
etykieta
        ↓
archiwizacja
~~~

To również automatyzacja.

Inny przykład:

~~~text
formularz
   ↓
arkusz
   ↓
zestawienie
~~~

---

# AI jako element automatyzacji

Przykład:

~~~text
nowy dokument
    ↓
AI tworzy streszczenie
    ↓
człowiek sprawdza
    ↓
wynik trafia do raportu
~~~

Warto określić, które kroki mogą działać automatycznie, a gdzie potrzebna jest decyzja człowieka.

---

# Nie automatyzuj niejasnego procesu

Jeżeli nie potrafimy wykonać procesu ręcznie i nie wiemy, jaki wynik jest poprawny, automatyzacja może tylko szybciej produkować błędy.

Dobra kolejność:

~~~text
1. wykonaj ręcznie,
2. zrozum kroki,
3. ustal oczekiwany wynik,
4. dopiero wtedy automatyzuj.
~~~

---

# Dobre materiały

- [GitHub Mobile](https://docs.github.com/en/get-started/using-github/github-mobile)
- [GitHub — SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)
- [GitHub — Authentication](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github)
- [Gmail — filtry](https://support.google.com/mail/answer/6579?hl=pl)

---

# Zadania dla studenta

Wszystkie rozwiązania umieść w folderze:

~~~text
zadania/09_praca_mobilna_integracje/
~~~

Po wykonaniu zadań folder powinien zawierać:

~~~text
zadania/09_praca_mobilna_integracje/
├── README.md
├── mobile_edit.md
├── mobile_report.md
├── ssh.md
├── cloud.md
├── integration_audit.md
├── ai_integration.md
├── automation/
│   ├── data.txt
│   ├── report.sh
│   └── report.txt
└── security_check.md
~~~

Nie zapisuj w repozytorium:

~~~text
prywatnych kluczy SSH
haseł
tokenów
kluczy API
plików z sekretami
~~~

---

## Zadanie 1. Mała zmiana mobilna

Za pomocą telefonu lub tabletu:

1. otwórz własne repozytorium,
2. utwórz `mobile_edit.md`,
3. wpisz:

~~~markdown
# Mobile edit

Ten plik został utworzony podczas pracy mobilnej.

## Urządzenie

telefon / tablet

## Sposób

GitHub Mobile / przeglądarka / inne
~~~

4. wykonaj commit:

~~~text
09: mobile edit
~~~

Następnie utwórz `mobile_report.md` i w 4–6 zdaniach napisz:

- co było wygodne,
- co było niewygodne,
- do czego telefon się nadaje,
- kiedy wybrałbyś komputer.

### Sprawdzenie

Będzie można sprawdzić plik i historię commita.

---

## Zadanie 2. SSH bez publikowania sekretów

Na komputerze, WSL albo Codespaces wykonaj:

~~~bash
ls -al ~/.ssh
~~~

Jeśli masz skonfigurowany SSH do GitHuba:

~~~bash
ssh -T git@github.com
~~~

Jeśli nie masz, nie konfiguruj go na siłę. Przeczytaj oficjalną instrukcję i opisz proces.

Utwórz `ssh.md`:

~~~markdown
# SSH

## Co to jest SSH?

...

## Klucz publiczny

...

## Klucz prywatny

...

## Dlaczego prywatnego klucza nie wolno commitować?

...

## Moja konfiguracja

SSH działa / SSH nie było konfigurowane

## Test

...
~~~

Jeśli testowałeś połączenie, wklej tylko końcowy komunikat.

**Nie wklejaj zawartości klucza prywatnego.**

### Sprawdzenie

Plik będzie sprawdzany pod kątem struktury i typowych oznak przypadkowo dodanego prywatnego klucza.

---

## Zadanie 3. Chmura i uprawnienia

Utwórz `cloud.md`.

Na pliku testowym sprawdź różnicę między:

~~~text
tylko ja
link tylko do odczytu
dostęp do edycji
~~~

Opisz:

1. różnice między ustawieniami,
2. co wybrałbyś dla gotowego raportu,
3. co dla dokumentu współautorskiego,
4. dlaczego link nie zawsze oznacza publiczny dostęp,
5. czym synchronizacja różni się od backupu.

Nie umieszczaj w repozytorium prywatnego linku wymagającego logowania.

---

## Zadanie 4. Audyt integracji

Wybierz dwa przykłady:

~~~text
AI + GitHub
AI + Gmail
AI + dysk chmurowy
~~~

Utwórz `integration_audit.md`.

Dla każdej integracji dodaj tabelę:

~~~markdown
| Pytanie | Odpowiedź |
| --- | --- |
| Co łączę? | ... |
| Po co? | ... |
| Jakie dane może odczytać? | ... |
| Czy może tworzyć dane? | ... |
| Czy może modyfikować dane? | ... |
| Czy może wykonywać akcje? | ... |
| Jak ograniczyć dostęp? | ... |
| Jak odłączyć integrację? | ... |
~~~

Nie musisz aktywować integracji, jeśli nie chcesz udzielać jej dostępu.

---

## Zadanie 5. Jedna integracja AI

Jeśli masz dostęp do AI połączonego z GitHubem, pocztą albo dyskiem, wykonaj jedno zadanie na danych kursowych lub testowych.

Przykład GitHub:

~~~text
Przeczytaj README.md.
Wskaż trzy najważniejsze pliki projektu.
Nie zmieniaj repozytorium.
~~~

Przykład poczta:

~~~text
Znajdź testowe wiadomości dotyczące kursu.
Przygotuj podsumowanie.
Nie wysyłaj żadnej wiadomości.
~~~

Przykład dysk:

~~~text
Przeczytaj wskazany dokument testowy.
Wypisz trzy najważniejsze informacje.
Nie modyfikuj pliku.
~~~

Utwórz `ai_integration.md`:

~~~markdown
# Integracja AI

## Użyta usługa

...

## Cel

...

## Zakres danych

...

## Prompt

...

## Wynik

...

## Jak sprawdziłem wynik?

...

## Czy AI wykonało akcję zapisu?

tak / nie
~~~

Jeśli nie masz dostępnej integracji, opisz jeden scenariusz i wymagane uprawnienia.

---

## Zadanie 6. Automatyzacja plików

Utwórz:

~~~text
automation/
~~~

Następnie:

~~~bash
seq 1 100 > automation/data.txt
~~~

Utwórz `automation/report.sh`:

~~~bash
#!/usr/bin/env bash

file="automation/data.txt"

lines=$(wc -l < "$file")
sum=$(awk '{s += $1} END {print s}' "$file")
first=$(head -n 1 "$file")
last=$(tail -n 1 "$file")

echo "file=$file" > automation/report.txt
echo "lines=$lines" >> automation/report.txt
echo "sum=$sum" >> automation/report.txt
echo "first=$first" >> automation/report.txt
echo "last=$last" >> automation/report.txt
~~~

Uruchom:

~~~bash
bash automation/report.sh
~~~

`automation/report.txt` ma zawierać:

~~~text
file=automation/data.txt
lines=100
sum=5050
first=1
last=100
~~~

### Sprawdzenie

Automat będzie mógł ponownie uruchomić skrypt i porównać wynik.

---

## Zadanie 7. Security check

Utwórz `security_check.md`:

~~~markdown
# Security check

- [ ] brak prywatnych kluczy SSH
- [ ] brak haseł
- [ ] brak tokenów
- [ ] brak kluczy API
- [ ] brak prywatnych linków do chmury
- [ ] brak prawdziwych danych osobowych
- [ ] integracje mają opisany zakres uprawnień
~~~

Dopiero po sprawdzeniu zmień `[ ]` na `[x]`.

Odpowiedz też:

> Co zrobić, jeśli sekret został przypadkowo zapisany w publicznym repozytorium?

Odpowiedź powinna wspomnieć o **unieważnieniu lub zmianie sekretu**, a nie tylko usunięciu pliku.

---

## Zadanie 8. README bloku

Utwórz `README.md`.

Powinien zawierać:

- podsumowanie pracy mobilnej,
- link do `mobile_report.md`,
- link do `ssh.md`,
- link do `cloud.md`,
- link do `integration_audit.md`,
- link do `ai_integration.md`,
- wynik automatyzacji,
- link do `security_check.md`,
- checklistę wszystkich zadań.

Dodaj tabelę:

~~~markdown
| Obszar | Główna zasada |
| --- | --- |
| telefon | małe zadania, nie ciężka edycja |
| SSH | prywatny klucz pozostaje prywatny |
| chmura | sprawdź uprawnienia |
| integracje | najmniejsze potrzebne uprawnienia |
| automatyzacja | najpierw zrozum proces, potem automatyzuj |
~~~

---

# Checklista końcowa

Przed zgłoszeniem bloku sprawdź:

- [ ] `mobile_edit.md` istnieje,
- [ ] wykonano commit `09: mobile edit`,
- [ ] `mobile_report.md` opisuje pracę mobilną,
- [ ] `ssh.md` rozróżnia klucz publiczny i prywatny,
- [ ] w repozytorium nie ma prywatnego klucza SSH,
- [ ] `cloud.md` opisuje poziomy dostępu,
- [ ] `integration_audit.md` opisuje dwie integracje,
- [ ] `ai_integration.md` dokumentuje zadanie lub scenariusz,
- [ ] `automation/data.txt` zawiera liczby od 1 do 100,
- [ ] `automation/report.sh` uruchamia się bez błędu,
- [ ] `automation/report.txt` zawiera `sum=5050`,
- [ ] `security_check.md` został sprawdzony,
- [ ] `README.md` zawiera linki i checklistę.
