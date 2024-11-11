Gonçalo Freitas, Mestrado em Engenharia Computacional, Nº Mec = 98012

Conteúdos do ficheiro .zip - Trabalho 3

	- Pasta 'codigos' com os ficheiros .py com o código para a resolução deste problema
		-> lossy_counter.py - Método 'Lossy Counter'
		-> prob_counter.py - Método 'Probabilistic Counter'
		-> exact_counter.py - Método 'Exact Counter'
		-> calculate_parameters.py - Código para calcular as métricas, referidas no relatório, para avaliar os modelos
		-> main.py - Código principal, usa o códigos acima para resolver o problema e guardar os resultados nos respetivos ficheiros .txt 
		-> estimation_time.py - Código utilizado para realizar a estimativa do tempo de cada algoritmo para ficheiros com N letras
	
	- Ficheiro .pdf com o relatório

	- Ficheiro .zip com todos os requisitos para compilar o relatório em LaTex

	- Pasta 'dirty_files' com os ficheiros tal como se pode descarregar de [1], isto é, não estão formatados para análise

	- Pasta 'clean_files' com os ficheiros 'limpos', isto é, formatados para a análise

	- Pasta 'counter' com 3 pastas no interior, cada uma respetiva a cada método.
		[2]-> Para análise indivual do ranking de letras de um livro, o nome de cada ficheiro encontra-se no formato "NomeDoLivro_Método_Parametro.txt" (parâmetro se for lossy/probabilistic)
		-> Para análise das métricas para avaliar os métodos (contem os 4 livros num ficheiro), o nome de cada ficheiro, encontra-se no formato "metricas_Método_Parametro.txt" (parâmetro se for lossy/probabilistic)
	
	- Visto o professor ter pedido, explicitamente, as tabelas das Top x letras e, a partir do ponto [2] estas possam ser dificeis de vizualizar, foi criada, adicionalmente,
	a pasta 'tops' que permite uma vizualiação mais fácil, do Top 3,5,10 e todas as letras ordenadas de forma de crescente; retornado por cada método para cada livro, isto é, todos os livros num ficheiro
		-> Formatação "NomeDoMétodo_parametro"(parâmetro se for lossy/probabilistic)

	- Pasta 'Extra -> Figuras' com as figuras utilizadas neste projeto e o código .m para a obtenção das figuras da estimativa 
	  de tempo de cada algoritmo

	- Devido ao limite de 100mb no envio do elearning não é possivel enviar os
	  ficheiros (da soma dos 3 livros), com N letras, N = [1000, 10000, 100000, 1000000, 10000000, 100000000]
	  Contundo, no ficheiro estimation_time_output.txt, que se encontra na pasta 'Extra', pode ser visualizado o tempo de execução de cada algoritmo para cada ficheiro com N palavras
	  Caso o professor queira estes ficheiros não hesite em pedir! (goncalojfreitas@ua.pt)

	- No projeto, para o método Probabilistic counter, para alem de se usar uma probabilidade de 1/(2^3), para comparação também se usou uma de 1/(2^8),
	  para o livro 'O livro de Cesário Verde', cujos resultados encontram-se na pasta 'Extra -> Probabilistic Counter, k=8'



[1] Project Gutenberg - https://www.gutenberg.org/