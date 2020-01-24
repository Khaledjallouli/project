# DHBW Heidenheim LaTeX Template

Dieses LaTeX Template ist für alle Arbeiten der Fakultät Technik der DHBW geeignet.

Im ersten Moment mag dies ein wenig verwirrend sein, aber in dieser Datei finden Sie die notwendigen Informationen, wo Sie bestimmte Einstellungen machen, und wo Sie Ihre Inhalte niederschreiben. 


### Die Datei main.tex

main.tex ist die Kerndatei des Templates und damit auch die Datei, welche kompiliert werden muss. Durch Importe anderer Datein wird die Dokumentenstruktur beschrieben (kann bei Bedarf geändert werden wenn z.B. kein Sperrvermerk gewünscht wird).

### ads

Im Ordner ads befinden sich folgende vordefinierte Vorlagen, welche nicht angepasst werden müssen (Anpassungen erfolgen automatisch):

* Deckblatt
* Eigenständigkeitserklärung
* Sperrvermerk
* LaTeX Document Header

### lang

Im Ordner lang befinden sich alle nötigen Übersetzungen. In der Datei settings/document.tex befindet sich ein Schalter, der entweder auf "de" oder "en" gesetzt wird, um eine deutsche oder englische Version zu erhalten.

### settings

In diesem Ordner gibt es zwei Dateien:

* general.tex
* document.tex

In der Datei general.tex sind grundlegende Einstellungen vordefiniert, welche nicht unbedingt geändert werden müssen.

Die Datei document.tex ist der Ort für die Angaben, die bei allen Arbeiten typischerweise anfallen:

| Variable | Beschreibung | Mögliche Werte |
| -------- | ------------ | -------------- |
| documentLanguage| Sprache der Arbeit | de<br/> en |
| documentType | Art der Arbeit | T2\\_1000 Projektarbeit (Semester 1 & 2) <br/> T2\\_2000 Projektarbeit (Semester 3 & 4) <br/> T2\\_3100 Studienarbeit (Semester 5) <br/> T2\\_3300 Bachelorarbeit |
| documentAuthor | Autor der Arbeit | |
| documentTitle | Titel der Arbeit | |
| documentPeriod | Dauer der Arbeit | |
| matriculationNumber | Matrikelnummer des Autors | |
| locationUniversity | Standort der DHBW | Heidenheim |
| department | Fakultät der DHBW in der sich der Autor befindet | |
| course | Kurs in dem sich der Autor befindet | |
| degree | Abschluss, welcher mit dieser Arbeit angestrebt wird | Bachelor of Science (INF2014-MI - INF2016-MI) <br/> Bachelor of Engineering (INF2014-IA/IM - INF2016-IA/IM) <br/> Bachelor of Science  (INF2017-IM/MI/IA) |
|releaseDate | Abgabedatum | |
| releaseLocation | Abgabeort | Heidenheim |
| companyName | Name des Unternehmens in dem der Autor angestellt ist | |
| companyLocation | Firmensitz | |
| tutor | Betrieblicher Betreuer der Arbeit | |
| evaluator | Zweitkorrektor der Arbeit | |

### content

Hier sind die einzelnen Kapitel als separate Dateien vorhanden. Beim Einfügen einer neuen Datei wird diese automatisch erkannt. Die Reihenfolge der Kapitel ergibt sich aus der Nummerierung in den Dateinamen.

### images


# Komponenten einer Wissenschaftlichen Arbeit

## Abstract

An abstract is a brief summary of a research article, thesis, review, conference proceeding or any in-depth analysis of a particular subject or discipline, and is often used to help the reader quickly ascertain the paper's purpose. When used, an abstract always appears at the beginning of a manuscript, acting as the point-of-entry for any given scientific paper or patent application. Abstracting and indexing services for various academic disciplines are aimed at compiling a body of literature for that particular subject.

The terms précis or synopsis are used in some publications to refer to the same thing that other publications might call an ``abstract''. In ``management'' reports, an executive summary usually contains more information (and often more sensitive information) than the abstract does.

Quelle: \url{http://en.wikipedia.org/wiki/Abstract_(summary)}


## Acronyms

nur verwendete Akronyme werden letztlich im Abkürzungsverzeichnis des Dokuments angezeigt
Verwendung: 
		\ac{Abk.}   --> fügt die Abkürzung ein, beim ersten Aufruf wird zusätzlich automatisch die ausgeschriebene Version davor eingefügt bzw. in einer Fußnote (hierfür muss in header.tex \usepackage[printonlyused,footnote]{acronym} stehen) dargestellt
		\acs{Abk.}   -->  fügt die Abkürzung ein
		\acf{Abk.}   --> fügt die Abkürzung UND die Erklärung ein
		\acl{Abk.}   --> fügt nur die Erklärung ein
		\acp{Abk.}  --> gibt Plural aus (angefügtes 's'); das zusätzliche 'p' funktioniert auch bei obigen Befehlen
	siehe auch: http://golatex.de/wiki/%5Cacronym
	
example: 
\acro{AGPL}{Affero GNU General Public License}
\acro{WSN}{Wireless Sensor Network}



## Appendix

(Beispielhafter Anhang)
 
Bei mehreren Anhangsteilen kann eine Art Inhaltsverzeichnis der Anhänge vorangestellt werden:

{\Large
\begin{enumerate}[label=\Alph*.]
	\item Assignment 
	\item List of CD Contents
	\item CD 
\end{enumerate}
}
\pagebreak

Mit z.B.:
\section*{A. Auflistung der Begleitmaterial-Archivdatei }
folgen dann die Anhangsteile. "*" verhindert hier die Nummerierung, da Anhänge ja üblicherweise mit Großbuchstaben durchgezählt werden.



# Contributors

Autor: Tobias Dreher, Yves Fischer
 Date: 06.07.2011

 Autor: Michael Gruben
 Date: 15.05.2013

 Autor: Markus Barthel
 Date: 22.08.2014

 Autor: Prof. Dr. Rolf Assfalg
 Date 23.03.2017

 Autor: Stefan Schneider
 Date: 06.06.2017