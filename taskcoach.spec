Summary:	Task Coach - simple open source todo manager to manage personal tasks and todo lists
Summary(hu.UTF-8):	Task Coach egy egyszerű, nyílt forráskódú teendő-nyilvántartó
Summary(pl.UTF-8):	Task Coach - prosty zarządca osobistej listy zadań i rzeczy do zrobienia
Name:		taskcoach
Version:	1.3.5
Release:	1
Epoch:		1
License:	GPL v3
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/taskcoach/TaskCoach-%{version}.tar.gz
# Source0-md5:	22c4eb0809a808cb8dd4dc994b2cc078
Patch0:		%{name}-desktop.patch
URL:		http://www.taskcoach.org/
BuildRequires:	python-devel
BuildRequires:	python-wxPython-devel
BuildRequires:	rpm-pythonprov
Requires:	python-wxPython
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Task Coach is a simple open source todo manager to manage personal
tasks and todo lists. Task Coach currently has the following features:

- Creating, editing, and deleting tasks and subtasks.
- Tasks have a subject, description, priority, start date, due date, a
  completion date and an optional reminder. Tasks can recur on a daily,
  weekly or monthly basis.
- Tasks can be viewed as a list or as a tree.
- Tasks can be sorted by all task attributes, e.g. subject, budget,
  budget left, due date, etc.
- Several filters to e.g. hide completed tasks or view only tasks that
  are due today.
- Tasks can be created by dragging an e-mail message from Outlook or
  Thunderbird onto a task viewer.
- Attachments can be added to tasks, notes, and categories by dragging
  and dropping files, e-mail messages from Outlook or Thunderbird, or
  URL's onto a task, note or category.
- Task status depends on its subtask and vice versa. E.g. if you mark
  the last uncompleted subtask as completed, the parent task is
  automatically marked as completed too.
- Tasks and notes can be assigned to user-defined categories.
- Settings are persistent and saved automatically. The last opened
  file is loaded automatically when starting Task Coach.
- Tracking time spent on tasks. Tasks can have a budget. Time spent
  can be viewed by individual effort period, by day, by week, and by
  month.
- The Task Coach file format (.tsk) is XML.
- Tasks, notes, effort, and categories can be exported to HTML and CSV
  (Comma separated format). Effort can be exported to iCalendar/ICS
  format as well.
- Tasks, effort, notes, and categories can be printed. When printing,
  Task Coach prints the information that is visible in the current view,
  including any filters and sort order.
- Task Coach can be run from a removable medium.
- Tasks and notes can be synchronized via a Funambol server such as
  ScheduleWorld.

%description -l hu.UTF-8
Task Coach egy egyszerű, nyílt forráskódú teendő-nyilvántartó.
Jelenleg a következő lehetőségei vannak:
- Feladatok és alfeladatok létrehozása, szerkesztése és törlése
- A feladatoknak címük, leírásuk, fontosságuk, kezdő, lejárati és
  bejezési idejük van és esetleg figyelmeztetés is. Lehet napi, heti
  vagy havi rendszerességgel is.
- A feladatokat listaként vagy faként is megnézheted
- A feladatokat sorbarendezheted tulajdonságuk szerint, pl. cím,
  költségvetés, lejárati idő, stb. szerint.
- Néhány szűrőt is használhatsz, pl. a befejezett feladatokat
  elrejtheted, vagy csak a ma esedékeseket láthatod.
- E-mailből is készíthetsz feladatot (Outlook vagy Thunderbird)
- Csatolmányokat is társíthatsz feladatokhoz, megjegyzéseket.
- A feladat állapota függ az alfeladatitól és vissza is.
- Felhasználói kategóriák létrehozása
- Beállítások végérvényesek és automatikusan elmentdőnek. Az utoljára
  megnyitott fájl nyílik meg legközelebb.
- A feladatokkal töltött idő követése, költségvetés létrehozása.
- A fájlformátum XML.
- HTML-be, CSV-be, iCalendar/ICS formátumokba exportálás.
- Nyomtatási lehetőség.
- Cserélhető adathordozóról is lehet futtatni.
- Funambol szerverről szinkronizálhatók.

%description -l pl.UTF-8
Task Coach to prosty, mający otwarte źródła zarządca zadań służący do
zarządzania osobistymi listami zadań i rzeczy do zrobienia (todo).
Aktualnie ma on następujące cechy:

- Możliwe jest tworzenie, edycja i usuwanie zadań i podzadań.
- Zadania mają temat, opis, priorytet, datę rozpoczęcia, datę
  płatności, datę ukończenia i opcjonalne przypomnienie; zadania mogą
  powtarzać się w cyklu dziennym, tygodniowym lub miesięcznym.
- Zadania mogą być oglądane jako lista lub drzewo.
- Zadania mogą być sortowane po wszystkich atrybutach, np. temacie,
  budżecie, pozostałym budżecie, dacie płatności itd.
- Istnieją różne filtry, pozwalające np. ukryć zadania ukończone lub
  oglądać tylko zadania płatne dzisiaj.
- Zadania można tworzyć przeciągając wiadomość e-mail z Outlooka lub
  Thunderbirda na przeglądarkę zadań.
- Można dodawać załączniki do zadań, notatek i kategorii poprzez
  przeciągnięcie i upuszczenie plików, wiadomości e-mail z Outlooka lub
  Thunderbirda albo URL-i na zadanie, notatkę lub kategorię.
- Status zadania zależy od podzadań i na odwrót. Np. jeśli zaznaczymy
  ostatnie niedokończone podzadanie jako zakończone, nadrzędne zadanie
  automatycznie zostanie zaznaczone jako także zakończone.
- Zadania i notatki mogą być przypisywane do kategorii zdefiniowanych
  przez użytkownika.
- Ustawienia są trwałe i zapisywane automatycznie. Ostatni otwarty
  plik jest wczytywany automatycznie po uruchomieniu Task Coacha.
- Możliwe jest śledzenie czasu spędzanego nad zadaniami. Zadania mogą
  mieć budżet. Spędzony czas można oglądać dla własnego okresu badań
  oraz dla dni, tygodni i miesięcy.
- Formatem plików Task Coucha jest XML.
- Zadania, notatki, badania i kategorie mogą być eksportowane do
  formatów HTML i CSV; próby można eksportować także do formatu
  iCalendar/ICS.
- Zadania, badania, notatki i kategorie można drukować; przy
  drukowaniu Task Coach drukuje informacje widoczne w bieżącym widoku z
  uwzględnieniem filtrów i kolejności sortowania.
- Task Coach może być uruchamiany z nośnika wymiennego.
- Zadania i notatki mogą być synchronizowane poprzez serwer Funambol,
  taki jak ScheduleWorld.

%prep
%setup -q -n TaskCoach-%{version}
%patch0 -p1

%build
%{__python} setup.py build --executable /usr/bin/python

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root $RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/taskcoach{.py,}

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/buildlib

install -d $RPM_BUILD_ROOT%{_iconsdir}
install icons.in/taskcoach.png $RPM_BUILD_ROOT%{_iconsdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}
install build.in/fedora/taskcoach.desktop $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc HACKING.txt INSTALL.txt PUBLICITY.txt README.txt TODO.tsk
%attr(755,root,root) %{_bindir}/taskcoach*
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/TaskCoach-%{version}-py*.egg-info
%endif
%dir %{py_sitescriptdir}/taskcoachlib
%{py_sitescriptdir}/taskcoachlib/*
%{_iconsdir}/taskcoach.png
%{_desktopdir}/taskcoach.desktop
