Summary:	Task Coach is a simple open source todo manager to manage personal tasks and todo lists
Summary(hu.UTF-8):	Task Coach egy egyszerű, nyílt forráskódú teendő-nyilvántartó
Name:		taskcoach
Version:	0.71.5
Release:	0.1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/taskcoach/TaskCoach-%{version}.tar.gz
# Source0-md5:	4265b00ae37f84507f8a1c69aa32a908
URL:		http://paintown.sourceforge.net
BuildRequires:	python-wxPython-devel
Requires:	python-wxPython
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

%prep
%setup -q -n TaskCoach-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT%{py_sitescriptdir}/buildlib

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt INSTALL.txt PUBLICITY.txt README.txt
%attr(755,root,root) %{_bindir}/taskcoach*
%{py_sitescriptdir}/TaskCoach-0.71.5-py2.6.egg-info
%dir %{py_sitescriptdir}/taskcoachlib
%{py_sitescriptdir}/taskcoachlib/*
