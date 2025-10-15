label storm:
    show storm2 with fade
    "Już parę godzin temu rozpętała się potężna burza śnieżna."
    "Drobinki zamarzniętej wody uderzały mnie gwałtownie w twarz, przez co nie wiedziałem, gdzie idę. Zgubiłem całkowicie drogę."
    "Czułem potworne zmęczenie – nie czułem od zimna nóg, a każdy kolejny krok zlewał się z poprzednim."
    "Nie wiedziałem już, czy to trwało 2 godziny, czy może już pół dnia."
    "Podróżowanie samemu było praktycznie wyrokiem samym w sobie, lecz nie miałem innego wyboru."
    "Moja poprzednia grupa rozpadała się na moich oczach – nie było sensu tego ciągnąć." 
    "Teraz muszę się skupić na jak najszybszym dotarciu do bezpiecznego miejsca oraz na znalezieniu nowych kompanów, którzy zapewniliby mi przeżycie w dziczy."
    "Powoli traciłem nadzieję, że znajdę jakiekolwiek schronienie, a zapadająca nieubłaganie noc napawała mnie grozą. Przede mną znajdowało się łagodne wzniesienie."
    hide storm2 with fade
    show storm1 with fade
    "Gdy doczłapałem się na jego szczyt, moje serce nareszcie zabiło szybciej na widok migotliwego, ciepłego światła na horyzoncie."
    "Nabrałem nadziei i z zaróżowionymi polikami zwiększyłem tempo chodu."
    "Zbliżyłem się w końcu na tyle, że byłem w stanie określić czym była ta delikatna poświata."
    hide storm1 with fade
    show outside_tavern with fade
    "Stała przede mną niewielkich rozmiarów chata, z której wydobywał się gwarny dźwięk rozmów, śmiechów i krzyków."
    hide outside_tavern with fade
    show tavern1 with fade
    "Wpadłem do środka zadyszany i cały oblepiony śniegiem jak bałwan. Czułem, że zakłóciłem tym wtargnięciem atmosferę tawerny, przez co gwar natychmiast ucichł."
    "Wszyscy z zaciekawieniem przyglądali mi się z większą lub mniejszą bezpośredniością."
    "Otrzepałem się z resztek białego puchu i podszedłem do baru."
    menu:
        "Siadasz i od razu zamawiasz, albo zagadujesz do barmanki."
        "Siadam i od razu zamawiam.":
            jump tavern_intro_1
        "Zagaduję do barmanki.":
            jump tavern_intro_2