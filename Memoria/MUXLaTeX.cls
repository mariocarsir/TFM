% Documentación básica para CLS: https://es.overleaf.com/learn/latex/Writing_your_own_class
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{MUXLaTeX}[27/04/2023 - MUXLaTeX]
%%%%%%%%%%%%%%%%%%%%%%%%% <--- COMIENZO DE LA PLANTILLA

%%%%%%%%%%%%%%%%%%%%%%% <- COMIENZO C. GENERALES

\LoadClass[a4paper, 11pt, oneside]{book}
\usepackage{acronym}
\usepackage{multirow}
\usepackage[table,xcdraw]{xcolor}
\usepackage{colortbl}
\usepackage{hyperref}
\usepackage{xurl}
\usepackage{mathpazo}
\usepackage{amsmath, amssymb}
\usepackage{siunitx}
\usepackage{enumitem}
% Un único \sisetup: antes había dos (este y otro más abajo), y el segundo
% pisaba al primero. Fusionados aquí.
\sisetup{
  per-mode = symbol,            % usa símbolo "por" en lugar de exponente
  per-symbol = /,               % el símbolo que usa es la barra /
  output-decimal-marker = {,},  % coma decimal (4,038) - guía tipográfica ERMA
  detect-all
}
% Unidades que siunitx NO trae de serie y que este TFM usa constantemente.
% Comprobado: \kW, \kWh, \W y \hour sí vienen definidas, estas no.
\DeclareSIUnit{\Wp}{Wp}     % vatio pico
\DeclareSIUnit{\kWp}{kWp}   % kilovatio pico — potencia del campo FV
\DeclareSIUnit{\MWp}{MWp}   % megavatio pico
\DeclareSIUnit{\MWh}{MWh}   % megavatio hora — consumo anual del CPD
\DeclareSIUnit{\kVA}{kVA}   % potencia aparente — inversores
\DeclareSIUnit{\kvar}{kvar} % potencia reactiva

% Margin setup
\usepackage[headheight=10ex,inner=2.5cm,
	outer=2.5cm, % Outer margin
	bindingoffset=.5cm, % Binding offset
	top=2.5cm, % Top margin
	bottom=2cm]{geometry}
\usepackage{ifthen}
\usepackage{afterpage}
\usepackage{float}
\usepackage{pdflscape}
\usepackage{pdfpages}
\setlength{\parskip}{0.7em}
\setlength{\parindent}{0pt}

%\usepackage[document]{ragged2e}
\usepackage{todonotes}
%\usepackage{hyphenat}
%\hyphenpenalty=10000
\usepackage[spanish]{babel}
\usepackage{watermark}
\usepackage[most]{tcolorbox}

\newcommand{\digital}[1]{
        \ifthenelse{\equal{#1}{no}}{
        \newcommand{\cambio}{
        \newgeometry{headheight=10ex,inner=2cm,
	outer=2cm, % Outer margin
	bindingoffset=.5cm, % Binding offset
	top=2.5cm, % Top margin
	bottom=2cm ,twoside}}
        }  
        {
        \newcommand{\cambio}{
        \newgeometry{headheight=10ex,inner=2cm,
	outer=2cm, % Outer margin
	bindingoffset=.5cm, % Binding offset
	top=2.5cm, % Top margin
	bottom=2cm}
        }
        }
}

%%%%%%%%%%%%%%%%%%%%%%% <- FIN C. GENERALES

%%%%%%%%%%%%%%%%%%%%%%% <- MOD. Cap/Sec

\definecolor{lechuga}{RGB}{39, 30, 32}
\definecolor{azulsection}{RGB}{39, 30, 32}
\definecolor{verdesection}{RGB}{39, 30, 32}
\definecolor{grissection}{HTML}{6D6E71}
\definecolor{redi}{RGB}{39, 30, 32}
%e3254a
\definecolor{good_black}{RGB}{36, 30, 32}
\definecolor{good_green}{RGB}{109, 191, 81}
\newcommand{\capitulo}[2]{
    \chapter*{Chapter #1. #2}    \addcontentsline{toc}{chapter}{\protect\numberline{#1}#2}}
% Modo alto contraste. Solo define \estilopagina, que sí usa main.tex.
% Se han eliminado \palitos y \logoUCM: no los llamaba nadie y \logoUCM
% apuntaba a logos de la UCM heredados del TFG que no existen en LOGOS/.
\newcommand{\bajavision}[1]{
 \ifthenelse{\equal{#1}{si}}{
    \newcommand{\estilopagina}{
        \pagecolor{good_black}
        \color{good_green}
    }
}{ \newcommand{\estilopagina}{}
}
}

\newcommand{\abstract}[1]{%
  \ifthenelse{\equal{#1}{si}}%
    {\newcommand{\insercion}{\input{Anexos/resumen.tex}}}%
    {\newcommand{\insercion}{}}%
}


\newcommand{\indicefiguras}[1]{

 \ifthenelse{\equal{#1}{si}}
    {\newcommand{\figuracion}{
            \listoffigures
        }
    }
    {
        \newcommand{\figuracion}{
        }
    }
}
% \figuras{ruta izq}{pie izq}{etiqueta izq}{ruta dcha}{pie dcha}{etiqueta dcha}
%
% Coloca dos figuras INDEPENDIENTES una al lado de la otra. Cada una recibe
% su propio número y su propio pie: p. ej. Figura 2.5 y Figura 2.6. Sirve
% para ahorrar espacio cuando son dos cosas distintas (dos gráficas de
% PVsyst, por ejemplo), no para partir una misma figura en dos paneles.
%
% Las etiquetas pueden ir vacías ({}), y entonces se usa fig:<pie> igual que
% en \figura; pero conviene darlas para que cambiar el pie no rompa los \ref.
%
% Ejemplo:
%   \figuras{prod_ene.png}{Producción en enero}{fig:prod-enero}
%           {prod_jul.png}{Producción en julio}{fig:prod-julio}
%
% OJO: la versión anterior metía las dos imágenes bajo UN SOLO pie y un solo
% número, así que no se podía referenciar cada una por separado. Nadie la
% usaba todavía, por eso se ha podido cambiar sin romper nada.
\newcommand{\figuras}[6]{
\begin{figure}[H]
    \centering
    \begin{minipage}[t]{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{#1}
        \caption{#2}
        \ifthenelse{\equal{#3}{}}{\label{fig:#2}}{\label{#3}}
    \end{minipage}\hfill
    \begin{minipage}[t]{0.48\textwidth}
        \centering
        \includegraphics[width=\textwidth]{#4}
        \caption{#5}
        \ifthenelse{\equal{#6}{}}{\label{fig:#5}}{\label{#6}}
    \end{minipage}
\end{figure}
}

% \figura[etiqueta]{ruta}{ancho}{pie}
%   etiqueta - OPCIONAL pero recomendada: clave estable para \ref.
%              Si se omite, se usa fig:<pie> igual que antes, pero entonces
%              cambiar el texto del pie rompe todas las referencias.
%              Ejemplo: \figura[fig:curva-carga]{img.png}{0.8}{Curva de carga}
%   ancho    - fracción de \textwidth; vacío = ancho completo.
\newcommand{\figura}[4][]{
\begin{figure}[H]
    \centering
    \ifthenelse{\equal{#3}{}} {\includegraphics[width=\textwidth]{#2}}{\includegraphics[width=#3\textwidth]{#2}}

    \ifthenelse{\equal{#4}{}}
    {}
    {
        \caption{#4}
        \ifthenelse{\equal{#1}{}}{\label{fig:#4}}{\label{#1}}
    }
\end{figure}
}
\newcommand{\indicetablas}[1]{

 \ifthenelse{\equal{#1}{si}}
    {\newcommand{\tabloides}{
            \listoftables
        }
    }
    {
        \newcommand{\tabloides}{
        }
    }
}
% Eliminadas \autoria y \direccion: hardcodeaban los datos del TFG
% (Grado en Ingeniería Eléctrica, Dr. Jorge Moreno Mohíno) y no las
% llamaba nadie. Autor y tutor del TFM se pasan como argumentos a
% \maquetacion desde main.tex.

\usepackage{titlesec}


\titleformat{\chapter}[hang]
{\Huge\bfseries\color{lechuga}}
{\color{lechuga} Capítulo \thechapter. }
{0em}
{}
\titlespacing{\chapter}{0pt}{0pt}{0pt}
\titlespacing{\section}{0pt}{0pt}{0pt}
\titlespacing{\subsection}{0pt}{0pt}{0pt}
\titlespacing{\subsubsection}{0pt}{0pt}{0pt}

\titleformat{\section}[hang]
{\Large\bfseries\color{azulsection}}
{\color{azulsection} \thesection. }
{0em}
{}

\titleformat{\subsection}[hang]
{\Large\bfseries\color{verdesection}}
{\color{verdesection} \thesubsection. }
{0em}
{}


\titleformat{\subsubsection}[hang]
{\Large\bfseries\color{grissection}}
{\color{grissection}}
{0em}
{}

%%%%%%%%%%%%%%%%%%%%%%% <- GENERAMOS EL ÍNDICE
\usepackage{titletoc}% http://ctan.org/pkg/titletoc
\newcommand{\indiceTFG}{
    \setcounter{tocdepth}{2} % 0=solo capítulos, 1=+secciones, 2=+subsecciones
    \tableofcontents

}

\titlecontents{chapter} % Comando a modificar
[0pt] % Espacio a la izquierda
{} % CÓDIGOS A LA IZQUIERDA
{\sffamily\bfseries\chaptername\phantom{l}\thecontentslabel\quad\quad}
{}
{\sffamily\bfseries\color{gray}\dotfill\color{black}\contentspage}


%%%%%%%%%%%%%%%%%%%%%%% <- FIN DE ÍNDICE

%%%%%%%%%%%%%%%%%%%%%%% <- FancyHDR

\usepackage{fancyhdr}
% Estilo general
\pagestyle{fancy}
\fancyhf{} % limpia cabecera y pie
\fancyfoot[C]{\thepage} % número de página abajo centrado
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}

% Estilo de las páginas "plain" (inicio de capítulo, páginas sólo con flotantes, etc.)
\fancypagestyle{plain}{%
  \fancyhf{}%
  \fancyfoot[C]{\thepage}%
  \renewcommand{\headrulewidth}{0pt}%
  \renewcommand{\footrulewidth}{0pt}%
}

%%%%%%%%%%%%%%%%%%%%%%% <- Fin de FancyHDR

%%%%%%%%%%%%%%%%%%%%%%%%% <--- FINAL DE LA PLANTILLA
\newcommand{\bibliografia}{
    \bibliographystyle{IEEEtran}
    \bibliography{biblio}
    \addcontentsline{toc}{chapter}{\textsf{\textbf{Bibliografía}}}
}
\usepackage{emptypage}
\usepackage[none]{hyphenat} % Desactiva la división de palabras
\sloppy % Permite un espaciado más flexible para evitar overflow de texto

\newcommand*{\portada}[3]{%
    
    % #1 = Título del TFG
    % #2 = Autor/a
    % #3 = Datos del tutor/a (p.ej. "Nombre y apellidos\\Departamento de ...")

    \hypersetup{
        colorlinks=true,
        linkcolor=black,
        filecolor=magenta,      
        urlcolor=cyan,
        pdftitle={#1},
        pdfpagemode=FullScreen,
    }%
    \pagenumbering{roman}%
    \thispagestyle{empty}%
    % Márgenes de la portada
    \newgeometry{left=2.5cm,right=2.5cm,top=2.5cm,bottom=2.5cm}%
    \afterpage{\restoregeometry}%
    \estilopagina

    % --- Parte superior: logos ---
    \begin{center}
        \begin{minipage}[c]{0.48\textwidth}
            \raggedright
            % >>> CAMBIA el nombre del archivo por el logo oficial de la UPM
            \includegraphics[width=0.5\textwidth]{LOGOS/upmlogo.jpeg}
        \end{minipage}%
        \begin{minipage}[c]{0.48\textwidth}
            \raggedleft
            % >>> CAMBIA el nombre del archivo por el logo oficial de la ETSIDI
            \includegraphics[width=0.6\textwidth]{LOGOS/etsidilogo.png}
        \end{minipage}

        \vspace{2cm}

        {\large UNIVERSIDAD POLITÉCNICA DE MADRID\par}
        \vspace{0.5cm}
        {\large ESCUELA TÉCNICA SUPERIOR DE INGENIERÍA Y DISEÑO INDUSTRIAL\par}
        \vspace{0.5cm}
        {\normalsize
        Grado en Ingeniería Eléctrica\par}

        \vspace{2cm}
        {\Large\bfseries TRABAJO FIN DE GRADO\par}

        \vspace{1.5cm}
        {\large\bfseries\itshape #1\par} % Título del TFG

        \vspace{1.5cm}
        {\normalsize\bfseries Autor/a:\ }{\normalsize\itshape #2\par}
    \end{center}

    \vspace{2cm}

    % --- Bloque inferior: co-tutor y tutor ---
    \noindent
    \begin{minipage}[t]{0.48\textwidth}
        \raggedright
        \textbf{}\\[0.5em]
        % >>> RELLENA ESTAS LÍNEAS EN EL .CLS CUANDO SEPAS LOS DATOS
        
        
    \end{minipage}%
    \begin{minipage}[t]{0.48\textwidth}
        \raggedleft
        \textbf{Tutor/a:}\\[0.5em]
        {\normalsize\itshape #3}
    \end{minipage}

    \vspace{1.0cm}

    \noindent
    % >>> CAMBIA "Madrid, mes, año" por la fecha real al final
    \hfill Madrid, enero, 2026

    \clearpage
    \cambio
    \pagestyle{fancy}
    \estilopagina
}
%%%%%%%%%%%%%%%%%%%%%%%%%%%% PORTADA DE FIRMAS
\newcommand*{\portadaFirmas}[3]{%
    % #1 = Título del TFG
    % #2 = Autor/a (no lo usamos ahora, pero lo dejamos por si acaso)
    % #3 = Datos del tutor/a

    \clearpage
    \thispagestyle{empty}

    \begin{center}
        % Logos arriba, igual que en la portada principal
        \begin{minipage}[c]{0.48\textwidth}
            \raggedright
            \includegraphics[width=0.5\textwidth]{LOGOS/upmlogo.jpeg}
        \end{minipage}%
        \begin{minipage}[c]{0.48\textwidth}
            \raggedleft
            \includegraphics[width=0.6\textwidth]{LOGOS/etsidilogo.png}
        \end{minipage}

        \vspace{2cm}

        {\large UNIVERSIDAD POLITÉCNICA DE MADRID\par}
        \vspace{0.5cm}
        {\large ESCUELA TÉCNICA SUPERIOR DE INGENIERÍA Y DISEÑO INDUSTRIAL\par}
        \vspace{0.5cm}
        {\normalsize Grado en Ingeniería Eléctrica\par}

        \vspace{2cm}
        {\Large\bfseries TRABAJO FIN DE GRADO\par}

        \vspace{1.5cm}
        {\large\bfseries\itshape #1\par} % título

    \end{center}

    \vspace{3cm}

    % Zona inferior para firma del tutor
    \noindent
    \begin{minipage}[t]{0.48\textwidth}
        \raggedright
        {\normalsize\bfseries Firma autor:\par}
        \vspace{2cm}
        \rule{5cm}{0.4pt}
    \end{minipage}
    \begin{minipage}[t]{0.48\textwidth}
        \raggedleft
        {\normalsize\bfseries Firma tutor:\par}
        \vspace{2cm}
        \rule{5cm}{0.4pt}
    \end{minipage}

    \clearpage
}

\newcommand{\paginaenblanco}{%
    \clearpage
    \thispagestyle{empty}%
    \null
    \clearpage
}
%%%%%%%%%%%%%%%%%%%%%% AGRADECIMIENTOS
\newcommand{\agradecimientosTFG}{%
    \clearpage
    \chapter*{Agradecimientos}%
    \addcontentsline{toc}{chapter}{\textbf{\textsf{Agradecimientos}}}%
    \input{Anexos/agradecimientos}% 
}
%%%%%%%%%%%%%%%%%%%% RESUMEN
\newcommand{\resumenTFG}{%
    \clearpage
    \chapter*{Resumen}%
    \addcontentsline{toc}{chapter}{\textbf{\textsf{Resumen}}}%
    \input{Anexos/resumen_es}% 
}

\newcommand{\listaAcronimos}{%
    \clearpage
    \chapter*{Lista de acrónimos}%
    \addcontentsline{toc}{chapter}{\textbf{\textsf{Lista de acrónimos}}}%
    \input{Anexos/acronimos}% 
}

\newcommand{\maquetacion}[3]{
    \portada{#1}{#2}{#3} % Portada
    \portadaFirmas{#1}{#2}{#3} % Portada de firmas
    \paginaenblanco % Página en blanc
    \agradecimientosTFG % Agradecimientos
    \paginaenblanco % Otra página en blanco
    \resumenTFG  % Resumen en español
    \insercion
    \indiceTFG
    \figuracion
    \tabloides
    \listaAcronimos
}

\newcommand{\clave}[1]{%
    % Palabras clave en español (no toca el índice)
    \par\vspace*{\fill}%
    {\noindent\large\textsf{\textbf{Palabras clave:} #1.}}\par%
}

\newcommand{\keywords}[1]{%
    % Keywords en inglés + añade "Abstract" al índice una sola vez
    \addcontentsline{toc}{chapter}{\textbf{\textsf{Abstract}}}%
    \par\vspace*{\fill}%
    {\noindent\large\textsf{\textbf{Keywords:} #1.}}\par%
}

\colorlet{mdtRed}{red!50!black}

\usepackage{multicol}
\hypersetup{pdfpagemode={UseOutlines},
bookmarksopen=true,
bookmarksopenlevel=0,
hypertexnames=false,
colorlinks=true,% Set to false to disable coloring links
citecolor=magenta,% The color of citations
linkcolor=blue,% The color of references to document elements (sections, figures, etc)
urlcolor=mdtRed,% The color of hyperlinks (URLs)
pdfstartview={FitV},
unicode,
breaklinks=true,
}

\doublehyphendemerits=10000 % No consecutive line hyphens
\brokenpenalty=10000 % No broken words across columns/pages
\widowpenalty=9999 % Almost no widows at bottom of page
\clubpenalty=9999 % Almost no orphans at top of page
\interfootnotelinepenalty=9999 % Almost never break footnotes

\RequirePackage{silence}
\WarningsOff[fancyhdr]
\WarningsOff[crimson]
\WarningsOff[fontenc]
\WarningsOff[babel]
% NO reactivar \WarningsOff[latex]: silenciaba TODOS los avisos de LaTeX,
% incluidos "Citation undefined", "Reference undefined" y "There were
% undefined references". El documento compilaba con éxito aparente mientras
% arrastraba citas y referencias rotas (que salen como ?? en el PDF).
% Verificado: con esta línea activa, un \cite inexistente no genera aviso.
\endinput