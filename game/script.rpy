# The game starts here.
# UUUUUUUUU
label start:
    scene burza1 with fade
    "Już parę godzin temu rozpętała się potężna burza śnieżna. Drobinki zamarzniętej wody uderzały mnie gwałtownie w twarz, przez co nie wiedziałem, gdzie idę."
    "Zgubiłem całkowicie drogę. Czułem potworne zmęczenie – nie czułem od zimna nóg, a każdy kolejny krok zlewał się z poprzednim. Nie wiedziałem już, czy to trwało 5 godzin czy może już pół dnia."
    "Powoli traciłem nadzieję, że znajdę w końcu jakiekolwiek schronienie, a zapadająca nieubłaganie noc napawała mnie grozą. Przede mną znajdowało się łagodne wzniesienie."
    "Gdy doczłapałem się na jego szczyt, moje serce nareszcie zabiło szybciej na widok migotliwego, ciepłego światła. Nabrałem nadziei i z zaróżowionymi polikami zwiększyłem tempo chodu."
    scene house with fade
    "Zbliżyłem się w końcu na tyle, że byłem w stanie określić czym była ta delikatna poświata. Stała przede mną niewielkich rozmiarów chata, z której wydobywał się gwarny dźwięk rozmów, śmiechów i krzyków."
    scene tavern1 with fade
    "Wpadłem do środka zadyszany i cały oblepiony śniegiem, całkiem jak bałwan. Czułem, że zakłóciłem tym atmosferę tawerny, przez co gwar natychmiast ucichł."
    "Wszyscy z zaciekawieniem przyglądali mi się z większą lub mniejszą bezpośredniością. Otrzepałem się z resztek białego puchu i podszedłem do baru."
    menu:
        "Usiądź i zamów coś":
            "W zamian za garść ziół leczniczych, które zdołałem zebrać po drodze,  dostałem danie składające się z dwóch ugotowanych ziemniaków, dużego smażonego grzyba i posiekanych liści sałaty. Popijałem je piwem."
            "Rozejrzałem się wokoło – w tawernie znajdowało się mnóstwo ludzi z różnych zakątków i miast."
            "Uznałem, że musiałem się znaleźć na tak zwanym „Obszarze Handlowym”, czyli w miejscu, które nie należy do żadnego klanu ani grupy i służy głównie do handlu, ale nie tylko dobrami fizycznymi."
            "Życie z każdym dniem robi się coraz trudniejsze."
            "Można usłyszeć krążące wśród ludzi informacje o ciągle zmieniającym się klimacie, a co za tym idzie także fauna i flora wyskakują nieustannie z coraz to bardziej przerażającymi stworzeniami, na które trzeba uważać."
            "Jako nomada podróżuję w wieloosobowych grupach i wspólnie zajmujemy się zbieraniem informacji o terenie, znajdywaniem i tropieniem zapasów oraz zbieraniem ważnych w handlu materiałów."
            "Nie mamy konkretnego miejsca, które moglibyśmy nazwać domem, ale wspieramy się nawzajem i sprawiamy, że czujemy się własną rodziną, szczególnie, gdy często tej prawdziwej już dawno nie mamy."
            "Jest to dla mnie ważne, aby jeszcze tej nocy znaleźć osoby, które byłyby skłonne połączyć ze mną siły chociaż na parę dni. Dzisiaj miałem po prostu farta i podejrzewam, że jutro mogę go już tyle nie mieć."
            show cass-placeholder with dissolve:
                subpixel True pos (-0.19, 0.01) 
            "Z rozmyślań wyrywa mnie pojawienie się przede mną białowłosej barmanki, która ze znudzoną miną zaczęła wycierać blat przede mną."
            "Spojrzała przed siebie i wtedy nasze oczy się spotkały – przyjrzała mi się od góry do dołu, po czym zagadnęła:"
            none "Pierwszy raz Cię tutaj widzę."
            none "Ta karczma nie jest postawiona na głównym szlaku towarowym, więc niewiele osób do niej zagląda… Czyżbyś się zgubił?"
            "Barmanka stała przede mną z zadziornym uśmiechem, czekając na moją reakcję."
            player "Przyznaję, że nie była to łatwa przeprawa… Burza śnieżna złapała mnie znienacka, ale koniec końców nie wyszło mi to tak bardzo na złe."
            player "Nie znam tych rejonów, więc dobrze jest mieć jakiś punkt zaczepienia w postaci chociażby karczmy."
            "Wyjaśniłem swoją sytuację bez ogródek. Zmierzyła mnie od góry do dołu, próbując dociec, skąd mogę w takim razie być. Nie ciągnęła tematu, zapewne uznając, że nie jest to jej sprawa."
            none "Jeśli faktycznie tak słabo znasz te rejony, to lepiej, żebyś wziął ze sobą tę mapę."
            none "Nie jest może zbyt duża, sam będziesz musiał ją sobie aktualizować, ale będziesz miał przynajmniej pojęcie, gdzie się znajdujesz."
            player "Dziękuję… Nazywam się (Imię). Tak się właśnie składa, że jestem kartografem, więc na pewno sobie z tym poradzę."
            cass "Ahhh… czyli jesteś nomadem? Jeśli jesteś sam, to nic dziwnego, że miałeś na zewnątrz trudne chwile. Ja jestem Cass, tutejsza barmanka."
            cass "I żebyś nie myślał, że tę mapę dałam Ci za darmo… Pamiętaj o lepszej zapłacie, gdy już skończysz jeść."
            player "Jasne… Czy może wiesz, czy znajdują się tutaj jacyś inni nomadzi?"
            "Zapytałem się z nadzieją, że znowu nie będzie drążyć tematu, chociaż domyślałem się, że nie jestem zbyt subtelny. Samotny nomada pytający o innych swojego pokroju."
            "Wiadomo, że potrzebuję ich, aby stąd wyjść i nie zostać od razu pożartym lub otrutym przez czarny bluszcz."
            "Patrzyła się na mnie przez parę sekund i zrozumiałem, że nic nie jest tutaj za darmo."
            player "Oczywiście informacja zostanie sowicie opłacona."
            "Cass uśmiechnęła się pobłażliwie i wskazała prawy kąt karczmy."
            cass "Cieszę się, że w końcu się nauczyłeś, jak tutaj działamy, złotko."
            "Od razu wyciągnąłem wszystko na stół, co uznałem, że mogłoby się spodobać Cass jako zapłata. Przed nią znajdowało się pęk popularnych ziół, mała grudka soli oraz woreczek z nasionami buraka."
            "Cass przyjrzała się każdemu przedmiotowi, po czym spojrzała mi prosto w oczy."
            cass "Z chęcią wezmę wszystko ze stołu, ale nie potrzebuję aż tyle nasion, dlatego to akurat Ci podaruję. A teraz wybacz, mam innych klientów do obsłużenia."
            "Informacje od niej słono mnie kosztowały, ale wiadomo, że nie ma już nic na tym świecie za darmo."
            "Moja uwaga od razu zwróciła się ku rogu pomieszczenia, który wcześniej wskazała mi Cass."
            "Zobaczyłem trójkę osób siedzących samotnie przy trzech różnych stołach."
            "Czyżby los był nareszcie po mojej stronie?"
            "Zbierałem w sobie przez chwilę odwagę do wstania i wykonania swojego planu."
        "Zagadaj do barmanki":
            show cass-placeholder with dissolve:
                subpixel True pos (-0.19, 0.01) 
            "Zauważyłem pracującą przy barze białowłosą barmankę, która ze znudzoną miną wycierała jeden z wielu niedaleko leżących brudnych kufli."
            player "Cześć! Totalnie zmarzłem po drodze. Dobrze, że trafiłem na waszą tawernę."
            "Zarzuciłem pod koniec szybki uśmiech."
            none "...hej. Jeśli podróżujesz sam, to faktycznie miałeś szczęście. Czyżbyś zgubił towarzyszy po drodze?"
            "Zapytała mnie z zadziornym wzrokiem."
            player "haha… wszyscy zgodnie uznaliśmy, że lepiej będzie, jeśli znajdziemy własne ścieżki."
            "Nerwowo potarłem dłońmi uda z nadzieją, że nie będzie drążyć tematu. Nadal robię się trochę drażliwy, gdy o tym myślę."
            none "I twoja akurat zaprowadziła Cię do tej speluny? Ciekawe…"
            "Zmierzyła mnie z góry do dołu. Nie byłem w stanie odgadnąć, o czym teraz myśli."
            none "Słuchaj, brzmisz na uroczego chłopaka, który potrzebuje pomocy, a tak się właśnie składa, że mam dzisiaj dobry humor."
            "Wyciągnęła z szafki za nią rulon papieru i położyła na blacie przede mną."
            none "To jest mapa Obszaru Handlowego, na którym się teraz znajdujemy. Pewnie to wiesz, że otaczają go z każdej strony różne klany i podupadłe miasta. Możesz w trakcie swojej podróży ją sobie uzupełniać, jeśli masz wystarczające umiejętności."
            "Uśmiechnąłem się od ucha do ucha. Nie sądziłem, że spotkam tutaj takiego dobrego człowieka. Może faktycznie miała po prostu dobry dzień, ale nie będę tego testować i przyjmę prezent z pokorą."
            player "Dziękuję! To na pewno ułatwi mi zapoznanie się z terenem. Akurat tak się składa, że wiem o mapach to i owo – z tym sobie poradzę."
            player "A co macie dzisiaj dobrego do zjedzenia? Umieram z głodu po takiej wyprawie."
            none "Przez śnieżycę nie dostaliśmy dostawy składników, więc mogę zaproponować Ci jedynie gulasz z grzybami i smażonym burakiem. Do picia polecam trunek z dzikiej róży – trochę Cię rozgrzeje."
            "Wyciągnąłem woreczek z grudkami soli na bar i gdy miałem zamiar sięgnąć po inne przydatne materiały do zapłaty, barmanka mi przerwała."
            none "Spokojnie, sól wystarczy. Jej najbardziej nam brakuje, dlatego więcej już nie wyciągaj. Zaraz podam Twoje zamówienie."
            "Po chwili dostałem parujące i smacznie pachnące danie. Zajadałem się potrawą i jednocześnie rozglądałem się po tawernie. Znajdowało się w niej mnóstwo ludzi z różnych zakątków i miast."
            "Jak już barmanka wspomniała, znajduję się na tak zwanym „Obszarze Handlowym”, czyli w miejscu, które nie należy do żadnego klanu ani grupy i służy głównie do handlu, ale nie tylko dobrami fizycznymi."
            "Życie z każdym dniem robi się coraz trudniejsze. Można usłyszeć krążące wśród ludzi informacje o ciągle zmieniającym się klimacie, a co za tym idzie także fauna i flora wyskakują nieustannie z coraz to bardziej przerażającymi stworzeniami, na które trzeba uważać."
            "Jako nomada podróżuję w wieloosobowych grupach i wspólnie zajmujemy się zbieraniem informacji o terenie, znajdywaniem i tropieniem zapasów oraz zbieraniem ważnych w handlu materiałów."
            "Nie mamy konkretnego miejsca, które moglibyśmy nazwać domem, ale wspieramy się nawzajem i sprawiamy, że czujemy się własną rodziną, szczególnie, gdy często tej prawdziwej już dawno nie mamy."
            "Jest to dla mnie ważne, aby jeszcze tej nocy znaleźć osoby, które byłyby skłonne połączyć ze mną siły chociaż na parę dni. Dzisiaj miałem po prostu farta i podejrzewam, że jutro mogę go już tyle nie mieć."
            "Nie mogę tutaj siedzieć bez końca. Jak tylko skończę posiłek, przejdę się po karczmie i, kto wie, może nawiążę nowe znajomości?"
    hide cass-placeholder with dissolve
    "Gdy już miałem zamiar się podnieść, pewien już całkiem podchmielony bywalec tawerny trzasnął dłonią o stół i wstał."
    "Cała sala od razu zwróciła na niego uwagę, ciekawa, co dalej się wydarzy."
    "Mężczyzna w już znaczącym wieku i z wyszczerbioną szczęką rzucał słowami na lewo i prawo. Ludzie zebrali się wokół niego, tworząc ciasny krąg."
    oldman "Mówię wam! Tam się dzieją rzeczy, o których w życiu wam się nie śniło!"
    audience "Tak, tak. Gadaj sobie staruszku…"
    oldman "Klnę się na swoje towary, że nie zmyślam! Słyszałem nawet krążącą legendę, która mówi, że korzystają z pradawnego artefaktu… a teraz jej wysłuchajcie."
    oldman_nvl "Nie tak daleko stąd, za lasem"
    oldman_nvl "Bagno kryje się pod czasem."
    oldman_nvl "Mroczne, pełne tajemnicy,"
    oldman_nvl "Gdzie spokoju nikt nie liczy."
    oldman_nvl "Ludzie w ruinach swe dni pędzą,"
    oldman_nvl "W cieniu strachu życie wstrętne."
    oldman_nvl "Nieznane istoty wciąż krążą,"
    oldman_nvl "Jak sępy nad miastem się wciąż zmożą."
    oldman_nvl "Nikt nie śmie z kryjówki wyjść,"
    oldman_nvl "Bo z bagien złe moce chcą ich gryźć."
    oldman_nvl "Lecz broń ukryta w rękach szamanów,"
    oldman_nvl "Chroni przed zgubą tych z bagien szatanów."
    oldman_nvl "Artefakt ze starego świata,"
    oldman_nvl  "Zło odpędza, gdy mrok ich oplata."
    audience "Czyżby mówił prawdę?"
    audience "Ale to w takim razie o jaki artefakt chodzi?!"
    audience "Czy można go zdobyć?"
    audience "Staruszku, no powiedz wreszcie, o jaki artefakt chodzi?"
    oldman "Już spokojnie, wiem, wiem. Jak tak bardzo chcecie to powiem. Mówi się, że artefakt ten to (rzyg)."
    "Staruszek zatoczył się z powrotem na krzesło i zasnął pijackim snem."
    "Tłum, zawiedziony brakiem odpowiedzi, rozrzedza się i jedynie nieliczni pozostali w obrębie stołu, rozmawiając ze sobą o przemowie starca."
    "Pierwszy raz w życiu słyszałem o takiej legendzie. Nie jestem pewny, czy aby nie były to jedynie majaki pijanego staruszka, ale warto popytać się ludzi obok, czy może sami czegoś na ten temat nie wiedzą."
    menu:
        "Kicha":
            pass
        "Mariusz":
            pass
        "Oliv":
            pass





 
    return
