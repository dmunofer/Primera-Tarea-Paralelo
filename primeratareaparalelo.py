from multiprocessing import Pool  # Importa la clase Pool del módulo multiprocessing
from time import sleep # Importa la función sleep del módulo time
import random # Importa el módulo random para generar números aleatorios
def scrape(url):
    # Define la función scrape que toma una URL como entrada
    print("starting", url) # Imprime un mensaje indicando que se está iniciando el raspado de la URL
    duration = round(random.random(),3) # Genera un número aleatorio entre 0 y 1, lo redondea a 3 decimales y lo asigna a la variable duration
    sleep(duration) # Duerme el proceso durante la cantidad de segundos especificada en duration
    print("finished", url, "time taken:", duration, "seconds")
    return url, duration
urls = ["a.com", "b.com", "c.com", "d.com"]
if __name__ == "__main__":
    pool = Pool(processes=4)
    data = pool.map(scrape, urls)
    pool.close()    
    print()
    for row in data:
        print(row)