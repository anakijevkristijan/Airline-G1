# Airline-G1
Задача: Креирајте Djangо апликација за менаџирање на летови со балони (hot air ballon).
Секој лет се карактеризира со задолжителна шифра, име на кој аеродром полетува и на кој
аеродром слетува, корисник кој го креирал летот, фотографија за летот, информација со кој
балон се изведува летот, пилот на летот и авиокомпанија која го реализира летот. За секој
пилот се чуваат негово име и презиме, година на раѓање, вкупно часови налет и чин кој го
има во компанијата. За секој балон се чуваат типот на балонот, име на производителот на
балонот и максимален дозволен број на патници во балонот. За авиокомпанијата се чува
нејзиното име, година на основање и информација дали лета надвор од Европа или не.
Дополнително, за секоја авиокомпанија се чува информација за пилотите со кои
соработува. Еден пилот може да биде соработник на повеќе авиокомпании.
Дел 1:
Креирајте ги соодветните модели кои ви се потребни за да овозможите правилно
функционирање на системот.
Потребно е да овозможите додавање на објекти преку Админ панелот, со забелешка
дека пилотите-соработници на една авиокомпанија се додаваат во делот за авиокомпанија.
Притоа, во рамки на Админ панелот потребно е да ги обезбедите следните
функционалности:
- При креирањето на летот, корисникот се доделува автоматски според најавениот
  корисник
- Откако еден лет ќе биде дефиниран и зачуван, истиот може да се промени само
  од корисникот кој го креирал летот
- Не е дозволено бришење на летовите за ниту еден корисник
- За пилотите и авиокомпаниите во листата се прикажуваат само нивните имиња
  (и презиме за пилотот)
  Дел 2:
  Со користење на Bootstrap рамката креирајте 2 темплејти за приказ на информациите
  од системот. Соодветно:
- /index/ - приказ на општи информации за системот, прикажано на Слика1
- /flights/ - приказ на сите летови кои се креирани од најавениот корисник и
  полетуваат од аеродром Скопје. Во овој приказ дополнително се наоѓа и форма
  за додавање на нов лет, прикажано на Слика2
  Откако ќе го изработите системот, креирање .zip фајл во кој е сместен целиот проект
  со сите негови пропратни елементи. Базата на податоци во проектот останува онаа која е
  дефинира од страна на Django, SQLite. Креирајте неколку објекти од моделите за да ја
  тестирате нивната функционалности и истите нека останат во базата при прикачувањето.
  *Напомена: Ќе се прегледуваат само оние апликации кои успешно ќе компајлираат,
  односно серверот успешно ќе се стартува (доколку некоја функционалност не ви
  работи, подобро да ја избришете отколку да јавува грешка).
  Пријатна работа!