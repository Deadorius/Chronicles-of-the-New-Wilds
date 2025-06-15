label tavern_argument:
    "Usiedliśmy wszyscy wspólnie przy okrągłym, drewnianym stole. Stanowiliśmy całkiem niezły widok. Jeszcze sam nie widziałem tak różnorodnej i ekscentrycznej grupy podróżnych, a tym bardziej do nich nie należałem."
    kicha "Dobra."
    "Kicha siedział zamyślony nad swoim rozpadającym się notatnikiem, gryząc koniec złamanego w połowie ołówka."
    kicha "Mamy w tej chwili dwie możliwości. Zostajemy tutaj jeszcze trochę, ogarniamy nasze zapasy żywności, jakość sprzętu oraz broni i sprawdzamy, co nam takiego brakuje w ekwipunku. Wyśpimy się w kwaterach i wyruszymy o poranku."
    kicha "Alternatywą jest wyjście od razu, co ma też swoje plusy i minusy…"
    oliv "Bla bla bla. – Oliv, już widocznie zniecierpliwiona, zaczęła rysować nożem po granicy stołu – Natura ma wystarczająco dużo do zaoferowania, nie musimy tutaj siedzieć i trząść portkami."
    oliv " A może boisz się, że masz za mało gaci na zmianę?"
    "Chytry uśmieszek pojawił jej się na twarzy."
    mariusz "Też się zgadzam z Oliv – zagrzmiał Mariusz, waląc pięścią w stół. – Przygoda nie przeżyje się sama. Jesteśmy mądrzy i zaradni, na pewno poradzimy sobie bez tego, wybacz mi Kiszko, ale przynudnawego planowania."
    "Kicha zmierzył ich oboje piorunującym wzrokiem, co o dziwo wystarczyło, aby ponownie zwrócili na niego uwagę."
    "Może najpierw dacie mi dokończyć swoją myśl?"
    "Po chwili ciszy spojrzał ponownie w swoje notatki i wrócił do swojego wywodu."
    "Miałem właśnie powiedzieć, że natychmiastowe wyjście także nie jest złą propozycją, bo po drodze powinniśmy zdążyć znaleźć odpowiednie schronienie, co da nam bezpieczeństwo i przewagę właśnie ze zbieraniem ewentualnych brakujących zasobów."
    "Niesie to ze sobą mimo wszystko ryzyko wymyślania pewnych rozwiązań na poczekaniu, będąc jednocześnie bez wystarczającej ilości snu, co może nam utrudnić podróż na dłuższą metę… Pewnie wiecie już, że jestem bardziej za pierwszym wariantem."
    oliv "Nie zmienię już zdania – powiedziała Oliv pewnym siebie głosem. – Tylko Zachary jeszcze nie podzielił się swoją opinią. Jako kartograf był już pewnie w wielu dziwnych miejscach i wie, co będzie nam mniej więcej potrzebne."
    oliv "Damy sobie radę."
    mariusz "Moja pobratymka dobrze prawi!"
    mariusz "Nie możemy pozwolić na to, aby nasze serca oddały się odruchom strachu i chowały się jak łucznicy trwożliwi, co w cieniu baszty chronią się przed gniewnym spojrzeniem wroga, zamiast stanąć z mieczem jak rycerze chwalebni!"
    kicha " "
    mariusz "Emmm… ekhem… Muszę jednakże zwrócić honor memu giermkowi, ponieważ niejednokrotnie jego błyskotliwe podejście do podróży uratowało nas przed pochopnymi decyzjami, więc jeśli Zachary przechyli szalę w stronę pierwszego planu, to także się ugnę."
    "Informuje ugodowo Mariusz, siadając z powrotem na miejscu, splatając ze sobą dłonie na stole i kierując wzrok posłusznie w dół."
    "Widziałem, że Kicha nie czuje się do końca komfortowo z nazwą giermka, ale pewnie nie chciał zaprzepaścić wsparcia Mariusza. Dał mu jedynie kuksańca w ramię"
    kicha "To jak Zachary, co o tym myślisz?"
    menu:
        "Z kim się zgadzasz?"
        "Z Kichą":
            jump kicha_agree
        "Z Mariuszem i Oliv":
            jump mariusz_agree

    
label kicha_agree:
    player "Sądzę, że warto spędzić chwilę na przygotowaniu się i odpoczynku. Lepiej się już teraz przygotować, niż potem żałować."
    player "W lasach i na mokradłach robi się coraz niebezpieczniej, zachowajmy wszelkie środki ostrożności. Jeśli się wyśpimy, szybciej dotrzemy do celu."
    "Kicha westchnął z ulgą, Mariusz nie skomentował mojego wyboru, a Oliv prychnęła."
    oliv "Ale nuda. Idę się przewietrzyć."
    show oliv_img:
        subpixel True 
        ypos -458 
        linear 0.20 ypos -669 
    oliv "Od tych wszystkich pijaków i ich wyziewów zaczyna robić mi się niedobrze."
    hide oliv_img with moveoutright
    "Oliv wstaje gwałtownie od stołu i rusza jak taran do drzwi wyjściowych. Nim całkiem znika za progiem, odwraca jeszcze do nas głowę. Nadal trzyma w ręce nóż."
    oliv "Słodkich snów trzęsiportki."
    "Gdy wyszła, zapadła chwilowa niezręczna cisza. Można było się w sumie spodziewać podobnej reakcji, ale nie w takim natężeniu."
    kicha "Nie wiem, czy przyjęcie jej do naszej grupy było dobrym posunięciem. Swoim wybuchowym temperamentem może w przyszłości narobić nam kłopotów."
    mariusz "Jest trochę porywcza, ale jej umiejętności walki i samoobrony są godne podziwu. Ma też świetny instynkt przetrwania i umie szybko podejmować decyzje."
    mariusz "Jest jak… Joanna d’Arc! Wojowniczka z sercem lwa i wiarą niezłomną."
    mariusz "Prowadzona przez boskie wizje, przekonała Karola VII, by dał jej oręż, i wiodła francuskie wojska ku zwycięstwu, przełamując oblężenie Orleanu."
    mariusz "Kto przeciw niej stanie, niech wie, iż mierzy się z duchem niezłomnym, zahartowanym w płomieniach bitew i przeznaczonym do wielkich czynów."
    "Razem z Kichą patrzyliśmy się przez chwilę na Mariusza w ciszy, nie wiedząc, co mu na to odpowiedzieć."
    player "Absolutnie nie wiem, o kim mówisz i skąd to wiesz, ale… faktycznie brzmi jak dzielna wojowniczka."
    kicha "Musisz się przyzwyczaić. Mariusz ma w zwyczaju przywoływać postaci z ksiąg o starym świecie."
    "Po zjedzeniu do końca kolacji, wzięliśmy od właścicielki karczmy klucze do pokoi i skierowaliśmy się do nich na górę."
    jump act2
    

label mariusz_agree:
    player "W dzisiejszym świecie wszystko zmienia się w mgnieniu oka. Możemy się teraz przygotować na to, co znamy, ale gdy tylko pojawi się jakaś nowa przeszkoda, szybko na niej polegniemy." 
    player "Najważniejszy jest instynkt i kreatywność, na pewno sobie z nimi poradzimy."
    "Kicha wzdychał niezadowolony, gdy Oliv z Mariuszem nakręcali się wzajemnie na “przygodę życia”."
    kicha "Tylko nie mówcie mi potem, że was nie ostrzegałem. Musimy być ostrożni i rozglądać się za *nazwa zioła*, *nazwa rośliny leczniczej* oraz *nazwa jadalnej rośliny*, jeśli chcemy przetrwać choć jedną noc na naszym prowiancie."
    oliv "Nie kitraj się tak Kicha, upoluję nam jakiegoś *nazwa zmutowanego królika albo coś*, upiekę go wieczorem na naszym *kempingu* i z pełnymi ustami na pewno nie będziesz już marudzić."
    show mariusz_img:
        subpixel True 
        ypos 80 
        linear 0.10 ypos -2
    "Widać było, że Mariusz jest już cały nabuzowany. Wstał energicznie z pięścią uniesioną ku górze."
    mariusz "Wyruszajmy zatem przyjaciele, przygoda czeka!"
    show kicha_img:
        subpixel True 
        zpos -384.0 
        linear 0.15 zpos -307.0 
        linear 0.15 zpos -381.0
        linear 0.15 zpos -307.0 
        linear 0.15 zpos -381.0 
    "Mariusz podszedł do Kichy i, wyszczerzony od ucha do ucha, poklepał go po plecach."
    mariusz "Nie martw się mój giermku, przeznaczenie jest po naszej stronie!"
    "Kicha przetarł oczy i próbował coś powiedzieć, ale poddał się w trakcie. Był już naprawdę zmęczony."
    "Po chwili Oliv i Mariusz wzięli mnie pod pachy z obu stron i wyszliśmy wspólnie z karczmy, żywiołowo rozmawiając o nadchodzącej wspólnej wędrówce."
    "Kicha, trochę naburmuszony, ociągał się za nami. Mimo wszystko czułem, że on także się cieszy, ale woli, jak sprawy wychodzą po jego myśli. W końcu się z tym pogodzi."
    jump act2