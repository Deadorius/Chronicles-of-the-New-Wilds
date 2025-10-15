label meeting_kicha:
    show kicha_img with moveinbottom:
        ypos -487
        xpos -0.13
        zpos -1500.0
        zoom 0.83
    "Zima dawała mu się we znaki – widać było, że jego skóra już dawno nie widziała słońca. Stał najbliżej ściany i, zamyślony, dłubał ołówkiem w ustach, a w drugiej ręce trzymając notatnik."
    show mariusz_img with moveinbottom:
        ypos -252
        xpos -1264
        zpos -517.0
    "Stał obok niego wysoki mężczyzna z jasnymi włosami i wydawało mi się, że otaczała go nadzwyczajnie przyjazna aura."
    hide mariusz_img with moveoutleft
    "Ten niższy wysłał po coś tego wyższego do baru i od razu było widać, że mu ulżyło."
    "Blondyn przy barze od razu rozpoczął konwersację z barmanką, więc widać, że jadaczka raczej mu się nigdy nie zamyka. Zaczynam współodczuwać ból jego kompana."
    show kicha_img with moveinbottom:
        ypos -487 xpos -0.13 zpos -1500.0 zoom 0.83

        linear 1.00 pos (-0.19, -252) zpos -384.0
    "Podchodzę po cichu do zamyślonego mężczyzny, który widocznie znajduje się teraz w swoim świecie."
    none "*szeptem* Jeśli przejdziemy przez mokradła, a potem …, ale jeśli po drodze napotkamy Warkożmija, to musimy zaopatrzyć się w …"
    player "Cześć, jestem Zachary!"
    show kicha_img:
        subpixel True 
        ypos -252 
        linear 0.1 ypos -639 
        linear 0.1 ypos -252 
    "Nieznajomy podskoczył w miejscu, przez co prawie wypuścił z rąk swój notatnik. Spojrzał na niego jak na szaleńca i zmierzył wzrokiem od stóp do głów."
    none "… czy mogę w czymś pomóc?"
    "Poprawił odruchowo okulary i czekał niepewnie na moją odpowiedź."
    player "Widziałem, że byłeś zainteresowany legendą, którą opowiadał tamten pijany starzec. Wiesz może o niej coś więcej?"
    none "Wow… jesteś całkiem bezpośredni. Mam wrażenie, że nie będzie to działać zawsze na twoją korzyść."
    player "Hahah… wiesz, to wszystko dlatego, bo szanuję twój czas i nie chcę go marnować na jakieś bezsensowne konwenanse."
    none "Okej, szanuję to. W takim razie, odpowiadając na twoje pytanie, tak, to prawda."
    none "Od dawna prowadzę badania o plemieniu, które świetnie się dostosowało do miejscowego środowiska, ale nie wiedziałem, że znajdują się akurat za bagnem. Muszę dostosować nasze plany do nowych informacji."
    player "Ciekawe… staruszek faktycznie wspominał o bagnie w swoim wierszu. Jeszcze nie poznałem osoby, która zapuszczałaby się w tamte rejony. Jest to nadal nieznany teren dla wielu kartografów, niestety także i dla mnie."
    none "W takim razie świetnie się składa, bo potrzebujemy kogoś, kto zna się na mapach, na pewno możemy przedyskutować wspólnie ten temat. Ja mam dość słabą orientację w terenie, a mój kompan… no cóż… powiedzmy, że nadaje się tylko do zabijania potworów."
    show mariusz_img with moveinbottom:
        pos (-961, 80) zpos 322.0 
    "Nagle, jak na zawołanie, podchodzi do nas wspomniany przed chwilą szeroko uśmiechnięty człowiek - w jednej ręce z piwem, a w drugiej ze szklanką wody"
    none "Kicha! Mój dobry druhu! Wziąłem twój ulubiony napój, nie musisz dziękować. Ah! A któż to stoi tutaj przed nami?"
    "Mam wrażenie, że blask jego uśmiechu i osobowość rozjaśnia przestrzeń wokół niego. Podaje mi rękę i tak mocno ściska moją, że już nie wiem, czy moje palce są jeszcze do użytku."
    mariusz "Jam jest Mariusz, we własnej osobie. Mam nadzieję, że mój przyjaciel także odpowiednio ci się przedstawił, czasami niestety zapomina o manierach."
    player "Jeśli dobrze zrozumiałem, to nazywa się Kicha."
    mariusz "Pamięć cię nie myli, mój przyjacielu!"
    "Widać, jak powieka Kichy drga i stara się mimo wszystko zachować spokój."
    kicha "Tak, Zachary przyznał się, że jest kartografem i że też jest zainteresowany tak zwaną Wioską Obłąkanych."
    mariusz "Czyżbyśmy zyskali nowego towarzysza?!"
    "Powiedział to z nieukrywanym entuzjazmem i położył przy tym swoją rękę na moim ramieniu."
    mariusz "Z nami czekają cię takie przygody, o których nawet byś nie śnił!"
    kicha "Mariusz, proszę cię, nie wieszaj się tak na nim, jeszcze złamiesz mu kark tą swoją wielką łapą. W dodatku - nie możemy zapraszać do naszego zespołu każdej osoby, która do nas podejdzie."
    mariusz "Musisz także pamiętać mój drogi giermku, że kartografowie są bardzo trudni do zdobycia, nie ma ich zbyt wielu, ponieważ jest to całkiem trudna profesja. Możliwe, że jest naszą jedyną opcją."
    kicha "Wiem, że wybór jest całkiem skromny, ale poznajmy może tego człowieka trochę lepiej, zanim zaproponujemy mu miejsce u nas."
    "Dodał także szeptem:"
    kicha "…A może jest mordercą?"
    player "Hej, emmm… ja was słyszę."
    jump common_meeting




label meeting_mariusz:
    "work in progress"

label meeting_oliv:
    show oliv_img with moveinbottom:
        ypos -471
        xpos -995
        zpos -637.0
    "Zbliżyłem się do rudowłosej dziewczyny, która bawiła się nożem motylkowym."
    "Nogi miała oparte na stole, a obok nich stał do połowy pełny kufel z alkoholem."
    "Odpychała się nogami od stołu, wprawiając krzesło w lekkie kołysanie. Wyglądała na znudzoną. Zanim zdążyłem się odezwać wbiła swój nóż w stół obok dłoni mężczyzny, który za bardzo zbliżył się do jej kufla."
    none "Kurwa staraj się palców nie stracić."
    none "Uważaj kurwa na palce."
    "Mężczyzna wstał gwałtownie, mamrocząc obelgi pod nosem. Zataczając się poszedł na  poszukiwania innego stolika."
    player "Em… przepraszam…"
    "Dziewczyna spojrzała w moją stronę. Wyciągnęła nóż ze stołu i zaczęła się nim bawić nie przerywając kontaktu wzrokowego."
    none "Co tam?"
    "Zmierzyła mnie wzrokiem i przekrzywiła głowę"
    none "Wyglądasz na spiętego."
    "Spojrzałem na dziurę w stole, pozostałość po wybryku dziewczyny. Powędrowałem wzrokiem z powrotem do jej noża. Zdawała się nie pojmować, co wywołało u mnie lekki niepokój."
    player "Ciężka podróż. Śnieżyca, mróz. Takie tam."
    none "Ah! Nowy! Choć, kurwa, siadaj!"
    "Rozpromieniła się i zdjęła nogi ze stołu. Poklepała tył pustego krzesła znajdującego się obok niej."
    "Uśmiechnąłem się nerwowo i zająłem wskazane wcześniej miejsce. Przyznaję, że nóż był dobrym argumentem."
    oliv "Oliv. No, to co cię tu sprowadza?"
    "Przechyliła głowę i z zainteresowaniem zmierzyła mnie wzrokiem. Przysunęła się do mnie nie dając mi odpowiedzieć, ani się przedstawić."
    
    nvl clear
    show oliv_img:
        zpos -560  
    oliv "Fajne wdzianko.{w=0.25}{nw}"
    show oliv_img:
        zpos -500
    oliv "Z daleka przybywasz?{w=0.25}{nw}"
    show oliv_img:
        zpos -440
    oliv "Jesteś nomadą, tak?{w=0.25}{nw}"
    show oliv_img:
        zpos -380
    oliv "Gdzie posiałeś resztę swojej grupy?{w=0.25}{nw}"
    show oliv_img:
        zpos -320
    oliv "Dokąd zmierzacie?{w=0.25}{nw}"
    show oliv_img:
        zpos -260
    oliv "Czym się zajmujesz?{w=0.25}{nw}"
    show oliv_img:
        zpos -200
    oliv "Mapami, tak?{w=0.25}{nw}"
    show oliv_img:
        zpos -100
    oliv "Nie patrz tak na mnie, z kieszeni ci wystaje.{w=0.25}{nw}"
    "Mrugnąłem kilka razy, przez chwilę przytłoczony ilością pytań i nagłym ożywieniem dziewczyny. Zerknąłem na mapę, która faktycznie wystawała mi z kieszeni." 
    "Mój wzrok powędrował do drzwi tawerny, wspomnienia moich wcześniejszych podróży zalały mój umysł. Westchnąłem i spojrzałem ponownie na dziewczynę."
    player "To… długa historia. Tak, jestem nomadą. Aktualnie podróżuje no… sam. I tak, jestem kartografem. A na imię mam Zachary."
    show oliv_img with move:
        zpos -50
    "Dziewczyna przysunęła się jeszcze bliżej, jej oczy błyszczały z podekscytowania."
    oliv "Kurwa, długie historie są najlepsze! No gadaj."
    "Wzięła długi łyk z kufla."
    oliv "Opowiadaj.{w=0.25}{nw}"
    oliv "Sam?{w=0.25}{nw}"
    oliv "Jak to sam?{w=0.25}{nw}" 
    oliv "Nie możesz być sam.{w=0.25}{nw}" 
    oliv "Jesteś nomadą.{w=0.25}{nw}"
    oliv "Podróżowanie samemu to-{w=0.25}{nw}"
    "Zaczęło mi się kręcić w głowie od tych jej ciągłych pytań. Nie chciałem myśleć o przeszłości. Nie chciałem myśleć o tym dlaczego znalazłem się w tej tawernie. Nie chciałem myśleć dlaczego jestem sam. Przerwałem jej."
    player "Słuchaj ja chcę się tylko dowiedzieć czy zrozumiałaś coś z tej wcześniejszej opowiastki? No wiesz, tej o ludziach w ruinach i szamanach."
    "Dziewczyna zamilkła na chwilę."
    oliv "Ah… jedna z tych długich historii"
    "Jej wzrok stał się mętny, jakby pogrążyła się we wspomnieniach. Znałem ten stan zbyt dobrze. Wzięła kolejny długi łyk z kufla. Odstawiła go z hukiem na stół. Po wcześniejszej melancholii nie zostało śladu."
    oliv "Powiadasz, że interesuje cię legenda."
    "Dziewczyna wróciła do bawienia się nożem motylkowym. Nie drążyłem tematu wcześniejszej zmiany nastroju. Nie jestem odpowiednią osobą, do poruszania takich tematów. Nie w tym momencie. Z resztą byłaby to kompletna hipokryzja z mojej strony."
    player "Tak. Legenda."
    oliv "Dziewczyna powróciła do swojego wcześniejszego podekscytowania."
    oliv "Za dużo to ja nie wiem. Ale widziałam już kiedyś artefakty ze starego świata. Wiesz, technologia sprzed apokalipsy nie została w całości stracona. Na przykład u nas korzystało się z falówek."
    player "Z czego?"
    oliv "Takich pudełek, dzięki którym można się porozumiewać na odległość."
    "Myśl o pudełkach, które pozwalają porozumiewać się na odległość zdawała się rozsadzać mi umysł."
    player "Zaraz, zaraz… to skąd ty jesteś?"
    "Dziewczyna zawahała się przez chwilę, ale szybko odzyskała swój standardowy entuzjazm."
    oliv "City Preppers."
    "Ponownie spojrzałem na nią z wytrzeszczonymi oczami."
    player "City Preppers? Serio? Jak tam jest?"
    "Tym razem to ona musiała mi przerwać."
    oliv "Długa historia."
    "Spojrzała na mnie wymownym wzrokiem, przywołując moje wcześniejsze słowa."
    "Westchnąłem lekko poirytowany. Chciałem wiedzieć więcej. Nigdy nie byłem w tamtejszych terenach. Ostatecznie rzuciłem temat."
    player "No dobra, a te artefakty? Myślisz, że mogłaś kiedyś używać artefaktu z legendy i nawet o tym nie wiedzieć?"
    "Dziewczyna wyglądała na wdzięczną za zmianę tematu."
    oliv "W sumie to całkiem możliwe."
    "W tym momencie rozpromieniła się i spojrzała na mnie. Uśmiechała się szeroko. Im dłużej tak na mnie patrzyła tym bardziej przypominała szaleńca."
    oliv "To co? Idziesz ze mną?"
    "Mrugnąłem."
    player "Ale, że do miejsca z legendy?"
    oliv "No tak! Idealna przygoda! No dawaj!"
    "Usłyszeliśmy brzdęk metalu i mamrotanie."
    none "Gdzie ty idziesz?! Mieliśmy iść do baru. Bar jest w drugą stronę."
    none "Ejże nie przesadzaj giermku! Choćże za mna. Nie! Do diabła, gdzieś ty się włóczysz?"
    none "Miałeś tak do mnie nie mówić."
    "Razem z Oliv powędrowaliśmy wzrokiem w kierunku dochodzących nas głosów."
    hide oliv_img
    show mariusz_img with moveinbottom:
        ypos -252
        xpos -1264
        zpos -517.0
    "Zauważyliśmy dwóch mężczyzn. Jeden z nich, blondyn, uśmiechał się do nas szeroko."
    show kicha_img with moveinbottom:
        ypos -487
        xpos -0.13
        zpos -1500.0
        zoom 0.83
    "Drugi, o kruczoczarnych włosach, miał na twarzy niezadowolony grymas i próbował zawrócić. Blondyn szybko złapał go za ubranie, udaremniając tym samym jego odwrót. Następnie zaciągnął go do naszego stolika."
    show mariusz_img:
        subpixel True 
        pos (-1264, -252) zpos -517.0 
        linear 1.00 pos (-961, 80) zpos 322.0 
    show kicha_img:
        subpixel True 
        pos (-0.13, -487) zpos -1500.0 
        linear 1.00 pos (-0.19, -252) zpos -384.0 
    show oliv_img:
        subpixel True ypos -458 zpos -708.0 
        xpos 880 
        linear 1.00 xpos -121 
    none"Witajcie dobrzy podróżnicy! Usłyszałem słowo “przygoda” i zanim żem się obejrzał już do Państwa lgnąłem!"
    none "Co ty wyprawiasz?"
    none "Witam się z naszymi nowymi towarzyszami!"
    "Blondyn nadal trzymał drugiego mężczyznę za ubrania. Z jego twarzy nie zniknął uśmiech. Drugi z nich westchnął, po czym zaczął masować swoje skronie."
    "Spojrzałem na Oliv zdziwiony, ale ona miała na twarzy równie wielki uśmiech co nasz rozmówca."
    oliv "Kurwa! Chcecie się do nas przyłączyć?!"
    "Dziewczyna podniosła głos z podekscytowania."
    player "Zaraz, zaraz… przyłączyć?"
    oliv "No do wyprawy oczywiście!"
    none "Tak, do wyprawy! A gdzie się właściwie wybieracie?"
    none "Czy mógłbyś chociaż raz podjąć jakąkolwiek decyzję PO otrzymaniu wszystkich informacji? Nie przed? Nie wiesz, gdzie oni idą i, patrząc na tego tutaj, on też nie jest pewny."
    "Czarnowłosy mężczyzna miał zamknięte oczy i ściskał pasek swojej sakwy, wyglądał jakby starał się uspokoić."
    none "Ah! No tak! Gdzież się podziały nasze maniery?"
    mariusz "Wołają na mnie Mariusz!"
    mariusz "A ten przyjemniaczek to Kicha."
    "Mariusz ukłonił się, a Kicha skinął lekko głową w naszym kierunku."
    oliv "Oliv. A on.. zaraz, jak ty miałeś na imię?"
    player "Zachary."
    mariusz "No! Toż już wszyscy się zaznajomiliśmy! To mówcie, gdzież ta się wybieracie?"
    oliv "Gadaliśmy o legendzie. Tej, co wcześniej opowiadał jeden z pijaków. Słyszeliście ją?"
    "Na te słowa Kicha, który do tej pory stał cicho, podniósł głowę."
    kicha "Tak, słyszeliśmy. To gdzieś na bagnach… cudowna fauna i flora. Rośliny, które ciężko spotkać gdziekolwiek indziej."
    kicha "Zawsze chciałem je zbadać osobiście."
    "Mariusz uradowany wkładem Kichy, klepnął go mocno w plecy. Kicha wydał z siebie jęk, po czym odsunął się od Mariusza."
    mariusz "To idealnie się składa! Ty sobie zbadasz swoje roślinki, a my rozwikłamy tajemnicę tych nieznanych istot!"
    "Kicha posłał Mariuszowi urażone spojrzenie, ale tamten kompletnie tego nie zauważył"
    player "W sumie brzmi jak ciekawy pomysł. Zrobiłbym mapy terenu… kto wie, może będę pierwszym kartografem, który nakreśli cały ten teren?"
    "Rozmarzyłem się trochę na tę myśl. Uśmiechnąłem się, poczułem ciepło w klatce piersiowej. Dawno nie czułem czegoś takiego. Nie od czasów podróży z moją dawną grupą."
    show oliv_img:
        xpos -121 ypos -458 zpos -708.0

        linear 0.25 xpos -121 zpos -708.0 ypos -720
    oliv "Czyli wszyscy są na tak! Zajebiście!"
    "Gwałtownie wstała przewracając krzesło."
    oliv "To co? Kiedy wyruszamy?"
    show tavern1 with fade
    jump tavern_argument








label common_meeting:
    "Dyskusję przerwał im lecący przed nosem kozik, aby następnie wbić się w ścianę pomiędzy mną a Kichą."
    kicha "Co jest! Jeszcze latających noży tu zabrakło. Kto to rzucił!"
    hide kicha_img
    hide mariusz_img
    with moveoutbottom
    show oliv_img with moveinbottom:
        pos (-121, -620) zpos -1276.0 
    "W tym samym momencie usłyszeliśmy za nami przewracane krzesła i wszechobecne oburzenie. Dziewczyna w niechlujnym wysokim kucyku przyszpiliła do ściany jakiegoś mężczyznę w średnim wieku."
    none "Nie zadzieraj ze mną, bo, uwierz mi, nie cofnę się przed niczym, aby zedrzeć ci z mordy ten uśmieszek."
    guy "Kurwa! argh… N-nie ujdzie ci to na sucho! Szef się dowie, co zrobiłaś i znowu skopiemy ci dupsko!"
    "Miotał tak się chwilę, aż w końcu puściła go i z łomotem runął na podłogę."
    none "Ta? I co mu powiesz? Że dziewczyna cię gnębiła? A jak mnie znajdziecie? Wy miastowi nie wytropicie nawet królika. A teraz znikaj mi z oczu, zanim naprawdę się wkurzę."
    "Mężczyzna wstał niepewnie i zrozumiał, że obserwuje ich prawie cała tawerna. Spojrzał ostatni raz groźnym wzrokiem na dziewczynę, po czym ostrożnie ruszył w stronę wyjścia."
    "Rudowłosa rozglądnęła się i w pewnym momencie spojrzała się właśnie na nas – ruszyła wtedy w naszą stronę"
    show oliv_img:
        pos (-121, -620) zpos -1276.0 
        linear 1.00 xpos -121 ypos -458 zpos -708.0
    none "O! Mój nóż. Tak się właśnie zastanawiałam, gdzie go wcięło."
    show kicha_img with moveinbottom:
        pos (-0.19, -252) zpos -384.0
        zoom 0.83
    kicha "Czy ty wiesz, że naraziłaś na niebezpieczeństwo wszystkich dookoła, rzucając nożem byle gdzie?! Czy nie wystarcza tobie fakt, że na zewnątrz grasują bestie, których nie jesteśmy sobie w stanie nawet wyobrazić?!"
    show mariusz_img with moveinbottom:
        pos (-961, 80) zpos 322.0 
    mariusz "Oj już się tak nie spinaj Kicha, przecież wylądował w ścianie, a nie w twojej głowie. Muszę przyznać że są to nie lada umiejętności łotrzyku."
    none "Dokładnie, typ wie, o co biega, więc nie dramatyzuj tak. Na pewno macie instynkt przetrwania, bo, jakimś cudem, jednak tutaj stoicie."
    "Patrzyła się na nas przez chwilę, gdy po chwili zauważyłem błysk zrozumienia w jej oczach."
    none "Chwila, czy to nie wy planujecie znaleźć miejsce ze wspomnianej lokalnej legendy?"
    kicha "Chcesz jeszcze powiedzieć, że nas podsłuchiwałaś?"
    none "Mariusz dał dosyć jasno do zrozumienia wszystkim przy barze, jakie macie plany…"
    "Kicha zmierzył morderczym spojrzeniem Mariusza, który złapał się za kark i zaczął delikatnie śmiać."
    player "W sumie nawet nawet nie wiemy, jak masz na imię."
    oliv "Nazywam się Oliv, do usług. Jestem początkującą nomadką, dlatego byłabym bardzo wdzięczna gdybyście wzięli mnie pod swoje skrzydła."
    "Oliv zrobiła słodkie wielkie oczy, co, przyznaję, prawie wymazało wszystkie moje wcześniejsze wątpliwości."
    kicha "Eeee… Sądzę, że jest to sprawa na pewno do przegadania. Myślę, że nasza współpraca może się udać, jeśli będziemy mogli sobie zaufać i dowiedzieć się, jakie mamy zamiary wobec odnalezienia Wioski Obłąkanych."
    "Kicha spojrzał na nas wyczekująco i wyciągnął notatnik. Poczułem się trochę spięty."
    oliv "Ja… *westchnięcie*. Potrzebuję po prostu odnaleźć artefakt z legendy."
    mariusz "Mój drogi giermku, czy naprawdę trzeba mieć powód do tego, aby iść na przygodę?"
    player "Tyle razy ci mówiłem, żebyś mnie tak nie nazywał-"
    mariusz "Już to widzę oczami wyobraźni: Ja, dzielny rycerz, mój giermek, kartograf oraz …"
    oliv "Umiem polować i znam się na walce."
    mariusz "Czyli skrytobójczyni wymierzająca własną sprawiedliwość."
    oliv "Może być."
    kicha "Mi zależy na odnalezieniu i dowiedzeniu się czegoś o nowych rasach, które przypominają ludzi."
    kicha "Niestety informacji na ich temat jest niewiele, a ludzie, którzy przeżyli z nimi spotkanie, często są ledwo kontaktujący. Ta legenda dała mi mały trop, który może mnie na nie naprowadzić."
    player "Ja po prostu potrzebuję nowej drużyny, żeby przetrwać…"
    "Aż mi głupio się zrobiło, że mam taki prosty powód."
    mariusz "Dobrze się składa! My potrzebujemy kompana!"
    kicha "Dobra, niech wam będzie. Nie mam już siły z wami walczyć, na coś się nadacie."
    oliv "Dobrze Panowie, skoro skończyliście się już przekomarzać jak baby na targu, może zdecydujemy teraz, jaki jest nasz następny krok."
    player "Dobrze by było pójść usiąść i to przegadać."
    oliv "To jak? Idziemy?"
    jump tavern_argument







