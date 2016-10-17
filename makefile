report_project1.pdf: Phase_plot.png Plot_of_states.png report_project1.tex report_project1.bbl report_project1.blg vanderpol_animation.html
	pdflatex report_project1.tex
	pdflatex report_project1.tex

vanderpol_animation.html: vanderpol_animation.ipynb
	ipython nbconvert vanderpol_animation.ipynb

Phase_plot.png Plot_of_states.png: 15307R001_python_figures.py
	python 15307R001_python_figures.py

report_project1.bbl report_project1.blg: report_project1.bib
	pdflatex report_project1.tex
	bibtex report_project1

clean:
	rm -f *.aux *.log *.blg *.bbl *.png *.html *.toc 
