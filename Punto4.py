import logging
import random
import threading
import time

from rwlock import RWLock

logging.basicConfig(format='%(asctime)s.%(msecs)03d [%(threadName)s] - %(message)s', datefmt='%H:%M:%S',
                    level=logging.INFO)

equipos = ["Boca", "River", "Racing", "Independiente", "San Lorenzo", "Huracán", "Gimnasia",
           "Estudiantes", "Velez", "Ferro", "Lanus", "Quilmes"]

partido = ["equipo1", "puntaje1", "equipo2", "puntaje2"]

lock = RWLock()


class Escritor(threading.Thread):

    def __init__(self, partido):
        super().__init__()
        self.partido = partido
        self.name = "Escritor-" + self.name[-1]

    def run(self):
        while True:
            lock.w_acquire()
            try:
                self.partido[0], self.partido[2] = self.get_equipo_random(), self.get_equipo_random()
                self.partido[1], self.partido[3] = self.get_goles_random(), self.get_goles_random()
                logging.info(f"Partido actualizado por: {self.name}")
            finally:
                lock.w_release()
                time.sleep(random.randint(1, 2))

    def get_equipo_random(self):
        equipo = equipos[random.randint(0, len(equipos) - 1)]
        if equipo not in self.partido:
            return equipo
        return self.get_equipo_random()

    def get_goles_random(self):
        return random.randint(0, 3)


class Lector(threading.Thread):

    def __init__(self, partido):
        super().__init__()
        self.partido = partido
        self.name = "Lector-" + self.name[-1]


    def run(self):
        while True:
            try:
                lock.r_acquire()
                logging.info(f"%s: el resultado fue: %s %s - %s %s",
                             self.name, self.partido[0], self.partido[1], self.partido[2], self.partido[3])
                time.sleep(random.randint(1, 5))
            finally:
                lock.r_release()
                time.sleep(random.randint(1, 2))


if __name__ == "__main__":
    hilos = []
    escritor = Escritor(partido)
    lector = Lector(partido)

    hilos.append(escritor)
    hilos.append(lector)

    for h in hilos:
        h.start()

    for h in hilos:
        h.join()
